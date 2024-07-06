+++
date = 2024-07-07T00:31:35+02:00
title = "A common problem with ADR implementations"
description = "Architectural decision records are great. But you need to define at which scope they operate."
tags = []
slug = "the-adr-problem"
+++
In the article [Scaling the Practice of Architecture,
Conversationally][scaling-arch] by Andrew Harmel-Law he talks about the concept
of [Architectural Decision Records (ADRs)][adr] as a way to align and document
architectural decisions.

[scaling-arch]: https://martinfowler.com/articles/scaling-architecture-conversationally.html
[adr]: https://martinfowler.com/articles/scaling-architecture-conversationally.html#adr

In short, an ADR is a record stored in a central _log_ where architectural
decisions are documented. Usually, the decision log is checked into version
control somewhere.

A record includes things like what the decision was, what alternatives were
considered, the consequences of the decision, and the context that led up to
it. Commonly, an ADR also has a URL that makes it easy to share it in
conversations.

Generally, I like ADRs. I think they solve multiple problems by

* giving a team a tool/template that forces them to make clear, actionable,
  documented architectural decisions.
* making it easy to refer to previous decisions.
* allowing engineers to quickly understand the architecture when joining a
  team.
* reducing the number of WTFs for people joining the team.

## The problem with ADRs is scoping

My biggest pet peeve with an ADR log is that I keep seeing people want to
implement one without having a well-defined scope. Since [architecture always
happens at multiple scales][arch-scale], scoping must happen before
implementing an ADR log into your team. Scoping happens on two dimensions:

 * **Vertical scoping (scale):** Should the decisions involve microservices,
   how you build individual applications, or how you organize your classes and
   functions and how they integrate? Or all?
 * **Horizontal scoping:** Are there certain microservices that should not be
   part of the decisions? Maybe certain microservices are owned by another
   department, etc. Or should all architectural decisions cover all Java and
   Python applications or just Java?

[arch-scale]: {{< relref "2024-07-03_architecture-at-multiple-scales.md" >}}

Where to draw the lines on scoping touches upon the topic of "alignment vs.
autonomy". The larger the ADR scope is, the more tedious it will be to make
decisions and get a full picture of all the decisions taken. On the other hand,
if you have multiple logs at different scopes, there is a risk the decisions
start to conflict with each other. [Which problem(s) are you trying to
solve?][solution-vs-problem]

[solution-vs-problem]: {{< relref "2024-07-06_the-problem-domain.md" >}}
