---
layout: single
title: "1.4 Node degree distribution"
date: 2024-11-07
thumbnail: "/assets/network_intro_1.png"
excerpt: "The probability distribution of choosing a node with degree $$k$$"
tags: ['networks']
read_time: true
---
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


When looking at the global properties of networks, we often like to determine the node degree of each node within our network. It is then convenient for us to determine the probability distribution of node degrees (i.e., the probability of choosing a node with degree $$k$$ out of all possible nodes $$N$$). Please see a formal definition of this distribution below:

> ### Definition 2: Node Degree Distribution
> Given an undirected network, $$G = \left\{ \nu, \epsilon \right\}$$, with $$N$$ nodes (as in Definition 1), the node degree distribution is a probability distribution, $$P(k)$$, such that:
> 
> $$\begin{equation}
> P(k) = \frac{n_k}{N}
>	 \end{equation}$$
>
> where $$n_k$$ is the number of nodes in the network with degree $$k$$.

By counting the number of nodes with degree $$k$$ and dividing by the total number of nodes, we are able to generate a discrete probability distribution for the node degree. Please see the node degree distribution for the network portrayed in Figure 1 below:

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
