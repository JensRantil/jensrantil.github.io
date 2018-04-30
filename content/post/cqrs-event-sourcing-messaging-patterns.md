---
title: "CQRS+Event Sourcing Messaging Patterns"
description: |
    Designing a decoupled, message based, system based on the CQRS pattern
    together with event sourcing require some thought. Since I've been thinking
    about it for a while now, I thought I'd share some thoughts so far.
date: 2013-05-26
tags: ["cqrs", "event sourcing", "distributed architecture"]
draft: false
---

CQRS+Event Sourcing Messaging Patterns
======================================

This post is partially related to my [previous blog
post](|filename|CQRS-time-to-rewind.rst) about
[Rewind](http://www.github.com/JensRantil/rewind) and
[Gorewind](http://www.github.com/JensRantil/gorewind).

Designing a decoupled, message based, system based on the
[CQRS](http://martinfowler.com/bliki/CQRS.html) pattern together with
[event sourcing](http://martinfowler.com/eaaDev/EventSourcing.html)
require some thought. Since I've been thinking about it for a while now,
I thought I'd share some thoughts so far.

CQRS
----

First let's think about the way information conceptually flows in a CQRS
system:

> Client issuing a command -&gt; Command -&gt; Command Handler -&gt;
> Event -&gt; Event Listeners/Projections

For now, we are not dealing with event sourcing and an event store.

Some definitions that will bring this blog post forward:

Command

:   A data structure instance with a command name in imperative, ex.
    `CreateBlogPost`. Most certainly it contains additional parameters
    such as URL for the blog post and it's text body.

Command Handler

:   The architectural instance that receives commands, checks their
    validitity and converts the command to an *event*. A command handler
    is optimized for fast validation/writes. If a command is valid, it
    is then published to all the event listeners that are interested in
    the event. It can also publish errors as events. See Asynchronicity
    and feedback loops\_. A command handler also guarantees that only a
    single command can modify an [aggregate
    root](http://en.wikipedia.org/wiki/Domain-driven_design#Building_blocks_of_DDD) concurrently.

Event

:   Most of the times, an event is the result of a command \[1\] \[2\]
    and is named as command, but in past tence. Example:
    `BlogPostCreated`. It is be debatable whether a single command can
    yield at most one event of it's allowed to yield multiple ones.

Event Listener

:   An architectural instance that receives events and does something
    with them. The most common case is to create a projection (for
    example, of blog posts) that quickly can be queried. In terms
    messaging event listeners are usually simply subscribers in a
    pubsub setup.

### Asynchronicity and feedback loops

The information flow above does not show any feedback loop back to
*Client issuing a command*. The CQRS pattern leaves that feedback loop
to the implementer. So the question is **how should a client know
whether a command succeeded or not?** There are different paths an
implementer can choose:

**Case 1: Command feedback by synchronous validation.**. The
command-issuing client sends its command to a command handler. It then
waits for the command handler to return with "Accepted" or "Failed:
&lt;Reason&gt;". This solution is probably the simplest and that CQRS
beginners are most comfortable with since it is similar to how
validation commonly is done through HTTP API calls. The downside is that
it is synchronous, pushing commands might take longer time. More so,
there's the choice of having another dependence or not.

**Case 2: Command feedback by forward event.** The command-issuing
client sends its command to a command handler. It immediately receives a
"Command received" response. The command handler later validates the
command. If validation passes it generates the expected event(s). If the
validation fails, an error event (ex. `BlogPostCreationFailed`) is
published. The client UI can later decide to poll/query for command
status, or even have the command state pushed out to it (if possible).

To be able to query whether a command failed or succeeded the client
need to have a unique ID for the command. This can be generated either
by the client or the command handler. The latter obviously will require
some feedback loop back to client on command invocation. A basic UUID
will suffice.

**Case 3: Command feedback by silence.** The command-issuing client
sends its command to a command handler. It immediately receives a
"Command received" response. In the case of blog post creation, a new
blog post will show up when the client queries the system for all blog
posts. If blog creation failed, a new blog post will obviously not show
up. The downside of this case is that the client has no idea to know
*what* went wrong.

**Case 4: Command feedback through a separate workflow.** In the case of
using event sourcing, events are persisted. If the command-issuing
client is one that might trigger a lot of errors, you might not want to
generate error events in fear of a client generating massive amounts of
validation errors and filling up the event store. To remedy this, one
approach would be to create a separate asynchronous pipeline for
validation errors. An idea would be to populate a cache with validation
errors and invalidate them with a
[TTL](https://en.wikipedia.org/wiki/Time_to_live).

There is nothing that says the above cases are mutual exclusive. In
fact, they can be combined, but as always there will be an increase in
complexity.

### Who is "Client issuing command"?

Case 4\_ above brings up another question; **who is "client issuing
command"?**.

If the client is a customer that creates issues commands through an API,
we should probably expect more validation errors. Customers usually
don't have as much domain knowledge as the upstream systems' owner.

If the client is simply your own web application's reaction to an HTTP
request, basic validation can be done in the web application that
catches 99% of all validation errors. The downside of this is that
validation logic will partially have to be doubly implemented. If a two
tier validation is implemented, simply dropping invalid commands (case
3\_) might definitely be an option.

A variation of having a web application is to have a GUI that only
enables commands that are possible. Maybe the GUI hinders a user to
change title of a blog post unless a blog is actually selected. If the
GUI prohibits 99% of the validation errors, case 3\_ might again be a
good candidate.

A common CQRS question is also how errors immediately are presented when
a command is issued. The common answer is; They don't. Many CQRS
proponents argue that 99% of commands will go through, and a GUI should
simply expect that blog post was published. There are multiple ways to
later tell the user something went wrong. For web applications, some
would argue that the user might as well simply reload the webpage to
update the latest blog posts if something goes wrong. There's a lot to
say about asynchronous UI, but I think I'm going leave it at that for
now.

Event Sourcing
--------------

Adding event sourcing to a CQRS pipeline makes things look something
like this:

> Client issuing a command -&gt; Command -&gt; Command Handler -&gt;
> Event -&gt; Event Store -&gt; Event Listeners/Projections

where an event store persists all events to disk and makes them
queryable.

Most commonly, an event store also handles groups of events so that they
can be grouped based on [aggregate
root](http://en.wikipedia.org/wiki/Domain-driven_design#Building_blocks_of_DDD).
This makes it possible to quickly get up to speed with a certain
aggregate root instead of reading through all events historically.

In Asynchronicity and feedback loops\_ we talked about the feedback loop
of command validation. Event sourcing brings other architectural
decisions to the table when it comes to feedback loop from the event
store:

### Failing disk writes

Previously we've only dealt with the fact that network could go down.
Luckily ZeroMQ (or similar technologies) makes sure that either a
messages delivered once fully, or not at all.

However, introducing an event store yields a new set of issues; syncing
an event store to the disk can fail because the disk is full, or because
it's broken.

### State (in)consistencies and life cycles

Before we talk about about feedback loops we need to talk about state in
a CQRS/event-sourced system. Generally state is stored in the following
parts:

Event handlers/projections

:   Receives events and builds state (performing a left fold of
    the events). This state is used for querying and can be thrown away
    to be rebuilt. This is the most recyclable state there is.

Event store

:   Stores all events. Receives events from command handlers.

Command handlers

:   Stores state that is required to make fast validation.

From what I've understood, an event store is supposed to be the primary
source of truth for an event sourced system. I've been fond of this idea
because it allows for event and command handlers to have short
lifecycles and come and go by demand, while the central event store can
sustain long slow lifecycles.

Interestingly, there is little online documentation on how command
handler state is handled in an event sourced CQRS system. So, here are
some of the different design choices that I've been considering:

**Case 1: No dependence.** Command handlers persists their state fully
separate from the event store. If anything goes wrong with events being
persisted, command handler state and event store might become
inconsistent. This is an inconsistency that might be hard to correct.

Also, if command handlers in case 1 uses a relational database, we are
back to where we started with trying to [avoid heavy schema
migrations](|filename|CQRS-time-to-rewind.rst) on system upgrade.

**Case 2a: Command handler builds state from event stores published
events.** Under the assumption that an event store only published events
that have been persisted, this means that event handler state always
will be consistent with the event store. It will also allow command
handlers to easily be upgraded, and easily be sharded if needed.

There are two downsides with the solution; Firstly, just like with case
3\_ no error will be published by the event store in case something
failed. Choosing a good timeout will be hard. Secondly, a command
handler will have to incorporate locking strategies to not allow two
commands to pass through before the first command's equivalent event
comes back, essentially making it synchronous with respect to event
store writes.

**Case 2b: Command handler builds state from their generated events.**
This, too, assures command handler and event store will be consistent,
are easily upgraded and sharded if needed. If combined with synchronous
write commands to the event store, the event store can respond with
"written" or "error". This makes it possible for the command handler to
know whether it should apply the event to its internal state or not.

### (Go)Rewind's implementation

[Rinat Abdullin](https://twitter.com/abdullin), a big CQRS proponent,
[hinted](https://twitter.com/abdullin/status/291827247210459136) that
most his code uses async communication as much as possible. Still, I
decided to stick to synchronous writes (case 2b\_) to the event store
for simplicity. Asynchronicity could be added to the write client within
if needed, I thought.

*Heck, rereading this blog post I notice it's a bit unstructured. I hope
you get the point, though! Feel free to make comments below. I'd love to
hear you input on this.*
