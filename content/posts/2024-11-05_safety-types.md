+++
date = 2024-11-05T16:19:35+02:00
title = "Reliability vs. Resilience"
description = "There are two types of safety."
tags = ["safety", "site reliability engineering", "testing"]
slug = "safety-type-1-and-2"
+++
In safety systems engineering (SSE) people talk about "safety type 1" and "safety type 2". The first one is about prevention & **reliability**, the second is about **resilience**. Type 1 has been around for a long time, and type 2 is [fairly new][holnagel-2015].

[holnagel-2015]: https://www.england.nhs.uk/signuptosafety/wp-content/uploads/sites/16/2015/10/safety-1-safety-2-whte-papr.pdf

## Prevention will not save us

Software systems (and software companies) are complex. And for complex systems, type 1 safety (prevention) will not save us. Three key reasons:

**Reason 1a:** It's impossible to prevent all failures from happening in a complex system. Many of them are [unknowns][unknown-unknowns] and we [can't know them beforehand][latent-errors]. This makes it impossible to prevent them from ever happening. You cannot write unit tests for all potential error scenarios you don't know about.

[unknown-unknowns]: https://en.wikipedia.org/wiki/There_are_unknown_unknowns
[latent-errors]: https://how.complexsystems.fail/#4

**Reason 1b:** The context around a system is never static. There is an assumption that all failure is introduced by an operator. But this is [not always the case][temporal-proximity]; For example, load changes over time, new users are registering, auto-scaling might happen, third-party providers might be unavailable, we run out of memory, or we run out of memory in our database. A system is dynamic on many dimensions, and many things can happen.

[temporal-proximity]: https://how.complexsystems.fail/#6

**Reason 2:** As long as an operator is making changes to a system, [mistakes *will* occasionally happen][action-gambles]. They can't fully be prevented. For example, every new deployment of some software runs the risk of breaking it. However, you _can_ reduce the _likelihood_ of mistakes happening. This is what type 1 has focused on.

[action-gambles]: https://how.complexsystems.fail/#10

## Resilient systems save us from unprevented errors

Safety type 2 instead focuses on resilience. It does not entirely replace safety type 1 - there is still value in automated checks in CI/CD - but the insight is that they will _not_ prevent all errors. Type 2 instead tries to make sure that **given that something is broken, we make sure to minimize the impact it has on the business**. Safety investments must be balanced between type 1 and type 2. In my experience, most companies focus too much on type 1.

Generally, companies that are resilient to errors handle unprevented errors much better. In a way, if you have a company that is good at safety type 2, you don't need to focus too much on prevention. For example, let's say that a change to a software system is first rolled out to 0.1% of a random subset of users, and that change can automatically be rolled back within 60 seconds. If the change has an unprevented bug, the bug has almost no negative impact on the business.

## The type 1 to type 2 shift

The shift from type 1 to type 2 has many implications. Here are some of the shifts that I have seen:

 * Service levels: There is a shift from talking about system quality (availability, latency, etc.) as "the system is either up or down" to "the system availability is X%".
 * The organization starts to understand that there can be a difference between a deployment of a system and a release of a feature.
 * Rollout strategy for new features is early on a key part of the development process. This includes working with things like staggered rollouts, random sampling & feature flags.
 * The time it takes to roll back a system becomes more important than preventing errors in the system. When an organization realizes that the details around rolling back are very error-prone, they realize that forward rollbacks are much simpler. They then focus on reducing the general time to deploy.
 * A stronger focus on the observability of user impact in production (service levels) over "if CI/CD passes, it works".
 * A stronger focus on [shipping things to _production_ over "if it works on staging, my work is done"][staging].
 * A stronger focus on getting smaller changes out in production as soon as possible (to know it's working) over weeks of work to prevent all possible bugs.
 * An organization celebrates learning from mistakes and is blameless.
 * A stronger focus on DevOps as a Culture; Developers are more involved with the rollout and how a system is being used by customers.
 * Incident training is a natural part of daily work - practicing for things going bad, because they eventually will.

[staging]: {{< relref "2024-05-12_on-staging-environments.md" >}}

The implication of shifting towards safety type 2 is also increased agility; You are resilient to experiments with negative outcomes.

## Further reading

 * [Richard Cooks's "Resilience In Complex Adaptive Systems: Operating At The Edge of Failure"][cook] from Vecolity 2013 was my first introduction to these ideas and they have followed me since.
 * [The Theory Behind Understanding Failure][failure] by Evan Smith.
 * [How Complex Systems Fail][complex-failure] by Richard Cook.

[cook]: https://www.youtube.com/watch?v=PGLYEDpNu60
[failure]: https://iamevan.me/blog/the-theory-behind-understanding-failure/
[complex-failure]: https://how.complexsystems.fail

{{< notice tip >}}
Heads up! [I offer consultancy services][services] in this space. Don't hesitate to reach out if you would like me to help your company improve when it comes to reliability, resiliency, architecture feedback, on-call, alerting, or incident training. :wave:

[services]: {{< relref "/pages/services" >}}
{{< /notice >}}
