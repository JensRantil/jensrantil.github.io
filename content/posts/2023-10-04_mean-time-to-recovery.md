+++ 
date = 2023-10-04T08:01:35+02:00
title = "MTTR is the wrong metric"
description = "We have been measuring Time to Recovery the wrong way all along."
tags = ["statistics"]
slug = "mttr-is-the-wrong-metric"
+++
{{< x user="JensRantil" id="1369762301293781002" >}}

Today I would like to talk about why Mean Time To Recovery (MTTR) is a wrong
metric to look at.

For the past few years many software engineers have been using [the DORA
metrics][dora] to track the performance of software delivery. One of the DORA
metrics is "Time to Restore Service", also known as "Mean Time To Recovery
(MTTR)". A couple of years ago Courtney Nash wrote ["MTTR is a Misleading
Metric—Now What?"][now-what] where she criticized that the MTTR concept is too
simplistic. I could not agree more.

[dora]: https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance
[now-what]: https://www.verica.io/blog/mttr-is-a-misleading-metric-now-what/

When I recently wrote [Mean vs. Median][mean-vs-median], I was reminded of
Courtney's

> [...] measures of central tendency like the mean, aren’t a good
> representation of positively-skewed data, in which most values are clustered
> around the left side of the distribution while the right tail of the
> distribution is longer and contains fewer values. The mean will be influenced
> by the spread of the data, and the inherent outliers.

[mean-vs-median]: {{< ref "posts/2023-10-03_mean-vs-median/index.md" >}}

In essence, she was saying that using the _mean_ as a performance number for
recovery times is a quite useless number.

Just like software engineers are using percentiles as a performance number for
latencies, we should be using _percentiles_ when analyzing recovery times. A
recovery time is just a latency to fix something, but usually in minutes/hours
instead of milliseconds/seconds.  We want to be able to know that the recovery
time for 95% of all incidents is being reduced; Mean does not say anything
about that.

So why is MTTR used in the first place and not PTTR (Percentile of Time To
Recover)? Probably because a mean is so much easier to calculate. DORA metrics
are gathered from lots of companies, and [percentiles are
hard][mean-vs-median].
