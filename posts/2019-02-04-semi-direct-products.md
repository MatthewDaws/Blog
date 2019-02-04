---
layout: post
title: Semi-direct products
latex
---

Motivated by some reading about quantum groups, I want to sketch how a semi-direct product of (topological)
groups is the same as having an idempotent group homomorphism.

Firstly, let's remember what the (external) [semi-direct product](https://en.wikipedia.org/wiki/Semidirect_product)
of groups is.  I will follow the notation of the book of [Kaniuth and Taylor](https://doi.org/10.1017/CBO9781139045391).
Let $N,H$ be (topological) groups, and denote by $\newcommand{\aut}{\operatorname{Aut}}\aut(N)$ the collection
of continuous group automorphisms of $N$.  Suppose we have a group homomorphism $\alpha:H\rightarrow\aut(N)$,
written as $h\mapsto \alpha_h$, which is continuous in the sense that $N\times H\rightarrow N;
(n,h)\mapsto \alpha_h(n)$ is continuous.

<!--more-->

Let $N \rtimes H$, the semi-direct product, be the topological space $N\times H$ equipped with the
group product
\[ (n,h)(m,g) = (n \alpha_h(m), hg). \]
It is easy to check that this is associate, that $(e,e)$ is the unit, and that $(n,h)^{-1} =
(\alpha_{h^{-1}}(n^{-1}), h^{-1})$.  Similarly, it is easy to check that the product and inverse
are continuous, so that $N \rtimes H$ becomes a topological group.

Let $\tilde N = \{(n,e) : n\in N\}$ and $\tilde H = \{(e,h):h\in H\}$.  These can be checked to be closed
subgroups of $N \rtimes H$ such that $\tilde N \cap \tilde H = \{e\}$ and $\tilde N\tilde H = N \rtimes H$.
For $(m,e)\in \tilde N$ and $(n,h)\in N \rtimes H$ we have that
\[ (n,h)(m,e)(n,h)^{-1} = (n\alpha_h(m), h)(\alpha_{h^{-1}}(n^{-1}), h^{-1})
= (n\alpha_h(m)n^{-1}, e), \]
which shows that $\tilde N$ is normal in $N \rtimes H$, and that $(\alpha_h(m),e)
= (e,h)(m,e)(e,h)^{-1}$, so that conjugation by $\tilde H$ in $N \rtimes H$ implements $\alpha$.

Conversely, suppose that $G$ is a topological group, with closed subgroups $N,H$, with $N$ normal,
$N\cap H=\{e\}$ and $G = NH$.  Define $\alpha:H\rightarrow\aut(N)$ by $\alpha_h(n) = hnh^{-1}$
for $h\in H, n\in N$.  As $N$ is normal, it follows that $\alpha$ makes sense, and
is a (continuous) group homomorphism.  Consequently, we can define $N \rtimes H$.  

Define $\theta:N \rtimes H\rightarrow G$ by $\theta(n,h)=nh$.  Then
\[ \theta(n,h)\theta(m,g) = nhmg = nhmh^{-1}hg = \theta(n\alpha_h(m), hg), \]
showing that $\theta$ is a group homomorphism.  By assumption, $\theta$ is onto, and if
$nh=e$ then $n = h^{-1} \in N\cap H$ so $n=h=e$, so $\theta$ is a bijection.  Thus $G$ is
isomorphic to $N \rtimes H$.

We now show the (I think less common) link with idempotent group homomorphisms.  With $G,N,H$ as
before, for $g\in G$ we can write $g=nh$.  This decomposition is unique, either by the above
map $\theta$, or by observing that if $nh=mg$ then $m^{-1}n = gh^{-1} \in N\cap H$ so
$m^{-1}n=e$ and $gh^{-1}=e$ so $n=m, g=h$.  Define $\phi : N \backslash G \rightarrow H$ by
$\phi(Ng) = h$ when $g=nh$ for some $n\in N$.  Notice that $g=nh$ for some $n\in N$ is equivalent
to $Ng = Nh$.  Then $\phi(Nh) = h$ for $h\in H$ so $\phi$ is
onto, and if $\phi(gN) = e$ then $g\in N$ so $gN=N$.  As $N$ is normal, of course $Ng_1 Ng_2
= N g_1 g_1^{-1}Ng_1 g_2 = N g_1g_2$.  Let $\phi(Ng_1)=h_1$ and $\phi(Ng_2)=h_2$, so that
$Ng_1=Nh_1$ and $Ng_2=Nh_2$, so $Ng_1g_2 = Ng_1 Ng_2 = Nh_1 Nh_2 = Nh_1h_2$.  Thus $\phi$
is a group isomorphism.  To argue that $\phi$ is continuous seems a little tricky, but it
follows rather easily if you view $G$ as being isomorphic to $N \rtimes H$.

Now let $p$ be the composition
\[ G \twoheadrightarrow N \backslash G \cong H \hookrightarrow G \]
which is a (continuous) group homomorphism.  Thus $p(g)=h\in H$ if and only if
$h = \phi(Ng)$, that is, $Nh=Ng$ or equivalently, $gh^{-1} \in N$.
Thus $p(h)=h$ for any $h\in H$, so the image of $p$ is $H$, and the kernel of $p$ is $N$.
In particular, $p\circ p=p$.

Conversely, let $G$ be a topological group, and let $p$ be a continuous group homomorphism
from $G$ to $G$, with $p\circ p =p$.  Let $N=\ker p$, a closed normal subgroup of $G$,
and let $H$ be the image of $p$, a subgroup.  As $p\circ p=p$ and $p$ is continuous, it
follows that $H$ is closed.  If $g\in N\cap H$ then $p(g)=e$ and $p(g)=g$, so $N\cap H=\{e\}$.
For $g\in G$, let $n = g p(g)^{-1} = gp(g^{-1})$ so $p(n) = p(g) p(g^{-1})
= p(g)p(g)^{-1} = e$.  Thus $g = n p(g) \in NH$.

Thus the semi-direct product construction is exactly captured by the notion of a group
with an idempotent group homomorphism.
