+++ 
date = 2023-11-06T19:45:35+02:00
title = "My simplicity toolkit: Architectural"
description = "Simple architectural constructs in my simplicity toolbox of choice."
tags = ["simplicity", "architecture"]
categories = ["My Simplicity Toolkit"]
slug = "software-architectural-simplicity"
draft = true
+++
**This post is part of of my blog series about [_My Simplicity
Toolkit_][simpl-toolkit]. I suggest you read [the initial
post][simpl-toolkit-init] before reading this post.**

[simpl-toolkit]: {{< ref "/categories/my-simplicity-toolkit/" >}}
[simpl-toolkit-init]: {{< ref "/posts/2023-11-06_my-simplicity-toolkit/index.md" >}}

INTRO
https://sre.google/sre-book/simplicity/

[simple-arch]: https://danluu.com/simple-architectures/

### Relational databases over NoSQL

### Microservice over...not microservices

### Server-side rendered over client-side rendered web pages

### One environment over multiple

Your staging environment will never look and behave like your production environment. Consider dropping your staging environment altogether and learn how to test in production using feature flags, canary deploys etc. instead.

### A managed runtime over Kubernetes
