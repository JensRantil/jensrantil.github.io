---
title: "Migrating to Python 3"
date: 2013-05-19
tags: [python]
draft: false
---

Migrating to Python 3
=====================

This post is partially related to my [previous blog
post](|filename|CQRS-time-to-rewind.rst) about
[Rewind](http://www.github.com/JensRantil/rewind).

I initially started the implementation of Rewind in Python 2.7. I
constantly kept test coverage to 100%, and I tried to stick to
[TDD](http://en.wikipedia.org/wiki/Test-driven_development) as much as
possible. The Python testing tool
[Nose](https://nose.readthedocs.org/en/latest/) proved to be very
valuable, as did [Travis CI](https://travis-ci.org/JensRantil/rewind).

After some time I thought "Hey, why work in Python 2 when Python 3 seems
around corner?". I installed Python 3.2 on my laptop and started
executing those tests. Travis CI helped a lot here to always make sure
that Rewind was backward compatible with Python 2.7. Ever nervous about
a test failing? Make pull request on [Github](http://www.github.com) and
Travis CI will tell you whether the pull request broke something or not.
Highly convenient. Migration to Python 3 can be summarized in three
paragraphs:

**Migrate from lists to iterators.** In many ways I like the changes to
the built-in functions `map` and `reduce`. Working with iterators are in
many ways a higher abstraction. I did have some code that expected these
functions to return lists. The flip side was that I sometimes had to
wrap in list:

``` {.sourceCode .python}
variable = list(map(func, someiter))
```

In hindsight, I probably should have used [list
comprehensions](http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)
for many of those cases as they are more readable...

**Use the 'bytes' type instead of 'string' where appropriate.** `bytes`
was introduced as a new type in Python 3. In the Rewind case, this
mostly involved ZeroMQ message frames handling, that takes `bytes`. This
also involved some conversion to and/or from `bytes` and `string`. I
tried to stick to `UTF-8` for this.

**Use 'string.format(...)' instead of 'string % ...' pattern.** Nuff
said.

Looking back
------------

In general, Python 3 is very backwards compatible (but Python 2 is not
forward compatible). As far as I can recollect, the only conditionals I
needed to make Python3 were aliasing of imports:

``` {.sourceCode .python}
try:
    # Python < 3
    import ConfigParser as configparser
except ImportError:
    # Python >= 3
    import configparser
```
