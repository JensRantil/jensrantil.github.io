---
title: "I'm a State Engineer. Are you, too?"
description: |
    "Lifecycle" and "state" are two words not used often enough.
date: 2013-11-18
tags: ["architecture", "programming", "state", "distributed architecture"]
---

I'm a State Engineer. Are you, too?
===================================

TL;DR: We need to have a more thorough discussion about state and
lifecycles in our industry.

I recently revisited [The Twelve-Factor App](http://12factor.net) by
[Heroku](https://www.heroku.com). It's a great read if you are deploying
your own application, are interested in (organizational and/or
technincal) scaling or curious of best practices when it comes to
deployment.

As I was reading the manifest it struck me that there are two words that
I hear all too infrequently in our industry, namely *state* and
*lifecycle*. The words have different meaning, yet they are related in
so many ways. All state has a lifecycle, otherwise the state would not
be worth thinking of.

Software engineers are surrounded by *state* all the time. So are
software architects. In fact, state can flow through every layer of a
software stack. Not to mention how state can be spread out across a
plethora in a distributed system; databases, caches, queues etc. State
also applies to a wide range of scopes; within a function/method, within
a class, within a software component, within a distributed application,
or even an orchestration of distributed applications.

As software engineers we need to respect state and how inherently
difficult it to get it right. The majority of bugs are related to state
in one way of another. This is why we always need to formalize how and
where state is stored. Asking the question "Do we need the state?" is
also worth doing so often.

The *how* is important. How can we as software engineers minimize errors
due to state? Here are a couple of ideas:

**Use constants as much as possible.** Make it clear that a variable
cannot be changed. The [Erlang](http://www.erlang.org) and
[Haskell](http://www.haskell.org) programming languages go as far as not
even allowing changing the values of any variable. One needs to define a
new variable.

**Use immutable data structures as much as possible.** Slightly related
to the previous paragraph. This is especially important when state is
moving through a system. Sure, this will make systems slower in some
case, but use immutability by default and mutability only where it's
really needed. In [Erlang](http://www.erlang.org) all state sent between
components (called "processes") is immutable.

**Isolate state** and **minimize inter-state dependencies**. Make sure
that the implementation modifying state is isolated. This makes it
easier to get an overview of various states in the system and what makes
them transition into new states. Two ways of isolating state are two put
it in a separate (possibly, green) thread or, even better, binding to a
function/method scope.

Isolation of state can be an argument to decouple components of a bigger
system into smaller isolated ones. Paradoxically, isolating state can
also introduce other issues. A common issue of decoupling state into
distributed components is that state transitions can fail due to network
and/or timing issues.

**Make state shortlived.** The fewer state changes the easier it becomes
to reason about them. This is where state *lifecycle* becomes an
important concept. A shortlived state makes programmers less prone to
introduce errors. Maybe your state can be computed from some other
external state.

The [Erlang](http://www.erlang.org) programming language brings the
concept of "supervisors" to the table. This enables you to do exactly
this.

**Start thinking about asynchronicity.** An async call between component
leads to a looser coupling. It also means that unexpected states will
not break other states.

**For distributed systems; learn about the CAP theorem.** The
[CAP](https://en.wikipedia.org/wiki/CAP_theorem) theorem states that in
the case of a network partition (P), you have choose between
[availability](http://basho.com/riak/) (A) and
[consistency](https://github.com/coreos/etcd) (C). The concept of a
[CRDT](http://pagesperso-systeme.lip6.fr/Marc.Shapiro/papers/RR-6956.pdf)
can also be interesting to know about if you'd like to relax consistency
a bit.

**Have a look at the concepts of CQS, CQRS, event sourcing.** Don't
worry, you don't necessarily have to use them. But give them some
thought for a moment.
[CQS](https://en.wikipedia.org/wiki/Command%E2%80%93query_separation)
and [CQRS](http://martinfowler.com/bliki/CQRS.html) are kind of similar.
[Event sourcing](http://martinfowler.com/eaaDev/EventSourcing.html) can
be used with CQRS to make things really badass. Are you optimizing for
reads or writes? Choose.

This list above is definitely not exhaustive and I'd love to get more
input in the comments below.

Over the past couple of years, learning new programming languages and
studying distributed systems engineering has given me a huge toolset
when it comes to reasoning about state. This is the one reason I
encourage software developers to learn about new software paradigms and
[one programming language per
year](http://blog.teamtreehouse.com/learn-a-new-programming-language-every-year).
My greatest insight into how state can be dealt with has definitely been
looking into how the [Erlang](http://www.erlang.org) programming
language. A good resource when it comes to distributed systems is
reading the [ZeroMQ Guide](http://zguide.zeromq.org/page:all).

Lately, I've been thinking about retitling myself as a "state engineer".
Maybe you should, too? Feel free to discuss below or contact me [by some
other means](|filename|pages/about-me.rst).
