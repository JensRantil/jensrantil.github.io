+++ 
date = 2023-05-09T08:24:19+02:00
title = "Code as self-serve experience"
description = "Code such as Terraform & Kubernetes is generally a horrible self-serve experience"
tags = ["platform engineering", "terraform"]
aliases = ["/posts/terraform-self-serve-experience/"]
slug = "2023-05-09_code-as-self-serve-experience"
+++

**Using "code as self-serve", such as Terraform or Kubernetes, in Platform
Engineering is a rather bad idea. Let me explain why!**

These days [there is all the rage around Platform Engineering][platform-eng],
and in fact I spent my last few years at `$previousEmployer` doing exactly
this.

One of the core tenets of "Platform Engineering" is the concept of
["self-serve"][self-serve]. That is, instead of a Platform team acting as a
blocker, you instead make sure to build a developer experience (DevEx) that
enables engineers to do something themselves exactly when they need it. Just In
Time! For example, if developers need a database they shouldn't need to reach
out to the Platform Engineering team and ask for one. Instead, they should
simply be able to easily fire up a new database themselves within a few
minutes.

[self-serve]: https://blog.cycloid.io/user-friendly-developer-self-service-the-key-to-platform-engineering

A common thing I have seen multiple Platform Engineering teams do is to use
(declarative) "code as self-serve", for example using Terraform or Kubernetes
(K8s). I don't know how many times I've heard a Platform team say

> No problem, we have a self-serve experience - the developers can just submit
> a pull request to our Terraform/Kubernetes code to create their new database.
> We will review it and merge it for them.

For example, if you don't have any kind of [abstraction layer around your
Kubernetes YAML][helm], writing >300 lines of YAML is _not_ a pleasant
experience. The same usually applies to Terraform.

[helm]: https://helm.sh

Generally, there are usually a few common problems with "code as self-serve":

**It's not beginner friendly.** While many engineers think "well, it's just
code", learning Terraform/K8s/et al. is neither simple, nor easy. Given how hard it
is to hire senior engineers these days, I think the aim should be to give
_junior_ engineers an easy self-serve experience. Having to learn Terraform to
create a database is like crossing the river for water.

**It has slow or hard to find feedback.** If a developer fills out the wrong
information in code, feedback is usually given through a hard-to-find CI/CD
output with a cryptic error message.

**Ownership issues.** Usually "code as self-serve" exists in a centralised
<abbr title="Version Control System">VCS</abbr> repository owned and maintained
by the Platform team. This means that there is a big risk that non-platform
engineers simply see the Platform team as the owners of the resources listed in
the repository. What you want is, the developers to make sure they feel
ownership the resources they create. Otherwise we just end up where the
industry was before DevOps (as a culture) was a thing.

**It can be slow.** Most source code changes requires code review. Having to go
through a code review for self-serve can make it a really bad experience.
Waiting a couple of hours for a code review approval is not what you would
want.

**Lack of change locality.** Creating a new microservices likely requires

 * A new git repository.
 * A new database.
 * A new load balancer
 * A skeleton source code containing a _Hello World_ implementation.
 * And more...

Code as self-serve has a tendency to ask the developer to make these changes in
_multiple_ places (because Terraform can't generate the source code etc.). A
nice developer experience in this case would be to trigger the creation of a
new service in _one_ place, not many.

[platform-eng]: https://www.honeycomb.io/blog/future-ops-platform-engineering

Finally, usually self-serve is critical to easily be able to start RnD projects
such as [spikes][spike] or <abbr title="Proof of concept">POCs</abbr>. As such,
a slow and complex self-serve experience can actually have a daunting impact on
company innovation.

What are the alternatives? Create a graphical user interface that guides the
users through the right choices, naming standards etc. Spotify's
[Backstage][bs] is one such alternative.

[bs]: https://backstage.io/

Above said, I understand the common journey for companies is to start with code
as self-serve. It's a good start! Just make sure to not get stuck there.
Platform Engineering involves thinking of developer experience with a product
mindset. Just like most SaaS companies will not ask their end-customers to
write YAML instead of using a GUI, the same applies to the domain of Platform
Engineering.
