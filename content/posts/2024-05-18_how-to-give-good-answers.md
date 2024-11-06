+++
date = 2024-05-18T22:20:35+02:00
title = "What's in a good answer?"
description = "Answering questions the right way can dodge many questions in the future."
tags = []
slug = "a-good-answer"
+++
_This is a follow-up on [How to Ask Good Questions][good-qs]._

[good-qs]: {{< ref "posts/2023-10-29_how-to-ask-good-questions.md" >}}

Just like asking questions is an art form, answering them requires some skill.
Here are some general recommendations on things to think about when answering a
question:

## Keep a friendly tone

A person asking a question is implicitly in a vulnerable position; They expose
themselves to not knowing something. I think that makes it extra important to
treat the person with extra respect for stepping out of their comfort zone.
This is particularly important with new-hires.

As such, keep a friendly tone. Assume good intent, and try to put your
annoyances aside. 

A friendly answer involves writing full sentences. Sloppy responses shine
through. This also means that simply pasting a URL should be avoided. It
is similar to responding with <abbr title="Read The F-ing Manual">RTFM</abbr>.
Don't just respond with

> https://docs.python.org/3/library/argparse.html#action

Instead, a better response is

> The `ArgumentParser` has a parameter called `store_const`. Have a look at
> https://docs.python.org/3/library/argparse.html#action.

Further, if this is someone asking questions from another part of your
workplace, remember that helping them out can be a great way to build
bridges and network across your workplace. Maybe one day that person will help
_you_ out.

## Avoid assumptions

It's easy to make assumptions about what the person asking a question has done or
tried. Not all people ask [the perfect question][good-qs]! Instead of assuming,
ask questions. For example, the example in the previous section could be
rephrased even better:

> The `ArgumentParser` has a parameter called `store_const` which I think is
> what you want to do. Have you had a look at
> [this](https://docs.python.org/3/library/argparse.html#action)?

In this example, we don't assume they haven't had a look at the URL. Instead,
we _ask_.

## Getting all the context

Sometimes you don't get the context you need in a question. If so, counter with
clarifying questions! This helps the person asking to know which information to
include next time they ask a question.

Make sure you ask as many clarifying questions as possible in _one_ message (to
avoid something similar to [NoHello][nohello]). Having a lot of back-and-forths
can take a lot of time. _If_ you notice there is a risk of having a lot of
roundtrips, reaching out to schedule a call might be faster than written
communication.

[nohello]: https://nohello.net

## Start with the answer

The [Minto Pyramid][minto] is a communication framework that focuses on saying
the most important thing first, adding your most important key arguments,
followed by details.

[minto]: https://untools.co/minto-pyramid

In the context of good answers, the Minto Pyramid means "start with actual
answer, share the key arguments why it is so, followed by optional additional
details".

As an example, let's say someone asks:

> What are the main components of a computer processor (CPU)?

The non-Minto Pyramid approach to answering this would be something like

> This is documented [here][cpu]. Registers provide temporary storage for
> instructions and data. The Control Unit (CU) manages the execution of
> instructions and data flow. The Arithmetic Logic Unit (ALU) performs
> arithmetic and logical operations. Therefore, the main components of a CPU
> are the ALU, CU, and Register Set.

Notice how the answer to the question is _the last sentence_. Someone
needs to read the entire blob of text to arrive there.

Answering using the Minto Pyramid inverts this. Here is an example answer:

> The main components of a CPU are the Arithmetic Logic Unit (ALU), the Control
> Unit (CU), and the Register Set. The ALU performs arithmetic and logical
> operations, the CU manages the execution of instructions and data flow, and the
> registers provide temporary storage for instructions and data. You can read more
> about this [here][cpus].

Notice how the question is answered in the first sentence, followed by more
details, and then followed by even more details as a reference. The reader can
stop at any time and still have gotten their answer. Much better.

[cpus]: https://en.wikipedia.org/wiki/Central_processing_unit 

## How did you get to the answer?

The last part of a Minto Pyramid answer, the "details", is an excellent place
to share _how_ you got to your answer. What did you look at? Is some log message,
or some piece of code, useful to understand why something works the way it does?
Please share it! Doing so enables someone to answer a similar question
themselves next time without your involvement. Enablement, ftw!

Similarly, how did _you_ learn about this? Did you read some books? Read a
useful blog post? References to things like that can also act as an inspiration
to learn a completely new subject and allow your colleagues to grow.

## Verify the recipient understood

"Did what I wrote make sense?" I think this is an inviting question after
writing a response. In certain cultures, saying that you did not understand is
rare. At least, help someone to express if there was something they didn't
quite follow!

## Don't be too fast

In this day and age, a lot of people expect immediate answers to questions posed
on chat/instant messaging (Slack, Microsoft Teams, etc.). This is somewhat
controversial, but sometimes you are doing yourself and the person asking a
disservice by answering too quickly.

Adding a delay to answer questions can have the following positive outcomes:

 * You give other people the opportunity to answer. I have seen other people
   hindering other people's growth or time to shine by being faster than them
   to answer questions.
 * You make people not expect immediate answers. This makes it less stressful
   for you to answer quickly in the future. If people don't think you are
   answering quick enough, have a conversation chat reply expectations!
 * You force people to practice searching for answers themselves. If people
   don't learn how to do this themselves, you are making yourself a bottleneck
   for your team!

## Can you answer in public?

I once used to be [hammered by questions in <abbr title="Direct messages">DMs</abbr>][knowledge-bottleneck]. People would reach out to me
personally, and every answer I gave had a single recipient.

[knowledge-bottleneck]: {{< relref "2023-08-29_the-knowledge-bottleneck-I-used-to-be.md" >}}

This meant that every answer I gave only benefitted a single person. If you
have ever been in a position of being a local expert at something, you quickly
start to notice that multiple people ask the same question. Could I do better?
(Hint: Yes!)

Every time someone reached out privately with a question that I thought would
benefit other people, I would respond with

> Hello! Would it be possible for you to ask that question in a public
> channel, instead? That way, other people can benefit from the answer. I will
> make sure the question is answered, either by me or someone else.

Doing this had multiple benefits:

 * I contributed to a culture of transparency where conversations were not just
   happening in silos.
 * I made sure that answers to questions could be read by other people.
   Knowledge sharing! I was making myself a true [force
   multiplier][force-multiplier].
 * I made people less dependent on _me_ to answer their questions. This reduced
   my [bus factor][bus-factor] and made it possible for other engineers to
   offload me. It also allowed others to show off their skills in public by
   getting to answer some questions themselves!

[force-multiplier]: https://www.amazon.se/-/en/Tony-Chatman/dp/0998992704
[bus-factor]: https://en.wikipedia.org/wiki/Bus_factor

## Build quality in

The last tip I have is also to ask yourself _why_ a question is being asked in
the first place? Asking something like the [Five Whys][five-whys] can be very
useful and help you to answer future questions implicitly instead of going
through you. Some realizations I have had when doing Five Whys are:

 * Realising that my workplace is lacking any formal training on something.
   This has made me give presentations on workshops to be proactive.
 * Realising that error messages are too cryptic and need to explain better
   what they mean or what action a user must take.
 * Realising that a logged message is really unclear and needs to be clarified.
 * Realising that the UX of a product is not good enough.
 * Realising that there is actually missing documentation that needs to be
   added somewhere.
 * And more.

[five-whys]: https://en.wikipedia.org/wiki/Five_whys

## Closing thoughts

If you write well-written responses, you can use them as reference material if
someone asks the same question again. Most chat apps allow you to copy the URL
to a response and paste it as a conversation (but remember, don't just answer
with a link!). Common answers can also be pinned :round_pushpin: in certain
chat apps ([such as Slack][pin-slack]) to make them easily found.

[pin-slack]: https://slack.com/intl/en-gb/help/articles/205239997-Pin-messages-and-bookmark-links

Also, if you notice someone isn't that great at asking questions. You can of
course also recommend that they have a look [my previous blog post on "How to
ask good questions"][good-qs]. :wink:
