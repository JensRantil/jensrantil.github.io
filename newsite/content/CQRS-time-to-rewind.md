CQRS - Time to Rewind
=====================

date

:   2013-05-19 21:21

tags

:   cqrs, distributed-architecture

For the last year I've been thinking a lot about
[CQRS](http://www.cqrsinfo.com)
\[[1](http://martinfowler.com/bliki/CQRS.html)\], [Event
Sourcing](http://martinfowler.com/eaaDev/EventSourcing.html) and
distributed architecture using [ZeroMQ](http://www.zeromq.org). I first
stumbled across the concept of CQRS through the mailing list for a [nerd
meetup in Helsingborg](http://www.meetup.com/SoftPub/), Sweden. This led
me to a lot of CQRS
[reading](http://msdn.microsoft.com/en-us/library/jj554200.aspx) and
[videos](http://cqrs.wordpress.com/video/), and with that the Event
Sourcing data model.

To try out CQRS and Event Sourcing in practise, I started writing an
open source event store about a year ago. I named it
[Rewind](http://www.github.com/JensRantil/rewind). This also opened up
for me to try some concepts that I had never tried before \[2\].

CQRS and Event Sourcing
-----------------------

But first, let's Rewind ;). Rewind's
[README](https://github.com/JensRantil/rewind/blob/develop/README.rst)
does a fairly good job at an elevator speech for *CQRS*:

> Have you ever been nervous of all those DBMSs schema changes when you
> are deploying your applications? They are gonna take too long, or
> break backward compatibility? Have you ever thought "Crap, I wish I
> had stored that information since earlier"? Have you ever felt your
> writing patterns and your reading patterns differ a lot, making things
> harder to scale? Issues like these can be solved using *CQRS* and
> *event sourcing*.
>
> *CQRS* (Command-Query Response Segregation) is an architectural
> pattern that aims to solve these issues by splitting up your
> architectural system into two parts:
>
> -   A *write side* that takes care of validating input and optimizes
>     for fast writes. The write side takes commands and outputs
>     corresponding events if the command validates correctly.
> -   A *read side* that listens to incoming events from the write side.
>     The read side is optimized for fast reads and incrementally build
>     up state that can be queried fast.
>
> While not required, it is common to use messaging between the write
> and read sides. This means that the system will be in an inconsistent
> state from time to time. This is usually not an issue and came be
> overcome in various ways.

A couple of additional things to note about CQRS:

-   As I see it, it is the architectural equivalent of the CQS design
    pattern.
-   It is a pattern that decouples systems very well. This can have huge
    implications when it comes to testability.
-   It's also worth noting that there are some similarities between
    Domain Driven Design
    ([DDD](http://www.wikipedia.org/Domain-driven_design)) and CQRS.
    Most vocabularies in DDD are used in CQRS; ubiquous language,
    aggregates, aggregrate root, value objects, bounded contexts etc.

The README then states about *Event Sourcing*:

> A common pattern used together with CQRS is *event sourcing*. The
> concept can be summarized as using state changes as primary
> persistence, instead of the final state. The state changes are called
> *events* and they are generated by the write side and delivered to the
> read side.
>
> The events are persisted in an event store that sits inbetween the
> read and write side of things. It takes care of three things:
>
> -   persisting all events to disk.
> -   being a hub/broker replicating all events from the write to the
>     read side of things.
> -   allowind fast querying of events so that different parts of the
>     system can be synced back on track and new components can be
>     brought back in play.

Rewind
------

Question was, how would a CQRS/event sourced system behave in
production? Could it scale out? Could writes be partitioned? What about
fault tolerance? I was tired of heavy database schema changes, I wanted
a nouvaeu way of testing and question some of the common practices.

Enter [Rewind](http://www.github.com/JensRantil/rewind); Rewind was my
pet project for a [major part of
2012](https://github.com/JensRantil/rewind/graphs/commit-activity). It
was *a Python implementation of an event store that supported multiple
backends*. It really gave me an opportunity to try everything I wanted.

The development of Rewind halted at the beginning of 2013. From thereon,
I instead used the lessons I had learnt and rewrote Rewind's
functionality in [Go](http://www.golang.org). The project was named
[GoRewind](https://www.github.com/JensRantil/gorewind).

Within the next couple of blog posts I plan to write about what I've
learnt from these two projects; design decisions, testability, ZeroMQ,
developing in Go among other things.