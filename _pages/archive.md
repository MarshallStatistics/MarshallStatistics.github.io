---
defaults:
layout: archive
title: "All posts"
permalink: /archive/
scope:
path: ""
type: pages
values:
search: false
layout: archive
author_profile: true
include: _includes/head/custom.html
favicon: "/favicon.ico"
---
Admittedly, this is a bit messy. I am aiming to fix this once I establish sensible grouping of posts within the site. Thanks for your patience!
<p style="font-family: 'Brush Script MT', cursive; text-align: right; font-size: 28px;">- Dan</p>

{% for post in site.posts %}
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
