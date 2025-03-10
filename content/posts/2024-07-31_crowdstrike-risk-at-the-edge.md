+++
date = 2024-07-31T17:36:35+02:00
title = "CrowdStrike: Risk assessment is better off at the sharp end"
description = "I think the CrowdStrike incident is a great example of centralized risk management gone wrong."
tags = ["security", "risk"]
slug = "centralised-risk-management"
+++
Today I wanted to write something about [the recent CrowdStrike Falcon incident][crowdstrike-incident] and about one contributing factor, namely _centralised risk management_.

[crowdstrike-incident]: https://en.wikipedia.org/wiki/2024_CrowdStrike_incident

## The importance of local risk assessment

I recently watched [the trailer][safety-differently-trailer] for the movie ["Safety Differently"][safety-differently] by Sidney Dekker. One of the things it talks about is that **the farther you are from a system, the less effective your risk management is likely to be**. This includes assessing risks and putting controls in place to mitigate those risks. Or to put it another way, the operators of a system _at the edge_ are usually the best people to do risk assessment, come up with controls, and defend against catastrophes.

[safety-differently-trailer]: https://www.youtube.com/watch?v=IEYN38nir_w
[safety-differently]: https://www.youtube.com/watch?v=EeIucLnEa24

For example, if you are a security & risk department far away from your developers, the controls you put in place for the developer's software will likely not reduce risk the way you expect. You might for example [add security controls that make _operational_ risk worse][operational-risk]. Instead of enforcing specific controls on all developers, a much better approach is to give the requirement and work _together_ with the developers to come up with a solution. Don't do "we must use nginx for TLS". Instead, tell them that transport encryption is a must and they get to pick their favorite HTTP server that works best for them.

[operational-risk]: {{< relref "2024-05-12_security-and-risk.md" >}}

## Tailored risk profiles

Different systems have different risk profiles. However, centralized risk management commonly doesn't tailor its risk assessment to subsystems.

For example, let's say I am a SaaS company. The company has a central authentication service and a service that sends out overnight mobile push notifications. The authentication system is much more important for the SaaS to function properly than the overnight push notifications. Customers must be able to log in at all times. Push notifications are much less important.

The above implication is that we probably want to do much more careful rollouts of changes to the authentication service than the push notification service. The former might need more observability, slower rollouts (gradually increasing over a couple of days), and a well-tested release candidate that has been battle-tested by the industry/company for at least a week or two - all this to ensure logins still work.

Centralized risk management tends to treat multiple systems the same, even though they have very different risk profiles. For example, a security department might require "all security upgrades must be rolled out immediately to all internal services" - even though certain systems such as the authentication system must be upgraded much more carefully!

## CrowdStrike and centralized rollouts

So, what does this have to do with CrowdStrike's Falcon incident? In the case of Falcon, CrowdStrike _centrally_ decided how to roll out a new version of Falcon to all customers, _independently of how sensitive the downstream systems were to risk_.

**Falcon had the same rollout strategy independently of whether it was pushing it out to a core system of an airline/bank, or a small SaaS startup.** The decision to perform an upgrade, how quickly, and in what way, should [be done at the "sharp end"][sharp-end]. It might be easy to point the finger at CrowdStrike for rolling out a bug, but I think it was CrowdStrike's customers that made the bigger mistake here; Configuring automatic 0-day upgrades to go out automatically to very critical core systems (where downtime is very very expensive) is not a smart thing. Rollouts like this should be staggered, tested, and possibly passed through a staging environment of some sort.

[sharp-end]: https://how.complexsystems.fail/#11

Above said, CrowdStrike could also had offered customers the possibility to auto-apply updates based on things like:
 * a **hardcoded minimum delay** such as "apply this after 2 days since release".
 * a **hardcoded maximum delay** such as "apply this at most after 5 days since release".
 * **compatibility score** (similar to [Dependabot][compat-score]) such as "apply this only if more than 10% of CrowdStrike's customers have applied it succesfully.

This would have allowed CrowdStrike's customers to tune their risk vs. speed apetite tailored to their specific system.

[compat-score]: https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates#about-compatibility-scores

Compare the CrowdStrike incident to the the global [Log4shell incident][log4shell] which happened in 2021. According to [the incident's wiki page][log4shell] it

> [...] had the potential to affect hundreds of millions of devices.

and

> [...] the vulnerability affected 93% of enterprise cloud environments.

Still, the rollouts to fix Log4shell did not bring down airlines or banks to any large extent. Why? I would guess it was because operators were able to carry out a controlled rollout of fixes to one system at a time, with testing along the way for each system based on its risk profile.

[log4shell]: https://en.wikipedia.org/wiki/Log4Shell

The CrowdStrike incident was a missed opportunity for our industry to tailor change management based on different risk profiles.
