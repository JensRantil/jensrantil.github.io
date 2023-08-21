---
title: "AWS ELBs and Availability"
date: 2018-05-06
tags: ["AWS"]
slug: aws-ELBs-and-availability
---
Recently I was reading the article ["Introduction to modern network load
balancing and
proxying"](https://blog.envoyproxy.io/introduction-to-modern-network-load-balancing-and-proxying-a57f6ff80236)
and I was reminded by something that has bothered, and still is bothering me,
about the AWS Load Balancers (ElasticLoad Balancers, or ELBs).  The article
quotes [the Wikipedia article about Load
Balancer](https://en.wikipedia.org/wiki/Load_balancing_%28computing%29) saying

> Using multiple components with load balancing instead of a single component
> may increase reliability and availability through redundancy.

I have always assumed that that's one of the major reasons why putting load
balancers in front of application servers. That's why I was surprised to learn
that if an AWS ELB make a TCP connection to an application it will _not_ retry
another application server. Instead, for HTTP mode, it will return an [HTTP
503](https://httpstatuses.com/503). At [Tink](https://www.tink.se/), we learnt
this the hard way many years ago when a few application servers ran out of
memory and restarted. On a few servers we also did in-place application
upgrades which also would yield 503s during the upgrade, _even if we were
draining the applications properly on shutdown_. We noticed that a spike of
5XXs were being returned to our end-users until the ELBs healthcheck had
realized the service was down.

[HAProxy](http://www.haproxy.org/), [nginx](https://www.nginx.com/) and most
other software proxies support retrying upstream servers. There are of course
cases where retries should not be done carelessly (such as for `POST`s), such
as after a request has been sent upstream, but a failed TCP CONNECT is not one
or them.

During AWS Summit Stockholm last year I tried to push the AWS architects as to
why this is but got no clear answer. Reasons I can think of:

 * To force AWS users deeper into the AWS ecosystem making them make API calls
   to drain ELBs before shutdown, or using auto scaling groups for software
   upgrades. Auto scaling groups will automatically drain servers. Note that
   using auto scaling groups will not avoid 503's if a server process for some
   reason crashes.
 * Retries will increase the latencies for end-users. I personally believe a
   single retry is much more expected than fail early. If course, there should
   be a limit to the number of retries. If you have 200 upstream servers,
   retrying all of them isn't viable!

I'll be attending this year's [AWS Summit Stockholm
2018](https://aws.amazon.com/summits/Stockholm-2018/). Maybe I'll get a better
answer this year!
