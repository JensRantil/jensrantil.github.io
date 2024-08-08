+++
date = 2024-08-08T20:55:35+02:00
title = "Natural solutions"
description = "Solutions fall naturally out of well-defined problems."
tags = ["problem space"]
slug = "natural-solutions"
+++
I recently wrote about [the solution vs. problem space][problem-solution]. For years I have had this belief that __given a problem that is well-defined enough, a solution will naturally unfold__. In other words, _solutions are the natural fallout of well-defined problems_.

[problem-solution]: {{< relref "2024-07-06_the-problem-domain.md" >}}

But what is "a well-defined problem" anyway? It means having the answer to the following:

 * **Problem you are trying to solve.**
 * **Scope of the solution.** Where to draw the boundary of what should be solved and what should not, when a solution must be ready, etc.
 * **Our requirements & non-requirements.**
 * **Knowing our [_needs, values, principles, practices & tools_][spine].**

[spine]: https://spinemodel.info

A common misunderstanding is that the list above must be known before starting a solution, leading to a waterfall process. This is not the case! One of the biggest shifts I have had as an engineering leader is being able to move more freely from solution to problem space _and back again_. Solving a problem usually involves an iterative process of moving back and forth between problem and solution space. For example, it can go something like this:

 1. My users are not noticing the login button on the front page. _(problem space)_
 2. Hm, how about I simply make it a big giant orange image with the text "Login"? _(solution space)_
 3. Yeah, but we would like the website to be SEO-friendly. Besides, maintaining images with text is probably not very maintainable over time. _(two new requirements, problem space)_
 4. Ah, I'll solve it using CSS instead. (new solution, solution space)
 5. But wait, we want the login link to look the same on all pages, not just the front page. _(new scope, problem space)_
 6. ...

Notice how every step naturally jumps between problem and solution space and vice versa.

## Implicit vs. explicit problem spacing

Most engineers iterate between the two spaces somewhat implicitly. However, there are three big reasons why there is much value in doing it more explicitly:

First, by being explicit about your problem space, you can **document your problem space for others to see**. I have found <abbr title="Request for Comments">RFCs</abbr> containing the background to a solution to be immensely useful when explaining to peers why something was done the way it was.

Secondly, it **reduces frustration**. As engineers, many of us have been told our job is to _solve_ problems, not define them. This is why many engineers are frustrated by meetings & workshops - spending time in the problem space means we are not doing our job. However, I believe that engineering is equally much about defining the problems we are trying to solve. (Don't get me wrong, there are unproductive meetings & workshops, too, though! :wink:)

Thirdly, by clearly defining the problem, I become **less attached to my proposed solution and more open to others** replacing it with something entirely different.

## Closing thoughts

A downside of explicitly working in the problem space is that people around you might feel frustrated that "we are not moving forward". I have seen this frustration from many people, irrespective of their role. I am confident that exploring the problem space implicitly solves a problem. However, not everyone does. Hopefully, this article help to clarify this.
