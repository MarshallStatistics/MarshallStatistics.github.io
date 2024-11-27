---
layout: single
title: "1.3 Determining the Precision of Estimating `β_0` and `β_1` using Fisher Information"
date: 2024-11-27
thumbnail: "/assets/beta_0_beta_1_thumbnail.png"
excerpt: "We shall introduce how we determine how precise our estimators are by using the Fisher Information matrix."
tags: ['doe']
read_time: true
---
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Whenever, we estimate a measurement in real life (e.g., the length of an object) it is normally a good idea to have in mind how precise you think you are with that estimation. In a sense, we are evaluating our own measurement. Therefore, in the context of regression, it makes sense to be able to detrmine how precise our estimators for $$\boldsymbol{\hat{\beta}}$$ are. In this post, we shall establish the framework for which precision of parameter estimation can be determined.  

Recall, our linear model is given by:

$$
\begin{equation}
\mathbf{y} = \mathbf{F} \boldsymbol{\beta} + \boldsymbol{\epsilon}
\end{equation}
$$

where:

$$
\mathbf{y} = \begin{equation}
\begin{pmatrix}
y_1 \\
y_2 \\
y_3 \\
\vdots \\
y_n
\end{pmatrix}, \text{      } \mathbf{F} = \begin{pmatrix}
1 & x_1 \\
1 & x_2 \\
1 & x_3 \\
\vdots & \vdots \\
1 & x_n
\end{pmatrix}\end{equation}, \text{      }\boldsymbol{\beta} = \begin{pmatrix}
\beta_0 \\
\beta_1 \\
\end{pmatrix}, \text{   and   } \boldsymbol{\epsilon} = \begin{pmatrix}
\epsilon_1 \\
\epsilon_2 \\
\epsilon_3 \\
\vdots \\
\epsilon_n
\end{pmatrix}
$$

Previously, we were able to derive a formula for the estimator, $$\boldsymbol{\hat{\beta}}$$, of the vector of parameters, $$\boldsymbol{\beta}}$$:

$$
\boldsymbol{\hat{\beta}} =  \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \mathbf{y}
$$

Now, we shall consider the precision of the estimator, $$\boldsymbol{\hat{\beta}}$$. Intuitively, we may recognise that the variance is a measure of data precision; a random variable with a large variance will likely return data points which are farther away from its mean. As such, let's calculate the variance of $$\boldsymbol{\hat{\beta}}$$.

Before we do this, a little rearranging is required to see what is happening more clearly.

$$
\begin{align}
\boldsymbol{\hat{\beta}} &= \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \mathbf{y} \\ \\
&= \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \left( \mathbf{F} \boldsymbol{\beta} + \boldsymbol{\epsilon} \right) \\ \\
&= \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \mathbf{F} \boldsymbol{\beta} + \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \boldsymbol{\epsilon} \\ \\
&= \boldsymbol{\beta} + \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \boldsymbol{\epsilon}
\end{align}
$$

Now it is in this form, we can compute the variance of $$\boldsymbol{\hat{\beta}}$$:

$$
\begin{align}
\text{Var}(\boldsymbol{\hat{\beta}}) &= \text{Var}\left(\boldsymbol{\beta} + \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \boldsymbol{\epsilon}\right) \\ \\
&= \text{Var}\left(\boldsymbol{\beta}\right) + \text{Var}\left(\left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \boldsymbol{\epsilon}\right) \\ \\
&= \text{Var}\left(\left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \boldsymbol{\epsilon}\right) \\ \\
&= \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \text{Var}\left(\boldsymbol{\epsilon}\right) \mathbf{F} \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \\ \\
&= \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \text{Var}\left(\boldsymbol{\epsilon}\right) \mathbf{F} \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \\ \\
&= \sigma^2 \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \mathbf{F} \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \\ \\
&= \sigma^2 \left(\mathbf{F}^T \mathbf{F}\right)^{-1}
\end{align}
$$

In line 3, we recall that the variance of a constant vector is zero. Moreover, in line 4, we note that if I have a constant matrix, $$\mathbf{A}$$, then $$\text{Var}\left(\mathbf{A}\boldsymbol{\epsilon}\right) = \mathbf{A} \text{Var}\left(\boldsymbol{\epsilon}\right) \mathbf{A}^T$$. From this, we have found a very important measure of precision for our estimator, $$\boldsymbol{\hat{\beta}}$$:

$$
\text{Var}(\boldsymbol{\hat{\beta}}) = \sigma^2 \left(\mathbf{F}^T \mathbf{F}\right)^{-1}
$$

Once we recall that $$\sigma^2$$ is uncorrelated with the coefficients contained in $$\boldsymbol{\hat{\beta}}$$, there are several remarks arising from this result:

- The variance of $$\hat{\beta_j}$$ is proportional to the $$j,j$$-th element of $$\left(\mathbf{F}^T \mathbf{F}\right)^{-1}$$
  
- The covariance of $$\hat{\beta_i}$$ and $$\hat{\beta_j}$$ is proportional to the $$i,j$$-th element of $$\left(\mathbf{F}^T \mathbf{F}\right)^{-1}$$

These remarks extend to larger (but finite-dimensional) collection of regression parameters,  $$\boldsymbol{\hat{\beta}}$$.

Furthermore, the matrix $$\mathbf{F}^T \mathbf{F}$$ is known as the Fisher Information matrix and is extremely important in experimental design; much of the work around optimising experiments requires us to minimise the variance of predictors and as such requires the maximisation of $$\mathbf{F}^T \mathbf{F}$$.

