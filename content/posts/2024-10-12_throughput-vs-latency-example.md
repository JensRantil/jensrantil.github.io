+++
date = 2024-10-12T00:41:35+02:00
title = "An example of throughput vs. latency"
description = "An example sometimes speaks more than a thousand explanations."
tags = []
slug = "throughtput-vs-latency-example"
+++
In software engineering jargon, people often speak of "performance" without defining specifically what they mean. Improving performance usually involves "increasing throughput", or "reducing latencies".

*Throughput* is measured in "units over time", for example, "bytes per second", or "cars passing by every day".

*Latency*, meaning "how long something takes", is measured in "time per operation". For example, how long it takes to load a website or send an image.

I remember my early days of trying to understand the difference. My breakthrough came when somebody gave the following example:

> "Suppose you want to transfer 10 petabytes of data from Europe to America. For this example, that would be ~10k hard drives.
> 
> One approach would be to transfer one hard drive at a time across the Atlantic subsea cables over the Internet. The latency of sending each hard drive would be fairly low (maybe an hour), but throughput very low (number of hard drives uploaded per hour).
> 
> A completely different approach would be to fill up an entire airplane with all the hard drives, fly them across the Atlantic, and deliver them to the destination data center. This latency of sending each hard drive would be very high (probably ~12 hours from datacenter to datacenter), but the throughput will be significantly higher (10k hard drives in 12 hours - or hundreds of hard drives per hour)."

This example also made me understand that _batching_ units of work (transferring many hard drives at a time) could increase throughput at the expense of latency. Parallelizing is usually an easy way to speed up throughput. Reducing latency is usually not as easy.

Maybe this example might help someone else. It sure did for me.
