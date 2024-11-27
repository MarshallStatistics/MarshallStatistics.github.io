---
layout: single
title: "1.2 Introduction to quadratic regression"
date: 2024-11-26
thumbnail: "/assets/scatter_quad_reg_annotated.png"
excerpt: "Extending our understanding of linear regression to the quadratic case."
tags: ['doe']
read_time: true
---
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Recall, linear regression allows us to model the interactivity of independent variables and dependent variables using a straight line. However, if our data does not follow a linear relationship, we should probably consider modelling the relationship using a quadratic model. This is a simple extension of the linear model; we just add an extra term! See below: 

$$
\begin{equation}
y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \epsilon_i
\end{equation}
$$

where $$\beta_0, \beta_1, \beta_2 \in \mathbb{R}$$ are coefficients illustrating the shape of our quadratic model. As with the linear case, we also have an error term $$\epsilon_i \sim \mathcal{N}(0, \sigma^2)$$ which accounts for the dispersion of the observed values about the straight line.

As before, we are also able to represent it using matrices:

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
1 & x_1 & x_1^2 \\
1 & x_2 & x_2^2 \\
1 & x_3 & x_3^2 \\
\vdots & \vdots & \vdots\\
1 & x_n & x_n^2 \\
\end{pmatrix}\end{equation}, \text{      }\boldsymbol{\beta} = \begin{pmatrix}
\beta_0 \\
\beta_1 \\
\beta_2 \\
\end{pmatrix}, \text{   and   } \boldsymbol{\epsilon} = \begin{pmatrix}
\epsilon_1 \\
\epsilon_2 \\
\epsilon_3 \\
\vdots \\
\epsilon_n
\end{pmatrix}
$$

Quadratic regression is used when a scatter graph of the data shows a nonlinear relationship that can be well-approximated by a parabolic curve. In order to illustrate this concept, please see the following example:

> ### Example 1: Non-linear relationships
> I wish to see how increasing the amount of fertiliser alters the yield I get from my crops. It's known that small amounts of fertilizer can improve yield significantly, but after a certain point, adding more fertiliser doesn't help much and might even decrease the yield due to over-fertilisation. To test this, I have collected the following data:
> 
>$$
>\begin{align}
>&x = \left\{0, 1, 2, 3, 4\right\} \ \leftarrow \texttt{Amount of fertiliser (kilograms)} \\
>&y = \left\{2, 4, 7, 8, 6\right\} \ \leftarrow \texttt{Yield (tonnes)}
>\end{align}
>$$
>
> Just like we did with the linear example, I have plotted this as a scatter graph below:
>
> <figure>
>  <img src="/assets/scatter_quad_reg.png" alt="A scatter plot showing the relationship between amount of fertiliser and >crop yield" title="A scatter plot showing the relationship between amount of fertiliser and crop yield"> <figcaption style="font-size: small;">Figure 1: A scatter plot showing the relationship between amount of fertiliser and crop yield. </figcaption>
></figure>
> Notice that we have a non-linear relationship that looks quadratic. In the next section, we shall develop the theory of least squares estimation for the quadratic case.


Fortunately, the least squares estimation theory which we discussed in our previous post (about the linear case) holds true in the quadratic case. We just need to remember that the design matrix has an extra column!

Using the least squares theory discussed in the previous post, we shall now seek to find the "best" value for $$\boldsymbol{\beta}$$ which best models this (presumably) quadratic relationship.

> ### Example 1 (continued): Least squares estimation for quadratic regression
> Let us refer back to our previous example in this post. Recall, our data collected was as follows:
> 
>$$
> \begin{equation}
> \mathbf{x} =
\begin{pmatrix}
0 \\
1 \\
2 \\
3 \\
4
\end{pmatrix}, \qquad
> \mathbf{y} =
\begin{pmatrix}
2 \\
4 \\
7 \\
8 \\
6
\end{pmatrix}
> \end{equation}
> $$
>
> We can plug this into our linear model:
>
> $$
\begin{equation}
\begin{pmatrix}
3 \\
5 \\
8 \\
9 \\
10
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0^2 \\
1 & 1 & 1^2\\
1 & 2 & 2^2 \\
1 & 3 & 3^2 \\
1 & 4 & 4^2
\end{pmatrix} \begin{pmatrix}
\beta_0 \\
\beta_1 \\
\beta_2
\end{pmatrix}
+
\begin{pmatrix}
\epsilon_1 \\
\epsilon_2 \\
\epsilon_3 \\
\vdots \\
\epsilon_n
\end{pmatrix}
> \end{equation}
$$
> 
> Now, the parameters for the line of best fit which minimise the squared errors can be found by the following formula:
>
> $$
> \begin{align}
> \boldsymbol{\hat{\beta}} &= \left(\mathbf{F}^T \mathbf{F}\right)^{-1} \mathbf{F}^T \mathbf{y} \\
> &= \left[ \begin{pmatrix} 1 & 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 & 4 \\ 0 & 1 & 4 & 9 & 16 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1\\ 1 & 2 & 4 \\ 1 & 3 & 9 \\ 1 & 4 & 16 \end{pmatrix}\right]^{-1} \begin{pmatrix} 1 & 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 & 4 \\ 0 & 1 & 4 & 9 & 16 \end{pmatrix} \begin{pmatrix} 2 \\ 4 \\ 7 \\ 8 \\ 6 \end{pmatrix} \\ & = \left[\begin{pmatrix}
5 & 10 & 30 \\
10 & 30 & 100 \\
30 & 100 & 354
\end{pmatrix}
\right]^{-1}\begin{pmatrix}
27 \\
66 \\
200
\end{pmatrix} \\ & = \begin{pmatrix} \frac{31}{35} & \frac{-27}{35} & \frac{1}{7} \\ \frac{-27}{35} & \frac{87}{70} & \frac{-2}{7} \\ \frac{1}{7} & \frac{-2}{7} & \frac{1}{14}\end{pmatrix}\begin{pmatrix}
27 \\
66 \\
200
\end{pmatrix} \\ & = \begin{pmatrix}
\frac{11}{7} \\
\frac{1142}{35} \\
\frac{-5}{7}
\end{pmatrix}
> \end{align}
> $$
>
> Therefore, $$\hat{\beta_0} \approx 1.571$$, $$\hat{\beta_1} \approx 36.629$$, and $$\hat{\beta_2} \approx -0.714$$.

This method simply extends to higher-order regression too; we would just simply add another term to the model
