+++
date = 2024-07-31T17:36:35+02:00
title = "CrowdStrike: Risk assessment is better off at the sharp end"
description = "I think the CrowdStrike incident is a great example of centralized risk management gone wrong."
tags = ["security", "risk"]
slug = "centralised-risk-management"
+++
Today I wanted to write something about [the recent CrowdStrike Falcon debacle][crowdstrike-debacle] and about one contributing factor, namely _centralised risk management_.

[crowdstrike-debacle]: https://en.wikipedia.org/wiki/2024_CrowdStrike_incident

## The importance of local risk assessment

I recently watched [the trailer][safety-differently-trailer] for the movie ["Safety Differently"][safety-differently] by Sidney Dekker. One of the things it talks about is that **the farther you are from a system, the less effective your risk management is likely to be**. This includes assessing risks and putting controls in place to mitigate those risks. Or to put it another way, the operators of a system _at the edge_ are usually the best people to do risk assessment, come up with controls, and defend against catastrophes.

[safety-differently-trailer]: https://www.youtube.com/watch?v=IEYN38nir_w
[safety-differently]: https://www.youtube.com/watch?v=EeIucLnEa24

For example, if you are a security & risk department far away from your developers, the controls you put in place for the developer's software will likely not reduce risk the way you expect. You might for example [add security controls that make operational risk worse][operational-risk]. Instead of enforcing specific controls on all developers, a much better approach is to give the requirement and work _together_ with the developers to come up with a solution. Don't do "we must use nginx for TLS". Instead, tell them that transport encryption is a must and they get to pick their favorite HTTP server that works best for them.

[operational-risk]: {{< relref "2024-05-12_security-and-risk.md" >}}

## Tailored risk profiles

Different systems have different risk profiles. However, centralized risk management commonly doesn't tailor its risk assessment to subsystems.

For example, let's say I am a SaaS company. The SaaS has a central authentication service and a service that sends out overnight mobile push notifications. The authentication system is much more important for the SaaS to function properly than the overnight push notifications. Customers must be able to log in at all times. Push notifications are much less important.

The above implication is that we probably want to do much more careful rollouts of changes to the authentication service than the push notification service. The former needs more observability, and possibly even a slow staggered rollout of changes to ensure logins still work.

Centralized risk management tends to treat multiple systems the same, even though they have very different risk profiles. For example, a security department might require "all security upgrades must be rolled out immediately to all internal services" - even though certain systems such as the authentication system must be upgraded much more carefully!

## CrowdStrike and centralized rollouts

So, what does this have to do with CrowdStrike's Falcon incident? In the case of Falcon, CrowdStrike _centrally_ decided how to roll out a new version of Falcon to all customers, _independently of how sensitive the downstream systems were to risk_.

**Falcon had the same rollout strategy independently of whether it was pushing it out to a core system of an airline/bank, or a small SaaS startup.** The decision to perform an upgrade, how quickly, and in what way, must [always be done at "sharp end"][sharp-end]. It might be easy to point the finger at CrowdStrike for rolling out a bug, but I think it was CrowdStrike's customers that made the bigger mistake here; Configuring automatic 0-day upgrades to go out automatically to very critical core systems (where downtime is very very expensive) is not a smart thing. Rollouts like this should be staggered, tested, and possibly passed through a staging environment of some sort.

[sharp-end]: https://how.complexsystems.fail/#11

I would not be surprised if Falcon security upgrade policies were enforced by central security departments far away from the "sharp end". Only time will tell if I am right.
