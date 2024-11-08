---
layout: single
title: "1.2 Incidence matrix"
date: 2024-11-07
thumbnail: "/assets/network_intro_1.png"
excerpt: "An introduction to the basics of networks and graph theory."
tags: ['networks']
read_time: true
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
Networks are used to describe many real-world phenomena such as the interaction within social structures and the mapping of transport links connecting cities. In this post, we shall introduce the fundamental concepts of network theory.

# Incidence matrix

We may wish to consider the connectivity of a graph from the perspective of its edges. This is known as the incidence matrix; a way of capturing how each node is incident (connected) to each edge.

> ### Definition 3: Incidence Matrix
> Given an undirected network (as in Definition 1), the incidence matrix, $$E$$, is defined as an $$N \times K$$ matrix where:
> 
> $$\begin{equation}
>	 	E_{ij} = \begin{cases} 1 \text{ if } \nu_i \in \epsilon_j\\
>	 		0 \text{ if } \nu_i \notin \epsilon_j\
>	 		\end{cases}
>	 \end{equation}$$
> 
> for integers $$i \in \left\{1, \ldots, N \right\}$$ and $$j \in \left\{1, \ldots, K \right\}$$

If we consider the graph in Figure 2, one can create its incidence matrix:

$$E = \begin{pmatrix}
1 & 0 & 0 & 1& 0 & 1& 1 \\
1 & 1 & 1 &  0& 0 & 0 & 0\\
0 & 0 & 1 &  1& 1 & 0 & 0\\
0 & 1 & 0 &  0& 1 & 1 & 0\\
0 &  0& 0 &  0& 0 & 0 & 1\\
\end{pmatrix}$$

To see this a bit more clearly, I have annotated which edge is incident to each node by labelling the columns and rows respectively.

<figure>
  <img src="/assets/network_intro_4.png" alt="An incidence matrix, annotated." title="An incidence matrix, annotated." style="width=50%;">
  <figcaption style="font-size: small;">Figure 4: An incidence matrix, annotated. </figcaption>
</figure>

This is an alternative way to portray the connectivity of the network and becomes very useful if your focus is on the edges between specific units. In transport networks, the edges are often the primary focal points of investigation.
