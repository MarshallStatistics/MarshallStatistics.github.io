---
layout: single
title: "Randomly Walking in Python, Stylishly"
date: 2024-09-23
thumbnail: "/assets/rw_sim.png"
excerpt: "A quick guide on plotting random walks in Python and how to make your plots nice in Matplotlib for beginners."
read_time: true
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
.definition {
    border: 2px solid #fff;
    padding: 10px;
    margin: 10px 0;
}
</style>

<figure>
  <img src="/assets/rw_sim.png" alt="A symmetric random walk running for fifty steps." title="A symmetric random walk running for fifty steps." style="width=100%;">
  <figcaption style="font-size: small;">Source: Marshall, using Python </figcaption>
</figure>

When learning about stochastic processes, we are often first introduced to the simple, symmetric random walk. In this post, I show how one can produce a plot of a random walk in Python and the various methods you can implement to make it look a little nicer.

Firstly, please see below the mathematical definition of a simple, symmetric random walk:


> ### Definition 1: Simple Random Walk
> Let $$\left\{X_i\right\} \sim \text{Be}(0.5)$$ for $$i \in \mathbb{N}$$ be a set of independent and identically distributed (i.i.d.) random variables, each taking either the value 1 or -1.
> Then, a simple symmetric random walk, $$S_n$$, of $$n \in \mathbb{N}$$ steps, is an iterative process given by
> \\
> $$
> S_{n+1} = S_n + X_n
> $$
> \\
> where $$S_0=0$$ denotes the initial starting point.


Rather handwavingly, one may think of a simple symmetric random walk as a walker stepping forward by one metre or backwards by one metre with equal probability for each step of their walk. Flip a coin: heads is forwards, tails is backwards. After $$n$$ flips, your displacement from your initial point is given by $$S_n$$.

One may of course generalise this by changing the step size from one metre and by changing the probability of stepping forward each step to be a value other than one-half. However, this is outside the scope of this post. We will instead focus on how to plot a simple symmetric random walk in Python. 

Let's start with the basics; we shall first implement our above definition in Python:

```python
# Imported libraries:
import matplotlib.pyplot as plt # # matplotlib enables us to produce and customise many of the plots visible throughout the code.  
import numpy as np # NumPy is a library which contains multiple methods required for data manipulation, particularly when working with arrays.

number_of_steps = 5 # How many steps does the random walk take. In this case, it is five. 
x = np.zeros(number_of_steps) # This creates an array of zeros to store the value of the random walk.

for i in range(1, number_of_steps): # For each step...
    step = np.random.choice([-1, 1])  # This chooses either 1 or -1 with equal probability
    x[i] = x[i-1] + step # This calculates the displacement of the random walk at time i.

print(x)
```
This will return an array, $x$, of the values after each step of the random walk. In my case, this returned an $x$ array of:

```
[ 0 -1 -2 -1 -2 ]
```

Let's now take a look at how to plot it!

```python
# Imported libraries:
import matplotlib.pyplot as plt # matplotlib enables us to produce and customise many of the plots visible throughout the code.  

plt.plot( x,               # This first argument is the thing we want to plot.
          marker='o',      # The second argument specifies the shape of each data point.
          mec = 'black',   # The third argument gives a nice outline around the marker
          linestyle='-')   # Linestyle allows you to specify whether you want a dashed line or not.
    
plt.title('Simple Random Walk') # Provides a title
plt.xlabel('Step') # Labels x-axis
plt.ylabel('Position') # Labels y-axis
plt.grid()   # This creates a set of gridlines on our plot.
```
Here is my output below:

<figure>
  <img src="/assets/rw_example.png">
</figure>

If you wish to save your image in Python, append your code with a line stating:

```Python
plt.savefig('rw_sim (1).png')
```

Pretty cool, eh?

## **References**
* P. R´ev´esz. Random walk in random and non-random environments. World Scientific, 2013.

