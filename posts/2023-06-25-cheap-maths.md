---
layout: post
title: Cheap mathematics
latex
---

A long-time-coming comment on a [post by John Baez](https://golem.ph.utexas.edu/category/2023/04/bargainbasement_mathematics.html) about "bargin-basement mathematics".  (But let's not do ourselves down-- the rest of the system is more than happy enough to do that for us-- so I shall say "cheap" not quite "bargain-basement").

The setup here is a [(monotone Galois connection)](https://en.wikipedia.org/wiki/Galois_connection), which consists of two posets $X$ and $Y$, and order-preserving maps
\[ L:X\rightarrow Y, \qquad R:Y\rightarrow X, \]
which satisfy $L(x)\leq y$ if and only if $x\leq R(y)$.  The exercise, whose solution I'll give below, is that while $L$ and $R$ may of course fail to be mutual inverses, if we define $X'=R(Y)$ and $Y'=L(X)$ then $L,R$ restrict to $X',Y'$ respectively to become mutual inverses.

<!--more-->

> **Lemma 1:** For any $x\in X$ we have $x\leq R(L(x))$, and for any $y\in Y$ with have $L(R(y)) \leq y$.

> _Proof:_ Given $x$, set $y=L(x)$ so certainly $L(x) \leq y$, and hence by the defining assumption, $x \leq R(y) = R(L(x))$.  Similarly, $R(y) \leq R(y)$ implies that $L(R(y)) \leq y$.

> **Lemma 2:** For any $x\in X'$ we have that $x=R(L(x))$.  For any $y\in Y'$ we have that $y=L(R(y))$.

> _Proof:_ Given $x\in X'$ there is $y\in Y$ with $x=R(y)$.  For any $z$, by Lemma 1, we have $L(R(z)) \leq z$ and so $L(R(L(x))) \leq L(x)$ and $x\leq R(y)$ so $L(x)\leq y$, hence conclude that $L(R(L(x))) \leq y$.  This implies that $R(L(x)) \leq R(y) = x$.  By Lemma 1, $x \leq R(L(x))$, and so $R(L(x)) = x$.

> Now given $y\in Y'$ there is $x\in X$ with $L(x)=y$, which implies that $x\leq R(y)$.  By Lemma 1, for any $z$, we have that $z\leq R(L(z))$ and so $R(y) \leq R(L(R(y)))$ so $x \leq R(L(R(y)))$.  This implies that $y = L(x) \leq L(R(y))$.  Lemma 1 tells us that $y \geq L(R(y))$, and so we conclude that $y = L(R(y))$.

We can now prove the main claim.

> **Claim:** $L$ and $R$ restrict to mutually inverse bijections between $X'$ and $Y'$.

> _Proof:_ By definition, $L$ maps into $Y'$ and $R$ maps into $X'$, so we obtain restricted maps $L:X'\rightarrow Y'$ and $R:Y'\rightarrow X'$.  We have shown that $x=R(L(x))$ for $x\in X'$ and $y=L(R(y))$ for $y\in Y'$.  We claim that $L$ is bijective.  This is clear, as $L(R(y))=y$ for any $y\in Y'$ shows $L$ is surjective, while $R(L(x))=x$ for any $x\in X'$ shows that $L$ injects.  Similarly $R$ is a bijection.

Notice that we never used that $L$ and $R$ preserve order, only that $L(x)\leq y \Leftrightarrow x\leq R(y)$.

The wikipedia article says a lot more, of course.

This is all quite neat, but I have struggled to think of a naturally occurring example in the sort of algebraic functional analysis which I study.
