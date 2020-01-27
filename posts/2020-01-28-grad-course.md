---
layout: post
title: Graduate Course 2020 part 1
latex
---

As part of my job, I have to give [two lectures](http://www.star.uclan.ac.uk/postgraduate-lectures/) to postgraduate students, as part of a "training programme" for them.  As we have no Mathematics PhD students, I will be speaking to (Astro-)Physicists and Astronomers.  This leave me with three choices, as I see it:

- Give an actual research talk, and loose everyone in 3 minutes (hands up who knows what a Hilbert Space is.  Oh.)
- Give a "public science" like talk on e.g. non-commutative geometry.  Hard to see how this contributes to "training".
- Speak about something Mathematical, but not related to my current research.  Something on basic statistics it is then.

So, my talks will be "A Mathematician looks at statistics".  These are some brief working notes: for the first talk at least I plan to give a "chalk-and-talk" with maybe some brief Python demonstrations.

<!--more-->

What is ["Statistics"](https://en.wikipedia.org/wiki/Statistics)?  To quote Wikipedia:

> Statistics is the discipline that concerns the collection, organization, analysis, interpretation and presentation of data.

Furthermore, we can broadly split the study of statistics into two areas:

1. [Descriptive statistics](https://en.wikipedia.org/wiki/Descriptive_statistics) which is the study of presenting data.

2. [Statistical inference](https://en.wikipedia.org/wiki/Statistical_inference) which, to quote, is "the process of using data analysis to deduce properties of an underlying probability distribution."

Rather crudely, one might say that the use of descriptive statistics is when you have access to all the data you need, and you wish to present it.  For example, the university knows the home address postcode of every student: how might we present this information visually to gain some knowledge of where our students come from?

Again, rather crudely, statistical inference occurs when we do not have access to all the data, but only a "sample".  The classical example is an election opinion poll: we contact, at random, a few thousand people, and ask them how they will vote in an election.  From this "sample" (which is a tiny fraction of the "population" of all voters) we can somehow determine what the likely outcome of the election will be.

This is a rather crude picture, as statistical inference also occurs in, for example, the following two situations:

1. We are interested in coin flipping.  We have a coin which we suspect is biased: more likely to land heads than tails.  How might we test is this suspicion is true or not?

2. We have luminosity data from two families of stars.  How might we decide if the two families are "different", or not?

Neither of these cases fits easily into the "sample from a population" framework.

Let's go back to what Wikipedia said: "...deduce properties of an underlying probability distribution".  In this first lecture, I want to first of all think about what a "probability distribution" is.

## Probability

In Mathematics statistics, the idea of "probability" is central.  In Mathematical probability, we have two key notions:

- A "probability space" which is the collection of all possible outcomes, called "events".
- A "probability" which is an assignment to each event of a number between 0 and 1 which represents the chance of that event occurring.  The sum of all probabilities should be 1 (representing that some event must occur).

As is tradition in maths, having given a definition, we proceed to some examples:

1. We toss a fair coin, and obtain a heads or tails.  The probability space is hence the "set" (a mathematical collection) $\{ H, T\}$ and the probability is
\[ \mathbb{P}(H) = \mathbb{P}(T) = 0.5. \]
This represents that getting a head, or getting a tail, is equally likely (and then $0.5$ is the only possibility if the total probability is 1)

2. We pick someone at random, and ask which month their birthday is in.  The probability space is the set of all months (or the numbers 1 to 12, perhaps?).  The probability assigns $1/12$ to each month, as there should be no bias as to which month a randomly chosen person is born in.  We might like to think if this is a realistic model of real people?

What does probability "mean"?  This is a deep philosophical problem.  As a mathematician, I am tempted to dismiss the question, and simply say that we have some axioms which we work with (this is the [Kolmogorov](https://en.wikipedia.org/wiki/Probability_axioms) view).  But to do statistics, we have to have some belief that mathematical probability is an accurate model of the world.  Without getting beyond my pay grade, a common justification of probability is given by the [law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers).  In the coin example, that the probabilities are equal is reflected in the fact that if we toss a coin many times, then we would expect to get, "roughly", "on average", the same number of heads as tails.  In the birthday month example, the situation is easier, as we could (in theory) find the birth month of everyone in the UK (for example) and then the probability is simply the proportion of each month which occurs.

This naive view is dangerous however, because it is easy to think of situations where we wish to speak of "probability" where either is it possible to sample the entire population, and nor is it possible to repeat an experiment many times (even in theory, never mind what is realistically possible).  However, I shall say no more.

A nice class of examples from considering [urn models](https://en.wikipedia.org/wiki/Urn_problem).  Consider a container (then "urn") which contains $n$ red balls and $m$ blue balls.

3. Consider removing a ball at random.  The probability space is just $\{ R,B \}$ representing the colour of the removed ball.  Then $\mathbb P(R) = n / (n+m)$ as there are $n+m$ balls in total, and $n$ of them are red.

We can extend this in lots of ways.  Maybe there are more than two colours.  Maybe we remove more than one ball.  Let us introduce some more notation: if $A$ is a set of events, then write $\mathbb P(A)$ for the probability that some event in the set $A$ occurs.

4. Consider removing three balls at once.  The probability space is $\{0,1,2,3\}$ representing the number of red balls removed.  Then $\mathbb P(\{0,1,2\})$ equals the probability of _not_ removing $3$ red balls.

## Random variables

In this last example, we can think of $R$ as being "the number of red balls removed".  This is a "variable": it is the whole number $0,1,2$ or $3$.  However, it is a "random variable" as it doesn't have a fixed value, but instead takes each value with a certain probability.  We write, for example, $\mathbb P(R=2)$ for the probability of drawing exactly 2 red balls.

We can perform arithmetic on random variables.  For example, if $B$ is the number of blue balls drawn, then $R+B=3$ and so $\mathbb P(R=2) =  \mathbb P(B=1)$.

## Continuous probability

How might we model the heights of people?  Notice the word "model" here: I am already thinking about how to reduce complicated real-world data to a simple mathematical description.  The key problem is that "height" is a continuous variable.  We deal with this by saying that it is only possible to talk about the probability of a random variable falling in some interval.

5. A textbook example models height using a [_Normal_ or _Gaussian Distribution_](https://en.wikipedia.org/wiki/Normal_distribution).  We choose two values: the mean $\mu$ and variance $\sigma^2$.  Choose $\mu=200cm$ and $\sigma = 20cm$ (I have no idea if these are realistic!).  We say that a random variable $X$ is $N(\mu,\sigma^2)$ when
\[ \mathbb P (a \leq X \leq b)
= \int_a^b \frac{1}{\sqrt{2\pi\sigma^2}} e^{-(x-\mu)^2/2\sigma^2} \ dx. \]
The formula is just a scaled Gaussian.  What matters is that we give a probability for $X$ to be a number between $a$ and $b$.  Notice that the probability that $X$ is between $-\infty$ and $\infty$ is 1, as we expect.<br/>
For example, $\mathbb P(190\leq X\leq 210)$ is about 38%.  

In this example, the probability depends on two parameters $\sigma,\mu$.  In the "urn" example, we chose the number of balls $n$ and $m$.  At present, we think of these as fixed, but later is might want to "estimate" these parameters from some data.

## Independence

Suppose we take our coin, and toss it twice.  We now have a new probability space: $\{ HH, HT, TH, TT\}$ of all 4 possible outcomes of two tosses.  What should be the probability?  It seems reasonable to think that each event should be equally likely, so each has probability $1/4$.

The key idea here is "independence".  We think of tossing one coin, and then tossing it again, and the _result of the first toss does not affect the second_.  Let $H_1$ be the event of getting a heads on the first toss, and $H_2$ getting a head on the second toss.  Then $H_1$ is set of outcomes $HT$ or $HH$, while $H_2$ is the set of outcomes $TH$ or $HH$.  Thus $H_1 \cap H_2$ (the _intersection_) is the event that we get both a head on the first toss, and a head on the second toss, that is, $HH$.  So
\[ \frac14 = \mathbb P(HH) = \mathbb P(H_1 \cap H_2) = \mathbb P(H_1)\mathbb P(H_2) =
\frac12 \times \frac12. \]

**Definition:** Two events $A$ and $B$ are _independent_ $\mathbb P(A\cap B) = \mathbb P(A) \mathbb P(B)$.

We might like to think about how this could not be so?

6. Suppose on a stretch of Motorway, there is a 5% chance of an accident each day.  It has been determined that speed is a large factor in accidents, and the day after an accident has occurred, there are extra police patrols, which reduces speeding, and so the chance of an accident to 3%.  There are never police patrols on the first day of the week.  What is the probability of an accident on both Monday and Tuesday?<br/>
The possible outcomes on Monday and Tuesday are $\{NN, AN, NA, AA\}$ where $A$ is accident, and $N$ is no accident.  We have that, for Monday,
\[ \mathbb P(A) = 0.05, \qquad \mathbb P(N) = 0.95, \]
and so
\[ \mathbb P(NN) = 0.95^2, \qquad \mathbb P(NA) = 0.95 \times 0.05. \]
However, the reaction of the police means that
\[ \mathbb P(AN) = 0.05 \times 0.97, \qquad \mathbb P(AA) = 0.05 \times 0.03. \]
Thus the events "accident on Monday" and "accident on Tuesday" are not independent.

(You might like to think about how we might, in the real world, obtain the probabilities involved here.  Google "regression to mean".)

The following is a "paradox":

7. Suppose we (fair) toss a coin 10 times and get a head every time!  Surely the change of the next toss being tails is rather higher than one half, as eleven heads in a row is rather unlikely!  (If you don't believe this, what do you think about the quote: "the number 32 hasn't been seen in the lottery for a while, so it's about time it turned up again.")

Of course, each toss is independent, and so the change of getting tails after 10 heads is 1/2, as it always is.

To make these sorts of calculations easier, we introduce some more notation:  Given sets of events $A$ and $B$, write
\[ \mathbb P(A|B) \]
for the probability of $A$ happening, given that $B$ has happened.
This is called _conditional probability_: the probability that $A$ occurs, conditional on $B$ having occurred.  In the traffic accident example, we had
\[ \mathbb P(A|\text{It is Monday}) = 0.05, \qquad
\mathbb P(A|\text{accident happened the day before}) = 0.03. \]

Then two events are independent if $\mathbb P(A|B) = \mathbb P(A)$.

We can derive a formula for $\mathbb P(A|B)$.  If $B$ is known to have occurred, then we consider a new probability space as being all the things which can occur, knowing that $B$ has occurred.  Then that $A$ occurs means that $A\cap B$ must occur (both $A$ and $B$ occur), but we need to normalise by dividing the probability that $B$ occurs.  Thus we obtain
\[ \mathbb P(A|B) = \frac{\mathbb P(A\cap B)}{\mathbb P(B)}. \]
(Note that in some Mathematical approaches to probability, this is actually
[taken as an axiom](https://en.wikipedia.org/wiki/Conditional_probability).)
We shall henceforth take this as the _definition_ of conditional probability.  If $A,B$ are independent that $\mathbb P(A\cap B) = \mathbb P(A)\mathbb P(B)$ and so
\[ \mathbb P(A|B) = \frac{\mathbb P(A\cap B)}{\mathbb P(B)}
= \frac{\mathbb P(A)\mathbb P(B)}{\mathbb P(B)}
= \mathbb P(A), \]
as we had before.  (So we start to see how "definitions" agree with "intuition" / "meaning".)

There are two key results to know here.

[**Law of total probability:**](https://en.wikipedia.org/wiki/Law_of_total_probability)
Suppose $B_1,\cdots,B_n$ are disjoint events which cover the whole of the probability space.  If $A$ is any event, then
\[ \mathbb P(A) = \sum_{k=1}^n \mathbb P(A|B_k)\mathbb P(B_k). \]

**Proof:** We can suppose $\mathbb P(B_k)\not=0$ as if it was $0$ we can ignore it.
By definition, $\mathbb P(A|B_k)\mathbb P(B_k) = \mathbb P(A\cap B_k)$.  As the union of the $B_k$ is the whole space, we know that
\[ A = \bigcup_k A\cap B_k. \]
As $A\cap B_k$ is disjoint from $A\cap B_j$ for $j\not=k$, and probability is additive,
we have
\[ \mathbb P(A) = \sum_{k=1}^n \mathbb P(A \cap B_k). \]

[**Bayes Theorem:**](https://en.wikipedia.org/wiki/Bayes%27_theorem)
$\mathbb P(A|B) \mathbb P(B) = \mathbb P(B|A) \mathbb P(A)$.

**Proof:** Using the definition we have
\[ \mathbb P(A|B) \mathbb P(B)
= \frac{\mathbb P(A\cap B)}{\mathbb P(B)} \mathbb P(B)
= \mathbb P(A\cap B). \]
Similarly, $\mathbb P(B|A) \mathbb P(A) = \mathbb P(A\cap B)$.  Thus both sides are
equal.

We often re-arrange as
\[ \mathbb P(A|B)  = \frac{\mathbb P(B|A) \mathbb P(A)}{\mathbb P(B)}. \]

This simple result is hugely useful in applications.  Here is a classical one:

8. A test for Coronavirus has a ["sensitivity"](https://en.wikipedia.org/wiki/Sensitivity_and_specificity) of 95% and a ["specificity"](https://en.wikipedia.org/wiki/Sensitivity_and_specificity) of 99%.  One in 100,000 people in the UK has Coronavirus.  I test positive!  Should I be worried?

We need to understand what these words mean:

- "Sensitivity" means "true positive".  95% here means that of 100 people with the virus, the test will say they have the virus 95 times (and get it wrong 5 times).
- "Specificity" means "true negative".  99% here means that of 100 people without the virus, the test will say they are in the clear 99 times (and say "yes" just once).

Let $C$ be the event I have the virus, and $\neg C$ the event I don't.  Let $T$ be the event I test for the virus, and $\neg T$ the event the test says I don't have the virus.  The questions gives us this information:
\[ \mathbb P(C) = 1 / 100,000, \qquad \mathbb P(T|C) = 0.95, \qquad
\mathbb P(\neg T|\neg C) = 0.99. \]
I want to know $\mathbb P(C|T)$: the probability I have the virus, given that I test positive for it.

By Bayes' Theorem, we have
\[ \mathbb P(C|T) = \frac{ \mathbb P(T|C) \mathbb P(C) }{ \mathbb P(T) }. \]
By the Law of Total Probability,
\[ \mathbb P(T) = \mathbb P(T|C)\mathbb P(C)
+ \mathbb P(T|\neg C)\mathbb P(\neg C). \]
Putting in the numbers gives
\[ \mathbb P(T) = 0.95 \times 1/100,000 + 0.05 \times 99,999 / 100,000
= 0.050,009, \]
and so
\[ \mathbb P(C|T) = \frac{0.95 / 100,000}{0.050,009}
\approx 1.9 \times 10^{-4}. \]
I should not worry!

Hopefully this seems a little counter-intuitive to you.  The test sounds quite accurate!  However, the virus is rather rare, and it is in fact this which really matters.  I have never meant this situation in real life, but I wonder if doctors are good at explaining this?  There are various visualisation tools, which I know from the work of [David Spiegelhalter](https://en.wikipedia.org/wiki/David_Spiegelhalter), which can help here.

## Next time

I like to think of Statistics as swapping the roles of "random variables" and "parameters".  For example:

9. An urn contains 10 red balls, and an unknown number of blue balls.  I draw a ball, observe its colour, and put the ball back in the urn.  Doing this 5 times I get BBBRB.  What is the most likely number of red balls?

10. We assume heights of students are distributed normally with $\sigma=20cm$.  We measure 10 Mathematics students and get a mean height of 190cm, and measure 10 Physics students and get a mean height of 195cm.  Are Physicists taller than Mathematicians?

I will talk about "parameter estimation" and "hypothesis testing", and maybe the Bayesian approach to this.