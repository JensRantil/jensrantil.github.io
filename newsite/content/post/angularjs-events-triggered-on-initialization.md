---
title: "AngularJS events on initialization"
description: "Triggering events from services might not always work..."
date: 2013-05-24
tags: ["AngularJS", "JavaScript"]
draft: false
---

AngularJS events on initialization
==================================

In my [previous post](|filename|refreshable-angularjs-service.rst) I was
giving an example of using [AngularJS](http://angularjs.org)
[events](http://docs.angularjs.org/api/ng.$rootScope.Scope#$emit).

I stumbled across a corner case that might be worth noting; If a service
is triggering an event on initialization, no controllers will get
notified of it. Here's an example:

<iframe width="100%" height="250"
src="http://jsfiddle.net/Ztyx/TdykU/2/embedded/"
allowfullscreen="allowfullscreen" frameborder="0"></iframe>
The reason why this is happening is simply because the controller have
not been instantiated. Setting a timer before emitting the event can be
done as a workaround:

<iframe width="100%" height="250"
src="http://jsfiddle.net/Ztyx/TdykU/3/embedded/"
allowfullscreen="allowfullscreen" frameborder="0"></iframe>
Now you know!
