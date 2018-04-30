---
title: "Bootstrapping: CouchDB as event store"
description: "Bootstrapping a project that uses event sourcing? Have a look at CouchDB."
date: 2013-09-02
tags: ["cqrs", "distributed-architecture", "CouchDB"]
draft: false
---

Bootstrapping: CouchDB as event store
=====================================

I've previously written about [what event sourcing
is](|filename|CQRS-time-to-rewind.rst). Reading about it, you might
think "heck, sounds great! But how do I get started?". This blog post
will propose a simple way.

A Minimum Viable Product
------------------------

The concept of a [minimum viable
product](http://en.wikipedia.org/wiki/Minimum_viable_product) states
that you shouldn't do more than absolutely necessary before releasing a
product. You need to release it when it's just good enough. If it's
received badly, you haven't invested too much time or energy into it.

So, how can you get started with event sourcing quickly and without
spending a lot of time coding an event store? Here are a couple of
options:

-   Use an append-only log file for the events. This has the advantage
    of being simple. The downside is that querying it slow (requires
    seeking it) and code to build state need to be handled
    fairly manually. It also means that you would have to handle
    checksumming and backup of data etc. yourself.
-   Have a look at [EventStore](http://www.geteventstore.com). It's a
    .NET event store that has both a hosted commercial as well as an
    open source implementation.
-   Consider using an RDBMS. RDBMSes do not, in general, have any type
    of notification framework for database changes/events. So either, it
    would be up to you to poll the database, or you would have to use
    some external notification framework (RabbitMQ etc.).

Recently I've been curious to see whether
[CouchDB](http://couchdb.apache.org) holds true as a viable event store
database. Event sourcing involves creating projections from events and
CouchDB's incremental map/reduce *views* sounded like a natural fit for
this.

Requirements
------------

The following were my requirements:

1.  Be able to store events as **incremental** state changes f various
    aggregate roots.
2.  Be able to store events as **unstructured data**. By that I mean
    they need to support various fields depending on event type.
3.  Query capabilities:

    I.  Be able to easily **query event chronologically grouped by
        aggregate root**. This would make it possible to create various
        timelines on an aggregate root basis.
    II. Be able to easily **query events chronologically independently
        of aggregate roots**. Together with "Listen to database changes"
        below, this would make it possible to build up complex states in
        external systems.
    III. Quickly create **prototypical projections**. This would make it
        possible to quickly query current state based on
        previous events.

    IV. **Listen for database changes.** This would enable me to push

    :   changes out to interested parties, as opposed to needing
        to poll.

4.  Support **atomic writes**. This is important to make sure that among
    concurrent writes of events, always only one will win.

A tentative implementation
--------------------------

So far I've been able to come up with an implementation that supports
all of the above requirements using CouchDB.

Let's look at three possible events for a simple adressbook:

<script src="https://gist.github.com/JensRantil/6416970.js"></script>
### Atomic writes and unique indexes in CouchDB

Consider the top level event properties:

#### \_id and aggregateType

`_id` contains three pieces of information separated by a colon (`:`).

-   Aggregate root type.
-   Aggregate root identifier.
-   Aggregate root version.

Let's look about them individually. To simplify, I'll start with the
version:

In event sourcing, an aggregate root moves from one version to another.
Each event increases the version of the aggregate root. While *type* and
*identifier* are immutable throughout the life cycle of an aggregate
root, version numbering is incremented. This means that concurrent
writes to a database can be done optimistically, failing only if a write
with the same `_id` was done previously.

The aggregate version is put at the end for increased readability of
`_id`.

If you intend to use CouchDB views to create projections of your events,
each event need to be specific to an aggregate type. There are multiple
ways of doing this:

-   **using an aggregate type field.** Simply setting
    `doc.aggregateType='contact'` for every event. This is a bit
    cumbersome and makes it harder to see what type an event
    happened to. The good thing is that a lot of disk space can be saved
    on this.
-   **prepending the aggregate root with a type, like in the
    example above.** While this would increase readability what the
    aggregate type the event is all about, it would increase the
    database size a fair amount. I have seen recommendations on the web
    to try to keep the `_id` small.
-   **make sure that every `doc.event.type` has a unique mapping to an
    aggregate type.** The event type `contactCreated` would obviously
    map to a contact. This solution would probably backfire eventually.
    I'd rather have an event type called `cescriptionChanged` instead of
    `contactDescriptionChanged`.
-   **having a single CouchDB-database for every aggregate type.** To
    keep the database in sync, I strongly suggest against this.

The aggregate type is put as the first part to easily distinguish what
event type we are working with when looking at events.

Inbetween the aggregate type and the version specifier, a unique
identifier is stored. It is unique throughout the lifetime of the
aggregate root.

#### globalId

globalId is an orderable ID that makes it possible to traverse through
the global order of events. In my examples I've used [type 1
UUIDs](http://docs.python.org/2/library/uuid.html#uuid.uuid1).

#### event

Holds the data that describes the event. event.type also contains a
string describing what type of event it is.

#### meta

This is a property not strictly related to the specific event, but
information that can be used for debugability. Examples are timestamps,
which client published the event, which user did it etc. The latter is
great information to create a highly auditable system.

### Event projection views

Using the previously described event schema, CouchDB's map/reduced based
views can be used to create most simple cases of projections:

Here's a design document that keeps track of the description of a
person:

<script src="https://gist.github.com/JensRantil/6417018.js"></script>
The secret sauce here is to use the aggregate root to to decide whether
to update the reduce state or not.

What a view cannot do is keep track of older versions of an aggregate
root. This requires building state in an external application that
tracks database changes. Good news is that this is fairly easy to do as
CouchDB ships with a [changes
API](http://guide.couchdb.org/draft/notifications.html). This makes it
easy for an external application to easily track state as events are
being published.

### Handling replication conflicts

One of CouchDB's unique selling points is *master-to-master
replication*. There's some cool stuff that this enables you to do. For
example you can easily implement syncing clients using libraries such as
[PouchDB](http://pouchdb.com) and
[TouchDB](http://labs.couchbase.com/TouchDB-iOS/).

Sadly, master-master replication comes with a cost; namely the fact that
it's possible that there can be replication conflicts if two or more
CouchDB instances changes a document and then sync. CouchDB uses
[MVCC](https://en.wikipedia.org/wiki/Multiversion_concurrency_control)
and automagically chooses a winner. Sometimes this might not be the
right winner. This happens you can [tell CouchDB that you prefer another
winner](http://guide.couchdb.org/draft/conflicts.html).

My example implementation above would not handle write conflicts very
well. It would be able to fix a basic conflict like this:

    1 -> 2 --> 3a
           \
            -> 3b

However, if a series of multiple events would conflict, it would be
impossible to recreate the different event history paths that might have
occured. The following conflicting events:

    1 -> 2 --> 3a -> 4a
           \
            -> 3b -> 4b

could mean either of these histories:

    1 -> 2 -> 3a -> 4a
    1 -> 2 -> 3a -> 4b
    1 -> 2 -> 3b -> 4a
    1 -> 2 -> 3b -> 4b

This could be problematic, as CouchDB could choose a corrupt event
history. Picking one event from one CouchDB source, and another event
from another CouchDB instance's line of history.

To remedy this, I would incorporate a `prevRevision` property for every
event. Every version of a CouchDB document would have a revision that
changes every time the document changes. By always refering to the
previous revision you would essentially have a single-linked history,
similar to the way [GIT](http://git-scm.com) works with its SHA-1's.

Other advantages of CouchDB
---------------------------

I've always been fond of CouchDB's different approach to dealing with
things as opposed to other databases. Here are a couple of other things
that are worthwhile to know about:

-   **Crash friendliness.** CouchDB uses an append-only file for
    it's data. To restore used up space a *compaction* need to
    take place. It's up the database maintainer to decide when a
    compaction happens. This append-only architecture means that CouchDB
    can crash at any time. In fact, the normal way to shut down CouchDB
    is simply to kill it.
-   **BigCouch.** BigCouch is a CouchDB proxy that sits in front of
    multiple CouchDB instances. It mirrors the CouchDB REST API as close
    as possible, but transparently uses real CouchDB instances
    as backends. This makes it possible to store huge amounts of data
    in CouchDB. The flipside is that
    [rereduce](https://wiki.apache.org/couchdb/Introduction_to_CouchDB_views#Reduce_vs_rereduce)
    steps in a view always need to take place in in BigCouch (which is
    usually not a problem).
-   **Commercial solutions**, such as
    [Cloudant](http://www.cloudant.com) and
    [IrisCouch](http://www.iriscouch.com).

An implementation
-----------------

I've started on an implementation of all of this, but I'm still trying
to figure out if it's too over-engineered or not :). Until then, I'll
keep it unpublished. Keep a lookout of [my Github
account](http://www.github.com/JensRantil) to see when it shows up!

Future improvements
-------------------

CouchDB has claimed to be "a a database for the web". It talks HTTP and
there's been numerous libraries that makes it possible to host a full
web application in a CouchDB instance. The means that CouchDB would
fully replace the classical web server (Apache, nginx etc.) setup.

Recently I've been trying to wrap my head around how [authorization
works in
CouchDB](http://blog.mattwoodward.com/2012/03/definitive-guide-to-couchdb.html),
especially when it comes to dealing with design documents. I'm not
entirely sure it would be possible to expose the whole event store
directly to the Internet. However, if this would be doable with correct
authorization it would allow some cool stuff such as fully hosting event
stored applications in CouchDB, possibly together with
[PouchDB](http://pouchdb.com).
