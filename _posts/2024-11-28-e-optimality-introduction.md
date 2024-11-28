---
layout: single
title: "3.2 `E`-Optimality Introduction"
date: 2024-11-28
thumbnail: "/assets/var_parameter_thumbnail.png"
excerpt: "Exploring `E`-optimality and how it asserts a solid experiment."
tags: ['doe']
read_time: true
---
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

The third measure of optimality we shall consider is $$E$$-optimality. This is where we seek to maximise the smallest eigenvalue of the information matrix. Recall that $$D$$-optimality focussed on maxmising the entire dterminant of the information matix, $$E$$-optimality is a more sepcific way of focussing on optimality where we ensure that the least rpecise estimator is as accurate as possible.

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

Now, let us compute the eigenvalues of this matrix. We first start by forming the characteristic polynomial (i.e., $$\text{det}\left[\mathbf{I} - \lambda\mathbb{1}\right]=0$$):

$$
\text{det}\left[\mathbf{I} - \lambda\mathbb{1}\right] = \begin{vmatrix} n - \lambda & \sum_{i=1}^{n} x_i \\ \sum_{i=1}^{n} x_i & \sum_{i=1}^{n} x_i^2 - \lambda \end{vmatrix} =^! 0
$$

Now, let's solve this equation for lambda:

$$
\begin{align}
0 &= (n - \lambda)\left(\sum_{i=1}^{n} x_i^2 - \lambda\right) - \left(\sum_{i=1}^{n} x_i\right)^2 \\ \\
&= \lambda^2 - \lambda \left(n + \sum_{i=1}^{n} x_i^2 \right) + n \sum_{i=1}^{n} x_i^2 - \left(\sum_{i=1}^{n} x_i\right)^2 \\ \\
\end{align}
$$

Notice that this is a quadratic equation. As such, we can use the quadratic formula to evaluate:

$$
\lambda_{\pm} = \frac{\left(n + \sum_{i=1}^{n} x_i^2\right) \pm \sqrt{(n + \sum_{i=1}^{n} x_i^2)^2 - 4\left(n \sum_{i=1}^{n} x_i^2 - \left(\sum_{i=1}^{n} x_i\right)^2\right)}}{2}
$$

Therefore, in the case of the linear model, we have two eigenvalues:

$$
\begin{align}
\lambda_{+} &= \frac{\left(n + \sum_{i=1}^{n} x_i^2\right) + \sqrt{(n + \sum_{i=1}^{n} x_i^2)^2 - 4\left(n \sum_{i=1}^{n} x_i^2 - \left(\sum_{i=1}^{n} x_i\right)^2\right)}}{2} \\ \\
\lambda_{-} &= \frac{\left(n + \sum_{i=1}^{n} x_i^2\right) - \sqrt{(n + \sum_{i=1}^{n} x_i^2)^2 - 4\left(n \sum_{i=1}^{n} x_i^2 - \left(\sum_{i=1}^{n} x_i\right)^2\right)}}{2}
\end{align}
$$

$$E$$-optimality seeks to maximise the smaller value of either $$\lambda_+$$ or $$\lambda_-$$; the precision of the estimators very much depends on your choice of design points, $$\left\{x_i\right\}$$, and the number of design points in your experiment, $$n$$.
