---
layout: single
title: "1.1 Estimating $\beta_0$ and $\beta_1$ using least squares estimation"
date: 2024-11-26
thumbnail: "/assets/scatter_graph_annotated.png"
excerpt: "We shall introduce least squares regression as a means to estimate $\beta_0$ and $\beta_1$."
tags: ['doe']
read_time: true
---
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Estimation forms the cornerstone of linear regression; we are interested in approximating our parameters for our linear model defined in the previous post. Here, it is timely to introduce the concept of statistical inference: we are characterising the population data by using sample data.

Recall, our linear model (from the previous post) is given by:

$$
\begin{equation}
y_i = \beta_0 + \beta_1 x_i + \epsilon_i
\end{equation}
$$

where $$\beta_0, \beta_1 \in \mathbb{R}$$ are coefficients indicating the intercept and gradient of our straight line respectively. We also have an error term $$\epsilon_i \sim \mathcal{N}(0, \sigma^2)$$ which accounts for the dispersion of the observed values about the straight line.

We were also able to represent it using matrices:

