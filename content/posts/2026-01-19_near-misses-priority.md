+++
date = 2026-01-19T16:48:35+02:00
title = "The missed incident priority: The Near Miss"
description = "Near misses are"
tags = ["Incident management"]
slug = "near-miss-incidents"
+++
> If a tree falls in a forest and no one is around to hear it, does it make a sound?

In my [article about incidents][incident], I wrote:

> "Raise an incident when you think a postmortem would be useful for what you are seeing."

This also includes raising an incident for a near miss. A **near miss** refers to an event that could have caused an incident, outage, security breach, or service degradation — but ultimately did not. Near misses can be a great source of learning, and [reducing near-misses can reduce actual incidents][safety-triangle].

[incident]: {{< relref "2025-12-17_what-is-an-incident.md" >}}
[safety-triangle]: https://www.ishn.com/articles/109182-the-safety-triangle-a-useful-yet-complicated-theory

Using your incident processes also for a near miss can be great. In my [previous article about incident priorities][incident-framework], I left out a crucial incident priority -- the one for near misses. As such, I usually recommend organisations also include a **priority 4** (for near misses) in their incident priority matrix. This is what the revamped matrix would look like:

[incident-framework]: {{< relref "2026-01-19_priority-severity-impact.md" >}}

<table>
  <tr>
    <th style="background-color: #f0f0f0;">Impact \ Severity</th>
    <th style="background-color: #f0f0f0;">None/Near Miss</th>
    <th style="background-color: #f0f0f0;">Low</th>
    <th style="background-color: #f0f0f0;">Medium</th>
    <th style="background-color: #f0f0f0;">High</th>
  </tr>
  <tr>
    <th style="background-color: #f0f0f0;">None/Near Miss</th>
    <td style="background-color: white; text-align:center;">Priority 4</td>
    <td style="background-color: white; text-align:center;">Priority 4</td>
    <td style="background-color: white; text-align:center;">Priority 4</td>
    <td style="background-color: white; text-align:center;">Priority 4</td>
  </tr>
  <tr>
    <th style="background-color: #f0f0f0;">Low</th>
    <td style="background-color: white; text-align:center;">Priority 4</td>
    <td style="background-color: #c6efce; text-align:center;">Priority 3</td>
    <td style="background-color: #c6efce; text-align:center;">Priority 3</td>
    <td style="background-color: #ffeb9c; text-align:center;">Priority 2</td>
  </tr>
  <tr>
    <th style="background-color: #f0f0f0;">Medium</th>
    <td style="background-color: white; text-align:center;">Priority 4</td>
    <td style="background-color: #c6efce; text-align:center;">Priority 3</td>
    <td style="background-color: #ffeb9c; text-align:center;">Priority 2</td>
    <td style="background-color: #ffc7ce; text-align:center;">Priority 1</td>
  </tr>
  <tr>
    <th style="background-color: #f0f0f0;">High</th>
    <td style="background-color: white; text-align:center;">Priority 4</td>
    <td style="background-color: #ffeb9c; text-align:center;">Priority 2</td>
    <td style="background-color: #ffc7ce; text-align:center;">Priority 1</td>
    <td style="background-color: #ffc7ce; text-align:center;">Priority 1</td>
  </tr>
</table>

I usually recommend only paging/alerting when customers _actually_ are impacted. As such, near misses are usually not paged for at all. Instead, they are discovered through dashboards, metrics, and logs - or simply brought up when someone discovered they were close to making a mistake. The latter obviously requires a large amount of [psychological safety][psyc-safe].

[psyc-safe]: https://blog.jobelenus.dev/blog/psychological-safety/

{{< notice tip >}}
Heads up! [I offer consultancy services][services] in this space. Don't hesitate to reach out if you would like me to help your company improve when it comes to reliability, resiliency, architecture feedback, on-call, alerting, or incident training. :wave:

[services]: {{< relref "/pages/services" >}}
{{< /notice >}}