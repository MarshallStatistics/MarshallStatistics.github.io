---
layout: single
title: "Randomly Walking in Python, Stylishly"
date: 2024-09-23
thumbnail: "/assets/rw_sim.png"
excerpt: "A quick guide on plotting random walks in Python and how to make your plots nice in Matplotlib for beginners."
read_time: true
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
.definition {
    border: 1px solid #000;
    padding: 10px;
    margin: 10px 0;
}
</style>

<figure>
  <img src="/assets/rw_sim.png" alt="A symmetric random walk running for fifty steps." title="A symmetric random walk running for fifty steps." style="width=100%;">
  <figcaption style="font-size: small;">Source: Marshall, using Python </figcaption>
</figure>

When learning about stochastic processes, we are often first introduced to the simple, symmetric random walk. In this post, I show how one can produce a plot of a random walk in Python and the various methods you can implement to make it look a little nicer.

Firstly, please see below the mathematical definition of a simple, symmetric random walk:

<div class="definition">
Let $\left\{X_i\right\} \sim \text{Be}(0.5)$ for $i \in \mathbb{N}$ be a set of independent and identically distributed (i.i.d.) random variables, each taking either the value 1 or -1.
Then, a simple symmetric random walk, $S_n$, of $n \in \mathbb{N}$ steps, is an iterative process given by
$$S_{n+1} = S_n + X_n$$
where $S_0=0$ denotes the initial starting point.
</div>

Rather handwavingly, one may think of a simple symmetric random walk as a walker stepping forward by one metre or backwards by one metre with equal probability for each step of their walk. Flip a coin: heads is forwards, tails is backwards. After $$n$$ flips, your distance from where you started is given by $$S_n$$.

One may of course generalise this by changing the step size from one metre and by changing the probability of stepping forward each step to be a value other than one-half. However, this is outside the scope of this post. We will instead focus on how to plot a simple symmetric random walk in Python. 

Let's start with the basics; we shall first implement our above definition in Python:



<figure>
  <img src="/assets/LV_GIF1.gif" alt="A stable predator-prey system described by the Lotka-Volterra equations." title="A stable predator-prey system described by the Lotka-Volterra equations over time.">
  <figcaption style="font-size: small;"> Figure 1: A stable predator-prey system described by the Lotka-Volterra equations. Source: Self-produced using Python. </figcaption>
</figure>


## **References**
* P. R´ev´esz. Random walk in random and non-random environments. World Scientific, 2013.

