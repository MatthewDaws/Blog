---
layout: post
title: Fixed points of complete positive maps
latex
---

The first of hopefully a few posts about actual Mathematics, the context of which will follow.  In [Watrous's QIT book](https://cs.uwaterloo.ca/~watrous/TQI/), Theorem 4.25 states the following:

> Let $\Phi:\mathbb M_n\rightarrow\mathbb M_n$ be a unital quantum channel with Kraus representation $\Phi(x) = \sum_a A_a x A_a^*$.  Then $\Phi(x)=x$ if and only if $A_a x = x A_a$ for each $a$.

(Here I translate slightly the language).  Whenever I see a statement about quantum channels, I ask myself if I can translate it into a more Operator Algebraic statement making more use of the Stinespring representation theorem, for example.  After much messing about, I realised that the key property is that $\Phi$ is _trace preserving_, and that this, together with [multiplicative domain theory](2019-08-04-multdomains.html), can be used to give a simple proof.  (Well, maybe not _simple_, but one adding some context.)

<!--more-->

Let's start by recalling some basic results, which I always forget somehow.  Let $A,B$ be $C^*$-algebras and $\Phi:A\rightarrow B$ be a completely positive map.  The Stinespring representation theorem tells us that if $B\subseteq \mathcal B(H)$ is a faithful representation, then there is a Hilbert space $K$, a $*$-representation $\pi:A\rightarrow\mathcal B(K)$, and a bounded linear map $V:H\rightarrow K$ such that $\Phi(a) = V^*\pi(a)V$ for each $a\in A$.  We call $(\pi,K,V)$ a _Stinespring dilation_ of $\Phi$, which is said to be _minimal_ if $\{ \pi(a)V\xi: \xi\in H, a\in A\}$ has dense linear span in $K$.  A minimal dilation is unique up to (obvious) unitary equivalence.  (It can sometimes be helpful to know that when $(\pi,K,V)$ is minimal, there is a $*$-homomorphism $\rho:\Phi(A)' \rightarrow \pi(A)'$ with $\rho(x)V = Vx$ for each $x\in\Phi(A)'\subseteq\mathcal B(H)$.  Then $\rho$ is automatially normal.)

For the following, see [Brozwn+Ozawa](https://zbmath.org/1160.46001) Proposition 1.5.7.

> **Theorem:** Let $\Phi:A\rightarrow B$ be a contractive completely positive map.  Then:
> 1. (The Schwarz Inequality) We have that $\Phi(a)^*\Phi(a) \leq a^*a$ for each $a\in A$;
> 2. (Bimodule structure) For $a\in A$, if $\Phi(a^*a) = \Phi(a)^*\Phi(a)$ then $\Phi(ba)=\Phi(b)\Phi(a)$ for each $b\in A$; and if $\Phi(aa^*) = \Phi(a)\Phi(a)^*$ then $\Phi(ab)=\Phi(a)\Phi(b)$ for each $b\in A$;
> 3. The space $A_{\Phi}=\{a\in A:\Phi(a^*a) = \Phi(a)^*\Phi(a), \Phi(aa^*)=\Phi(a)\Phi(a)^*\}$ is a $C^*$-subalgebra of $A$, and $\Phi$ restricted to $A_\Phi$ is a $*$-homomorphism.

> _Proof:_ Let $B\subseteq\mathcal B(H)$ be faithful, and let $(\pi,K,V)$ be a Stinespring dilation of $\Phi$.  As $\Phi$ is a contraction, $\|V\|\leq 1$ and so $VV^*\leq 1$.  For $a\in A$ we have
> \[ \begin{split} \Phi(a^*a)-\Phi(a)^*\Phi(a) &= V^*\pi(a)^*\pi(a)V^* - V^*\pi(a)^*VV^*\pi(a)V \\
&= V^* \pi(a)^* (1-VV^*) \pi(a)V \geq 0, \end{split} \]
> giving the Schwarz Inequality.
>
> Furthermore, we notice that $\Phi(a^*a) = \Phi(a)^*\Phi(a)$ if and only if $(1-VV^*)^{1/2}\pi(a)V=0$.  If this holds, then for $b\in A$,
> \[ \Phi(ba) - \Phi(b)\Phi(a) = V^*\pi(b)(1-VV^*)\pi(a)V = 0. \]
> Similarly, $\Phi(aa^*)=\Phi(a)\Phi(a)^*$ is equivalent to $(1-VV^*)^{1/2}\pi(a)^*V=0$, equivalently, $V^* \pi(a) (1-VV^*)^{1/2} = 0$.  This implies that $\Phi(a)\Phi(b) = \Phi(ab)$ for each $b\in A$.
>
> We now consider (3).  As $\Phi$ is positive, it is a $*$-map, and so $a\in A_\Phi$ implies that $a^*\in A_\Phi$.  If both $\Phi(a^*a) = \Phi(a)^*\Phi(a)$ and $\Phi(aa^*)=\Phi(a)\Phi(a)^*$
then by (2) we know that $\Phi(ba)=\Phi(b)\Phi(a)$ and $\Phi(ab)=\Phi(a)\Phi(b)$ for each $b\in A$.  Hence, given $a,b\in A_\Phi$ we have
> \[ \Phi((ab)^*ab) = \Phi(b^*a^*a) \Phi(b) = \Phi(b^*a^*) \Phi(a) \Phi(b) = \Phi((ab)^*) \Phi(ab), \]
> using that $b\in A_\Phi$, then that $a\in A_\Phi$, and then that $b\in A_\Phi$.  Similarly, $\Phi((ab)(ab)^*) = \Phi(ab)\Phi((ab)^*)$ and so $ab\in A_\Phi$.  As $\Phi$ is continuous, it is easy to see that $A_\Phi$ is closed, hence a $C^*$-subalgebra of $A$.  We have already shown that $\Phi$ restricted to $A_\Phi$ is a $*$-homomorphism.

We can now prove our abstract commutation result.

> **Proposition:** Let $\Phi:A\rightarrow A$ be completely positive, and suppose there is a faithful state $\varphi\in A^*$ with $\varphi\circ\Phi = \varphi$.  The collection of fixed points of $\Phi$ (those $a\in A$ with $\Phi(a)=a$) forms a $C^*$-subalgebra of $A_\Phi$.

> _Proof:_ Given $a\in A$ with $\Phi(a)=a$, also $\Phi(a^*)=a^*$, by the Schwarz Inequality, $a^*a \leq \Phi(a^*a)$, and so $\Phi(a^*a)-a^*a\geq 0$, but also $\varphi( \Phi(a^*a)-a^*a ) = 0$, and so as $\varphi$ is faithful, $\Phi(a^*a) = a^*a$.  As $a^*$ is also fixed by $\Phi$, also $\Phi(aa^*) = aa^*$.  Hence $a\in A_\Phi$.  Given $a,b$ fixed, also $a^*$ is fixed, and $\Phi(ab) = \Phi(a)\Phi(b)$ because $a,b\in A_\Phi$, so $\Phi(ab)=ab$.  We conclude that the fixed points form a $C^*$-subalgebra of $A_\Phi$.

A Cesaro mean arguments shows that if $\Phi$ is unital, there is always some invariant state.  However, without there being a _faithful_ invariant state, the collection of fixed points can fail to be an algebra.  For example, let $A=\mathbb C^3$ with the pointwise product, let $\Phi$ be the linear map with matrix form
\[ \begin{pmatrix} 1/4 & 1/4 & 1/2 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \]
This is positive, hence completely positive (as $A$ is abelian), but for example, the vector $(1,-1,2)^T$ is fixed while its square $(1,1,4)^T$ is not.

> **Proposition:**  Let $\Phi:A\rightarrow A$ be completely positive and unital, and suppose there is a faithful state $\varphi\in A^*$ with $\varphi\circ\Phi = \varphi$.  Let $(\pi,K,V)$ be a minimal dilation of $\Phi$.  Then $a\in A$ is fixed by $\Phi$ if and only if $\pi(a)V = Va$.

> _Proof:_ If $\pi(a)V=Va$ then $\Phi(a) = V^*\pi(a)V=V^*Va=a$, as $V^*V=1$ as $\Phi$ is unital.  Conversely, by the above, we know that if $\Phi(a)=a$ then $a\in A_{\Phi}$ so $\Phi(ba)=\Phi(b)\Phi(a) = \Phi(b)a$ for each $b\in A$.  For $\xi,\eta\in H$,
> \[ (\pi(b) V \eta | \pi(a) V \xi) = (\eta | \Phi(b^*a) \xi) = (\eta | \Phi(b^*)a\xi) = (\pi(b)V\eta | Va\xi). \]
> (Here I write my inner-products linear on the right.)  By minimality, vectors of the form $\pi(b)V\eta$ are linearly dense, and so we conclude that $\pi(a)V\xi = Va\xi$, that is, $\pi(a)V = Va$ as claimed.

If $(\pi',K',V')$ is another dilation, not assumed minimal, then there is always a unitary $u:K' \rightarrow K'$ which intertwines $\pi$ and $\pi'$, and satisfies $uV = V'$.  (Use that $(\pi,K,V)$ is minimal, and check that $u : \pi(a)V\xi \mapsto \pi'(a)V'\xi$ extends by linearity to a well-defined isometry.)  Then $\pi'(a)V' = u \pi(a)V = uVa = V'a$ if $a$ is fixed (and $\Phi$ satisfies our hypotheses).

Now come back to a quantum channel $\Phi:\mathbb M_n \rightarrow \mathbb M_n$ (so $\Phi$ is completely positive and trace-preserving).  As the trace is invariant (and can be normlised to a state!) our proposition applies.  To make a link with Kraus operators, we need to recall what the Stinespring representation looks like in this case.  Any $*$-representation $\pi:\mathbb M_n\rightarrow\mathcal B(K)$ has the form $\pi(a)=a\otimes 1$ where $K\cong\mathbb C^n \otimes H$ for some auxiliary Hilbert space $H$.  Let $(e_i)$ be an orthonormal basis for $H$, so $V:\mathbb C^n\rightarrow K = \mathbb C^n\otimes H$ has the form $V\xi = \sum_i A_i\xi \otimes e_i$ for some matrices $(A_i) \subseteq \mathbb M_n$ with $1 = V^*V = \sum_i A_i^*A_i$.  Then $\Phi(a) = V^*(a\otimes 1)V = \sum_i A_i^* a A_i$ gives the Kraus form (here I adopt a convention that privilages UCP maps).  That $\Phi$ is trace-preserving means that $\sum_i A_i A_i^* = 1$ as well.  (Notice that any _minimal_ dilation will have $K$ finite-dimensional, so $H$ will also be finite-dimensional, and all sums will be finite.)

> **Theorem:** Let $\Phi:\mathbb M_n\rightarrow\mathbb M_n$ be a unital quantum channel with Kraus representation $\Phi(x) = \sum_a A_a x A_a^*$.  Then $\Phi(x)=x$ if and only if $A_a x = x A_a$ for each $a$.

> _Proof:_ From the proposition above and the discussion after, $\Phi(x)=x$ if and only if $\pi(x)V=Vx$ for any Stinespring dilation $(\pi,K,V)$.  Such a dilation is given by $\pi(x)=x\otimes 1$ on $K=\mathbb C^n\otimes K'$ and $V\xi = \sum_a A_a^*(\xi)\otimes e_a$ where $(e_a)$ is an orthonormal basis of $K'$.  Then $\pi(x)V=Vx$ if and only if $A_a^* x = x A_a^*$ for each $a$, which is equivalent to $A_a x^* = x^* A_a$ for each $a$.  As $\Phi(x)=x$ if and only if $\Phi(x^*)=x^*$, the claim follows.

So we have our more abstract proof.