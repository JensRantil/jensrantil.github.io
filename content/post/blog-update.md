---
title: "Blog Update"
date: 2018-05-06
tags: []
draft: false
---

I'm happy to announce I've finally gotten the time to migrate my blog from
[Pelican](https://blog.getpelican.com/) to [Hugo](https://gohugo.io)! The
migration started [way too long
ago](https://github.com/JensRantil/jensrantil.github.io/commit/01cc978f5d0f5b09fd8203b838c8ef314314f4ac).
Life came in the way and last week, I finally got the time to migrate all
content.

## What this means for you as a reader

Given that I've put [Continuous
Delivery](https://github.com/JensRantil/jensrantil.github.io/commit/25ee8f37ca094e666170245ecfc7dfb9b74fee08)
in place and Hugo doesn't require a virtual Python environment and other bloat
around it, writing posts will be much easier. So, expect a more continuous flow
of content!

## Migration process

It seem like I'm [not the only one migrating to
Hugo](https://www.google.com/search?q=migrated+to+hugo&ie=utf-8&oe=utf-8&client=firefox-b-ab),
but in short this was my process:

 1. I set up a basic Hugo site in the [same Github repo as
    before](https://github.com/JensRantil/jensrantil.github.io).
 2. I converted all previous content (in
    [reStructuredText](http://docutils.sourceforge.net/rst.html)) to
    [Markdown](https://en.wikipedia.org/wiki/Markdown) using [Pandoc]() and
    [this](https://gist.github.com/zaiste/77a946bbba73f5c4d33f3106a494e6cd).
    The metadata (or ["Front
    Matter"](http://gohugo.io/content-management/front-matter/) as called in
    Hugo) had to be manually updated to look correct in the converted filed.
 3. I [started creating my own
    theme](https://github.com/JensRantil/jensrantil.github.io/commit/57eb935b4dc7237e559413827c83ffe923024a8c)
    from examples on Bootstrap 3 layouts.
 3. I realized I would never get the new site published if I had to create
    things from scratch :-) I settled on the
    [Minimal](https://github.com/calintat/minimal) Hugo theme by browsing
    through the [public Hugo themes](https://themes.gohugo.io/).
 4. I did some [minor adjustments]
 4. I converted the pages that had resources (images etc.) to ["Page
    Bundles"](http://gohugo.io/content-management/page-bundles/).
 5. I [added continuous
    delivery](https://github.com/JensRantil/jensrantil.github.io/commit/25ee8f37ca094e666170245ecfc7dfb9b74fee08)
    from `development` branch on Github to automatically have
    [TravisCI](https://travis-ci.org/) publish a new version of the blog as
    soon as I push new posts.

## Stuff remaining

 * Migrate the Disqus comments from the old URL structure to the new.
 * Some adjustments to make the text a little larger. I think the minimal theme has a bit too small text. I want to improve readability.
 * Correct header hierarchy. I've filed a bug about it [here](https://github.com/calintat/minimal/issues/68). The headers also look a but out of place in terms of sizing.

## Credits

This website would not have been created this fast if it wasn't for the amazing
people behind [Hugo](http://gohugo.io) and
[@calintat](https://github.com/calintat) who made the [Minimal
theme](https://github.com/calintat/minimal).
