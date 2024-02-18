+++ 
date = 2024-02-16T14:00:35+02:00
title = "A maturity model for data-driven teams"
description = "Gathering and presenting metrics is not the end goal. Acting on it regularly is."
tags = ["metrics", "data-driven", "observability", "service levels"]
slug = "a-data-driven-maturity-model"
aliases = ["metrics-maturity"]
+++
I recently read the excellent article [Data is not a
Strategy][data-not-strategy]. It reminded me that I've been wanting to share
some of my own learnings and thoughts when it comes to data-driven teams:

[data-not-strategy]: https://www.amorphousdata.com/blog/data-is-not-a-strategy

I was part of a big push to introduce service levels at my previous job. The
objective of the project was to make our company data-driven when it came to
operational excellence. A thing I kept seeing was that many people saw the
project as a _technical_ project; gathering metrics, creating tooling for
defining SLIs/SLOs & dashboards, etc. We did all of that work, but still the
project did not succeed. Why? I kept reminding people that

> Success for this project is when every team looks at their Service Levels
> dashboard(s) at least once per week and act on them.

It turns out that when it comes to making a team data-driven (KPIs,
Observability, Service Levels...), having all the collection and tooling in
place is _not_ the end goal. **The end goal is for people to use data
regularly and _have data guide their decisions_.** From this perspective,
getting the technical foundation in place is easy. But [changing the
behavior][technical-social] of people is the more important, and harder,
problem to solve.

[technical-social]: https://blog.glyph.im/2024/02/let-me-tell-you-a-secret.html

Based on what I have seen, I think a team's journey to become more data-driven
loosely follows this path:

 1. **Collection.** (technical) Gathering data.
 2. **Query tooling in place.** (technical) Having tools in place to execute
    one-off queries.
 3. **Ad-hoc queries for deeper understanding.** (behavioral) Teams are now
    executing one-off queries to understand how something works in detail.
    This makes them answer specific questions they might have.
 3. **Some project(s) have clearly defined targets.** (behavioral) For certain
    projects where it is easy to measure an outcome, "current status", (where we
    are today, ie. 10% drop in user signup) & "target goal" (where we expect to
    end up, ie. reduce user signup drops by 20%) is documented. However, at
    this stage, the team never goes back to see if they hit the target.
 5. **Some project(s) are looped back during the finish line to check if they met
    the target.** (behavioral) Same as above, but for certain projects, the
    team goes back to the initial target and checks whether the target was met
    or not.
 4. **Dashboards in place.** (technical) Dashboards are generally a
    prerequisite to standardize on certain metrics. Until now, metrics are
    queried for ad-hoc and are not as easily accessible.
 6. **Regularly looking at metrics.** (behavioral) This is where there are
    rituals in place to look at data regularly. Teams learn things but
    generally don't act on them. Dashboards are almost a prerequisite for this.
 7. **Regularly adjusting for missing data & metrics.** (behavioural &
    technical) Certain teams get stuck looking at predefined dashboards. A
    common fallacy is to have a centralized platform team define metrics for
    all teams. A true metrics-driven team creates metrics tailored to _its_
    problems & domain.
 8. **Regularly acting & course-correcting based on metrics.** (behavioural)
    This is where a team not only learns new things but regularly asks
    themselves "Do we need to act on this metric?". This also includes tracking
    the progress of projects through data.
 9. **Most or all projects are naturally data-driven.** (behavioral) Most
    projects now have clear "current status" and "target goal". Tracking
    the progress of projects by comparing them to their target is a natural part of
    executing a project. Once those projects are delivered, you use data to
    verify the project delivered according to the initial target set out.
    Finally, data is used to understand & learn from why a failed project did
    not succeed.

What's interesting is that all the technical-only steps above _don't add any
value_. The steps that actually _do_ add value are the behavioral changes. As
such, I have come up with a Metric Maturity model that so far seems to apply
pretty well:

 1. **Ad-hoc queries for deeper understanding.**
 2. **Some project(s) have clearly defined targets.**
 3. **Some project(s) are looped back during the finish line to check if they
    met the target.**
 4. **Regularly looking at metrics.**
 5. **Regularly adjusting for missing data & metrics.**
 6. **Regularly acting & course-correcting based on metrics.**
 7. **Most or all projects are naturally data-driven.**

If you want your team to improve on their Service Levels, Observability, KPI
journey, I highly recommend asking yourself where you are in this maturity
model and how to take your team to the next level.
