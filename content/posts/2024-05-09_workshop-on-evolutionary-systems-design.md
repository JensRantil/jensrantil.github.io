+++ 
date = 2024-05-09T19:45:35+02:00
title = "A workshop on evolutionary systems design"
description = "Evolutionary design requires practice."
tags = ["workshops"]
categories = []
slug = "evolutionary-systems-design-workshop"
+++
The [Agile Manifesto][agile-manifesto] states

[agile-manifesto]: https://agilemanifesto.org

> **Responding to change** over following a plan

This implies that we must design our systems to be malleable to change and
allow for _evolutionary design_.

Becoming good at evolutionary systems design requires practice, and sadly,
programming education doesn't teach this enough! Because of this, I ran a
workshop at `$previousEmployer` to teach how you can arrive at a completely
different solution if building it up iteratively vs. having all the
requirements from the start.

The workshop started with a small presentation where I gave some
Object-Oriented Design advice ([SOLID principles][SOLID], composition over
inheritance), mentioned a few [design patterns][design-patterns], and explained
what [CRC cards][crc] were.

[crc]: http://agilemodeling.com/artifacts/crcModel.htm
[SOLID]: https://en.wikipedia.org/wiki/SOLID
[design-patterns]: https://en.wikipedia.org/wiki/Design_Patterns

The whole workshop only used pen and smallish (important!) index cards; The
attendants were asked to split into groups of 2-3 people and design a hotel
booking system using CRC cards only.

{{< notice info "Why should CRC cards be smallish?" >}}
[Wikipedia][crc] sums it up pretty well:

> Using small cards minimizes the complexity of the design, reduces class
> responsibilities and keeps designers focused on the essentials of the classes
> without exploring implementation details. [...]

[crc]: https://en.wikipedia.org/wiki/Class-responsibility-collaboration_card
{{< /notice >}}

In the first part of the workshop, I gave them all the requirements in one batch
and asked them to design the system.

The second part consisted of four iterations. In the first iteration, I asked
them to design a hotel booking system with just a subset of the requirements.
In the second iteration, I added some more requirements on top of what had been
given in iteration one. I asked how they would adjust their design. In the last
phase, I gave them all the remaining requirements such that all requirements
added up to the same list of requirements in the first part of the workshop.

{{< notice warning "A successful mistake of unclear requirements" >}}
By mistake, I was pretty unclear about a few requirements. I remember saving
the whole situation by saying “Yes, in the real world requirements can be
vague.  What would you do if you were designing a hotel booking system?“.
:smile:
{{< /notice >}}

We wrapped up the workshop by having a conversation about how not knowing the
next requirements impacted their design. We did this by comparing the first
solution with the final solution from the second part of the workshop.

The value of using CRC cards instead of class diagrams or actual code for this
workshop should not be understated. The focus of the workshop was to focus on
_high-level_ design and not get bogged down by details. Based on experience,
particularly less experienced engineers easily get distracted by details. Using
CRC cards allowed the attendees to quickly iterate on different solutions
without getting stuck on field naming, syntax, or implementation details.

**Credits:** Lots of kudos to my friend [Mike Ciavarella][mike-ciavarella] who
taught me a variation of this workshop at [SRECon][srecon] EMEA back in 2019!

[mike-ciavarella]: https://www.linkedin.com/in/mikecee/
[srecon]: https://www.usenix.org/srecon
