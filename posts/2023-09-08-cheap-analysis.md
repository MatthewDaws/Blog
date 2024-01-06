---
layout: post
title: Cheap analysis
latex
---

This is a follow-on to [an older post](2023-06-25-cheap-maths.html) prompted by a comment from Yemon Choi (an old friend who is now a colleague).  There are of course many examples of monotone Galois connections in Functional Analysis.  Here is one example which I like.

Let $E$ be a Banach space. Let $\mathcal X$ be the collection of all linear subspaces of $E$, ordered by inclusion.  Let $\mathcal Y$ be the collection of all linear subspaces of $E^*$ (the dual space of all continuous linear functionals) ordered by reverse inclusion.

Given $F\in\mathcal X$ we define
\[ \mathcal L(F) = \{ f\in E^* : f(x)=0 \ (x\in F) \} \in \mathcal Y, \]
the annihilator of $F$, easily seen to be a subspace.  If $F_1 \leq F_2$ then $F_1 \subseteq F_2$ and so $\mathcal L(F_1) \supseteq \mathcal L(F_2)$ (if $f$ vanishes on $F_2$ it will vanish on $F_1$).  So $\mathcal L(F_1) \leq \mathcal L(F_2)$ and $\mathcal L$ is order-preserving.

Similarly given $F\in\mathcal Y$ define
\[ \mathcal R(F) = \{ x\in E : f(x)=0 \ (f\in F) \}\in \mathcal X, \]
the pre-annihilator of $F$.  This is again an order-preserving map.

<!--more-->

Let $F\in\mathcal X$ and $G\in\mathcal Y$.  Then
\[ \begin{split}
& \mathcal L(F) \leq G \\
\Leftrightarrow\quad & \mathcal L(F) \supseteq G \\
\Leftrightarrow\quad & f\in G \implies f(x)=0 \ (x\in F) \\
\Leftrightarrow\quad & x\in F \implies f(x)=0 \ (f\in G) \\
\Leftrightarrow\quad & F \subseteq \mathcal R(G) \\
\Leftrightarrow\quad & F \leq \mathcal R(G).
\end{split} \]
Hence we have the required condition.

If we run the abstract argument, we obtain a bijection between the images of $\mathcal R$ and $\mathcal L$.  Here some non-trivial Functional Analysis appears in the guise of the [Hahn-Banach Theorem](https://en.wikipedia.org/wiki/Hahn%E2%80%93Banach_theorem).  The image of $\mathcal L$ is the collection of all weak$^*$-closed subspaces of $E^\ast$, while the image of $\mathcal R$ is the collection of all (norm) closed subspaces of $E$.  This bijection is of course well-known, but it's fun to see it appear here.

