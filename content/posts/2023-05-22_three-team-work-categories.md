+++
date = 2023-05-22T19:01:45+02:00
title = "Three categories of teamwork"
description = "A useful model for sourcing teamwork."
tags = ["teamwork", "product teams"]
slug = "three-teamwork-categories"
aliases = ["three-team-work-categories"]
+++

I recently wrote the post ["The Three Buckets model" for my own
time][bucket-model]. It reminded me of a similar model for how _teams_ could
spend their time.

[bucket-model]: {{< ref "/posts/2023-05-21_three-buckets-of-my-time.md" >}}

Back in the day I had a product owner (PO) for a former team who used to start
off our sprint planning sessions with

> Here are the key **product asks** I think we should deliver this sprint. What
> *team initiatives* are _you_ interested in driving?

I really loved this opening! I thought it was a great way to initiate a
conversation between product and engineering - inviting everyone’s expertise to
the table. It also brought a sense of autonomy, trust and shared ownership of the
backlog.

In essence, we categorized every sprint task into these three categories:

-	Product asks
-	Team initiatives
-	Operational work (<abbr title="Keep The Lights On">KTLO</abbr>)

Let me go through the three categories in detail:

**Product asks** were the most important product-related features to be worked
on. A product backlog can be infinitely long. As such, our PO would pick the
1-4 most important features that needed to be delivered. The PO made it very
clear which ones were negotiable and which ones were not.

These tended to be slightly less strategic and of more urgent nature.

**Team initiatives** were initiatives that came from our engineering team. This
could be dealing with technical debt, improving observability, building a proof
of concept, improving our automated tests or test tooling, or constructing a
new internal tool that would help us solve a specific problem in the future.

These initiatives also included non-technical tasks. There were product
initiatives that came out of the team; Experiments we wanted to try with the
product itself. I discovered that the more mature the product team is, the more
product initiatives the engineers can come up with.

The team initiatives were naturally more strategic. By allowing team
initiatives to be planned into the sprint, it allowed our team to ship at a
sustained pace. It also gave us an opportunity to try out new things.

**Operational work** was urgent work that could not be postponed to another
sprint. This included things like:

-	**Keep The Lights On (KTLO).** This could be like expanding our database
    disks to not run out of disk space, or optimizing memory usage to not run
    out of memory.
-	**Fixing bugs.**
-	**Unblocking other teams.**
-	**Answering questions** from internal teams or external customers.
-	**Known unknowns** such as “Hey, heads up that we might need to support
    team X with Y but we don’t know when or how”.
-	**Unknown unknowns** of things that naturally happened during the sprint we
    could by no means plan for (flooding in the datacenter? 😬😅).

Distribution between the categories?
------------------------------------

Over time, our aim was a 33%/33%/33% split between the categories, but we were
flexible. Sometimes we had sprints which were more product-focused. Other
sprints were more focused on doing operational work or team initiatives.

The _one_ rule we had, though, was that we always at least had _one_ task from
each category. Without this rule, we would risk ending up doing short-term
product tasks only - or simply spend our entire days refactoring our systems to
the perfect rocket ship when we really needed an airplane.

"Will we make it?"
------------------

Once we had our candidate tasks, we had an open and safe conversation about
whether we thought we would be able to deliver all tasks. If needed, we
prioritized and pruned tasks to try to avoid overplanning. If we felt like we
had underplanned, we brought in more tasks.

"We are all product"
--------------------

A former manager always used to tell me

> Jens, we are all product.

By saying this, he was reminding me that “the product and engineering” shared
the same goal; building an awesome product together. By having these three
categories for teamwork, I found that product and engineering started working
much closer together, with the same goal in mind, focusing on the right thing,
at the right time.
