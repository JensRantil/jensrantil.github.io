+++
date = 2025-01-10T13:26:35+02:00
title = "Raise and Release"
description = "A practical principle for sharing concerns constructively and letting go of ownership when decisions are outside your control."
tags = ["leadership", "safety", "security", "feedback"]
slug = "raise-and-release"
+++
Amazon's founder Jeff Besos is famous for his "disagree and commit" management principle used in leadership. [According to Wikipedia][disagree-commit], it means "that individuals are allowed to disagree while a decision is being made, but that once a decision has been made, everybody must commit to implementing the decision".

[disagree-commit]: https://en.wikipedia.org/wiki/Disagree_and_commit

I have a slight variation on this which I call "Raise and Release", which happens _before_ a decision has been made. I use this principle particularly when someone proposes something I strongly disagree with -- or know will fail -- but for cases where I can't affect the actual decision. Usually, it is for cases where I am "consulted" or "informed" in the [RACI][raci] sense.

[raci]: https://en.wikipedia.org/wiki/Responsibility_assignment_matrix

"Raise and Release" involves a two-step process. The "Raise" step means, I gather up feedback in written text where I explain why I think the proposal is a Bad Idea:tm:. This can be in a public chat or as a feedback comment in an RFC document. For really complex feedback, I have even found myself writing up a 2-pager or a public blog post[^1] explaining my reasoning.

[^1]: If I ever write a blog post about something, I obviously leave my employer out of it. I never write a blog post about something that is strictly internal to a company, contain any sort of trade secrets, or would impact security in any way.

I have found it important for the feedback to have a linkable URL. By doing so, I can share a link to my feedback in any conversation, now or in the future.

If I believe there is a very big/expensive/serious failure approaching, I have obviously also notified a manager.

The "Release" step involves two things:

First, I let the involved people know that "This is my feedback on why I think this idea is a bad one, but I will let _you_ decide if you would like to progress with it or not". That is, I make it very clear this is not my decision to make.

Secondly, I move on and release this issue from my responsibilities, my emotional burden, the decision process, and the outcome's consequences. Poff. I have done my part.

## An example

Some time ago I worked with some engineers who proposed to introduce a public HTTP API that worked with batches of items. Having had many years of (bad) production experience with this (and knowing the pain of API deprecations), I knew that there were many pitfalls with the solution. However, this project and the implementation decisions were not mine.

Initially, I voiced my concerns informally. But I noticed that they were taken rather lightly. This led me to write my blog post ["The downsides of batch APIs"][batch] which I shared as a link in the RFC document as well as in a public chat.

[batch]: {{< relref "2023-05-03_downsides-of-batch-apis.md" >}}

I moved on. Luckily, the engineers picked up my feedback and decided to avoid batched APIs. Win!

(A bonus for writing my thoughts as a blog post is that I am now able to share a link to the blog post if I am ever in a similar position in the future, independent of my employer.)

## Closing thoughts

Throughout my years, I have found the "Raise and Release" principle to be really helpful; It has covered any personal repercussions for failures but also saved the organizations I have worked from some expensive mistakes -- when people have been willing to listen. By sharing my feedback in public, I have had a URL to share in future conversations with engineers and managers, or even future employers.

Personally, the "Raise and Release" principle has also helped me to not waste my social capital or spend any energy on decisions I simply could not affect.

Not all hills are worth dying on. With the "Raise and Release" principle, some of my employer's failures are no longer _my_ failure.
