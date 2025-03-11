+++
date = 2025-03-11T10:38:35+02:00
title = "The Dangers of an IDE"
description = "A modern IDE constantly nudges you to couple your code in a bad way."
tags = ["Simplicity", "Testing"]
slug = "integrated-development-environments-harmful"
+++
_I recently stumbled across the post ["Does Visual Studio Rot The Mind?"][vs] and I was reminded of a blog post that I read a very long time ago and could not find on the Internet. I thought I would write down the gist of that article here such that I can share links to it later._

[vs]: https://charlespetzold.com/etc/DoesVisualStudioRotTheMind.html

There is this theory that the best and most beautiful code was written before the nineties, before the introduction of modern <emph title="Integrated Development Environments">IDEs</emph> such as VSCode, Eclipse, IntelliJ, Visual Studio, et al. Why? It forced programmers to keep their code in their heads.

As programmers, it is our duty to keep complexity to a minimum. As I wrote in [my simplicity series][simplicity-series], complexity means "something that has been braided together". In short, it is coupled. Most programmers know that good code has ["loose coupling, high cohesion"][wiki-coupling]. But why?

[simplicity-series]: {{< relref "2023-11-06_my-simplicity-toolkit" >}}
[wiki-coupling]: https://en.wikipedia.org/wiki/Coupling_%28computer_programming%29

Contrary to common beliefs, programmers spend the majority of their time _reading code_. For example, we debug why something is not working the way we expect, or we are trying to figure out where to implement our new feature. The fewer things we need to keep in our head at one point in time, the easier it is to understand the code we are looking at. The same applies to modifying code. This is why we try to avoid patterns like [Action at a Distance][distance], work with abstractions to not have to know the details, or organise our source code in modules.

[distance]: https://en.wikipedia.org/wiki/Action_at_a_distance_(computer_programming)

Modern IDEs work against that. They allow you to treat your source code as a giant, unstructured list of files, classes, functions, and global variables. All these can be accessed "at your fingertips" at all times through what is know as "code completion", "auto-complete", "IntelliSense" etc. These are all problematic.

If I am working in one part of my source code, I should generally not have to care about other parts of the source code - keeping fewer things in my head. Code completion constantly nudges you to consider using classes and functions in a completely different part of the source code. It nudges you to couple difference modules in ways that they should not interact[^1].

[^1]: Certain programming languages (C++, C#, ...) _do_ have support for namespacing which can help with this. That said, not all programming languages have this. There are also build systems such as [Bazel][bazel] that support access control lists for which modules are allowed to import other modules. Finally, there are also [testing libraries that allow you to enforce your source code layout][arch-unit], but I consider that outside the scope of this blog post.

[bazel]: https://bazel.build
[arch-unit]: https://www.archunit.org

There is value in having to `cd` into a directory and only keep that code in your head. If you haven't tried it, I encourage you to [try to code something in a simple editor][not-always-ide][^2] at some point. You need to approach coding in a completely different way -- learning to keep the mental space small & lean. Learning that will also make you a better programmer in an IDE.

[^2]: For example, Vim or Emacs.

[not-always-ide]: https://medium.com/better-programming/why-you-shouldnt-always-use-an-ide-28ed8c7e6843

About 15 years ago, I worked with a colleague who told me there was this Swedish programmer at a large corporation who would write all of his Java code _in Notepad_. This programmer was surprisingly productive. We laughed about it, but in retrospect, I think that programmer might actually have been onto something.