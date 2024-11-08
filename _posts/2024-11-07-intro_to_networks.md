---
layout: single
title: "Introduction to Undirected Networks"
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

# Nodes and edges

In the same way that we can portray a function with a plot, we can model a network with a graph. A graph is made up of nodes connected by edges. The following example will motivate understanding here. 

We can create a graph of the network between you and a friend; there are two nodes (you and your friend) connected by an edge (a straight line representing your friendship):

<figure>
  <img src="/assets/network_intro_1.png" alt="A simple graph of the network between you and a friend." title="A simple graph of the network between you and a friend." style="width=50%;">
  <figcaption style="font-size: small;">Figure 1: A simple graph of the network between you and a friend. </figcaption>
</figure>

It is customary to call nodes $$\nu$$ with a subscript to differentiate between each node. You can see here that 'you' are labelled $$\nu_1$$ and 'your friend' is represented as $$\nu_2$$. The edge connecting them is denoted by $$\epsilon_1$$, following the same subscript rules as our nodes.

A graph can consist of more than one node, you may wish to construct a network between you, your friend group, and an acquaintance of yours.

<figure>
  <img src="/assets/network_intro_2.png" alt="A simple graph of the network between you, your friend group, and an acquaintance of yours." title="A simple graph of the network between you, your friend group, and an acquaintance of yours." style="width=50%;">
  <figcaption style="font-size: small;">Figure 2: A simple graph of the network between you, your friend group, and an acquaintance of yours. </figcaption>
</figure>

Now we have this intuition, let's define a simple, undirected graph.

> ### Definition 1: Undirected Graph
> An undirected network is a set of nodes, $$\nu = \{\nu_1, \nu_2, \ldots, \nu_N\}$$, and a set of edges, $$\epsilon = \{\epsilon_1, \epsilon_2, \ldots, \epsilon_K\}$$, for $$K, N \in \mathbb{N}$$ such that each edge in $$\epsilon$$ connects an element in $$\nu$$ to another (not necessarily distinct) element of $$\nu$$.

This definition implies there is a directed graph. In fact, our edges can be directed in a single direction. 

However, for the rest of this post, we will consider undirected graphs. I may create a future post on directed graphs at a later date.

It is almost always important to consider the connectivity of nodes. This is where the real *magic* of networks reveals itself. Fortunately, there is a super legible way to convey the interconnectivity of nodes - this is known as the adjacency matrix.

# Adjacency matrix

The adjacency matrix tells us what nodes are connected to each node in a legible format.

> ### Definition 2: Adjacency Matrix
> Given an undirected network (as in Definition 1), the adjacency matrix, $$A$$, is defined as a symmetric $$N \times N$$ matrix where:
> 
> $$
> \begin{equation}
>     A_{ij} = \begin{cases}
>     1 & \text{if } (i, j) \in \epsilon \\
>     0 & \text{if } (i, j) \notin \epsilon
>     \end{cases}
> \end{equation}
> $$


If we consider the graph in Figure 2, one can create its adjacency matrix:

$$A = \begin{pmatrix}
0 & 1 & 1 & 1 & 1 \\
1 & 0 & 1 & 1 & 0 \\
1 & 1 & 0 & 1 & 0 \\
1 & 1 & 1 & 0  & 0 \\
1 & 0 & 0 & 0 & 0 \\
\end{pmatrix}$$

To see this a bit more clearly, I have annotated which node is connected to each node by labelling the rows and columns respectively.

<figure>
  <img src="/assets/network_intro_3.png" alt="An adjacency matrix, annotated." title="An adjacency matrix, annotated." style="width=50%;">
  <figcaption style="font-size: small;">Figure 3: An adjacency matrix, annotated. </figcaption>
</figure>

As you can see, in congruence with Figure 2, everybody knows everybody in your friend group, and your acquaintance is only known by you. The adjacency matrix allows us to represent the connectivity of a given network without having to draw the graph. It is easy to imagine that drawing a graph with a large number of nodes and/or edges can become quite a headache.
 
# Incidence matrix

We may wish to consider the connectivity of a graph from the perspective of its edges. This is known as the incidence matrix; a way of capturing how each node is incident (connected) to each edge.

> ### Definition 3: Incidence Matrix
> Given an undirected network (as in Definition 1), the incidence matrix, $$E$$, is defined as an $$N \times K$$ matrix where:
> 
> $$\begin{equation}
>	 	E_{ij} = \begin{cases} 1 \text{ if node } \nu_i \text{ is incident to edge } \epsilon_j\\
>	 		0 \text{ otherwise }
>	 		\end{cases}
>	 \end{equation}$$

If we consider the graph in Figure 2, one can create its incidence matrix:

$$$$

To see this a bit more clearly, I have annotated which edge is incident to each node by labelling the columns and rows respectively.

**annotated incidence matrix here**

This is an alternative way to portray the connectivity of the network and becomes very useful if your focus is on the edges between specific units. In transport networks, the edges are often the primary focal points of investigation.
