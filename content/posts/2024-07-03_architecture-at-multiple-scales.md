+++
date = 2024-06-03T09:40:35+02:00
title = "Architecture at multiple scales"
description = "Architecture is a fractal concept."
tags = []
slug = "multiscale-architecture"
+++
There is a belief that "software architecture" only involves designing the "big
picture" of how software is built. For example, drawing boxes and arrows how
microservices integrate, or how larger modules of a code base should be
organized and coupled together.

I beg to differ. I think of architecture simply as "how to organize and
associate technical components" where the term "technical component" is left
explicitly vague. Just like defined above, a technical component _can_ be a
microservice, or a module. But it can equally be how functions call each other,
or even the order of how sub-components (if conditionals and for loops) in a
function are written. That is, I think of _architecture_ as concept that
applies _both at grand scales and micro scales_. Sort of like a
[fractal][fractal].

[fractal]: https://en.wikipedia.org/wiki/Fractal

I believe that every engineer has the role of an architect, but simply at
different scales. This is why the article [Scaling the Practice of
Architecture, Conversationally][scaling-arch] by Andrew Harmel-Law is so
useful. It talks about ways to push architectural decisions out onto all
engineers.

[scaling-arch]: https://martinfowler.com/articles/scaling-architecture-conversationally.html
