---
layout: post
title: Spectral bounds on the chromatic number
latex
---

Recently [Clive Elphink](https://www.researchgate.net/profile/Clive-Elphick-2) gave us a nice seminar where he discussed some of his "conjectures in spectral graph theory".  Clive has an interesting history: after a career in business, he is now semi-retired and returned to research mathematics.  By his own admission, he is more on the experimental side, and his talk said almost nothing about proofs.  Here is a old result in this area:

> **Theorem [Hoffman]:** We have that $\chi(G) \geq 1 + \frac{\lambda_1}{-\lambda_n}$.

I explain the notation shortly, but in words, this result relates a vertex colouring of a graph to the eigenvalues of the adjacency matrix.  To me, this seems hugely surprising, as why would the spectrum of $A$ have anything to do with a vertex colouring?  I want to explain the elegant arguments of Elphick and Wocjan, and also some generalisations to quantum colourings (in part 2).

<!--more-->

### The setup

Let us set the scene.  Here a [_graph_](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)) is $G=(V,E)$ where $V$ is a finite set of vertices, and $E$ is a set of undirected edges.  We disallow loops, and between a pair of vertices there can be at most one edge, so our graph is _simple_.  Often we write $u\sim v$ to indicate there is an edge between vertices $u$ and $v$.  Set $n=|V|$ and $m=|E|$; sometimes we identify $V$ with $[n]=\{1,2,\cdots,n\}$.  A [_colouring_](https://en.wikipedia.org/wiki/Graph_coloring) of $G$ is an assignment $f:V\rightarrow[c]$ such that $u\sim v \implies f(u)\not=f(v)$, that is, adjacent vertices are coloured distinctly.  The minimal $c$ we can choose is the _chromatic number_ $\chi(G)$.

The [_adjacency matrix_](https://en.wikipedia.org/wiki/Adjacency_matrix) of $G$ is $A=A_G$, the $\{0,1\}$-valued matrix indexed by $V\times V$ with $A_{u,v}=1$ if and only if $u\sim v$.  As $G$ is undirected, $A$ is symmetric/hermitian, and so has real eigenvalues and a complete set of orthogonal eigenvectors.  Let $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$ be the eigenvalues listed in non-increasing order.

> **Lemma:** If $G$ is non-trivial, then $\lambda_1>0$.  Further, $\sum_i \lambda_i=0$ and so $\lambda_n < 0$.

> _Proof:_ Let $(e_u)$ be the standard unit vector basis of $\mathbb C^V$, choose $u\sim v$, and set $\xi=e_u+e_v$.  Then $(\xi|A\xi) = A_{u,u} + A_{u,v} + A_{v,u} + A_{v,v} = 2$, so $-A$ is not positive.  Thus there must be some strictly positive eigenvector, so $\lambda_1>0$.

> The sum of the eigenvalues is the trace of $A$, which is $0$.

That $\lambda_1>0$ is also a consequence of the [Perron–Frobenius theorem](https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem).

### Colourings to matrix properties

As this is an informal writeup, I will not give precise references, but instead list some further reading at the end.  For now, I follow a couple of papers of Elphick and Wocjan.  The first hint of a link between colourings and matrices is the observation that given a colouring $f:V\rightarrow [c]$ (wlog every colour is used), we can permute the vertices to list them in colour order, that is, find $1=n_0 < n_1 < \cdots < n_{c-1} < n_{c}=n$ so that $f(u)=i$ exactly when $n_{i-1} \leq u < n_i$.  We partition the standard basis $(e_i)_{i=1}^n$ of $\mathbb C^n$ according to this partition, and hence view matrices in $\mathbb M_n$ as $c\times c$ block matrices.  As vertices which share a colour cannot be adjacent, if we view $A$ as such a block matrix, the diagonal blocks are all zero.
\[ A = \begin{pmatrix} 0_{n_1} & * & \cdots & * \\
* & 0_{n_2-n_1} & \vdots & * \\
\vdots & \ddots & \ddots & \vdots \\
* & * & \cdots & 0_{n-n_{c-1}}
\end{pmatrix} \]

Letting $P_i$ be the orthogonal projection on the $i$th block, that is, the span of $e_{n_{i-1}},\cdots,e_{n_i-1}$, we equivalently have that $P_i A P_i = 0$ for each $i\in [c]$.  This sort of operation has a name in [Quantum Information Theory (QIT)](https://en.wikipedia.org/wiki/Quantum_information).

### Pinchings and twirlings

> **Definition:** Let $(P_i)_{i=1}^c$ be orthogonal projections which sum to $1 \in \mathbb M_n$.  The operation
> \[ \mathcal C: \mathbb M_n\rightarrow \mathbb M_n; \quad
x\mapsto \sum_{i=1}^c P_i x P_i \]
> is called a _pinching_.

There is a seemingly unrelated operation using unitary matrices.

> **Definition:** Let $(U_i)_{i=1}^d$ be a collection of unitary matrices in $\mathbb M_n$.  The operation
> \[ \mathcal D: \mathbb M_n\rightarrow \mathbb M_n; \quad
x\mapsto \frac{1}{d} \sum_{i=1}^d U_i x U_i^* \]
> is called a _twirling_.

In fact, any pinching can be expressed as a twirling.  Let $(P_i)_{i=1}^c$ be orthogonal projections which sum to $1$ and let $\zeta$ be a $c^{\text{th}}$ root of unity (so $\zeta^c=1$ and $\zeta^k\not=1$ for $1\leq k < c$; e.g. we could have $\zeta = e^{2\pi i/c}$).  Set
\[ U = \sum_{k=1}^c \zeta^k P_k
\quad\implies\quad
U^*U = \sum_{k,l=1}^c \zeta^{-l} \zeta^k P_l P_k
= \sum_{k=1}^c \zeta^{k-k} P_k = 1, \]
and similarly $UU^*=1$, so $U$ is unitary.  Here we used that the projections are orthogonal and sum to $1$.  Similarly, that the projections are orthogonal shows that $U^t = \sum_{k=1}^c \zeta^{kt} P_k$.  For any matrix $x$,
\[ \mathcal D(x) = \frac1c \sum_{k=1}^c U^k x (U^*)^k
= \frac1c \sum_{k,t,s=1}^c \zeta^{k(t-s)} P_txP_s
= \sum_{t=1}^c P_txP_t = \mathcal C(x), \]
using that $\frac{1}{c} \sum_{k=1}^c \zeta^{kr} = \delta_{r,0}$.

### The proof

We can now prove Hoffman's bound.

> _Proof (of Hoffman's Theorem):_ As argued above, if $G$ admits a vertex colouring using $c$ colours then, after permuting the vertices, we can find "coordinate" projections $(P_i)_{i=1}^c$ such that the pinching of the adjacency matrix satisfies $\mathcal C(A)=0$.  (Here "coordinate projection" means a projection onto the span of some of standard unit vector basis elements $(e_i)_{i=1}^n$.)

> Form $U$ as above, so the twirling also satisfies $\mathcal D(A)=0$.  As $\zeta^c=1$ we see that $U^c = \sum_{k=1}^c P_k = 1$ and hence
> \[ \mathcal D(A)=0 \implies A = \sum_{k=1}^{c-1} U^k(-A)(U^*)^k. \]
> Let $v$ be a unit length eigenvector for the eigenvalue $\lambda_1$, so $(v|Av) = (v|\lambda_1 v) = \lambda_1$ while
> \[ \sum_{k=1}^{c-1} (v|U^k(-A)(U^*)^kv)
= \sum_{k=1}^{c-1} ( (U^*)^k v | (-A) (U^*)^k v )
\leq (c-1) \lambda_{\max}(-A), \]
> where $\lambda_{\max}(-A) = -\lambda_n$ is the greatest eigenvalue of $-A$.  Here we used that for each $(U^*)^k v$ is a unit vector, for any $k$.

> We have hence shown that $\lambda_1 \leq (c-1) (-\lambda_n)$ or equivalently, $c \geq 1 + \frac{\lambda_1}{-\lambda_n}$.  As $\chi(G)$ is the minimal choice for $c$, this establishes Hoffman's bound.

Many other spectral bounds on $\chi(G)$ can be established in a rather similar way; for details see the papers by Elphick and Wocjan listed below.

### References / Further reading

Bhatia, Rajendra
"Pinching, trimming, truncating, and averaging of matrices."
Am. Math. Mon. 107, No. 7, 602-608 (2000). [Zbl 0984.15024](https://zbmath.org/0984.15024)

Elphick, Clive; Wocjan, Pawel
"Spectral lower bounds for the quantum chromatic number of a graph."
J. Comb. Theory, Ser. A 168, 338-347 (2019). [Zbl 1421.05042](https://zbmath.org/1421.05042)

Elphick, Clive; Wocjan, Pawel
"An inertial lower bound for the chromatic number of a graph."
Electron. J. Comb. 24, No. 1, Research Paper P1.58, 9 p. (2017). [Zbl 1358.05104](https://zbmath.org/1358.05104)

Elphick, Clive; Wocjan, Pawel
"Unified spectral bounds on the chromatic number."
Discuss. Math., Graph Theory 35, No. 4, 773-780 (2015). [Zbl 1326.05080](https://zbmath.org/1326.05080)

Wocjan, Pawel; Elphick, Clive
"New spectral bounds on the chromatic number encompassing all eigenvalues of the adjacency matrix."
Electron. J. Comb. 20, No. 3, Research Paper P39, 18 p. (2013). [Zbl 1295.05112](https://zbmath.org/1295.05112)
