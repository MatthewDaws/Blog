---
layout: post
title: From pinchings to quantum colourings
latex
---

Finally, I can combine the [last post](2023-07-07-quantum-chromatic-numbers.html) with [a post 3 ago](2023-07-03-fixed-points.html).  This argument is from a paper of Elphick and Wocjan, attributed there to Roberson.

Fix a graph $G$ with adjacency matrix $A$.

> **Theorem:** Let $\mathcal C$ be a pinching on $\mathbb M_n\otimes\mathcal B(H)$ with $\mathcal C(A\otimes 1_H)=0$ and $\mathcal C(D\otimes 1_H)=D\otimes 1_H$ for each diagonal matrix $D$.  Then $\mathcal C$ arises from a quantum colouring of $G$, in the manner described before.

<!--more-->

> _Proof:_ Let the pinching be $\mathcal C(x) = \sum_k P_k x P_k$ for some projections $(P_k)$ on $\mathbb C^n\otimes H$ with $\sum_k P_k=1$.  As $P_k=P_k^*$, we see that $\mathcal C$ is completely positive, and unital as $\sum_k P_k=1$.  If $H$ is finite-dimensional, we compute that
\[ \newcommand{\tr}{\operatorname{Tr}} \tr(\mathcal C(x)) = \sum_k \tr(P_kx_Pk) = \sum_k \tr(P_k^2x) = \tr(x), \]
> so $\mathcal C$ is a quantum channel.

> (If $H$ is infinite-dimensional separable, then $\mathbb C^c\otimes H \cong H$ and we can regard $\mathcal C$ as acting on $\mathcal B(H)$.  We can find a trace-class operator $d$ with full support which is diagonal with respect to the orthogonal decomposition given by the $(P_k)$.  Thus $P_kd=dP_k$ for each $k$.  Then the functional $\phi(x) = \tr(xd)$ is faithful, and invariant, because
\[ \phi(\mathcal C(x)) = \sum_k \tr(P_kxP_kd)
= \sum_k \tr(x dP_k) = \tr(dx) = \phi(x). \]
> If $H$ is not separable, then we can find a family of invariant functions which together are faithful, and this is sufficient for the proof of our [fixed point result](2023-07-03-fixed-points.html) to still work.)

> As $\mathcal C$ is written in Kraus form, we conclude that each $P_k$ commutes with the fixed points, in particular, with $D\otimes 1_H$ for each diagonal matrix $D$.  This means that each $P_k$ has the form
\[ P_k = \sum_{v\in V} e_v e_v^* \otimes P_{v,k} \]
> for some projections $(P_{v,k})$ on $H$.  (Here recall that $n=|V|$ so $\mathbb C^n$ is indexed by $V$.)  Then
\[ 1 = \sum_k P_k = \sum_v e_ve_v^* \otimes \sum_k P_{v,k} \]
> and so $\sum_k P_{v,k}=1$ for each $v$.

> Finally,
\[ \begin{split} 0 &= \mathcal C(A\otimes 1_H) = \sum_{u,v} e_u e_u^* A e_v e_v^* \otimes \sum_k P_{u,k} P_{v,k} \\
&= \sum_{u\sim v} e_u e_v^* \otimes \sum_k P_{u,k} P_{v,k}, \end{split} \]
> as $e_u^*Ae_v = A_{u,v}=1$ only when $u\sim v$.  Choose $u\sim v$, so we have that $\sum_k P_{u,k} P_{v,k} = 0$.  As $\sum_k P_{u,k} = 1$, the projections $(P_{u,k})_k$ are orthogonal, so given $l$,
\[ 0 = \sum_k P_{u,l} P_{u,k} P_{v,k} = P_{u,l} P_{v,l} \]
> which is the second condition to be a quantum colouring.

I wonder if some similar result holds for [quantum graphs](https://arxiv.org/abs/2203.08716).
