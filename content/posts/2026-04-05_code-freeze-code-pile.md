+++
date = 2026-04-05T22:42:12+02:00
title = "Code freezes"
description = "Code freezes can undermine the very thing they are meant to protect."
tags = ["risk", "safety", "site reliability engineering", "service levels", "management", "leadership", "metrics"]
slug = "code-freeze"
aliases = ["code-freezes"]
+++
**Code freezes** commonly stirs up strong emotions within the engineering community. Either people find them useful, or hate them. Some companies have a code freeze on Fridays, others do it over the December holidays, or around important dates when systems must be extra stable, such as Black Friday.

## Code freeze?

In short, a _code freeze_ is when changes to a software system are suspended to make it more stable. But the devil is in the details:

* Are bug fixes still allowed to be deployed? All bug fixes? Or just some?
* Are releases through feature flags or configuration changes allowed?
* What about infrastructure changes?
* Mutations (inserts, updates, deletes, alters) to a SQL database allowed?[^1]
* What process is defined to decide if something can go out or not? Who decides?
* When does the code freeze end?
* How will the code freeze be lifted? How will you handle the backlog of changes that need to be applied when we come out of a code freeze?
* **Ultimately, what are the success criteria?** How do you measure whether the code freeze actually helped?[^3] A code freeze can simply postpone unstable changes to when the code freeze is lifted.

[^3]: Service levels are very useful for this.

**All these important questions need answering before entering a code freeze.** If there is anything you should take away from this article, it is that.

It's also worth remembering that [a system can change and break even without anyone touching it][different-changes]. During a code freeze, the environment around it keeps changing. During a code freeze, disks can still fill up, traffic can spike, or a hidden bug can surface. The website [how.complexsystems.fail][hcf] has more on this.

[different-changes]: https://cherkaskyb.medium.com/what-is-that-change-that-is-the-source-of-all-instability-c3eb03c5fdc3
[hcf]: https://how.complexsystems.fail

## Why not code freezes?

Generally, I believe engineers who are against code freezes dislike them because the above questions go unanswered, particularly the question about whether a code freeze actually has a measurable effect in the long run.

Further, introducing a code freeze can signal that a company is not willing to invest in better change processes. Instead of "let's do code freezes," it could instead focus its attention and energy on "What improvements to our processes can we change, such that we are comfortable making changes to our systems at any point in time?"

In essence, a code freeze could be sticking your head in the sand without any actual long-term stability improvements.

{{< notice example >}}
> "If it hurts, do it more often."

This is a commonly used phrase within the Continuous Deployment community. If your deployments are painful and impact customers badly, do it _more often_, and get better at it instead of doing them less frequently. That is, exercise the "deployment muscle" more often! :muscle:

Applying the same mindset to code freezes would mean stopping them, and instead getting better at shipping software.

See also my blog post on [Reliability vs. Resilience][safety-post].

[safety-post]: {{< relref "2024-11-05_safety-types.md" >}}
{{< /notice >}}

## A tale of a code freeze

A few years ago (in 2021), I was working as a Staff Engineer for a company with about 250 engineers.

The company had a series of incidents over the summer that made our products unavailable. Serious bugs were being shipped to production and slipped past a fairly extensive CI/CD pipeline (which obviously did not catch the issues). Our most important customer was very unhappy. I could likely write a whole slew of post-mortem blog posts about all this, but ultimately, when I showed up for work one Monday, our **CTO decided to introduce a company-wide code freeze**.

The code freeze came with a few rules:

Across the entire company, **only _one_ change at a time was allowed to be applied to our systems**. A _change_ was loosely defined as a merged pull request, an infrastructure change[^1], or executing a mutating[^2] SQL query. Any manual work that altered the state of our systems, really.

[^1]: A new ACL rule in firewall, etc.
[^2]: `INSERT`, `UPDATE`, `DELETE`, and `ALTER` statements.

A giant company-wide **change backlog spreadsheet** was created, containing a list of all the changes our engineers wanted to make to our systems. All changes were mostly applied in <abbr title="First In, First Out">FIFO</abbr> fashion. The spreadsheet had tens of columns, and any engineer who wanted to make a change had to add a line in the spreadsheet and answer things like:

* What the change was
* Why the change needed to be made (from a product standpoint)
* Which engineer was responsible for the change
* Priority of the change
* What the risks were
* What controls had been executed beforehand to make sure the change would work properly
* How the change would be verified after the fact
* How the change would be rolled back in case it did not work

A **"war room"**[^4] was created. It was a continuously staffed Google Meet video call. A rotating schedule was set up to ensure the video call always had at least one Engineering Director and one Staff Engineer. Engineers were expected to monitor the backlog spreadsheet and join the video call when it was their turn to make a change. My task as a Staff Engineer was to:

* Review the next change in the spreadsheet and ask clarifying questions to the engineer.
* Decide, together with the Engineering Director, whether to accept the change.
* Ask the engineer to share their screen while applying the change, and show that the change applied cleanly.

I guess the "war room" was an ad-hoc Change Advisory Board (CAB), if you will.

Personally, I was not a big fan of becoming an Ivory Tower gatekeeper for all our engineers. From a leadership perspective, our Staff Engineers shared a vision that we wanted to be enablers, not blockers. But, unfortunately, we were voluntold to do the opposite.

[^4]: I have personally never been a fan of the war rhetoric in business... :shrug:

### The code freeze backlog and stability

A queued up change, such as a pull request, has a freshness to it. If one deploys a change that has been lingering for weeks, one rarely remembers the details; debugging the change will be harder, rolling back is riskier, and arguing for why the change was made is harder.

**When the code freeze eventually started lifting, we had over 1,500 pull requests queued up to be merged.** During the code freeze, our engineers had been coding away, queueing up insane amounts of changes that needed to go out.

Do you think stability improved? :smile:

### Getting out of code freeze

All in all, the code freeze was fully gone after something like six weeks. Slowly, the code freeze was lifted from one team at a time. A coloring system was introduced: Red, yellow, and green for each team. Each team had to explain its quality assurance processes and was given a color code for its change process maturity.

In retrospect, I doubt a lot of actual technical <abbr title="Quality Assurance">QA</abbr> improvements were made. The outcome was mostly engineers being more afraid of f-ing up, and becoming more careful with the changes they made. My hunch is that development velocity slowed down significantly.

If the outcome was to temporarily avoid stability incidents, the code freeze was a success. I doubt that long-term stability improved, though. Unfortunately, stability wasn't measured adequately, so no one will know for sure.

## Conclusion

Code freeze as a knee-jerk reaction can solve a short-term stability issue, but it also carries the risk of not solving the long term stability issues. At worst, a code freeze can undermine the very thing it is meant to protect.

If I were ever in a leadership position of arguing for a code freeze, I would make sure to clarify the exit criteria and success metric before introducing it.
