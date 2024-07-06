+++
date = 2024-07-06T17:12:35+02:00
title = "The Problem Space"
description = "Many engineers lack skills in the problem space."
tags = []
slug = "the-problem-domain"
+++
As engineers, we are great at solving problems and working in the "solution
space". But, unfortunately, many engineers are quite bad at defining the
problem(s) we are trying to solve in the "problem space". Let me explain!

Working in the **solution space** involves things such as designing, coding,
drawing, improving performance, or refactoring. It's usually what many
engineers would describe as "work".

The **problem space**, on the other hand, involves things like defining the
objective of a task, what the requirements are, what is in scope, what is out
of scope, and attending workshops. It also includes prioritizing what is the
most important thing to solve now, and which things can be done later. The
problem domain also includes _understanding your customers and the problems
they are facing_.

## "Engineers only work in solution space"

At certain workplaces, there is an expectation that someone _else_ than
engineers should work in the problem space; Engineers are supposed to get
well-defined tickets such that they can implement a solution. I don't believe
in this for a couple of reasons:

First, just like [architecture happens at multiple scales][arch-scales], there
are problems at multiple scales. And some of those problems are yours and only
yours to solve. For example, in which order you implement something, how you
implement a function, or where and when you comment on your code. All of those
depend on the problem space. If you are coding alone or in a team
(context/requirement), you likely write code comments (solution) differently.

[arch-scales]: {{< relref "2024-07-03_architecture-at-multiple-scales.md" >}}

Secondly, tickets are rarely complete. When implementing a solution, there are
most commonly new questions that come up that are not covered in a
specification; Where should the button exist? Which color and size should it
have? How should the error be presented if the customer doesn't enter anything
in the second field? When answering these questions, there are two routes an
engineer can take: Either you push back the ticket with "unclear requirements",
or the engineer can understand the problem space enough to come up with some
quick requirements and solve the problem themselves. The former will make
implementation _slow_ and very [waterfally][waterfally]. The latter will make
you progress without getting blocked.

[waterfally]: https://www.atlassian.com/agile/project-management/waterfall-methodology

## Moving between domains

The best engineers I have ever worked with are the ones who can fluidly move
between the problem and solution space. By doing so, they

* understand their customers and the problem they face which allow them to
  understand more holistically _why_ something must be implemented the way it
  is.
* can quickly fill in the gaps in missing requirements. For example, how long
  will the solution live? How well-designed does this feature need to be? Will
  we need to solve this for all microservices or just one for now?
* can take initiative to solve problems, and implement new features, without
  needing to wait for someone else to tell them what to do.

Having these skills can be a very effective way to get promoted (if you are not
working in an organization with role silos).
