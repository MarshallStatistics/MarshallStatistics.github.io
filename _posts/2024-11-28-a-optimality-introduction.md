---
layout: single
title: "3.2 `A`-Optimality Introduction"
date: 2024-11-28
thumbnail: "/assets/var_parameter_thumbnail.png"
excerpt: "Exploring `A`-optimality and how it asserts a solid experiment."
tags: ['doe']
read_time: true
---
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

The second measure of optimality we shall consider is $$A$$-optimality. This is where we seek to minimise the average variance of our estimators.

If you recall from our section on regression, we claimed that the variance of an estimator is a measure of its precision. We also established a formula for the variance of the regression coefficients, $$\boldsymbol{\hat{\beta}}$$ using the design matrix, $$\mathbf{F}$$:

$$
\text{Var}(\boldsymbol{\hat{\beta}}) = \sigma^2 \left(\mathbf{F}^T \mathbf{F}\right)^{-1}
$$

where the design matrix is given by

$$
\mathbf{F} = \begin{pmatrix}
1 & x_1 \\
1 & x_2 \\
1 & x_3 \\
\vdots & \vdots \\
1 & x_n
\end{pmatrix}
$$

Therefore, our Fisher information matrix becomes:

$$
\begin{align}
\mathbf{I} &= \mathbf{F}^T \mathbf{F} \\ \\
& = \begin{pmatrix}
1 & 1 & 1 & \ldots & 1\\
x_1 & x_2 & x_3 & \ldots & x_n
\end{pmatrix} \begin{pmatrix}
1 & x_1 \\
1 & x_2 \\
1 & x_3 \\
\vdots & \vdots \\
1 & x_n
\end{pmatrix} \\ \\
&=  \begin{pmatrix}
n & \sum_{i=1}^{n} x_i \\
\sum_{i=1}^{n} x_i & \sum_{i=1}^{n} x_i^2
\end{pmatrix}
\end{align}
$$

We should also recall that the $$j$$-th diagonal element of the inverse Fisher information matrix is proportional to the variance of the $$j$$-th estimator, $$\hat{\beta_j}$$. Therefore, in order to find the average variance of our estimators we should compute the trace of the inverse information matrix.

To show this let's compute the inverse Fisher information matrix:

$$
\begin{align}
\mathbf{I}^{-1} &= \frac{1}{n \sum_{i=1}^{n} x_i^2 - \left( \sum_{i=1}^{n} x_i \right)^2} 
\begin{pmatrix} \sum_{i=1}^{n} x_i^2 & -\sum_{i=1}^{n} x_i \\ -\sum_{i=1}^{n} x_i & n \end{pmatrix}
\end{align} 
$$

Now, compute its trace (recall that the trace of a matrix is just the sum of its diagonal elements):

$$
\text{Trace}(\mathbf{I}^{-1}) = \frac{\sum_{i=1}^{n} x_i^2 + n}{n \sum_{i=1}^{n} x_i^2 - \left( \sum_{i=1}^{n} x_i \right)^2}
$$

This is the definition of $$A$$-optimality; the precision of the estimators very much depends on your choice of design points, $$\left\{x_i\right\}$$, and the number of design points in your experiment, $$n$$.
