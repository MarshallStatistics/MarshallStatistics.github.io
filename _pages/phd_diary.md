---
defaults:
layout: archive
title: "PhD DIary"
permalink: /phd_diary/
scope:
path: ""
type: pages
values:
layout: single
author_profile: true
include: _includes/head/custom.html
favicon: "/favicon.ico"
---

<h1>My PhD Diary</h1>

<ul>
  {% for post in site.tags.phd-diary %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
