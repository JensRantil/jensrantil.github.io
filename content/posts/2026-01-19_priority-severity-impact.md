+++
date = 2026-01-19T16:14:35+02:00
title = "Incident priority, severity & impact"
description = "An actionable model on how to categorize incidents."
tags = ["Incident management"]
slug = "incident-priority-severity-impact"
+++
An [incident][incident] framework usually has the concept of an **incident priority**: priority 1 ("Systems are DOWN!"), priority 2 ("I can log in, but there is a bug."), etc. Incident priorities are mostly used for two things:

[incident]: {{< relref "2025-12-17_what-is-an-incident.md" >}}

**Operational:** To help operators and on-callers quickly guide them on how serious an ongoing incident is and help them prioritize their work. A low-priority (priority 3) incident can wait until after the weekend. For example, a high-priority (priority 1) incident means "all hands on deck" and possibly waking up your colleagues in the middle of the night.

**Strategic:** To be able to build statistics and see trends in incidents at a company[^1]. Are there more high-priority incidents this quarter than last? Are we getting quicker at coming back to a working state for our high-priority incidents (improved [resilience][safety-types])? Etc.

[safety-types]: {{< relref "2024-11-05_safety-types.md" >}}
[^1]: Here be devils! Statistics on incidents can be useful, but at worst, [they can be useless][goodhart].
[goodhart]: https://en.wikipedia.org/wiki/Goodhart's_law

## Priority levels

A common priority framework has a 3-level priority with recommended guidance on urgency. For example, I have seen something like this in on-caller playbooks:

1. **Priority 1**: Things are burning. Fix the issues as soon as possible. Don't hesitate to bring in, or wake up, _anyone_ who might be able to fix the issue. The on-caller will be paged immediately, regardless of the hour.
2. **Priority 2**: There is smoke, but no fire. Fixing this can usually wait until the morning. The on-caller will be paged during _awake hours_ (07:00-23:00).
3. **Priority 3**: There is a possibility of smoke and fire. This can usually be postponed until office hours. The oncaller will be paged during _office hours_ (Mon-Fri 09:00-17:00).

## A priority assessment framework

A common incident priority model I have used is based on **severity** and **impact**:

<table>
  <tr>
    <th style="background-color: #f0f0f0;">Impact \ Severity</th>
    <th style="background-color: #f0f0f0;">Low</th>
    <th style="background-color: #f0f0f0;">Medium</th>
    <th style="background-color: #f0f0f0;">High</th>
  </tr>
  <tr>
    <th style="background-color: #f0f0f0;">Low</th>
    <td style="background-color: #c6efce; text-align:center;">Priority 3</td>
    <td style="background-color: #c6efce; text-align:center;">Priority 3</td>
    <td style="background-color: #ffeb9c; text-align:center;">Priority 2</td>
  </tr>
  <tr>
    <th style="background-color: #f0f0f0;">Medium</th>
    <td style="background-color: #c6efce; text-align:center;">Priority 3</td>
    <td style="background-color: #ffeb9c; text-align:center;">Priority 2</td>
    <td style="background-color: #ffc7ce; text-align:center;">Priority 1</td>
  </tr>
  <tr>
    <th style="background-color: #f0f0f0;">High</th>
    <td style="background-color: #ffeb9c; text-align:center;">Priority 2</td>
    <td style="background-color: #ffc7ce; text-align:center;">Priority 1</td>
    <td style="background-color: #ffc7ce; text-align:center;">Priority 1</td>
  </tr>
</table>

**Severity** is defined as how bad the incident is in terms of functionality. Usually, an incident playbook has specific examples such as:

1. **Low**: Basic functionality is impacted. Maybe the product looks ugly (broken font?), but is fully usable.
2. **Medium**: Key functionality is impacted. For an online word processor, this might mean that the copy-paste functionality is broken.
3. **High**: Functionality impacting the entirety of the product: Unable to reach the product, unable to log in, etc.

Similarly, **impact** is defined as how many users or customers are affected by the incident, and how broadly it affects the business. Common impact levels are:

1. **Low**: A small number of users are affected, or the impact is minor and mostly inconvenient, with little business or customer-facing consequences.
2. **Medium**: A limited but significant group of users or customers is affected. Workarounds may exist, and the business impact is noticeable but contained.
3. **High**: A large portion of users or customers are affected, or the incident impacts critical customers, revenue, legal obligations, or brand reputation.

In my article ["Reliability vs. Resilience"][safety-types], I wrote about the value of minimizing the impact of bugs. If there is a bug, but no one is experiencing it, the bug is less serious. Having impact as part of the priority assessment makes it very clear that your organization values a resilient rollout of changes.

Also, it's worth pointing out that severity and impact are _estimates_. A recommendation I have given is the always lean on the higher end if uncertain. Better to be safe than sorry.

{{< notice info >}}
**Update:** I have written an addendum to this article. If you are curious, have a look at [The missed incident priority: The Near Miss][near-miss].

[near-miss]: {{< relref "2026-01-19_near-misses-priority.md" >}}
{{< /notice >}}

{{< notice tip >}}
Heads up! [I offer consultancy services][services] in this space. Don't hesitate to reach out if you would like me to help your company improve when it comes to reliability, resiliency, architecture feedback, on-call, alerting, or incident training. :wave:

[services]: {{< relref "/pages/services" >}}
{{< /notice >}}

## References

Here are some references you can use if you would like to read more about similar models:

* [PagerDuty's Incident Response severities](https://response.pagerduty.com/before/severity_levels/)
* [Honeycomb arguing against incident severities](https://www.honeycomb.io/blog/against-incident-severities-favor-incident-types)
