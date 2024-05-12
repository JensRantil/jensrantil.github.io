+++ 
date = 2024-05-12T15:44:35+02:00
title = "On staging environments"
description = "The cost-benefit ratio for your staging environment is probably higher than you think."
tags = ["staging environment", "testing"]
slug = "on-staging-environments"
+++
> The ultimate quality assurance is when customers get their hands on your
> software and actually try it. _That's_ when you know if your software does what
> it's supposed to do or not. This happens in production.

Every technical decision has a tradeoff, but certain things are
rarely challenged in our industry. Having a staging environment[1], and having
every change go through the staging environment, are two of those things.

So, what is a staging environment? It is a full replica of a production
environment. Do you have a backend service running in production? Then you also
need that service in staging. Do you have a database in production? Then you
need a database in your staging environment. Etcetera. Most companies having a
staging environment require every change to first go through staging to verify
that the change works before hitting production.

{{< notice info "Many names" >}}
[1] A staging environment can have many names: staging, QA, pre-prod,
preproduction, testing, etc.
{{< /notice >}}

## Reasons for _not_ having a staging environment

There are multiple reasons why I consider having, and using, a staging
environment as wasteful. They can be summed up in three big categories:

 * A staging environment gives a false sense of safety.
 * It slows down developer velocity.
 * It has a high operational cost.

Let me explain:

### Not sustainable

As engineers, we are all encouraged to build up automated test suites (unit
tests, etc.) to make sure that tests can verify that today's behavior will work
in the future. Manual testing, such as the one used in a staging environment,
is frowned upon in our industry. Yet, why are we doing it? I think staging
environments encourage manual testing. If we want to Build Quality In(tm), we
need automated testing.  If we need automated testing, we need to stop manual
testing. A great way to stop manual testing is to not have a staging
environment.

### A false sense of safety

I have heard the argument "So, if we don't test it in staging - how do we know
if it works in production?". There is an assumption that everything that works
on staging will work in production. As most Site Reliability Engineers (SREs)
are aware of, this isn't true. By definition, a staging environment is
_different_ than production. Here are some common things that can differ
between staging and production:

 * The amount of data being stored.
 * Traffic patterns
 * Runtime configuration
 * Feature flags
 * And more...

**Believing that a change will work in production if it works on staging is a
fallacy.**

### "We need to test our infrastructure changes"

Infrastructure changes _can_ be safely done without a staging environment, but
it requires a different mindset. The key is to think about gradual rollouts and
routing of new functionality. See the bottom of this article for some
staging-independent ways to do this.

Here are some staging-independent ways to test things in production without
negatively impacting users:

 * Feature flags on users or accounts to route to different infrastructure.
 * [Weighted round-robin DNS records.][aws-weighted-dns]
 * [Partitioning of users based on identifiers in source code][source-sharding]
   to route to different infrastructure. For example "all users with UUID
   starting with '00' use the new cache cluster".
 * [Round-robin users in source code][rr-source] to different infrastructure
   components.

I think the engineers who are best at this, are the true DevOps engineers who
can freely move between being a developer and operations person. Knowing where
to introduce the new functionality gradually is key.

Being able to do the above requires a strong focus on good observability. How
will you make sure that your change doesn't break anything?

### Cost

A staging environment has infrastructure costs. For complex systems, this cost
can be significant. Every service you run in production must run in staging.
Every database running in production, must also run one in staging. Databases
can be expensive...

There is also the cost of maintaining a staging environment. This is either
salary costs for more engineers or slower development. See more below.

### Slower feedback cycle in the development of software

The DORA metric "lead time to production" is defined as the average time it
takes to get a change out in production. If every change must go through a
staging environment, it will significantly impact this metric negatively.

"get a change out in production" also includes rollbacks. If there is a bug
rolled out to production it will take much longer to revert that change if it
also needs to go out to a staging environment.

### Foundation for miscommunication

If you have ever worked at a company with a staging environment I am sure you
have occasionally been confused because the user you are looking for doesn't
exist in the environment you are looking at. You are looking at the wrong
environment. If there are multiple environments, communicating which
environment must happen in _every internal bug report conversation_:
Slack/IM/chat/e-mail conversation must include which environment. This has a
cost.

I have debugged issues for more than one hour only to realize that the issue
only happens in one environment but not the other.

### "But we need to test those UX changes"

I agree that getting feedback on UX changes can be a challenge. While it _is_
possibly to codify automated UX tests using Selenium and/or Playwright,
manually testing a UX is pretty much a requirement to get early feedback on how
a UX _feels_.

A full staging environment is _not_ a requirement to be able to do this. It can
be done by starting up a [frontend preview per pull request[pr-preview], and
have that frontend pointing to a production backend.

[pr-preview]:
https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html

A pull request environment as a full replica of a production environment has
all the same downsides as having a staging environment. I would avoid that.

#### "But we need to test the frontend changes with the backend changes"

Deploy your backend changes with backward compatibility. Then test your
frontend changes. Simple as that. Deploying a frontend and a backend change as
an "atomic" deploy is a bad practice anyway.

### "But we need to have it for security reasons"

Some companies implement a separation between staging and production data by
having a staging environment. There are other, cheaper, controls that can solve
that in a completely different way; Tag all users as either being a test user
or a production user. And introduce access control based on this tag.

It's also worth pointing out that having two environments will _not_ protect
anyone from leaking data between two production users which in my opinion is a
much more serious bug.

I think having a staging environment is a good example of [a security control
that doesn't consider other forms of risks][security-risks].

[security-risks]: {{< relref "2024-05-12_security-and-risk.md" >}}

## Ways to relax the dependency on a staging environment

Here are some staging-independent ways to test things in production without
negatively impacting users:

 * Partitioning users by using feature flags on users or accounts.
 * [Partitioning users based on identifiers in source code][source-sharding] to
   route to different infrastructure. For example "all users with UUID starting
   with '00' use the new cache cluster".
 * [Weighted round-robin DNS records.][aws-weighted-dns]
 * [Round-robin users in source code][rr-source] to different infrastructure
   components.
 * Gradual/staged rollouts such as "blue-green deployment" and "canary
   deployments".
 * Pull request environments to mostly test frontend changes.
 * Smoke tests to make sure a deployment rolled out properly.
 * End-to-end tests to make sure that important user flows work after a
   deployment.
 * Automatic rollback on errors.

[aws-weighted-dns]: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
[source-sharding]: https://github.com/JensRantil/java-canary-tools?tab=readme-ov-file#weightedshardedbuilder
[rr-source]: https://github.com/JensRantil/java-canary-tools?tab=readme-ov-file#weightedroundrobinbuilder

In the article ["Why CEOs are failing software engineers and other creative
teams"][ceo-fail], Gene Bond talks about how Creative Management has the goal
to to drive down the cost of failure, not the number of failures. This is
exactly what some of these tools do.

[ceo-fail]: https://iism.org/article/why-are-ceos-failing-software-engineers-56

## Reasons for _having_ a staging environment

I have seen staging environments being required for compliance reasons. If I
would end up in that situation, I would make sure to at least deploy to
production and staging in parallel, if I could.

## Closing thoughts

Certain workplaces have _more_ than one pre-production environment (hello,
banks! :wave:). I have seen banks internally having multiple environments
("staging", "testing", "qa", "pre-production"...) Suffice to say, everything in
this document applies to all of these pre-production environments
proportionally to the number of additional environments that need to be
maintained.

Having a staging environment can be useful for [town planners][town-planner].
But if a company values moving quickly over risk averseness, I would strongly
suggest to not have a staging environment.

[town-planner]: https://orghacking.com/pioneers-settlers-town-planners-wardley-9dcd3709cde7
