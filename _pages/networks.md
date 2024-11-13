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

For the purposes of this section, we shall solely discuss undirected networks. You do not need to know what undirected means at this stage.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sorted Posts</title>
</head>
<body>
    <ul>
        {% assign posts_with_numeric_title = site.tags.networks | map: 'post' %}

        {% for post in posts_with_numeric_title %}
          {% assign numeric_title_parts = post.title | remove: " " | split: "." %}
          {% assign numeric_title = numeric_title_parts[0] | plus: 0 %}
          {% if numeric_title_parts.size > 1 %}
            {% assign numeric_title = numeric_title | append: "." | append: numeric_title_parts[1] %}
          {% endif %}
          {% assign post.numeric_title = numeric_title %}
        {% endfor %}

        {% assign sorted_posts = posts_with_numeric_title | sort: 'numeric_title' %}

        {% for post in sorted_posts %}
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
    </ul>
</body>
</html>


<div style="text-align: right;"> <img src="/assets/back_to_home_button.png" alt="custom emoji" width="50px" height="50px"> <a href="/">Return to home page</a> </div>

