---
title: Sets and Structures
date: '2016-12-01T11:24:20+04:00'
lastmod: '2016-12-08T11:52:30+04:00'
original_id: '{A574}'
original_name: settheory
original_blob: blob/B/5/067.txt
revisions: 12
author: admin
last_editor: admin
tags:
- math
categories:
- math
wikislug: settheory
draft: false
topics:
- foundations
---

[Math](math.md) | [Abstract Algebra](abstractalgebra.md) | [ZF Axioms](zf.md) |
[Set Theory](settheory.md) |
[Number Theory](numbertheory.md)}
[Groups](groups.md) |
[Quotient Groups](quotientgroups.md) |
[Rings](rings.md) |
[Commutative Rings](commutativerings.md) |
[Fields](fields.md) |
[Group Actions](group.md) |
[Modules](modulesalegbra.md) |
[Vector Spaces](vectorspaces.md) |
[Linear Operators and Matrices](linearoperators.md) |
[Inner Product Spaces](innerproductspaces.md) |
[Tensors](tensors.md) |
[Exterior Algebras](exterioralgebras.md) |
[Theory](galois.md "MISSING PAGE") |
[Polynomial Rings](multivariable.md "MISSING PAGE") |
[Category Theory](categorytheory.md) |

![math-800](/assets/math-800.jpg)
{.center}

# [Sets and Structures](settheory.md)

Set Theory is the **[Machine Language](machinelanguage.md "MISSING PAGE")** of mathematics. It's a very low
level language, close to the machine, so to speak. In set theory with define really primitive
operations on even more primitive types data. Set theory in a way isn't as illuminating as
high level mathematics but in another way, it is the light that makes all of math possible.

When I first came across set theory I found it really quite a strange thing. I couldn't quite
wrap my head around why it was there at all, why the symbols looked so weird and what the
fuss was about at all. I had no teachers, just some books and the internet at large. It was
a mess.

I hope that in the following pages I can do something to reduce the mess. Although I suspect
that like everyone else, I will just be adding to it.

### What Sets do

There are going to be parts of this site which are rigorous and parts that are not,
parts that are more explanatory, especially from the viKid sense of view. So bear
with me here.

You will find the Zermelo-Frankel Axioms of Set theory below. Which are great, a
rigorous foundation that is good to understand but yet, on looking at them again
utterly lifeless.

What I want to do here is explain the need for set theory at all. I want to understand
why we need such a theory.

The point of set theory, the whole point of set theory in my opinion is that it
**studies the idea of what 'an idea' is.**

It is the ontological basis for all ideas in terms of themselves. It is recursive like
most modern theories, but its importance is greater than that.

In set theory. An idea is defined by **the contents of the idea and nothing else.**

Both parts are important, 1. the contents and 2. nothing else.

Let me repeat. An idea is its contents and **nothing else**.

So what happens when we have only nothing, that is, no contents.

This is the special case, the root of all set theory. It is called the **empty set**.

Otherwise represented as {}

- [Zermelo-Frankel Axioms](zf.md)

### What Structures are and what they do

Structures are essentially Sets with **Rules**. The rules, often called
**operations** allow us to transform (or create) one set into another.

For example, the **+** operator is one such rule.

1 + 1 = 2.

All we have done here is operate on a set (1) and produced another (2).

And yes, in set theory, numbers are sets themselves.

And what are these Rules? Well they are sets too! So in many senses, structures
are the study of how sets interact to produce new sets.

Or how ideas interact to produce new ideas. This is genesis, it mathematics.

### Why it matters: a short history

Set theory was born in the 1870s when Georg Cantor, studying Fourier series, needed to talk about infinite collections of points. He found something nobody expected: **there are different sizes of infinity.** Then, around 1901, Bertrand Russell found a crack in the naive version. Consider the set of all sets that are not members of themselves, \(R = \{x : x \notin x\}\). Is \(R\) a member of itself? If it is, it isn't; if it isn't, it is. Mathematics had a contradiction in its basement.

The repair, by Ernst Zermelo (1908) and later Abraham Fraenkel and others, was the [Zermelo-Fraenkel axioms](zf.md): careful rules about which sets you are allowed to build. Usually with the Axiom of Choice added (ZFC), they are the standard foundation on which nearly all of mathematics can, in principle, be written down.

### An everyday analogy: bags

Think of a set as a bag. What matters is what's inside, not the order or how many times you wrote it down: \(\{1, 2\} = \{2, 1\} = \{1, 1, 2\}\). Bags can contain other bags. And the empty bag \(\{\}\) is still a bag, which is the thing to notice, because a bag containing an empty bag, \(\{\{\}\}\), is *not* empty. It has one thing in it.

### A worked example: building numbers from nothing

Here is the "genesis" promised above, made precise by John von Neumann. Start with only the empty set and define

$$ 0 = \{\}, \quad 1 = \{0\} = \{\{\}\}, \quad 2 = \{0, 1\}, \quad 3 = \{0, 1, 2\}, \;\dots $$

Each number is the set of all the numbers before it, so the number \(n\) has exactly \(n\) members. "Less than" becomes "is a member of": \(2 < 3\) because \(2 \in 3\). Out of nothing but the empty set and the rule "collect what you have so far", we get all the natural numbers. Pairs, fractions, real numbers and functions can then be built the same way, one layer at a time.

### A second example: there is no biggest infinity

The **power set** \(\mathcal{P}(A)\) is the set of all subsets of \(A\). For \(A = \{a, b\}\):

$$ \mathcal{P}(A) = \{\{\}, \{a\}, \{b\}, \{a, b\}\} $$

Two elements gave four subsets; in general \(n\) elements give \(2^n\). Cantor proved that even for infinite sets, \(\mathcal{P}(A)\) is always strictly bigger than \(A\). The proof is the famous diagonal trick: given any attempt to match each element \(x\) of \(A\) with a subset \(f(x)\), the subset \(D = \{x : x \notin f(x)\}\) cannot be anybody's match. (Notice it has the same shape as Russell's paradox. That is no coincidence.) So the natural numbers are infinite, the real numbers are a *bigger* infinity, and there is a bigger one again, forever.

Whether there is an infinity strictly between the naturals and the reals is the **Continuum Hypothesis**. Gödel (1940) and Paul Cohen (1963) showed that ZFC can neither prove nor disprove it. The axioms simply don't decide.

### Common misconceptions

- **"A set is a list."** Order and repetition don't count. \(\{1, 2, 2\}\) has two elements.
- **"The empty set is nothing."** It is something: a set with no members. There is exactly one of it.
- **"All infinities are the same size."** The naturals and the reals are provably different sizes.
- **"Mathematicians think in sets."** Mostly they don't, any more than programmers think in machine code. Set theory is the guarantee underneath, not the everyday language.

### How it connects

- [ZF Axioms](zf.md): the formal rules.
- [Set Relations](setrelations.md), [Reflexivity](reflexivityrelation.md), [Symmetry](symmetryrelation.md) and [Transitivity](transitivityrelation.md): relations are themselves sets of pairs.
- [Logic](logic.md): "and", "or", "not" correspond to intersection, union and complement.
- [Groups](groups.md) and [Abstract Algebra](abstractalgebra.md): sets with structure.
- [Category Theory](categorytheory.md): the main alternative point of view.

The truth revealed: you can build all of mathematics from an empty bag, provided you are careful about which bags you are allowed to make.

## [Set Relations](setrelations.md)

## Source, Links & Reading Lists

- [Topic List @ Wikipedia](https://en.wikipedia.org/wiki/List_of_set_theory_topics)
- [A Bunch of Set Theory and a Bit of Logic by Ronald Garcia](https://www.cl.cam.ac.uk/teaching/1011/L21/6%20-%20Sets.pdf)
- [Metamath](http://us.metamath.org/index.html)
- [Modus Ponens & Tollens](https://www.cs.ucsb.edu/~pconrad/cs40/lessons/logic/modusPonensModusTollens.html)
- [Affirming the Consequent @ Wikipedia](https://en.m.wikipedia.org/wiki/Affirming_the_consequent)
