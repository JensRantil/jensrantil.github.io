+++
date = 2024-05-28T22:20:35+02:00
title = "Monorepos and atomic deploys"
description = "All your changes must be backwards compatible."
tags = []
slug = "deployment-are-not-atomic"
+++
Today I would like to discuss change management and deployments. I will start
by describing two problematic deployment scenarios and discuss various
solutions to them:

## Monorepos are easy

A "Monorepo" is a single <abbr title="Version Control System">VCS</abbr> (Git,
Mercurial, et al.) repository in which multiple _projects'_ source code reside.
Example projects could be things like:

 * Backend services
 * Frontend services
 * Common cron jobs that need to be executed
 * And more.

A common developer journey is to make changes to multiple projects. For
example, adding a new product feature usually involves modifying both a backend
API and a frontend component, or multiple backend services.

If the source codes for these projects are spread across multiple repositories
a developer must make at least one commit in each repository. This could be
considered [wasteful movement][muda]. Waste that having a Monorepo avoids.

[muda]: {{< relref "2023-06-27_waste-in-software-development.md" >}}

## Easy is not simple

By storing source code for all these projects in one Monorepo repository we
don't need to jump between multiple repositories. Instead of we can make a
single commit across multiple projects. Neat! Want to change the name of a JSON
response field used between two backend services. Easy! Want to stop sending an
unused JSON field from the frontend? You can include remove the field in the
backend in the same change. Easy!

Some of you might already know where I am going with this. :) It turns out that
things are not so easy as they might think. The thing is, the projects are
_never_ rolled at the exact same time (atomically). Instead, one will finish
before the other, and most certainly in undefined order.

For the examples above, this means that there is no protection from:

 * The frontend stopping to send the JSON field before the backend has stopped
   requiring it.
 * The backend server starts requiring the new JSON field name before the other
   backend service's client has started using the new field name.

In both cases, things will be broken while a deployment is ongoing.

Now, this is where someone might say "Yeah, but it's just while the deployment
is ongoing. It will just be a temporary glitch." I would like to challenge that
in two ways:

Firstly, a deployment usually happens gradually and _takes time_. The more
traffic you have, the more instances, the longer a deployment takes. Even for
smaller deployment it can take between 5-10 minutes. Would you be fine with
customers having a broken product for that long?

Secondly, to make a statement like that above - you need to _measure_ the
availability impact of your customer. If you do, and only a fraction of the
customers are impacted, sure go ahead and be less stringent with your deploys!

## Solutions

So, what can we 
