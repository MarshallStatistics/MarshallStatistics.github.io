---
layout: archive
title: My PhD Diary
---

<h1>My PhD Diary</h1>

<ul>
  {% for post in site.tags.phd-diary %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
