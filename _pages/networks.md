---
defaults:
layout: archive
title: "Notes on Networks"
permalink: /networks/
scope:
path: ""
toc: true
type: pages
values:
layout: single
author_profile: true
include: _includes/head/custom.html
favicon: "/favicon.ico"
search: false
---

I am currently in the process of putting some notes together on networks and graph theory. Please do let me know your thoughts or improvements either via X / Twitter or LinkedIn. I hope these notes are useful!
<p style="font-family: 'Brush Script MT', cursive; text-align: right; font-size: 28px;">- Dan</p>

## &sect;1 An introduction to (undirected) networks

Networks are used to describe many real-world phenomena such as the interaction within social structures and the mapping of transport links connecting cities. Throughout this section, we shall introduce the fundamental concepts of network theory.

For the purposes of this section, we shall solely discuss undirected networks. You do not need to know what undirected means at this stage.

<div class="posts-list">
  {% assign filtered_posts = site.posts | where: "title", "1." %}
  {% assign sorted_posts = site.posts | sort: "title" %}

  <!-- List posts with titles starting with "1." -->
  {% for post in filtered_posts %}
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

  <!-- List remaining posts -->
  {% for post in sorted_posts %}
    {% unless post.title starts with "1." %}
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
    {% endunless %}
  {% endfor %}
</div>




<div style="text-align: right;"> <img src="/assets/back_to_home_button.png" alt="custom emoji" width="50px" height="50px"> <a href="/">Return to home page</a> </div>

