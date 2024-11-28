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

In essence, we wish to minimise the variance as much as possible, since a smaller variance means a more precise estimator. To do this, we often consider maximising $$\left(\mathbf{F}^T \mathbf{F}\right)$$ in some way. Recall, that in the linear model


the design matrix is given by


Thus, we should purposefully choose our values of the independent variable (at which a response should be measured) for $$\left(\mathbf{F}^T \mathbf{F}\right)$$ to be maximised.

Over the next few posts, we shall discuss three popular measures of optimality:

- D-optimality
- V-optimality
- G-optimality
