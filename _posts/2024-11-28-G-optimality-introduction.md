---
layout: single
title: "3.5 `G`-Optimality Introduction"
date: 2024-11-28
thumbnail: "/assets/var_parameter_thumbnail.png"
excerpt: "Exploring `G`-optimality and how it governs a solid experiment."
tags: ['doe']
read_time: true
---
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Before we consider $$G$$-optimality, we need to discuss prediction variance. This is the variance of $$\mathbf{\hat{y}}$$:

$$
\mathbf{\hat{y}} = \boldsymbol{\hat{\beta}}^T \mathbf{f(x)} 
$$

where:
- $$\mathbf{f(x)} = \begin{pmatrix}1 \\ x \\ x^2 \\ \vdots \\ x^n\end{pmatrix} $$
- $$n$$ is the $$n$$-th order of the regression model (i.e., if we are working with linear regression, our vector on the right-hand side would only contain the first two elements).

Now, to calculate Var($$\mathbf{\hat{y}}$$), we recall the linearity of the variance to obtain:

$$
\begin{align}
\text{Var}\left(\mathbf{\hat{y}}\right) &= \text{Var}\left(\boldsymbol{\hat{\beta}}^T \mathbf{f(x)} \right) \\ \\
&= \mathbf{f(x)}^T \text{Var}\left(\boldsymbol{\hat{\beta}}^T \right) \mathbf{f(x)} \mathbf{f(x)} \\ \\
&= \mathbf{f(x)}^T \sigma^2 \left( \mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{f(x)} \\ \\
&= \sigma^2 \mathbf{f(x)}^T \left( \mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{f(x)} \\ \\
\end{align}
$$

Thus, we have obtained the prediction variance (i.e., the variance of \mathbf{\hat{y}}). In fact, we often choose to work with the standardised variance which has been scaled with the number of trials and with the variance of the error, $$\sigma^2$$:

> ### Definition 1: Standardised variance
> The standardised variance, $$d(x, \epsilon)$$ of a predictor $$\mathbf{\hat{y}}$$, for $$N$$ data points is given by:
>
> $$
> d(x, \epsilon) = N \mathbf{f(x)}^T \left( \mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{f(x)}
> $$
>
> As mentioned above, this is the predictor variance which has been scaled for the number of trials, $$n$$, and the variance of the error, $$\sigma^2$$.

Now we may introduce the fifth measure of optimality, $$G$$-optimality. This is where we seek to minimise the maximum of the standardised variance, $$d(x, \epsilon)$$, over the design space.

Let's take a look at an example to illustrate this idea. Consider the following design matrix:

$$
\mathbf{F} = \begin{pmatrix} 1 & -0.5 \\ 1 & 0 \\ 1 & 0.5\end{pmatrix}
$$

Then, we can compute the standardised variance as follows:

$$
\begin{align}
d(x, \epsilon) & = N \mathbf{f(x)}^T \left( \mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{f(x)} \\ \\
&= 3 \mathbf{f(x)}^T \left( \begin{pmatrix} 1 & 1 & 1 \\ -0.5 & 0 & 0.5 \end{pmatrix} \begin{pmatrix} 1 & -0.5 \\ 1 & 0 \\ 1 & 0.5 \end{pmatrix}\right)^{-1} \mathbf{f(x)} \\ \\ 
&= 3 \mathbf{f(x)}^T \left( \begin{pmatrix} 3 & 0 \\ 0 & 0.5 \end{pmatrix}\right)^{-1} \mathbf{f(x)} \\ \\ 
&= 3 \mathbf{f(x)}^T \begin{pmatrix} \frac{1}{3} & 0 \\ 0 & 2 \end{pmatrix} \mathbf{f(x)} \\ \\ 
&= 3 \begin{pmatrix} 1 & x \end{pmatrix} \begin{pmatrix} \frac{1}{3} & 0 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ x \end{pmatrix} \\ \\ 
&= 3 \left( \frac{1}{3} + 2x^2 \right) \\ \\
&= 3 \left( \frac{1}{3} + 2x^2 \right) \\ \\
&= 1 + 6x^2
\end{align}
$$

This $$d(x, \epsilon)$$ has a maximum over the design region $$x \in [-0.5, 0.5]$$ at $$x=0.5$$ or $$x=0.5$$ is $$2.5$$.

$$G$$-optimality requires us to choose a sensible design over the design space to minimise this maximum, as this would help to minimise prediction variance. 
