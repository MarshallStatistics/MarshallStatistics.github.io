---
layout: single
title: "1.0 Introduction to Probability in Fair Experiments"
date: 2024-11-08
thumbnail: "/assets/network_intro_6.png"
excerpt: "An introduction to probability. This is a core prerequisite to be able to understand statistical theory."
tags:
read_time: true
---
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
Probability theory provides a foundation to be able to understand statistics. It allows us to measure the chance of an event or outcome occurring.

Typically, we are taught from a very young age the even chance of heads landing in a fair coin flip. The outcome in this case would be the coin landing heads as part of a coin flip experiment. The term 'fair' here refers to the coin being 'unbiased'; each outcome has an equal probability of occurring. We first learn about fair experiments when studying probability as they are easy to model.

For instance, in the rolling of a fair die, we have a one-sixth chance of rolling a four. This is because there are six outcomes that are possible and one of them is rolling a four. 

We may colloquially define the probability of an outcome occurring as the proportion of ways my wanted outcome could occur divided by the number of total outcomes of my experiment. Or, more mathematically:

$$\text{The probability of the outcome occurring} = \frac{\text{The number of ways that outcome could occur}}{\text{The total number of outcomes of my experiment}}$$

where the fraction bar of course denotes division. Consider the following motivating example to illustrate this approach: 

> ### Example 1:
> **If I roll a fair die, what is the probability of rolling a two?**
>
> We first calculate the number of ways that outcome could occur. Of course, in one roll, there is only one opportunity to roll a 2.
>
> Next, we consider the total number of outcomes for a die roll. We may roll a 1, 2, 3, 4, 5, or 6 in one roll. Thus, the total number of outcomes is six.
>
> Now, we have everything we need to substitute into the above formula:
>
> > $$\begin{align}
> \text{The probability of the outcome occurring} &= \frac{\text{The number of ways that outcome could occur}}{\text{The total number of outcomes of my experiment}}\\
> & = \frac{1}{6}
> \end{align}$$
>
> Clearly, we could have chosen any possible number present on a die - not just the number two - and obtained the same probability. This is a direct result of the die being fair. 

Now for a more complicated example:

> ### Example 2:
> **If I roll two fair dice and add together the results of each die, what is the probability that I attain a sum of three?**
>
> Again, we first calculate the number of ways that outcome could occur. To do this, we acknowledge that there are two different ways that this chosen outcome could occur. Namely,
>
> **Way 1:** I could roll a one from the first die and a two from the second die.
> 
> **Way 2:** I could roll a two from the first die and a one from the second die.
>
> This means that there are two different ways that I could get my desired outcome.
>
> Now, we must consider all the different possible outcomes of the experiment. As an exercise, list the combinations of outcomes for rolling two different die. You should find that there are 36 different outcomes.
>
> We have all the information we need, so let's use our informal equation above:
>
> $$\begin{align}
> \text{The probability of the outcome occurring} &= \frac{\text{The number of ways that outcome could occur}}{\text{The total number of outcomes of my experiment}}\\
> & = \frac{2}{36}
> \end{align}$$
>
> Hence, the total probability of our desired outcome is \frac{2}{36}. Converting this fraction to a percentage reveals that we have a 5.6% chance to get our desired outcome. 

## Relative frequency

In fact, the first equation introduced in this section only holds for fair experiments, in which each outcome may appear with equal probability. Realistically, the outcomes of an event are not always equally likely to occur; bias is inherent in many real-world phenomena.

A more general view to take would be to imagine probability as a measure of the relative frequency of an event occurring (i.e., the frequency of your chosen outcome occurring divided by the total number of trials conducted). For example, out of sixty individual dice rolls, I would expect to see a 2 land one-sixth of the time. Alternatively, if I flipped a fair coin sixty times, I would expect to see heads land half of the time.

Let's motivate this notion of relative frequency with the following example. 

> ### Example 3:
> **I wish to see if a coin is unbiased. I flip it a hundred times and it lands heads 80 times. Is my coin fair?**
>
> To begin, it would make sense to calculate the relative frequency of heads occurring:
>
> $$\begin{align}
> \text{Relative frequency of heads} &= \frac{\text{The number of heads obtained}}{\text{The total number of trials}}\\
> & = \frac{80}{100}
> \end{align}$$
>
> We see that heads appeared 80% of the time. As such, we may wish to conclude that the coin may be biased towards landing heads. Can you be certain that it is biased? It may be a fair coin that just so happened to land heads 80% of the time.
>
> What could you do to be more certain that the coin is biased?
>
> You could conduct more trials to be more sure. This question, and being able to measure to what extent you can be certain that the coin is biased, is answered by the theory of hypothesis testing. You do not need to know what hypothesis testing is at this stage. Relative frequency can give us a good indication as to whether a coin is biased but is by no means definitive. 


## Introduction to Notation
Let us now delve into the notation of probability. I would like to preface this by saying the notation of probability confused me for a long time (and actually put me off studying statistics initially!). It is my aim to be able to reframe the examples we have discussed above with the new notation. As always, if there are any questions, please do reach out to me!

We shall first start by introducing some concepts:

* An *outcome* is any result from a single run of your experiment. In a coin flip, the outcome could be either 'coin landing heads' or 'coin landing tails'. In our notation, we may wish to denote an outcome by a letter (e.g., $$H$$ for heads or $$T$$ for tails) or a number (e.g., $$1$$ for 'dice landed on one' or $$6$$ for 'dice landed on six'). This is for brevity and to save us writing out what the event is - I would much rather write $$A$$ than provide a long description of the event each time I wish to refer to it.
* An *event* is a collection of one or more outcomes. For instance, I may wish to find out the probability of heads landing twice. This could be described as the event comprised of the outcome 'coin landing heads' once and the outcome 'coin landing heads' again. Just like I did with the event, I can denote the event by a letter (e.g., $$S$$) and I can show using notation that $$S$$ is the event that I get two heads by writing $$S = \left\{H, H\right\}$$. The curly brackets mean a set in mathematics. Without going into too much detail, you can think of these curly brackets as representing a collection of outcomes, with the letters inside the curly brackets representing individual outcomes.

Now, if I wanted to write 'the probability of outcome $$H$$ occurring is 0.5' I would write this with a $$\mathbb{P}$$ for probability, as in:

$$\mathbb{P}(H) = 0.5$$





