+++ 
date = 2023-08-29T14:06:33+02:00
title = "The Knowledge Bottleneck I used to be"
description = "Solely optimizing for task cycle-time is a short-term thing."
slug = "the-knowledge-bottleneck-I-used-to-be"
+++
## The problem

I was working at a startup and was the only engineer doing SRE & operations-related work. This included things like setting sane limits, scaling systems, provisioning servers, configuring AWS, CI/CD, as well as a mix of various supporting infrastructure such as databases, monitoring & alerting tools, and caches. At the time the startup consisted of a team of maybe 20 engineers or so.

For some time I thought I was doing great - I was shipping a ton of changes in small increments across the stack and our infrastructure. We had Infrastructure as a Code (IaaS) in place which allowed us to iterate quickly on things. Whenever something was broken, I was on it! Whenever someone needed my assistance, I was fixing it. My cycle time for fixing things was _short_ and I was proud to show our engineers how one could work truly in short cycles and get a ton of Shit Done(tm). I was fixing business problems at amazing speed - I thought I had reached a global optimum at work!

However, there were two problems I was seeing; I was a bottleneck, and I was increasingly stressed:

"Bottleneck?", you might think. I was definitely _not_ a bottleneck when it came to _cycle time_ of tasks picked up. However, there was an increasing realization that I was a _knowledge bottleneck_; Our engineering organization did not know SRE practices and had very little operations knowledge. A lot of work had to be done by me - either because I knew how it would be done, or because it would be done faster.

Being a knowledge silo also meant that I was hindering the growth of other engineers. The best engineers I have ever worked with are the ones who understand the full software development life-cycle, including SRE practices and operations work. I wanted to be an enabler for growth, but at the time I didn't have all the tools in place for that to happen (more on that later).

As most engineers know, performance usually revolves around *throughput & latency*. "Cycle time" is the latency of performing a task. On top of this, we have [Little's Law][littles-law] that loosely states that "throughput is proportional to the number of actors doing some work in parallel". In the context of our organization, my being a knowledge bottleneck meant that other engineers could not do the work I was doing. This made me a _throughput bottleneck_.

[littles-law]: https://en.wikipedia.org/wiki/Little%27s_law

On top of this, being a knowledge bottleneck gave me a high [bus factor][bus-factor]; The organization was not resilient to me being gone -- and, oh boy, did I feel it! I constantly had a bad conscience about being sick or taking a day off from work. I felt stressed because of that. And I felt stressed because I knew I [had the entire company built on the stack I was maintaining][xkcd-card-house].

[bus-factor]: https://en.wikipedia.org/wiki/Bus_factor
[xkcd-card-house]: https://xkcd.com/2347/

All of these insights led me to conclude that I had been one-sidedly optimizing for short-term cycle time. My sole focus on cycle time was not in the long-term interest of me, my team, nor my company. Increasing throughput & resiliency of losing me would have a great positive impact on my team and on the business. I concluded I needed to make myself a True [Force Multiplier][force-multiplier].

[force-multiplier]: https://www.amazon.se/-/en/Tony-Chatman/dp/0998992704

## The solution for me

I am a teacher at heart. I love teaching. From day one at this startup, I did so much knowledge sharing: I shared links in Slack & in code reviews, I took the time to explain how things worked -- and I did a fair amount of presentations and some workshops. I shared everything from infrastructure knowledge to how to write good code and unit tests. In fact, I think I was doing all the teaching I could except one thing -- taking a step back and allowing other people to do the work I was doing.

It turns out, that most startups have a tendency to optimize for solving short-term problems over the long term. Short-term means "solving this one particular problem X" and it is easy to get caught in "let's just have Jim-the-expert fix that" ([hero culture][hero-culture]), or "I will just fix that much faster than anyone else" (not really hero culture, but close).

[hero-culture]: https://www.inteqgroup.com/blog/transforming-a-hero-culture

That is, taking a step back to create space for others is _hard_. Not only due to the short-term forces mentioned above but also because it can be hard for oneself (am still useful???).

For me, I was lucky and had a ticket out. As it turns out, I got the opportunity to work for 6 weeks from another side of the globe. Adding a 12-hour latency to answer questions in Slack is an amazing way to encourage colleagues to try out things themselves. Every morning I woke up I would see a few "Hello Jens - could you help me with X?", followed by "Never mind! I figured it out!".

## The next few years

As opposed to what many people think, delegating to others what you are good at doing is a very effective way to grow in your career and get promotions. It sure was for me. Moving away from being a knowledge and throughput bottleneck gave me a springboard to work on new exciting projects, many of them of my own choosing. Eventually, it gave me a promotion to work as a Staff Engineer within a 300-person engineering organization.

I have seen certain engineers get stuck doing what they are good at. I would actually say that's a much bigger risk of losing your job in the long run than moving on with new tasks, finding & solving new interesting problems, and "always be learning".

Eventually, I also discovered mob programming and have increasingly been doing pair programming. By rotating who is coding, you force people with less knowledge to do the work instead of you. It's a great way to share knowledge and offload responsibilities from me.

Finally, by no longer putting myself in the spotlight I feel like I have transitioned to be a true team member. I know it's cheesy, but there truly is no "I" in "team".

## My learnings

In short, I learned that

 * optimizing for short-cycle time for performing tasks only is a short-term solution.
 * even though you think you are not a bottleneck (for cycle time), you can still be a bottleneck in terms of knowledge & throughput.
 * being a knowledge bottleneck means you are a throughput bottleneck.
 * moving out of being a knowledge silo can be _hard_.
 * optimising for a team is the most long-term sustainable thing to do for you, for your team, and for your company. That usually involves focusing on avoiding being in a knowledge silo.

Now, what's the next thing you would like to stop doing - so you can work on that next cool project, or make that career move, you've always been dreaming of?
