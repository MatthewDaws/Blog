---
layout: post
title: Polar decomposition of functionals
latex
---

A well-known fact from the basic theory of von Neumann algebras is the polar decomposition of
normal functionals: given $\newcommand{\ip}[2]{\langle #1, #2 \rangle}$
$\varphi\in M_{&ast;} $ there is $\omega\in M_{&ast;}^+$ and a partial isometry $v\in M$
with $\varphi = v\omega$.  If $v^* v$ is equal to the support of $\omega$, then this decomposition is unique, and we write $|\varphi|$ for $\omega$.

I am mostly following [Takesaki's book](https://books.google.co.uk/books/about/Theory_of_Operator_Algebras_I.html?id=dTnq4hjjtgMC&redir_esc=y)
here; but the material is also nicely presented in a the [MSc thesis of Zwarich](https://uwspace.uwaterloo.ca/handle/10012/3920).
Neither of these sources quite gives a correct proof (IMHO) so I thought I would record here the main
steps in proving existence.

<!--more-->

We shall need two lemmas, which are Chapter III, Lemma 3.2 and Lemma 4.1 in Takesaki, and 2.12.1 and 3.6.1 in Zwarich.

> **Claim 1:** Let $A$ be a $C^{&ast;}$-algebra and let $\omega\in A^* $.  If there is
$a\in A^+$ with $\|a\|\leq 1$ and $\ip{a}{\omega} = \|\omega\|$, then $\omega\geq 0$

> **Claim 2:** Let $M$ be a von Neumann algebra, and let $\omega\in M_*$.  If $e\in M$
if a projection with $\|e\omega\| = \|\omega\|$ then $e\omega =\omega$.

We can now proceed with the existence part of the proof.
By Hahn-Banach, there is $a\in M$ of norm one with $\|\varphi\| = \ip{a}{\varphi}$.
Let $a^{&ast;} = u|a^{&ast;} |$ be the polar decomposition of $a^{&ast;} $.  Thus $u^{&ast;} a^{&ast;} = |a^{&ast;} |$ and $e=uu^{&ast;} $ is the projection onto the closure of the image of $a^{&ast;} $.  Define $\omega = u^{&ast;} \varphi$.

Then $u\omega = uu^{&ast;} \varphi = e \varphi$.  Also $ea^{&ast;} = u|a^{&ast;} | = a^{&ast;}$ so $ae = a$.
Thus we have that
\[ \|\varphi\| = \ip{a}{\varphi} = \ip{ae}{\varphi} = \ip{a}{e\varphi}
\leq \|e\varphi\| \leq \|\varphi\|, \]
and so there is equality throughout, which implies that $\|e\varphi\| = \|\varphi\|$.
By Claim 2, $\varphi = e\varphi = u\omega$.

We now observe that
\[ \|\varphi\| = \ip{a}{\varphi} = \ip{|a^{&ast;} |u^{&ast;} }{\varphi} = \ip{|a^{&ast;} |}{\omega}
\leq \|\omega\| = \|u^{&ast;} \varphi\| \leq \|\varphi\|, \]
so again we have equality, and hence $\ip{|a^{&ast;} |}{\omega} = \|\omega\|$.
From Claim 1 we conclude that $\omega$ is positive.

Finally, as $u^{&ast;} u \omega = u^{&ast;} u u^{&ast;} \varphi = u^{&ast;} \varphi = \omega$ we have that
$u^{&ast;} u \geq s(\omega)$, the support projection of $\omega$.  Setting
$v = us(\omega)\in M$ we have that $v$ is a partial isometry, because
\[ v^{&ast;} v v^{&ast;} = s^{&ast;} u^{&ast;} u s s^{&ast;} u^{&ast;} =
s^{&ast;} s s^{&ast;} u^{&ast;} = s u^{&ast;} = v^{&ast;}, \]
where I have written $s=s(\omega)$.
Also $v\omega = us(\omega)\omega = u\omega = \varphi$, and finally
$v^{&ast;} v = s u^{&ast;} u s = s = s(\omega)$ as required.

Writing out $C^{&ast;}$-algebra theory in markdown is a pain...
