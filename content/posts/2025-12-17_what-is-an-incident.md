+++
date = 2025-12-17T16:57:35+02:00
title = "What is an incident, anyway?"
description = "What is an incident, anyway? How do we define it? When should you declare an incident?"
tags = ["incident management"]
slug = "what-is-an-incident"
+++
Incident process?
===
Many companies have an incident process. An incident process (often called an incident management process) is a defined set of steps an organization follows to detect, respond to, manage, resolve, and learn from incidents that disrupt normal operations or pose a risk.

<figure>
{{<mermaid>}}
flowchart LR
    A[Incident detected] --> B
    B[Incident declared] --> C
    C[Mitigation in place] --> D
    D[Incident resolved] --> E
    E[Incident review] --> F
    F[Corrective / Preventive Actions] --> G[Incident closed]
{{</mermaid>}}
<caption>A common incident process.</caption>
</figure>

The exact meaning depends a bit on the field, but the core idea is the same: handle unexpected problems in a structured, repeatable way.

A key part in an incident process is _learning_ from incidents. It involves things like

1. Bringing everyone involved into a room, discuss what happened, lessons learned, and coming up with [candidate action items][action-items] to reduce the likelihood of something similarly happening again (a Postmortem); and
2. Implementing the above action items.

[action-items]: {{< relref "2024-10-31_incident-action-items.md" >}}

<figure>
{{<mermaid>}}
flowchart LR
    A[Incident detected] --> B
    B[Incident declared] --> C
    C[Mitigation in place] --> D
    D[Incident resolved] --> E
    subgraph Learnings
    E[Postmortem] --> F
    end
    F[Corrective / Preventive Actions] --> G[Incident closed]
{{</mermaid>}}
<caption>Learning from incidents.</caption>
</figure>

[^1]: Also known as incident review, learning reviews, after-action review (AAR), post-incident analysis, etc.

Incident?
===
A question that has commonly been brought up during my incident trainings has been **"But what is an incident, anyway? How do we define it?"**. Knowing what an incident is and is not is crucial. It has a direct impact on when to declare an incident, and when not to.

Yet, defining what an incident is can be surprisingly hard. Many definitions somehow seem to miss an important part. For example, [ChatGPT tells me][chatgpt]

> "An incident is an unplanned event that:
>
> * Disrupts services or operations
> * Reduces quality or performance
> * Poses a security, safety, or compliance risk"

Even this definition misses the crucial aspect of [learning from "near misses"][safety-types] - when things _almost_ went bad.

[chatgpt]: https://chatgpt.com/share/6942ca02-e938-8007-a527-b16d8783fa57
[safety-types]: {{< relref "2024-11-05_safety-types.md" >}}

An incident definition needs to be

 * **Easy to remember** such that anyone remembers it; and
 * **Be actionable** in such a way that anyone quickly knows when to declare an incident.[^2]

So far, my favourite definition is

> An incident is an event in which the organisation has an opportunity to learn something.

or phrased somewhat differently

> Raise an incident when you think a postmortem would be useful for what you are seeing.

These definitions are outcome-focused. It assumes that the most important outcome of an incident is the learning part - avoiding that something happens again.
 
[^2]: Within some of the organisations I have worked in, _anyone_ could declare an incident.

{{< notice tip >}}
Heads up! [I offer consultancy services][services] in this space. Don't hesitate to reach out if you would like me to help your company improve when it comes to reliability, resiliency, architecture feedback, on-call, alerting, or incident training. :wave:

[services]: {{< relref "/pages/services" >}}
{{< /notice >}}