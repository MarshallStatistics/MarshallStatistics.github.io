---
defaults:
layout: archive
title: "Design of Experiments"
permalink: /design_of_experiments/
scope:
path: ""
type: pages
values:
toc: true
layout: single
author_profile: true
include: _includes/head/custom.html
favicon: "/favicon.ico"
---
I am currently in the process of putting some notes together on experimental design. Please do let me know your thoughts or improvements either via X / Twitter or LinkedIn. I hope these notes are useful!
<p style="font-family: 'Brush Script MT', cursive; text-align: right; font-size: 28px;">- Dan</p>

## &sect;1 An Introduction to Regression

Though not strictly under the guise of experimental design, regression provides a solid introduction to much of the analysis that we conduct in experimental design - particularly when discussing optimal designs. 

I thought that this would be a good place to start, since no experimental design knowledge is required to understand regression.

<div class="posts-list">
  {% assign sorted_posts = site.posts | sort: "title" %}

  <!-- List posts with titles starting with "1." and the "doe" tag -->
  {% for post in sorted_posts %}
    {% if post.title contains "1." and post.tags contains "doe" %}
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
    {% endif %}
  {% endfor %}
</div>

<div style="text-align: right;"> <img src="/assets/back_to_home_button.png" alt="custom emoji" width="50px" height="50px"> <a href="/">Return to home page</a> </div>

## &sect;3 An Introduction to Design Optimality

I am aiming to provide a formal introduction to experimental design in the future (see the currently missing &sect;2). For now, and for the purposes of my studies, I wish to make notes on optimality. I believe this follows on nicely from our discussions of the design matrix in the first section. Much of design optimisation theory relies on minimising the variance of the estimator(s) in some form.

<div class="posts-list">
  {% assign sorted_posts = site.posts | sort: "title" %}

  <!-- List posts with titles starting with "3." and the "doe" tag -->
  {% for post in sorted_posts %}
    {% if post.title contains "3." and post.tags contains "doe" %}
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
    {% endif %}
  {% endfor %}
</div>

<div style="text-align: right;"> <img src="/assets/back_to_home_button.png" alt="custom emoji" width="50px" height="50px"> <a href="/">Return to home page</a> </div>
