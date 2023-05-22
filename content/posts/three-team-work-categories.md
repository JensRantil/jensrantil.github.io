+++ 
date = 2023-05-22T19:01:45+02:00
title = "Three categories of team work"
description = "A useful model for sourcing team work."
tags = ["team work", "product teams"]
+++
I recently wrote about ["The Three Buckets model" for my own
time][bucket-model]. It reminded me of a similar model I used to use for how
_teams_ should spend their time.

[bucket-model]: {{< ref "/posts/three-buckets-of-my-time.md" >}}

An excellent product owner (PO) for a former team would start off our sprint
planning sessions with

> Here are the _key product asks_ I think we should
deliver this sprint. What _team initiatives_ are you coming in with?

I loved this! This opened up for a conversation between product and engineering
around what to focus on - putting everyone's shared expertise at the table. It
also improved a sense of autonomy and ownership of the backlog for the
engineers.

In essence, we categorised every sprint task into these three categories:

 * Product asks
 * Team initiatives
 * Operational work (<emph title="Keep The Lights On">KTLO</emph>)

Let me go through the three categories in detail:

**Product asks** were the most important product-related features to be worked on. A
product backlog can be infinitely long. As such, our PO would pick the 1-4 most
important features that needed to be delivered. The PO made it very clear which
ones were negotiable and which ones were not.

Product asks tended to be less strategic and of more urgent nature. Totally fine,
a business urgency can be a good thing as long as is not the only thing that
takes up the sprint board!

**Team initiatives** were initiatives from our engineering team. From a
technical perspective, this could be everything from dealing with technical
debt, improving observability, building a proof of concept, improving our
automated tests or test tooling, or constructing a new internal tool that would
help us solve specific problems in the future.

But team iniatives not only included technical tasks. There were also product
initiatives coming out of the team; Experiments we wanted to try out with the
product itself. I discovered that the more mature _product_ team we were, the
more product initiatives came out of the team itself.

The team initiatives were naturally more strategic in nature. Allowing team
initiatives to be planned into the sprint allowed our team to ship at a
sustained pace. It also, gave us opportunity to try out new things and
innovate.

**Operational work** was urgent work that could not be postponed to another sprint.
This included things like:

 * **Keep The Lights On (KTLO).** This could be things like expanding our
   database disks to not run out of disk space, or optimising memory usage to
   not run out of memory.
 * **Fixing bugs.**
 * **Unblocking other teams.**
 * **Answering questions** from internal teams or external customers.
 * **Known unknowns** such as "Hey, heads up that we might need to support team
   X with Y but we don't know when or how".
 * **Unknown unknowns** of things that naturally happened during the sprint we
   could by no means plan for (flooding in the datacenter? 😬😅).

## Distribution between the categories?

At the time, our ballpark figure was to aim for a 33%/33%/33% split between the
categories, but we were flexible. Sometimes we had sprints which were more
product-focused. Other sprints were more focused on doing operational work or
team initiatives.

The _one_ rule we had, though, was that we always at least had _one_ task from
each category. Without this rule, we would risk ending up only doing short-term
product tasks - or simply spend our entire days refactoring our systems to the
perfect rocket ship when we really needed an airplane.

## "Will we make it?"

Once we had our candidate tasks, we had an open and safe conversation about
whether we thought we would be able to deliver all tasks. If we needed, we
prioritised and pruned tasks to try to avoid overplanning. If we felt like we
had underplanned, we brought in more tasks.

## "We are all product"

A former manager always used to tell me "Jens, we are all product" - reminding
me that "the product and engineering" shared the same goal - building an
awesome product, together. By having these three categories for team work, I
found that product and engineering started working much closer together, with
the same goal in mind, focusing on the right thing, at the right time.
