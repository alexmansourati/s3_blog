#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alex Mansourati'
SITENAME = u'Alex Blog'
SITEURL = "http://localhost:8000"

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/alexmansourati'),
          ('Github', 'http://www.github.com/amansourati'),
	  ('Instagram', 'http://www.instagram.com/alexmansourati'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/Users/alexmansourati/virtualenv/pelican/pelican-themes/svbhack"

USER_LOGO_URL = SITEURL + '/static/images/my_logo.png'

TAGLINE = 'Data Scientist devoted to statistical rigor and automation. Work @ Vantage Analytics.'

DELETE_OUTPUT_DIRECTORY = False
