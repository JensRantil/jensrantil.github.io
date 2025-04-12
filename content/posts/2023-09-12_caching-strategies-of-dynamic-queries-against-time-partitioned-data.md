+++ 
date = 2023-09-12T21:25:33+02:00
title = "Fine-grained caching strategies of dynamic queries"
description = "A flexible approach to balance against many reads or writes."
slug = "fast-aggregate-queries-on-dynamic-data"
+++
Today I would like to talk about caching strategies for aggregate queries over
time-based data which is updated often. This is something I spent significant
brain-cycles on my previous job and I would love to share some of my findings.

## Example data & use case

For the sake of the rest of this post, let's say we have a relational database table containing financial transactions:

| **date (ASC)** | **id** | **userId** | **description** | **amount** | **tags**                   |
|----------------|--------|------------|-----------------|------------|----------------------------|
| 2023-05-22     | 1      | 1          | BestBuy         | $42        | ["tools"]                  |
| 2023-05-29     | 2      | 2          | Netflix         | $9.9       | ["entertainment"]          |
| 2023-05-29     | 3      | 2          | Lowe's          | $42        | ["tools"]                  |
| 2023-06-03     | 4      | 2          | Amazon          | $22        | ["tools", "entertainment"] |
| ...            | ...    | ...        | ...             | ...        | ...                        |

The table has a secondary ordered index on the `date` column in such a way that
one can quickly query a slice of the dates (ie `... WHERE date BETWEEN
'2023-05-24' AND '2023-05-31'`). Let's assume that the table consists of enough
rows in such a way that `SELECT SUM(amount) FROM transactions` is slow.

The access pattern **requirements** for this table are as follows:

 1. Mutations (ie. insertions, updates, and deletes) can happen to any of the
    rows. That is, the table is not append-only.
 2. Mutations happen more frequently than querying.
 3. Customers are interested in summing up the amounts of a subset of
    transactions using custom filters dynamically generated from a web
    interface. Things they can filter on is
    1. tags, amount, and description.
    2. on date ranges.
 4. Customers expect consecutive queries to return quickly.

## Implementation

It turns out that the above requirement is a surprisingly hard problem to
solve! I like to relax engineering problems a bit to understand what is
actually hard, so let's build up a solution from scratch where we relax some of
the problems:

### Immutable data

For now, let's assume that the table is immutable (ie. mutations are not
allowed). So, what is wrong with simply constructing a `SELECT` query against
immutable data? Well, it turns out that querying it is too slow (requirement
4). The classic way to solve this is to add a caching layer* in front of the
database. We use the SQL query as our cache key, and return the cached value if
it exists - otherwise, run the expensive query against the database.

(Memcache and Redis are two excellent distributed caches that could be used for
this - and can be scaled horizontally. For certain applications, you might even
be fine with an in-memory cache in your client.)

### In-place mutations & user partitioning

As pointed out in our original requirements, our data is *not* immutable. So,
let's now assume that our data can be mutated. That is, added, removed, or
deleted. This means that we need cache invalidation to avoid returning stale
data. Since the list of all SQL query cache keys isn't known beforehand, we
need to invalidate *all* keys. Most caches support this.

The problem with invalidating the full cache is fairly obvious; Every write
will make _every_ following query slow since it needs to hit the database.
That's no good.

It's worth pointing out that if the transactions would be tied to a `userId`,
at least we could invalidate only that user's cache keys. Certain caches
(looking at you Redis) support iterating over the cache keys, but most don't.
Either way that would be an expensive operation. A workaround for this would be
to start working with *hashing*. If we introduce a new table, called
`cache_invalidation_token` mapping a `userId` to some random [nonce][nonce]
that gets updated every time we modify a user's financial transaction (within
the same *database* transaction), we could then use `HASH(sql) XOR
NONCE(userId)` as our cache lookup key. By updating the nonce on every write,
we would implicitly invalidate all the SQL results. Neat!

As a side note `cache_invalidation_tokens` mapping could be stored in a cache
itself. Whether to store it next to the `transactions` table is a matter of how
certain you want to be that the cache invalidation happens on every write if
there is a network partition. You can of course also automatically add TTLs to
the `cache_invalidation_tokens` cache to handle that case, occasionally risking
intermittent stale data from time to time. Trade-offs, trade-offs...

[nonce]: https://en.wikipedia.org/wiki/Cryptographic_nonce

### Date-based partitioning

The problem with the above approach is that every cache invalidation requires a
full pass over all the user's data again. Can we do better? Usually, yes, and
this is where things get interesting; We can do more fine-grained cache
invalidation by date. By partitioning our cached SQL results by date, for
example, month, we can invalidate only certain parts of our data. Let me
explain:

If we instead define our `cache_invalidation_tokens` mapping as `(userId, year, month)
=> nonce` (refered to as `NONCE(x)` from now on), the query
```sql
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND
  date BETWEEN '2023-01-01' AND '2023-06-01'
```
would trigger five cache lookups and potentially five SQL query executions:
```sql
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND
  date BETWEEN '2023-01-01' AND '2023-02-01';
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND
  date BETWEEN '2023-02-01' AND '2023-03-01';
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND
  date BETWEEN '2023-03-01' AND '2023-04-01';
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND
  date BETWEEN '2023-04-01' AND '2023-05-01';
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND
  date BETWEEN '2023-05-01' AND '2023-06-01';
```
Each SQL query would first check if the cache key `HASH(sql) XOR NONCE(userId,
year, month)` exists, followed by a query against the primary table on cache
miss. Finally, all the results would be summed up to a final `SUM(amount)`.
Further, every mutation would then need to update with a new random nonce for
`(userId, year, month)` (as before, either in a database transaction or in a
cache).

The above-described approach is a trade-off between shorter scans on average
when data has been mutated, at the cost of more queries against the database.
The size of the time buckets (months etc.) really depends on the tradeoffs
between

 * the number of queries hitting the database and the cache.
 * whether mutations usually update certain date ranges (ie. close to today).
 * how often reads happen (to keep the cache updated).

### Advanced: Prepopulating the cache hot

If low latency is needed for certain known SQL queries, there is nothing
stopping a database writer from asynchronously populating the cache afterward.
For example, maybe summing the amount without any custom filtering is so common
that populating that in the cache is worth it.

The two popular distributed caches [Memcached][memcached] and [Redis][redis]
both support [atomic incrementation of integers][memc-incr] which also could be
done at write instead of a full recalculation and storing cache invalidation
tokens.

[memcached]: https://memcached.org/
[redis]: https://redis.com/
[memc-incr]: https://github.com/memcached/memcached/blob/efee763c93249358ea5b3b42c7fd4e57e2599c30/doc/protocol.txt#L354

### Advanced: 2-phase lookups

The careful reader might have noticed my example above was slightly contrived;
the date range for my example query was covering even months. What if
someone would query
```sql
SELECT SUM(amount) FROM transactions WHERE
    userId=123
  AND
    date BETWEEN '2023-01-05' AND '2023-04-15'
```
? Ie.
```sql
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND
  date BETWEEN '2023-01-05' AND '2023-02-01';
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND
  date BETWEEN '2023-02-01' AND '2023-03-01';
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND date BETWEEN '2023-03-01' AND '2023-04-01';
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  description='Netflix' AND
  date BETWEEN '2023-04-01' AND '2023-04-15';
```
The likelihood for the first and last query to be found in the cache would be
rather small, as the SQL query would be fairly unique.

A fix for this would be to do **two lookup phases**: First you would do a pass
of all cache lookups, wait for them to be done, and then execute *a single* SQL
query based on the ranges not within the cache, ie. something like:
```sql
SELECT SUM(amount) FROM transactions WHERE
  (date BETWEEN '2000-01-01' AND '2015-01-01')
OR
  (date BETWEEN '2017-01-01' AND '2023-01-01')
```
This would definitely reduce the number of queries against the database, but
not the `cache_invalidation_tokens` cache!

### Advanced: Hierarchical date-based partitioning

Another problem would be the query:
```sql
SELECT SUM(amount) FROM transactions WHERE
  userId=123 AND
  date BETWEEN '2000-01-01' AND '2023-01-01'
```
In the worst-case scenario, if nothing is found in the cache, this would
trigger `23 years * 12 months = 276 query` executions against the database! Further the cache would get hit pretty often.

To avoid excessive cache and database lookups, one could instead use
**hierarchical date-based partitioning** where nonces are introduced for
different date partition granularity. For example, `NONCE(userId, year)`,
`NONCE(userId, year, month)`, and `NONCE(userId, year, month, day)`. A mutation
of a financial transaction with the date `2013-08-03` for user X, would then
invalidate the cache for the keys `(X, 2013)`, `(X, 2013-08)`, and `(X,
2013-08-03)`. The query logic above would become more complex, but would prefer
querying in the following priority if possible:

 1. year partition from cache.
 2. month partition from cache.
 3. day partition from cache.
 4. SQL query against the relational primary data.

The hierarchical approach would have the benefit of reducing the hits to the
relational database while taking a cost in amplifying the writes needed to
`cache_invalidation_tokens` as well as the storage needed for it.

## Conclusion

Introducing finer-grained partitioned caching is a useful tool to not have to
invalidate all caches on every mutation.

One important aspect this article did _not_ cover too much is the importance of
finding the right abstraction such that you can easily iterate on caching
strategies like this. You need a single place that can control how data is
written to the relational database, as well as how that data is accessed. If
you have many different clients accessing your database, you can't do this kind
of work easily.

## Addendum I: On read/write ratio & caching

A common way to categorize computer systems is whether they have a high
read/ratio or a low read/write ratio. The ratio is high if there are more reads
than the writes. It is low if there are more writes than reads.

An example of a *high read/write* ratio could be an address book; you look
things up very often, but you rarely update your contacts. *Low read/write
ratio* could be when you have a lot of data being received but you rarely look
at it. A good example of that is a logging system; Your application will write
lots of log lines, but you will most likely rarely look at every log.

I once heard someone say something of the like

> Solving high read-write ratio problems is fairly easy. Solving low read-write
> ratio problems is fairly easy. The hard problem is when you have closer to a
> 1:1 ratio between reads and > writes.

It's so true! If I recall correctly, the quote came from someone when they were
talking about [the <abbr title="Command-Query Responsibility
Segregation">CQRS</abbr> pattern][cqrs] . It's a pattern where you explicitly
split your system into one part that takes care of writes (validation & data
consistency) and another part that takes care of serving reads.

[cqrs]: https://martinfowler.com/bliki/CQRS.html

The reason why this is a tricky engineering problem to solve is that we are
bordering the land of a 1:1 ratio.

The nice thing about the hierarchical date-based approach is that it allows for
some flexibility in how much you would like to optimize for reads vs. writes
without turning into an either-or decision.

## Addendum II: On general ranged data

This article was written with date-based table records. There is nothing
stopping someone from taking a more general approach to partitioning other
types of columns!
