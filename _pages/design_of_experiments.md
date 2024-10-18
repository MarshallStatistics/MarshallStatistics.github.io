---
defaults:
layout: archive
title: "Design of Experiments"
permalink: /design_of_experiments/
scope:
path: ""
type: pages
values:
layout: single
author_profile: true
include: _includes/head/custom.html
favicon: "/favicon.ico"
---
This is my weekly PhD diary, where I informally discuss what I have learned both technically and personally.
{% for post in site.tags.doe %}
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
