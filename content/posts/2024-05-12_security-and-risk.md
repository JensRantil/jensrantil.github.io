+++ 
date = 2024-05-12T10:28:35+02:00
title = "Security is one part of risk"
description = "What are we trading when focusing on security?"
tags = ["security", "risk"]
slug = "security-and-risk"
+++
I think our software industry sometimes is blindsided when it comes to
security. Don't get me wrong, I am of course in favor of good security
practices. But I think we could get better at understanding the trade-offs when
improving security.

## A story

At a previous employer, we partnered with a big bank. They were using our
SaaS's REST API over the Internet. For security they used

 * **TLS** for encryption to make sure no one was eavesdropping over the
   Internet.
 * a **static API token** to authorize with us.
 * **[certificate pinning][certificate-pinning]** to make sure they were
   talking to us over the Internet (and not Eve-the-evil-hacker).

[certificate-pinning]: https://sv.wikipedia.org/wiki/Certificate_pinning

The <abbr title="Chief Information Security Office">CISO</abbr> department of
this particular bank reached out to us and required us to to use [mutual
TLS][mtls] (mTLS) since it was "more secure". I thought their request was
[security theatre][theatre]; it would not improve our security in any
particular way.  Also, we had used TLS+pinning+token for many years, it worked
well, had good processes in place for this, and knew how it worked.

[theatre]: {{< relref "2023-09-13_the-theater-tasks-that-add-value.md" >}}

[mtls]: https://en.wikipedia.org/wiki/Mutual_authentication#mTLS

Ever tried to argue against a bank? I tried to explain that we already covered
all their _actual_ requirements:

 * No one could eavesdrop.
 * We knew they were the ones making API calls to us.
 * They knew they were making API calls to us and not someone else.

Further, I knew that mTLS would require authentication on a different network
layer. It would add more technical complexity for us. Also, we did not want to
become a <abbr title="Certificate Authority">CA</abbr> and start doing
complicated <abbr title="Certificate signing requests">CSRs</abbr>. Still, the
customer keps pushing for this.

The pushback felt hopeless, but one day I had a breakthrough! I explained to
the customer that their solution had **"operational risk"**, particularly
around certificate expiration and renewal. The term "operational risk" was like
a magic password that opened up new doors in the conversation. The CISO
representative responded with:

> "Oh, operational risk you say? That makes a lot of sense. Our department not
> only works with security but with all types of risks. We weigh different types of
> risks against each other. We will consider your operational risk!"

With that, I never heard from them again. I won my argument!

My biggest learning from this was how useful it is for **a security department
to take a more holistic approach to risk**. Without this, you are missing what
you are trading for "higher security".

## Other types of risk

Here are some examples of "operational risk" that I have seen/heard being
down-prioritized at various companies:

 * **Systems stability.** My example above is a good example of this. We risked
   downtime if certificates would expire.
 * **Reduced speed of development.** For some companies, innovation might be
   more important than security.
 * **Human error.** Certain security controls add more manual work and
   increases the risk of making mistakes.
 * **Cost increases.** There are plenty of SaaS and AWS services to
   improve security, but they add costs. If you are a company low on
   budget, enabling every security service out there will add costs.
   Not to mention that the salary for engineers implementing security controls also
   is a thing.

The above list is likely not exhaustive.

## Closing thoughts

I have heard people refer to companies as having "an unhealthy security
culture" if they don't have the right controls in place. Similarly, I would say
that companies that focus _too much_ on security can have an unhealthy security
culture.

It's okay to say no to adding additional security control. My personal approach
to security is to take an iterative approach, focusing on the highest security
risks, but weighing the controls against other types of risk.
