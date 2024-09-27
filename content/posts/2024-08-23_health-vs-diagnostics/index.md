+++
date = 2024-08-23T09:32:35+02:00
title = "Health vs. Diagnostic metrics"
description = ""
tags = []
slug = "health-vs-diagnostics-metrics"
+++
Today I would like to discuss two types of metrics, namely "health metrics" and "diagnostics metrics". I keep seeing many people struggle to understand the difference and I hope this post will shine the light on the difference and why it matters. Understanding the difference between those two types of metrics has been a game-changer for me. 

This article will have some references to technical tools, but largely it applies to non-technical work, too.

## Executive summary

{{< notice "info" >}}

The presentation "Amazon’s approach to failing successfully" has [a great slide][aws] presenting the key differences between health and diagnostic metrics. In short, this is what it says:

[aws]: https://youtu.be/yQiRli2ZPxU?si=ppy0o0qt7_D6gaYv&t=1343

<u>Health metrics</u>

* Answers the question: Am I failing?
* Does not answer the question: Why am I failing?
* Always set alarms on these
* Be conservative in defining

<u>Diagnostic metrics</u>

* Answers the question: What is the value of this thing I measured?
* Might answer the question: Why isn't my system working?
* Sometimes set alarms on these
* Be liberal in defining

{{< /notice >}}

## The problem with diagnostics metrics

Today's product organizations are drowning in metrics. The sky is the limit to what we can measure. Even if we don't collect any data ourselves, our providers supply us with an endless amount of metrics. If you start up a database on AWS, or boot a virtual machine on AWS EC2, you get tens of metrics per instance.

Instead of starting from "What questions do we want to ask?", organizations start from "Which data do we have?". And this is problematic because it means we don't prioritize which data is more important than the other. More importantly, _we risk not seeing the forrest for all the trees_.

The majority of metrics are what are called "diagnostic metrics". They measure something and sometimes they are useful to figure out why something isn't working the way we expect. But they don't tell us anything if our systems are healthly overall.

When asking "What are the 1-3 metrics that show that you are succeeding?" very few people are able to articulate them.

## Enter "Health metrics"

Health metrics is 

## A short tale

When I started my career (~2008 or so) I used [Nagios][nagios] (later forked to [Icinga][icinga]) to monitor and alert when things were failing in our backend. I was setting up alerts for all sorts of things that could go wrong:

* High CPU usage
* High memory usage
* High JVM memory usage
* High number of open file descriptors
* High network bandwidth
* High disk space usage
* Process X is not running
* Cron job execution failures
* ...

[nagios]: https://www.nagios.org
[icinga]: https://icinga.com

Every time something broke in production, I set up an alert. I felt in control of our system. And I was happy that we had great monitoring in place. Eventually, every server had maybe 25-35 different possible alerts configured.

One rainy day, we had an incident where we started running out of memory on the <abbr title="Java Virtual Machine">JVM</abbr>. We received an alert. Yay! But the same minute we also started receiving alerts on high CPU usage because the JVM's memory garbage collector was constantly trying to reclaim memory. This was the start of configuring various silences of alerts to avoid getting multiple alerts on an incident. In this example, I made sure to silence the CPU alerts if we ran out of JVM memory.

Suddenly I was juggling a fairly complex set of intricate dependencies between a large set of alerts. Maintaining all these rules took a lot of time and energy.

Despite all these alerts, our alerting setup did not do what we wanted. We saw two big categories of issues:

**We had alerts triggering, but the customers did not notice anything.** This is a great example of a [bad alert][good-alerting] - it's not actionable. Alerts like this would wake up someone in the middle of the night despite no customers being impacted. For example, maybe we had one server crashing, but all other servers behind the same load balancer were happy.

**We kept having incidents that did not trigger any alerts.** Why? Because our alerts were based on failures we had previously seen. By definition, this did not handle future unknown failures.

[good-alerting]: https://blog.danslimmon.com/2017/10/02/what-makes-a-good-alert/

[complex-systems-fail]: https://how.complexsystems.fail/#4

## Impact-driven alerting

Software systems are complex. They consist of many moving parts that are braided together. [Complex systems contain changing mixtures of failures latent within them][complex-systems-fail] and _enumerating all the type of failures is close to impossible_. This means that **defining a functioning system as "no specific failures are observed" is a fallacy**.

What we instead want to do, is to monitor the success of our system from the customers' point of view and **define the absence of success as a failure**. At a very high level, this is what [_service levels_][service-levels] are all about.

A metric that measures high-level **health metric**. If focuses on whether the product is usable from a customer perspective.

[service-levels]: https://sre.google/workbook/implementing-slos/

For example, instead of monitoring all the types of errors that could happen above, I would monitor the ratio of HTTP 2XX responses on the load balancer - and create an alert if, say, that ratio is less than 99%. If a customer was impacted by a memory leak, a spinning CPU loop, a bandwidth bottleneck, or something else, it would all trigger an alert. The load balancer would know if the customer was negatively impacted because we would start to return HTTP 5XX responses.

Instead of managing many different alerts, I would manage _one_ alert focusing on 1) the customer impact and 2) making sure the customer can successfully use the product. This is what I call impact-driven alerting, ie. focusing on what customers experience.

## Diagnostics metrics

A common counter-argument against the above alerting setup is "But how do I know exactly which error is happening when I wake up at night an look at the alert?". The answer to that is "You don't.". That's what you have dashboards for.

A dashboards is a predefined view over all the _diagnostics metrics_ 