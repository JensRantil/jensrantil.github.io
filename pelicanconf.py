#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jens Rantil'
SITENAME = u"Jens Rantil's Hideout"
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Stockholm'

THEME = 'themes/svtle'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

AUTHOR_BIO = ("Swedish/English, fullstack software engineer"
              ' (<a href="http://www.telavox.se" target="_blank">@Telavox</a>),'
              ' <a href="http://www.lth.se/english/education/programmes/master_engineering/engineering_mathematics/">MSc'
              ' in Engineering Mathematics</a>, traveller, nerd, juggler,'
              ' guitarist, african drum player. Inspired Swede.')

# Blogroll
LINKS =  (('Twitter', 'http://www.twitter.com/JensRantil'),
          ('Github', 'http://www.github.com/JensRantil'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
