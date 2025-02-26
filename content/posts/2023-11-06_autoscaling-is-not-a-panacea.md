+++ 
date = 2023-11-06T17:25:35+02:00
title = "Autoscaling is not a panacea"
description = "There is a belief that autoscaling will solve problems it will not."
tags = ["simplicity"]
slug = "autoscaling-not-a-panacea"
+++
Back in the day when The Cloud (AWS) was The New Hot Thing, I thought
autoscaling would solve most of our problems related to costs, availability,
performance, and scalability. Over the years, I have learned that autoscaling
has a high maintenance cost, adds complexity, and [doesn't solve all those
problems I initially thought it would][automation-ironies]. In this article I
will give examples of incorrect assumptions I made when it came to autoscaling:

[automation-ironies]: https://en.wikipedia.org/wiki/Ironies_of_Automation

**"Once we have autoscaling, we will never have any performance problems."** I
thought any traffic spike would immediately be handled by autoscaling. Suddenly
receiving 20k requests per second within a minute? My service would scale up
immediately, handle those requests, and then quickly scale down! I had three
invalid assumptions here:

 * _"Autoscaling will react within a second."_ This isn't true.  Autoscaling
   usually kicks in within _minutes_. And usually you don't want autoscaling to
   be that sensitive anyway as it likely would immediately overprovision the
   number of instances.
 * _"My application will start within a few seconds."_ Ever started a large
   Java service? Booting up an ORM, loading all the classes, and reading up
   stuff from a database takes time. I've seen many services taking close to a
   minute to start..
 * _"My application is the bottleneck."_ Anyone who has done any significant
   performance benchmark knows that the performance bottleneck [moves
   around][max-flow-min-cut]. For example, an application backed by supporting
   infrastructure such a database can usually only scale up until a certain
   level until _the database_ turns into the performance bottleneck instead.
   That said, based on experience 99% of the time, _the database_ is the
   bottleneck, not your application...

[max-flow-min-cut]: https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem

**"Once we have autoscaling, our stability will improve."** Autoscaling offers
automated restarts of services. That's great and definitely improves system
stability since crashed, or deadlocked, services automatically gets restarted.

However, autoscaling also (optionally) comes with scaling up and down. Over and
over again, I have seen downscaling impact availability; shutdowns not properly
draining ongoing HTTP requests and improperly set shutdown timeouts killing
processes prematurely.

Scaling up can, surprisingly, also impact stability negatively. If your
application is doing any lazy loading, it can be slow until it has warmed up
(hello Java!). This is a problem that gets magnified if you scale up
frequently. There are workarounds here, though. You _can_ spend time heating
your process after startup.

Further, since there is no subsecond autoscaling there will be a time until
scale-up happens. During that time, your service might not be able to serve all
your requests. This is where load-shedding and retries can help - and now you
have another problem to solve!

**"Scaling up can not be done until infinity!"**. Your autoscaling group has a
limit on the maximum number of instances configured by you. AWS also maintains
limits which usually always kick in at the worst possible time degrading your
system. Funnily enough, increasing the max instances limit tends to introduce
an [induced demand][induced-demand] such that you start hitting your new
limit...

[induced-demand]: https://en.wikipedia.org/wiki/Induced_demand

**"Once we have autoscaling, I will not need to tune the _vertical_ sizing of
my system."** Memory usage of processes increases over time, and the amount of
memory/CPU can have an impact on latency. For example, more memory/CPU
resources can reduce the impact garbage collection has. Request-based limits
(maximum length on request body etc.) help here, but over time adjusting the
vertical sizing usually needs to happen unless your workload never changes.

Another problem with autoscaling is that it implicitly invalidates all the
hardcoded constants found during a performance benchmark. When you run
performance benchmarks, you usually configure the optimal number of threads in
thread pools, database connection pool size, etc. All of those constants are
_based on the current state of your architecture, including the number of
instances running_. Once any of these things change, you need different
settings. If you truly need optimal performance with autoscaling, you also need
to invest in something like [Conc][conc] or [Netflix's
`concurrency-limits`][conc-limits].  Introducing autoscaling means you now have
a new problem.

[conc]: https://github.com/JensRantil/conc
[conc-limits]: https://github.com/Netflix/concurrency-limits

**"Once we have autoscaling, I will not need to tune the horizontal sizing of
my system."** When enabling autoscaling, you go from simply maintaining the
number of instances to also having to understand, maintain, and adjust

 * upscaling policy, including the maximum number of instances allowed to run.
 * downscaling policy, including the minimum number of instances allowed to
   run.
 * shutdown timeouts.
 * shutdown processes, including proper draining of traffic.
 * startup health checks.
 * scheduled scaling policies.

Turns out there were even more knobs now! More complexity.

**"Autoscaling will save me money."** This is mostly true! Unless you have
spiky traffic and end up configuring your upscaling policy to be very
aggressive and your downscaling to rarely scale down.  I have seen systems that
constantly run on the maximum number of instances. In that case, I would
probably disable autoscaling altogether.

**"I can easily autoscale stateful infrastructure."** The database is slow?
Just scale up more instances! There are three common misconceptions here:

The first one is that copying data has no weight. Starting up another database
instance means you must first copy all the data it needs to serve.  Independent
of if your database stores 10 GB, 50 GB, 100 GB, or 1 TB, this will take time.

The second misconception is that horizontally scaling _writes_ can be done
easily. While this _is_ true if you are running certain NoSQL databases, it is
not for ACID-compliant databases such as RDBM/PostgreSQL/MySQL.  For an RDBM,
you will likely need to do some sharding. Switching between shards can have an
impact on availability.

The third misconception is that database performance will be good immediately.
Generally, databases contain caches (looking at you, MySQL & PostgreSQL) that
need to be "heated" (populated, loaded into RAM) until they can be considered
fully performant. This impacts performance for the first minutes/hour when a
new database instance has come up.

## Conclusion

Whether autoscaling is useful to you requires a cost-benefit analysis. If you
are not hitting any memory or CPU limits nor cost is a big problem, I would
suggest you stay away from automatic upscaling/downscaling to keep things
simple.
