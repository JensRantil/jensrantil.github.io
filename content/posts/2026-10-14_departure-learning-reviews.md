+++
date = 2026-10-14T15:35:12+02:00
title = "Departure learning reviews"
description = "Hiring someone is expensive. How can a company learn from non-mutual departures?"
tags = []
slug = "departure-learning-reviews"
aliases = ["hiring-learning-review"]
+++
I think many companies could use a formal _learning review_ process for non-mutual employee departures.

A "non-mutual departure" could be initiated by either party in an employment relationship, either by the employee or the employer. What they have in common is that one side is unhappy. Maybe the company was unhappy with the employee’s performance. Or maybe the employee left after 12 months because the job was not a good fit.

Within <abbr title="Site Reliability Engineering">SRE</abbr> and Systems Safety Engineering, it is common to have a formal process where you bring everyone together after an incident, review what happened, what can be learned from it, and how the same situation can be avoided in the future. This is called a _Learning Review_[^1].

[^1]: Also known as post-mortems, incident reviews, after-action reviews (AAR), post-incident analysis, etc.

Done right, learning reviews can be hugely beneficial. And contrary to what many people believe, reviews do not necessarily need to be [a heavy process][heavy-process] with a lot of documentation and preparation.

[heavy-process]: {{< relref "2024-12-06_good-process-is-invisible.md" >}}

Hiring someone is expensive. It usually takes at least 6-9 months for someone to learn a new job. And at least 18 months to get really good at it. That is a significant investment. A learning review for an employee departure would bring manager(s), HR representatives, hiring manager, hiring interviewers, possibly team members, and others into the same room to explore questions like these:

 * Looking back:
   * Why did this person depart? It is a red flag if the answer only blames the employee or points to a single root cause.
   * Were there any issues with onboarding or training?
   * Did the company give early, clear, and actionable feedback to the employee about a mismatch? When? How?
   * How did the company handle receiving feedback from the employee? Did it change in any way?
   * Hiring process: Why was this person hired in the first place?
 * Looking forward:
   * Ultimately, how can the company avoid ending up with this kind of departure in the future? ([reliability][safety-types])
   * How can mismatches be discovered during the hiring process? ([reliability][safety-types])
   * Can onboarding or training be improved?
   * How can feedback be given earlier and better? ([resilience][safety-types])
   * If a bad hire has already been made, how can the company and its employee realise _earlier_ that a departure is the best way forward? ([resilience][safety-types])

[safety-types]: {{< relref "2024-11-05_safety-types.md" >}}

This past year, two of my friends were let go with severance. My friends learned a tonne from it and have come out of it much stronger. But I honestly wonder if their former employers learned anything at all.

The closest thing I have seen to a learning review for departures is the [_exit interview_][exit-int]. Those interviews are definitely useful, but I do think there is value in bringing multiple people together to learn as a group, not just a single interviewer.

How is your company learning from bad departures?

[exit-int]: https://www.peoplehr.com/en-gb/resources/blog/exit-interviews/