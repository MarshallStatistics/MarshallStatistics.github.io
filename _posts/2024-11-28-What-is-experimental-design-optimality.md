---
layout: single
title: "3.0 What is experimental design optimality?"
date: 2024-11-28
thumbnail: "/assets/var_parameter_thumbnail.png"
excerpt: "We shall introduce the concept of optimality in the context of experimental design and discuss its importance."
tags: ['doe']
read_time: true
---
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

The purpose of experimental design is to extract the most information out of your experiment. If you plan ahead, consider which factors are most important, and design an experiment that utilises fewer runs at lower costs, you may end up with a satisfactory experiment. However, how do we know whether our experiment will result in a precise estimation of the cause-and-effect relationship we seek to investigate? In this section, we will discuss approaches that allow us to quantify such precision.

If you recall from our section on regression, we claimed that the variance of an estimator is a measure of its precision. We also established a formula for the variance of the regression coefficients, $$\boldsymbol{\hat{\beta}}$$ using the design matrix, $$\mathbf{F}$$:

$$
\text{Var}(\boldsymbol{\hat{\beta}}) = \sigma^2 \left(\mathbf{F}^T \mathbf{F}\right)^{-1}
$$

Thus, we know that the precision of the regression coefficients (i.e., how good the results of our experiment model the cause-and-effect relationship we wish to investigate) is dependent on the design of the experiment itself. This result motivates much of the theory of experimental design optimisation.

In essence, we wish to minimise the variance as much as possible, since a smaller variance means a more precise estimator. To do this, we often consider maximising $$\mathbf{F}^T \mathbf{F}$$ in some way. Recall, that in the linear model

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

the design matrix is given by

$$
\mathbf{F} = \begin{pmatrix}
1 & x_1 \\
1 & x_2 \\
1 & x_3 \\
\vdots & \vdots \\
1 & x_n
\end{pmatrix}
$$

Thus, we should purposefully choose our values of the independent variable (at which a response should be measured) for $$\mathbf{F}^T \mathbf{F}$$ to be maximised. Fortunately, there are quantifiers to assist us in determining optimal design and what these values of the independent variable should be.

Over the next few posts, we shall discuss some popular measures of optimality:

- A-Optimality seeks to minimise the average variance of the parameter estimates.

- D-Optimality seeks to maximise the determinant of the information matrix, which is equivalent to minimizing the volume of the confidence ellipsoid for the parameter estimates.

- E-Optimality seeks to maximise the minimum eigenvalue of the information matrix.

- T-Optimality seeks to maximise the geometric mean of the eigenvalues of the information matrix.

- G-Optimality seeks to minimise the maximum prediction variance over the design space, which is useful for designs aimed at prediction rather than parameter estimation. We will establish what this means in a future post.


