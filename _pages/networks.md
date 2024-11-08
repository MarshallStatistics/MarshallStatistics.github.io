---
defaults:
layout: archive
title: "Notes on networks"
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
I am currently in the process of putting some notes together on networks and graph theory. Please do let me know your thoughts or improvements either via X / Twitter or LinkedIn. I hope these notes are useful!
<p style="font-family: 'Brush Script MT', cursive; text-align: right; font-size: 28px;">- Dan</p>

## An introduction to (undirected) networks

Networks are used to describe many real-world phenomena such as the interaction within social structures and the mapping of transport links connecting cities. Throughout this section, we shall introduce the fundamental concepts of network theory.

For the purposes of this section, we shall solely discuss undirected networks. You need not know what undirected means at this stage.

{% for post in site.tags.networks %}
  <article class="post">
    <div class="post-content-thumbnail">
      {% if post.thumbnail %}
        <img src="{{ post.thumbnail }}" alt="Thumbnail for {{ post.title }}" class="post-thumbnail">
      {% endif %}
      <div class="post-content">
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        {% if post.excerpt %}
          <p>{{ post.excerpt }}</p>
        {% endif %}
      </div>
    </div>
  </article>
{% endfor %}

<div style="text-align: right;"> <img src="/assets/back_to_home_button.png" alt="custom emoji" width="50px" height="50px"> <a href="/">Return to home page</a> </div>

