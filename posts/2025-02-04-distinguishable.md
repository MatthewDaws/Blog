---
layout: post
title: Distinguishable 
latex
---

A little mathematics: I have claimed the following in a number of talks, hence perhaps a proof is called for.  Given two [Density Matrices](https://en.wikipedia.org/wiki/Density_matrix) $\rho_1, \rho_2$ (so positive-semidefinite, trace one matrices) we say that the associated quantum states are _distinguishable_ when $\newcommand{\Tr}{\operatorname{Tr}}\Tr(\rho_1 \rho_2) = 0$.  Let $T$ be a quantum channel; we are interested in when $T(\rho_1)$ and $T(\rho_2)$ are distinguishable.

**Claim:** $T(\rho_1)$ and $T(\rho_2)$ are distinguishable if and only if $\Tr\big(T(|\xi\rangle\langle\xi|) T(|\eta\rangle\langle\eta|) \big)=0$ for each $\newcommand{\im}{\operatorname{Im}}\xi \in \im(\rho_1)$ and $\eta \in \im(\rho_2)$.

<!--more-->

We can expand a density matrix $\rho_1$ as $\rho_1 = \sum_i |\xi_i \rangle \langle \xi_i|$ for some orthogonal family $(\xi_i)$ (this is just diagonalisation of positive matrices).

Similarly let $\rho_2 = \sum_j |\eta_j\rangle\langle\eta_j|$.  Then
\[ \Tr(T(\rho_1)T(\rho_2))=0
\quad\Leftrightarrow\quad
\sum_{i,j} \Tr\big( T(|\xi_i \rangle \langle \xi_i|) T(|\eta_j \rangle \langle \eta_j|) \big) = 0
\qquad\qquad (\dagger). \]
Given positive $x,y$ we see that $\Tr(xy) = \Tr(y^{1/2} x^{1/2} x^{1/2} y^{1/2}) = \Tr(z^*z) \geq 0$ say, where $z = x^{1/2} y^{1/2}$.  So each summand in the right-hand-side of $(\dagger)$ is positive, and hence $(\dagger)$ is equivalent to $\Tr\big( T(|\xi_i \rangle \langle \xi_i|) T(|\eta_j \rangle \langle \eta_j|) \big) = 0$ for each $i,j$.  This proves the "if" part of our claim, as each $\xi_i$ is in the image of $\rho_1$, and similarly for $\eta_j$.

Recall that $\rho_1$ and $\rho_1^{1/2}$ have the same image (diagonalise, for example).  Let $\xi \in \im(\rho_1)$, so $\xi = \rho_1^{1/2}(\xi')$ for some $\xi'$.  Then, for any $\psi$,
\[ (\psi | |\xi\rangle\langle\xi| \psi)
= (\psi|\xi)(\xi|\psi)
= (\psi|\rho_1^{1/2}(\xi')) (\rho_1^{1/2}(\xi')|\psi)
= (\rho_1^{1/2}(\psi)|\xi')(\xi'|\rho_1^{1/2}(\psi)). \]
Using Cauchy-Schwarz, this is
\[ \leq \|\xi'\|^2 \|\rho_1^{1/2}(\psi)\|^2
= \|\xi'\|^2 (\psi|\rho_1(\psi)). \]
This holds for all $\psi$ and so $|\xi\rangle\langle\xi| \leq \|\xi'\|^2 \rho_1$.  Set $k_1 = \|\xi'\|^2$.  Similarly, for $\eta\in\im(\rho_2)$ there is $k_2\geq0$ with $|\eta\rangle\langle\eta| \leq k_2 \rho_2$.  Then
\begin{align\*}
\Tr\big(T(|\xi\rangle\langle\xi|) T(|\eta\rangle\langle\eta|) \big)
&= \Tr\big(T(|\eta\rangle\langle\eta|)^{1/2} T(|\xi\rangle\langle\xi|) T(|\eta\rangle\langle\eta|)^{1/2} \big) \\\\
&\leq k_1 \Tr\big(T(|\eta\rangle\langle\eta|)^{1/2} T(\rho_1) T(|\eta\rangle\langle\eta|)^{1/2} \big) \\\\
&= k_1 \Tr\big(T(\rho_1)^{1/2} T(|\eta\rangle\langle\eta|) T(\rho_1)^{1/2} \big) \\\\
&\leq k_1 k_2 \Tr\big(T(\rho_1)^{1/2} T(\rho_2)) T(\rho_1)^{1/2} \big)
= k_1 k_2 \Tr\big( T(\rho_1) T(\rho_2) \big).
\end{align\*}
So, if $T(\rho_1)$ and $T(\rho_2)$ are distinguishable, then also $\Tr\big(T(|\xi\rangle\langle\xi|) T(|\eta\rangle\langle\eta|) \big)=0$, showing the "only if" part of the claim.

Notice that we only used that $T$ was positive (so preserves the semi-definite ordering).
