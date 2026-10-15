+++
date = 2026-10-15T23:42:12+02:00
title = "Always log your entire configuration when booting"
description = "This makes it much easier to debug when something is broken."
tags = ["programming", "observability", "provisioning"]
slug = "log-config-on-boot"
+++
Here is a small tip that has saved me a lot of time: _Always log your entire parsed configuration when your service or application boots._ Or at least, support logging it through a verbose logging level. In practice, this can be logging the entire parsed YAML structure[^1], your config struct, or all the variables you have set from environment variables. No matter how you load your configuration, log it (but mask your secrets).

[^1]: _Don't_ log your raw YAML. If you do, your might have a bug in your application where you parse and/or extract your YAML into variables (or a struct).

This habit has helped me more than once. If my application is failing to start, the first thing I do is sanity-check that my configuration has been read and parsed properly.

Say my CI/CD pipeline generates a YAML config file from [AWS Config][aws-config], stores it as a `ConfigMap` in Kubernetes, and then modifies my Kubernetes `Deployment`. A typo can slip in at any step. If my parsed application configuration can be checked through logs, I can quickly assess whether there is a bug in my application or in my CI/CD deployment pipeline.

[aws-config]: https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html

Do yourself a favor and log your parsed configuration on boot. You will thank me later.
