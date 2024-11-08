---
layout: single
title: "1.3 Node degree"
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

# Node degree

Another important measure of connectivity is the node degree of a given node within a network. A formal definition of the node degree can be found below.

> ### Definition 4: Node Degree
> Given an undirected network, $$G = \left\{ \nu, \epsilon \right\}$$, with $N$ nodes (as in Definition 1), the node degree of a given node $$\nu_i$$ can be defined by the adjacency matrix:
> 
> $$\begin{equation}
> \text{deg}(\nu_i) = \sum_{j = 1}^{N} A_{ij}
>	 \end{equation}$$
> 
> for integer $$i \in \left\{1, \ldots, N \right\}$$

One can think of the node degree as the number of connections that the node in question has. This can be a useful quantifier of a person's popularity or a measure of how accessible an area is by transport links.

In the network portrayed in Figure 2, we can count the node degree by either using the adjacency matrix or by counting how many edges are attached to each node. Check that you can do this by confirming my results below with the graph in Figure 2:

$$\begin{align}\text{deg}(\nu_1) &= A_{11} + A_{12} + A_{13} + A_{14} + A_{15} \\
&= 0 + 1 + 1 + 1 + 1 \\
&= 4 \end{align}$$

$$\begin{align}\text{deg}(\nu_2) &= A_{21} + A_{22} + A_{23} + A_{24} + A_{25} \\
&= 1 + 0 + 1 + 1 + 0 \\
&= 3 \end{align}$$

$$\begin{align}\text{deg}(\nu_3) &= A_{31} + A_{32} + A_{33} + A_{34} + A_{35} \\
&= 1 + 1 + 0 + 1 + 0 \\
&= 3 \end{align}$$

$$\begin{align}\text{deg}(\nu_4) &= A_{41} + A_{42} + A_{43} + A_{44} + A_{45} \\
&= 1 + 1 + 1 + 0 + 0 \\
&= 3 \end{align}$$

$$\begin{align}\text{deg}(\nu_5) &= A_{51} + A_{52} + A_{53} + A_{54} + A_{55} \\
&= 1 + 0 + 0 + 0 + 0 \\
&= 1 \end{align}$$

This tells us that node $$\nu_1$$ has the highest node degree and is therefore the most connected node in this network. In the next section, we will discuss what we can do with this information to infer global properties of the network. 

## Node degree distribution

When looking at the global properties of networks, we often like to determine the node degree of each node within our network. It is then convenient for us to determine the probability distribution of node degrees (i.e., the probability of choosing a node with degree $$k$$ out of all possible nodes $$N$$). Please see a formal definition of this distribution below:

> ### Definition 5: Node Degree Distribution
> Given an undirected network, $$G = \left\{ \nu, \epsilon \right\}$$, with $$N$$ nodes (as in Definition 1), the node degree distribution is a probability distribution, $$P(k)$$, such that:
> 
> $$\begin{equation}
> P(k) = \frac{n_k}{N}
>	 \end{equation}$$
>
> where $$n_k$$ is the number of nodes in the network with degree $$k$$.

By counting the number of nodes with degree $$k$$ and dividing by the total number of nodes, we are able to generate a discrete probability distribution for the node degree. Please see the node degree distribution for the network portrayed in Figure 2 below:

$$
 \begin{equation}
     P(k) = \begin{cases}
     \frac{1}{5} & \text{if } k = 1 \\
     \frac{3}{5} & \text{if } k = 3 \\
     \frac{1}{5} & \text{if } k = 4 \\
     0 & \text{ otherwise }
     \end{cases}
 \end{equation}
 $$

It is customary to exclude the values of degree value $$k$$ in the degree distribution for which there are no nodes present. Notice in our previous calculations that there was one node with degree one, three nodes with degree three, and one node with degree four. The node degree distribution is a probability distribution that encompasses the proportion of node degrees seen throughout the network.
