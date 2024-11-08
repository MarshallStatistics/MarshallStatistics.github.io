---
defaults:
layout: archive
title: "Networks"
permalink: /networks/
scope:
path: ""
type: pages
values:
layout: single
author_profile: true
include: _includes/head/custom.html
favicon: "/favicon.ico"
---
I am currently in the process of putting some notes together on networks and graph theory. Please do let me know your thoughts or improvements either via email or LinkedIn. I hope these notes are useful!

<p style="font-family: 'Brush Script MT', cursive; text-align: right; font-size: 24px;">- Dan</p>

{% for post in site.tags.networks %}
  <article class="post">
    <div class="post-content-thumbnail">
      {% if post.thumbnail %}
        <img src="{{ post.thumbnail }}" alt="Thumbnail for {{ post.title }}" class="post-thumbnail">
      {% endif %}
      <div class="post-content">
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        <p class="post-meta">
          <i class="fa fa-calendar"></i> <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
        </p>  
        {% if post.excerpt %}
          <p>{{ post.excerpt }}</p>
        {% endif %}
      </div>
    </div>
  </article>
{% endfor %}

<div style="text-align: right;"> <img src="/assets/back_to_home_button.png" alt="custom emoji" width="50px" height="50px"> <a href="/">Return to home page</a> </div>

