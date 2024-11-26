---
layout: single
title: "1.1 Estimating `$\beta_0$` and `$\beta_1$` using least squares estimation"
date: 2024-11-26
thumbnail: "/assets/scatter_graph_annotated.png"
excerpt: "We shall introduce least squares regression as a means to estimate `$\beta_0$` and `$\beta_1$`."
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

As mentioned in our previous post, we wish to estimate our coefficients contained in \boldsymbol{\beta}. Also, recall that we defined \boldsymbol{\epsilon} to be the deviations from the straight line. Hence, if we seek to find values for \boldsymbol{\beta} which minimise $$\boldsymbol{\epsilon}$$, we will obtain a model which most accurately represents the linear relationship between the values of our independent variable (\mathbf{x}) and those of our dependent variable (\mathbf{y}).

To do this, we must first construct a function for the errors (\boldsymbol{\epsilon}) and then find the value of \boldsymbol{\beta} which minimises the function. It is most sensible to square the errors, as each element of \boldsymbol{\epsilon} may be either negative or positive. If we consider the squared errors, we are only really taking into account how much the absolute value of each element of \boldsymbol{\epsilon} is contributing to the overall error. Cool, eh? Let's take a look at constructing this function (recall that to sum the squared elements of a column vector we multiply the vector with its transpose). Thus, our function starts as:

$$\boldsymbol{\epsilon}^T\boldsymbol{\epsilon}$$

Now, we use the model to recognise that $$\boldsymbol{\epsilon} = \mathbf{y} - \mathbf{F} \boldsymbol{\beta}$$/. Let's substitute this expression for $$\boldsymbol{\epsilon}$$ in and try to expand the brackets:

$$
\begin{align}
\boldsymbol{\epsilon}^T\boldsymbol{\epsilon} &= (\mathbf{y} - \mathbf{F} \boldsymbol{\beta})^T(\mathbf{y} - \mathbf{F} \boldsymbol{\beta}) \\
&= \mathbf{y}^T \mathbf{y} - 2\mathbf{y}^T \mathbf{F} \boldsymbol{\beta} + \boldsymbol{\beta}^T \mathbf{F}^T \mathbf{F} \boldsymbol{\beta}
\end{align}
$$

Remember, we are looking to find the value of $$\boldsymbol{\beta}$$ which minimises our squared error function. Therefore, we must differentiate our squared error once with respect to $$\boldsymbol{\beta}$$, set this result equal to zero and solve for $$\boldsymbol{\beta}$$. This will give us the value of $$\boldsymbol{\beta}$$ which best fits our data (as it minimises the absolute value of the errors as much as possible).

Deriving matrix equations can get a bit tricky, so we will explain afterwards what has happened:

$$
\begin{align}
\frac{\mathrm{d} \boldsymbol{\epsilon}^T\boldsymbol{\epsilon}}{\mathrm{d} \boldsymbol{\beta}} = 0 - 2\mathbf{F}^T \mathbf{y} + 2 \mathbf{F}^T \mathbf{F} \boldsymbol{\beta}
\end{align}
$$

The first term vanishes, since $$\mathbf{y}^T \mathbf{y}$$ will return a constant. Thus, its derivative will be zero. The second term appears as though \mathbf{y} and \boldsymbol{\beta} swap places. This is because when taking the derivative of a scalar product involving matrices, the differentiation results in transposing the matrix \mathbf{F}. The third term is written in quadratic form, so we use the fact that the derivative of a quadratic form $$\boldsymbol{\beta}^T \underline{\underline{A}} \boldsymbol{\beta}$$ with respect to $$\boldsymbol{\beta}$$ is $$2 \mathbf{A}\boldsymbol{\beta}$$, where A is a symmetric matrix. In this case $$\mathbf{A} = \mathbf{F}^T \mathbf{F}$$.

Now we have our derivative, we shall now set it to zero and solve for $$\boldsymbol{\hat{\beta}}$$ which are our values of $$\boldsymbol{\beta}$$ which minimise our squared error function. Thus, our above equation becomes:

$$
\begin{align}
0 &= - 2\mathbf{F}^T \mathbf{y} + 2 \mathbf{F}^T \mathbf{F} \boldsymbol{\hat{\beta}} \\
\Rightarrow \ \mathbf{F}^T \mathbf{F} \boldsymbol{\hat{\beta}} &= \mathbf{F}^T \mathbf{y} \\
\Rightarrow \ \boldsymbol{\hat{\beta}} &=  \left(\mathbf{F}^T \mathbf{F}\right)^(-1) \mathbf{F}^T \mathbf{y}
\end{align}
$$

Therefore, using this equation, we can find the value of \boldsymbol{\beta} which minimises the overall absolute value error as much as possible. Let's ground this with an example.


