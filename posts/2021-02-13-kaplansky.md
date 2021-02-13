---
layout: post
title: Counter-examples to Kaplansky Density
latex
---

I've added a short document to my [Mathematical writeups](https://github.com/MatthewDaws/Mathematics/tree/master/Kaplansky2) collection.  Thanks to Yemon Choi for a conversation which motivated me to write this up, and to Philip Spain who alerted me to the work of Harry Dowson.

It would be interesting to have a _natural_ Banach Algebra example.  By this, I mean a naturally occurring example of a dual Banach Algebra $M$ and a weak$^\ast$-dense subalgebra $A\subseteq M$ such that there is a unit vector in $M$ which is not the weak$^\ast$-limit of any bounded net in $A$.

What do I mean by "natural" here?  Some possible examples:

- Let $E$ be a reflexive Banach space with the approximation property. Then it's known that $\mathcal B(E)$ is the bidual of $\mathcal K(E)$.  Thus $\mathcal K(E)$ is weak$^\ast$-dense in $\mathcal B(E)$, but in this case, we do have an (isometric) version of Kaplansky Density, because biduals satisfy [Goldstine's Theorem](https://en.wikipedia.org/wiki/Goldstine_theorem).  I still think this example is a little interesting: if $E$ had the metric approximation property, given $T\in\mathcal B(E)$ it is easy to write down a net in $\mathcal K(E)$ which converges to $T$ and is bounded by $\|T\|$.  If $E$ merely has the approximation property then this seems less clear to me, though it is ensured by the general theory.

- Let $G$ be a locally compact group, and consider $PM_p(G)$ which by definition is the weak$^\ast$ closure of $PF_P(G)$ inside $\mathcal B(L^p(G))$.  Excepting when $p=2$ I do not know if we have Kaplansky Density here, though if $G$ has a suitable approximation-like property (amenability, or a weakening) then I believe one can show this: I don't know if this is explicitly in the literature.
