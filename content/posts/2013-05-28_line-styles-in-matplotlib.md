---
title: "Line styles in matplotlib"
date: 2013-05-28
slug: line-styles-in-matplotlib
---
I'm a big fan of [matplotlib](http://matplotlib.org/) and tend to use it
every time I'd like to plot something. A while ago I had a line plot
with many lines and ran out of default colors. When that happens,
matplotlib will reuse the previously used colors.

I used Python's
[itertools](http://docs.python.org/2/library/itertools.html) overcome
this:

``` {.sourceCode .python
import itertools
import pylab as p}
look = itertools.cycle(itertools.product(['-', '--', '.-', ':', ','], 'bgrcmykw'))
look = it.imap(lambda x: string.join(x, ''), look)
for item in data.items():
    p.plot(item.X, item.Y, next(look), label=item.label)
```

I hope this little piece of code will come in handy for someone else!
