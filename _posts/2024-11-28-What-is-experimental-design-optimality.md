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

The purpose of experimental design is to extract the most information out of your experiment. If you plan ahead, consider which factors are most important, and design an experiment that utilises fewer runs at lower costs, you may end up with a satisfactory experient. However, how do we know whether our experiment will result in a precise estimation of the cause-and-effect relationship we seek to investigate? In this section, we will discuss approaches that allow us to quantify such precision.

If you recall from our section on regression, we claimed that the variance of an estimator is a measure of its precision. We also established a formula for the variance of the regressions coefficients' precision using the design matrix:

