+++ 
date = 2023-05-03T12:50:41+02:00
title = "The downsides of batch APIs"
description = "Many small API calls are usually better than one large one."
tags = ["architecture", "api", "simplicity"]
slug = "downsides-of-batch-apis"
+++

When an HTTP API is too slow to call repeatedly I have seen engineers
immediately turn to making the API *do more in one unit of work*. I think this
pattern can be very harmful, and have many battle scars from this, so I thought
I would write a post about it.

## An example

Let's start with example: You have a web service that stores TODO items. It has
an API endpoint, `POST /todo`, which gets called to add a new TODO item. Here
is an example request/response:

```
POST /todo
{text: "Do laundry", "completed": false}

200
{"msg": "Saved TODO!"}
```
(300 ms)

## A throughput bottleneck enters the stage

The API works great until your TODO service has turned into a hugely successful
TODO SaaS which allows users to import their TODOs from their previous TODO
platforms. With the click of a button, we now want users to be able to import
10,000 TODOs from the competitor. The immediate problem? Importing them would take

    10,000x300ms = 3,000,000 ms = 3,000 seconds = 50 minutes

. 50 minutes is a long time!

## The batching solution

The go-to solution by many is to modify the API endpoint above (or
introduce a new "ingest API endpoint") such that it has a larger unit of work.
In this case, we modify it to take a *list* of TODOs instead:

```
POST /todo
[
    {"text": "Do laundry", "completed": true},
    {"text": "Fix flat tire", "completed": true},
    {"text": "Write that love letter to Rita", "completed": true},
    {"text": "Call my best buddy Brad", "completed": true},
    {"text": "Do the dishes", "completed": true}
]

200
{"msg": "Saved 5 TODOs!"}
```
(500 ms)

The assumption here is that the API roundtrip is the problem - so doing a
single API roundtrip (and usually a single roundtrip to the underlying
database), we sped up the API endpoint a _lot_.

At a glance, this solves the problem in a seemingly simple way! Suddenly we
have one roundtrip to the API instead of 10k. Sure, the time takes a little
longer, but that's expected since we _are_ storing more activities than a
single.

## The Costs

However, contrary to common beliefs, the above-described solution has many
hidden downsides that incur future implementation, maintenance, and operational
costs:

**Validation semantics complexity** (implementation). Every time you make an
API call and validation fails, you likely need to start returning a _list_ of
validation errors including _which_ (list index) item failed validation and
how. This turns into one additional thing the API caller must handle.

**Behaviour semantics confusion** (implementation). The API caller will need to
read the documentation (if there is some!) to see what happens if _one_ of the
TODOs aren't passing validation. Is it storing all other TODOs? Or are none of
them stored?

**Debuggability and understandability** (maintenance). Generally, if something
goes wrong (weird HTTP response code returned), the caller will spend a
significant amount of time trying to figure out _which_ of the TODOs, if any,
was faulty. Mapping a single TODO to a single API call makes debuggability and
understandability much easier.

**Code complexity** (maintenance). This is a minor one, but from now on we need
to iterate over a list of TODOs in our API endpoint source code everywhere;
validation, storing, logging, counting, etc.

**Memory/CPU bottlenecks** (operational). There is a risk that you have some
user who decides to import 100 million TODOs. Suddenly, your application runs
out of memory and starts crashing - impacting your other users. You can of
course set upper limits on request body size and/or number of TODOs (best
practice!). Now you need to incur the cost of maintaining documentation of that
limit...

**Worse observability** (operational). Your latency metrics can't be trusted as
much anymore. A key thing when working with performance is to reduce the
variability/variance of API call latencies. Without that, you will not be able
to trust your latency metrics. With the batching solution above, you will have
no idea if latencies spiked because your service was overloaded - or someone
simply decided to import 1 million TODOs in one giant API call.

At `$previousJob`, I had to bucket my latency metrics by list size to get a
better feel for whether our systems were having issues, or users simply
submitted larger units of work. Unnecessary complexity!

**Horisontal scalability issues (operational).** The idea with horizontal
scalability is that you can throw more machines/service instances at a problem
to increase throughput. Generally one uses a load balancer for this. If you are
working with large requests, the work will not be spread evenly.

([Even distribution of load][lb-strategies], particularly for uneven unit of
work is a classically _hard_ distributed systems engineering problem - let's
not go there...)

[lb-strategies]: https://www.youtube.com/watch?v=FC0DARpayhw

**Limit creep** (maintenance). Strictly this isn't a problem (and possibly this
is [slippery slope][slippery-slope]), but I can't help to mention that once
you've opened up the can of worms of working with list/request limits, there is
a strong risk you will simply start bumping the limit over and over again until
the above issues grow in magnitude. You are essentially shooting yourself in
the foot slowly over time. Saying no to batching from the start is one way to
avoid this.

[slippery-slope]: https://en.wikipedia.org/wiki/Slippery_slope

**Virality of batching** (?). Finally, what I have observed is that once you
start doing a larger unit of work in your public API, a larger unit of work also
starts creeping into every corner of your backend systems. Your API perimeter
team will start asking all internal services to support batching. Suddenly you
have the above-mentioned issues all over your backend and not just at the
perimeter.

## An alternative

Really, the problem we have here is one of [queueing theory][qt] and [Amdahl's
law][amdahl]. There are two routes we can take to solve our slow ingestion:

 * **Improve the unit of work.** This is what we did above!
 * **Parallellize the work.** This is what I am proposing to do below.

The latter usually comes with none of the above costs and pushes complexity to
the calling client. Instead of making _one API call with 10k TODOs_ we make
_10k API calls, each with a single TODO_.

There is a problem with the above, though; An API rarely supports 10k
concurrent API calls, particularly until it has scaled up (using auto-scaling,
which you have in place, right? 😉). There are ways to combat this:

 * **Putting a limit on concurrent API calls in the client.** A [counting
   semaphore][cs] is one way of doing this. A group of threads/coroutines
   popping from a queue is another.
 * **Making API calls [idempotent][idempotency] and implement retries.** Make a
   timed out, or failed, request retried without having duplicates. Usually,
   this is done by the client submitting the identifier of the TODO to avoid
   duplicates.  This has the added benefit of adding resiliency - if your
   service has a general hiccup, this might save you big time!
 * Adding **rate-limiting** to the server to make sure it doesn't get
   overwhelmed by many API calls.

[qt]: https://en.wikipedia.org/wiki/Queueing_theory
[amdahl]: https://en.wikipedia.org/wiki/Amdahl%27s_law
[cs]: https://www.guru99.com/semaphore-in-operating-system.html
[idempotency]: https://en.wikipedia.org/wiki/Idempotence

## When is batching a good idea, then?

Batching _can_ be useful if you want to make sure that all TODOs are
added [atomically][atomicity]. I.e. "either zero or all TODOs were added".

[atomicity]: https://en.wikipedia.org/wiki/Atomicity_(database_systems)

However, there is a way to do this in a different way by using a transactions
API similar to database transactions:

 1. `POST /todo/start?transactionId=abc123`
 2. `POST /todo?transactionId=abc123`
 3. `POST /todo?transactionId=abc123`
 4. ...
 5. `POST /todo?transactionId=abc123`
 6. `POST /todo/end?transactionId=abc123`

This does not avoid _all_ problems above, but some. But I would first start
challenging the requirement if atomicity is truly needed and worth it...
