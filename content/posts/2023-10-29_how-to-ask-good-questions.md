+++ 
date = 2023-10-29T10:01:35+02:00
title = "How to ask good questions"
description = "Asking a good question makes you get your answer faster."
tags = []
slug = "asking-good-questions"
+++
As engineers, we all occasionally need to reach out and ask for help. Asking
questions is an art! By asking a question in a good way, you will receive the
answer you are looking for, faster. A well-phrased question is also respectful
of the intended audience's time - not wasting their time to have to ask
clarifying questions etc.

As someone who has been answering questions and mentoring engineers for many
years, this post is a collection of useful practices to get your questions
answered quickly, efficiently, and effectively. Most recommendations in this
post are independent of where the question is asked: Towards a local senior
engineer in person or over a DM, on IRC for some open source project, on Stack
Overflow, or in your company Slack, etc.

## First, do your research

When I was in high school, I had a teacher in my programming class who joked
that he did not know the programming language he was teaching. Our Principal
had made a mistake in hiring someone for C++, when he was later told to teach
the C programming language. Ignoring the fact that [C _mostly_ is a subset of
C++][c-c++], his immediate response to most questions was

> "Have you tried googling for it? That's what all programmers do when they get
> stuck."

The fact that all programmers constantly google for things is so true! By
asking us to search for the answer ourselves first, he

 * made us practice looking for information. This is an invaluable skill!
 * offloaded work from himself. If he could make all students find answers to a
   third of their questions, he would have reduced his workload by 33%!

I am sure most of us have done the "Hey, do you know X? ...never mind, I
figured it out!". That's usually when we fire off a question _slightly_ too
fast and bother someone prematurely.

[c-c++]: https://isocpp.org/wiki/faq/c#is-c-a-subset

Looking for your answer is quite dependent on what you are trying to figure
out, some sources could be:

 * A `README` file.
 * Your company's
   * intraweb/wiki.
   * source code.
   * mailing lists.
 * Searching for similar questions/discussions in your chat system (Slack,
   Discord, etc.).
 * Stack Overflow
 * Google. :)
 * Community spaces for your programming language, or the library you are
   trying to use. Most of them have [an IRC channel][cassandra-irc] or
   [Slack][gopher-slack] etc.
 * A third party library's source code. I have learned _so_ much by doing this.
   Highly recommended!

[gopher-slack]: https://invite.slack.golangbridge.org/
[cassandra-irc]: https://cwiki.apache.org/confluence/display/CASSANDRA2/IRC

Don't get stuck doing research, though! It's better to get an answer to a
question which have been asked before than to get stuck looking for an answer
that doesn't exist. Timeboxing for 5-30 minutes to look for a solution can
avoid putting unnecessary load on your organisation, on your team, or fellow
programmers. It also has a benefit prepping you to understand an answer if you
_do_ need to ask your question!

## Communicate well

Phrasing a question is about communication. Here are some recommendations:

### Write the question in one message

Try to include as much information in _one_ message. This avoids the ["Don't
ask to ask"][dont-ask-to-ask] and ["Hello."][nohello] situations.  There are
few as frustrating things as constantly having to do a lot of unnecessary
back-and-forths when answering questions.

[dont-ask-to-ask]: https://dontasktoask.com
[nohello]: https://nohello.net

### Bundle all the information

A well-phrased question includes the following:

**The overall problem you are trying to solve.** Instead of just writing "I am
trying to use this class", you also write "I am trying to make my code do Y".
Or even better, "I am trying to make my code do Y, to be able to implement the
product feature Z.". By doing this, you avoid the [_XY-problem_][xy-problem].
Sometimes knowing the context of what you are trying to do leads to the insight
that it can be done in a much better, different, way.

**The context.** Is this for a specific environment or microservice? Is this
for one-off solution or a sustainable solution? For former hints that someone
could share a one-off hack or workaround.

**The urgency if you question.** Are you stuck solving an incident? Let people
know! Have you found a **workaround**? Let people know as it signals it's less
urgent. Further, let people know if you are blocked or not - and when you would
love to have an answer (ie. "I would appreciate if someone could give me some
input on this before the end of the day! 🙏").

**What you have tried, what you expected, and what happened instead.** This is
the classical information included in a good bug report. Make sure that the
reader can somehow access the _exact_ error message & log output if there is
such. Add links to other systems (CI/CD) etc., if possible.

**Your research.** Please include what you found when you did your research.
Was there anything in particular that showed up? Something that hinted you
could solve your problem in a specific way? Why did that solution not work?

**Additional information** such as whether this worked before or not, or if you
have a suspicion what might be wrong.

**References.** Links to a Jira ticket, pull requests, CI/CD builds, commit
SHAs, logs etc.

Also, don't be hard on yourself if you realize that you forgot to attach some
needed information to your question. See it as a learning opportunity for your
next question. ✨

[xy-problem]: https://xyproblem.info

### Start with the most important ask

I used to work with a colleague who would ask their question in the completely
wrong order:

> In the production environment, I got this error message. I typed in X. Google
> gave me [this][placeholder-link], but I don't think it helps. I am trying to
> achieve Y.

This meant that every time they asked me, I had to buffer _all_ the information
in my head until I could answer.

[The Minto Pyramid][minto] is a communication framework which helps to simplify
communication. In short, it is about splitting your message into Conclusion
(the most important thing), Key Arguments (the main takeaway), followed by
Details (optional, but useful info). Using the Minto pyramid can be highly
useful when phrasing a question!

**Conclusion:**

> Does anyone know how to do X in Y?

**Key points:**

> I am trying to achieve Z in our production environment. I have tried A and
> was expecting B to happen, but it fails with C... [The reference
> documentation][placeholder-link] hints it should work. I am currently able to
> work around this, and I don't think this ever worked before (based on searching
> in Slack).

**Detailed information:**

> I tried googling for this. It brings up [this link][placeholder-link] which
> doesn't really make sense in this case... [This pull request][placeholder-link]
> on Github _might_ have tried to achieve something similar back in the day don't
> know. You can find the logs for my error message [here][placeholder-link].

Notice how I preferred to use links to things instead of pasting large bodies
of logs into my message above. Inlining lots can make a reader overwhelmed. If
you _do_ need to do it, many collaboration tools (Slack/Discord/...) support
[uploading code snippets which can be collapsed/expanded][slack-snippet].
E-mail supports file attachments.

[minto]: https://untools.co/minto-pyramid
[slack-snippet]: https://slack.com/intl/en-se/slack-tips/share-code-snippets

Finally, use paragraphs or bullets for long messages! This makes it much easier
to digest your message. Most collaboration tools (such as Slack) can add new
lines `shift+return` to split into multiple paragraphs.

### Read the room

Asking good questions also means reading the room. This is where company
culture partially comes in! Some examples:

 * If you are at a company where working on weekends/evenings is frowned upon,
   maybe you could write your question during office hours instead? Slack has a
   feature to schedule messages which is useful here.
 * Be careful with cross-posting your question in multiple chat rooms. It might
   be frowned upon and has a risk of DDoSing your community. If you cross-post,
   prefer to direct people to the place where you would like the answer to
   avoid parallel threads on the topic.
 * If there is an ongoing incident, maybe you could hold off with asking your
   question.
 * Avoid `@channel` ping in Slack to disturb everyone (unless it's a really
   urgent question).
 * Asking too many questions in public Slack channels has a risk of giving you
   a bad reputation. Ask for feedback by someone in your community if you are
   worried about this! One way to combat this, is to send of questions to
   specific people. That said, read about load-balancing below!

### Load-balance your questions

As a domain expert, it's easy to get bogged down in answering questions all
day. If you can, try to spread your questions to multiple people. The easiest
way to do this is to ask your question in a public space (public chat room,
etc.) where multiple people can pitch in to answer. This also has the benefit
of other people being able to read the answers and learn something!

### Follow up when you have an answer

If you find the answer to your question, share it! This signals to others that
they can stop looking for an answer. But it also means you enable others to
avoid ending up in the same situation as you in the future.

Did someone help you solve the problem? Give them credit and thank them. ❤️ That
will increase the chance for you to get help in the future!

## Conclusion

By following these recommendations you will make your colleagues happier,
improve communication, and - most importantly - get your answers quicker.

Finally, whenever you have learned something new, remember that it's now your
responsibility to share this knowledge with other people if they ever happen to
have the same question!

## References

I am by no means the first to write down how to ask questions. If you are
interested in learning more, here are a couple of additional sources:

 * [How to ask questions in Linux IRC help channels][linux-questions]. It
   focuses more asking questions in public IRC, than in private company
   settings.
 * [How To Ask Questions The Smart Way][questions-the-smart-way] by Eric S.
   Raymond

[questions-the-smart-way]: http://www.catb.org/~esr/faqs/smart-questions.html
[linux-questions]: http://www.sabi.co.uk/Notes/linuxHelpAsk.html

[placeholder-link]: https://example.com/
