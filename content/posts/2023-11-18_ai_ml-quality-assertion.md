+++ 
date = 2023-11-18T23:55:35+02:00
title = "An AI/ML accuracy tale"
description = "Estimating accuracy for AI/ML systems isn't as simple as one would think."
tags = ["AI", "ML", "service levels"]
slug = "ai-ml-accuracy-tale"
+++
I recently read the article ["What I learned getting acquired by
Google"][google-acquired] by Shreyans Bhansali. Shreyans wrote

[google-acquired]: https://shreyans.org/google

> On the other hand there was the discovery that most Search improvements are
> manually reviewed by engineers through ‘side-by-side’ comparisons between old
> and new results...on spreadsheets! 

The above quote reminded of how hard, and often understated, quality assurance
(QA) in AI/ML systems is. Each change to a model needs to be validated, and
validation is _hard_ and _cumbersome_. Also, the fact that models can have a
_freshness_ does not help - that means that quality assurance must be done
continuously and treated as a [service level][sl].

[sl]: https://sre.google/sre-book/service-level-objectives/

To make my case, I thought I could share a tale about a classification system I
used to work on a bit.

## A tale

At a former employer we had a system that categorized a stream of financial
transactions using ML. For example, "MacDonald's" was categorized as
"Restaurant", and "H&M" was categorized as "Clothing", etc. If we were
uncertain, we set the category "Uncategorized". The users could adjust
incorrectly categorized transactions if they were wrong. Our goal was to
measure the [accuracy][accuracy] of how well these categories were applied by
the ML model.

[accuracy]: https://en.wikipedia.org/wiki/Accuracy_and_precision

> Was this category (in)correct?

Initially, we considered to ask for explicit feedback ("Was this category
correct?") from the user in the UI. However, we concluded that we did not want
to make our UX bloated. We asked ourselves, can we somehow figure out whether
our classification is accurate without changing our UX?

Our first iteration was a service level based on the ratio between the “number
of manual corrections” and “total categorizations”. This did not work very well
for two big reasons: Partially because it varied immensely between users and
how eager they were to adjust incorrectly categorized data or not. But mostly
because a lot of users were only adjusting the categories when they had bought
something different in a store; ie. buying "makeup" from "H&M" instead of
"Clothing". This made our numbers look much worse than they were! We did not
get any positive feedback on the correct classifications.

Our next take was not to categorize 1% of all financial transactions to force
our users to set the correct category. When they did set it, we compared what
they set against what our model would have guessed. Our service level was
defined as the "number of adjustments that matched our ML model's guess"
divided by the "total number of adjustments".

Randomly uncategorising 1% was a good idea! But it turned out to have a
surprising backlash from users; They perceived our classification as accuracy
having become significantly worse:

> "Why are you unable to categorize 'MdDonalds'?? C'mon, I expect better from
> you!

It turns out, we were not classifying some of the things we were certain about.
Could we do better?

We were lucky that our ML could spit out a certainty measure for our
classification between [0,1]. We started using the probability of skipping
categorizing a transaction based on the inverse of that certainty. That meant
"McDonalds", having a high certainty, was rarely skipped anymore. Good!

Instead of certainty, the inverse frequency could have been a different factor
to use to avoid common descriptions being randomly skipped. As far as I know,
we never pursued that approach.

Through a series of events, our business pivoted and started having customers
using our classification API and presenting the result in a UI of their own.
Since the customers could not always adjust incorrect categories in the UI, we
had to resort to manual quality assurance instead where people would sit and
verify that categories were correctly identified. This also made it hard for
use to treat ML accuracy as a service level. We instead had to do higher
quality assurance before release time, instead.

## In conclusion

Measuring AI/ML model quality takes a lot of creativity bordering SRE practises
(such as service levels, release strategies) and UX aspects - and there can be
some fun surprises along the way. :) Sometimes, manual QA through something
like [Amazon's Mechanical Turk][amt] is the easiest way to go about it, but if
you can somehow build in feedback mechanisms through your UX that is usually
much better to continuously measure service quality.

The customer is always right. Manual quality assurance will never be as
accurate as the one from customers, but it might be good enough.

[amt]: https://www.mturk.com/
