---
layout: post
title: Multiplicative Domains
latex
---

Reading [Ng, Viselter, Amenability of locally compact quantum groups and their unitary co-representations](https://mathscinet.ams.org/mathscinet-getitem?mr=3723633)
[Arxiv](https://arxiv.org/abs/1609.08920) I was reminded by a result/technique that I often forget: that of the _multiplicative domain_ of a completely positive map.
The following result is due to [M.D. Choi](https://projecteuclid.org/download/pdf_1/euclid.ijm/1256051007) (though I like the presentation in
[Paulsen's book](https://www.researchgate.net/publication/200524409_Completely_Bounded_Maps_and_Operator_Algebras)).

Let $\phi:A\rightarrow B$ be a unital completely positive (UCP) map between unital $C^\ast$-algebras.  If $a\in A$ with $\phi(a)^\ast\phi(a) = \phi(a^\ast a)$ then already $\phi(ba) = \phi(b)\phi(a)$ for any $b$.  If this is the "right hand version" then there is a left hand version, and a bimodule version.

<!--more-->

A nice application is the following: suppose that $u\in A$ is unitary, and that we know that $\phi(u)$ is also unitary.  Then $\phi(au) = \phi(a)\phi(u)$ for any $a\in A$.  This follows, of course, because $u^\ast u=1$ and $\phi(u)^\ast\phi(u)=1$ so we have equality as $\phi$ is unital.

The application of Chi-Keung and Ami is to multiplicative unitaries which allows them to give an incredibly short proof that amenability of representations respected weak containment.

I want to just say a couple of words about why this is perhaps not too surprisingly.  (More than a couple of words is maybe not warranted, as the proof itself is not so long, using the Schwarz inequality).  Any UCP map is of the form $\phi(a) = V^\ast \pi(a)V$ where $\pi:A\rightarrow B(H)$ is a $\ast$-representation, and $V:K\rightarrow H$ is an isometry (here I assume $B\subseteq B(K)$).  If $u\in A$ is unitary then so is $\pi(u)$, and so that $V^\ast \pi(u) V$ is unitary is a strong condition:

- $\pi(u)$ must restrict to a unitary on the image of $V$;
- thus $VV^\ast\pi(u)V = \pi(u)V$;
- then $\phi(a)\phi(u) = V^\ast\pi(a) VV^\ast\pi(u) V=V^\ast \pi(au)V = \phi(au)$.

Coda: Looking at the Stinespring dilation is often profitable.
