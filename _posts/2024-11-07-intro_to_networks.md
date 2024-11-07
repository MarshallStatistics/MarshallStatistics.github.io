---
layout: single
title: "Introduction to Networks"
date: 2024-11-07
thumbnail: "/assets/network_intro_2.png"
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

# Nodes and edges

In the same way that we can portray a function with a plot, we can model a network with a graph. A graph is made up of nodes connected by edges. The following example will motivate understanding here. 

We can create a graph of the network between you and a friend; there are two nodes (you and your friend) connected by an edge (a straight line representing your friendship):

<figure>
  <img src="/assets/network_intro_1.png" alt="A simple graph of the network between you and a friend." title="A simple graph of the network between you and a friend." style="width=50%;">
  <figcaption style="font-size: small;">"Figure 1: A simple graph of the network between you and a friend. </figcaption>
</figure>

It is customary to call nodes $$\nu$$ with a subscript to differentiate between each node. You can see here that 'you' are labelled $$\nu_1$$ and 'your friend' is represented as $$\nu_2$$. The edge connecting them is denoted by $$\epsilon$$, following the same subscript rules as our nodes.

A graph can consist of more than one node, you may wish to construct a network between you, your friend group, and an acquaintance of yours.

<figure>
  <img src="/assets/network_intro_2.png" alt="A simple graph of the network between you, your friend group, and an acquaintance of yours." title="A simple graph of the network between you, your friend group, and an acquaintance of yours." style="width=50%;">
  <figcaption style="font-size: small;">"Figure 2: A simple graph of the network between you, your friend group, and an acquaintance of yours. </figcaption>
</figure>

It is almost always important to consider the connectivity of nodes. This is where the real *magic* of networks reveals itself. Fortunately, there is a super legible way to convey the interconnectivity of nodes - this is known as the adjacency matrix.

# Adjacency matrix

	\begin{definition} (Adjacency Matrix)
		\label{adj-matrix}
	 Given an undirected network (as in Definition \ref{def-network}), the adjacency matrix, $A$, is defined as a symmetric $N \times N$ matrix where:
	 \begin{equation*}
	 	A_{ij} = \begin{cases*} 1 \text{ if } (i, j) \in \mathcal{E} \\
	 		0 \text{ if } (i, j) \notin \mathcal{E}
	 		\end{cases*}
	 \end{equation*}
	\end{definition}
 
# Incidence matrix

