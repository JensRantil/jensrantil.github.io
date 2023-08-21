---
title: "A follow-up on CouchDB as event store"
description: "A different implementation of CouchDB event store."
date: 2014-03-25
tags: ["CouchDB", "cqrs", "distributed-architecture"]
slug: 2014-03-25_follow-up-on-couchdb-as-eventstore
---
I [recently](|filename|couchdb-as-event-store.rst) wrote about using
CouchDB as an event store. One issue that I mentioned briefly was that
my proposed solution would not work for a single aggregate root yielding
multiple key/values in a CouchDB view:

> What a view cannot do is keep track of older versions of an aggregate
> root.

Recently I've been revisiting this problem (because I find it fun to
think about) and have a slightly different solution to propose, namely
to store all events for a single aggregate in a single document. That
is, make the document have a list of events. This will solve all
previous requirements as well as:

-   Support versioning of aggregates in a single CouchDB view.
-   Support generating multiple key/values for a single aggregate root.
-   Make conflict resolution easier to deal with and reason about.

One argument against this solution is that CouchDB does not support
atomic document modifications. This means that a user would have to
first `GET` the document (with all events), append the new event and
then write the new document (`PUT`). With aggregate roots that has a lot
of events this would yield a great overhead in network latencies and
storage (since CouchDB is an append only database).

Good news is CouchDB has [update
handlers](https://wiki.apache.org/couchdb/Document_Update_Handlers) that
can be used to avoid the extra HTTP roundtrip. An update handler lets
you can define a URL that you make a single post to. The handler will
append the new event to the list and store the updated document.

I've heard somewhere that giant lists in a single CouchDB document is
not recommended. I wouldn't dismiss this idea because of that. In many
domains there aren't that many changes to an aggregate root after
creation. Imagine an adressbook contact as an aggregate root. I don't
think I've ever made more than ten changes to a contact. At the same
time, this CouchDB solution for storing event sourced aggregate roots
would probably not be viable if you had 10\^6 changes to an aggregate
root...
