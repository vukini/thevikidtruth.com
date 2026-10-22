---
title: The Zermelo-Frankel Axioms
date: '2016-07-29T11:44:02+04:00'
lastmod: '2016-11-29T12:05:38+04:00'
original_id: '{A230}'
original_name: zf
original_blob: blob/B/3/021.txt
revisions: 22
author: admin
last_editor: admin
tags:
- math
categories:
- math
wikislug: zf
draft: false
topics:
- foundations
---

# The Zermelo-Frankel Axioms

The ZF-Axioms are kind of a bed rock in Mathematics. A place where everything can
begin. Now this is not the only way to formalise mathematics. There many theories
around. I haven't got there yet. Category theory and Homeotopic type theory come to
mind here.

Now, let the caveat be stated here clearly.

**I am not a mathematician, I am not formally trained in the topic and I do
understand there may be errors here. If you are so disposed and would like to
free the Internet of error. Please let me know! I will be happy to be schooled in
this manner. What appears below is how I have understood the subject and it may
be helpful to you.**

## The plain idea

The ZF axioms are a short list of **rules for building sets**. They say which sets exist to begin with (an empty one, an infinite one) and which operations are allowed to make new sets from old ones (pairing, union, power set, picking out members). Anything you can't build with these rules, you are not allowed to assume exists.

## Why it matters

Around 1901 Bertrand Russell showed that "any collection you can describe is a set" leads to contradiction (the set of all sets that don't contain themselves). Zermelo's answer in 1908, refined by Fraenkel and Skolem in the 1920s, was to stop letting sets spring into being from any description and to *grow* them instead, carefully, from below. With the Axiom of Choice added the system is called **ZFC**, and it is the standard foundation of modern mathematics: practically every theorem you have ever met can, in principle, be written and proved inside it.

## An everyday analogy: a building code

Think of the axioms as a building code. You may build on the ground (the empty set). You may put two things in a box, empty boxes into a bigger box, and so on. You may not build a box that contains itself or that is "the box of all boxes". The code doesn't tell you what to build; it guarantees that whatever you build won't fall down.

## A worked example: making an ordered pair

Sets ignore order, \(\{a, b\} = \{b, a\}\), yet mathematics needs ordered pairs \((a, b)\) for coordinates and functions. Kuratowski's trick uses only Pairing:

$$ (a, b) = \{\{a\}, \{a, b\}\} $$

The element that appears in *both* inner sets is the first coordinate; the other is the second. Check: \((1, 2) = \{\{1\}, \{1, 2\}\}\) but \((2, 1) = \{\{2\}, \{1, 2\}\}\). Different sets, so order now matters. From ordered pairs come relations, functions, and eventually all of analysis. That is how a handful of austere axioms grow into mathematics.

Below are the axioms one by one, with my notes. A tidier modern statement of each is given in LaTeX after the original notation.

## Axiom of Extensionality

Means that any two sets with the **same members** is the **very same set.**

```
  ∀x∀y (∀z z ∈ x ≡ z ∈ y) ≡ (x = y)
```

Lets hold this true that for **every set x & y**, where for **all z** such that **z is member of x if & only if it
is also a member of y**, this is the same as saying **x = y**

## Axiom of the Empty Set

There is a set with no members.

```
  ∃x∀y y ∉ x
```

There exists a set **x** that for all **y**, **y** is **not a member** of **x**.

## Axiom of Unordered Pairs

From any **two sets x & y**, we can **construct a set** that contains both **x & y**.

The notation for that set is {x,y}.

```
  ∀x∀y ∃z ∀w w ∈ z ≡ (w = x ∨ w = y)
```

This says for **every pair of sets x & y** there exists a set **z** (for all **w**) that contains x and y
and no other members. Here **w** act like a dummy variable, it cannot equal anything but **x or y**.

## Axiom Schema of Separation

*(This one was missing from my original list.)* Given any set \(A\) and any property \(\varphi\), the members of \(A\) that have the property form a set:

$$ \forall A\,\exists B\,\forall x\,\big(x \in B \Leftrightarrow (x \in A \land \varphi(x))\big) $$

This is exactly the fix for Russell's paradox. You may not form "the set of all \(x\) such that \(\varphi(x)\)"; you may only **cut out** a subset from a set that already exists. Example: from the natural numbers, separate the even ones.


## Axiom of Union

```
  ∀x∃y ∀z z ∈ y ≡ (∃t z ∈ t ∧ t ∈ x)
```

Given any set **x**, there is a set **y** such that, for any element **z**,
**z** is a member of **y** if and only if there is a set **t** such that **z** is a member of **t** and **t** is a member of **x**.

In plain words: you can empty all the boxes inside a box onto one table. If \(x = \{\{1, 2\}, \{2, 3\}\}\), then \(\bigcup x = \{1, 2, 3\}\). Together with Pairing this gives the familiar \(A \cup B = \bigcup \{A, B\}\).


## Axiom of Infinity

```
  ∃x∅ ∈ x ∧ [∀y (y ∈ x) → (y ∪ {y} ∈ x)]
```

$$ \exists x\,\big(\varnothing \in x \land \forall y\,(y \in x \Rightarrow y \cup \{y\} \in x)\big) $$

There is a set that contains the empty set and, whenever it contains \(y\), also contains the "next" set \(y \cup \{y\}\). That is precisely the von Neumann construction \(0, 1, 2, 3, \dots\) from [Set Theory](settheory.md). Every other axiom only builds finite things from finite things; this is the one place infinity is simply *declared* to exist.


## Axiom Scheme of Replacement

```
  B(u, v) ≡ [∀r(r ∈ v ≡ ∃s[s ∈ u ∧ A n (s, r)])]
```

```
  [∀x∃!yA n (x, y)] → ∀u∃v(B(u, v))
```

The notation above got garbled in my notes. Cleanly: if a formula \(\varphi(x, y)\) defines a function (each \(x\) has exactly one \(y\)), then the image of any set under it is a set:

$$ \forall x\,\exists! y\,\varphi(x, y) \;\Rightarrow\; \forall u\,\exists v\,\forall y\,\big(y \in v \Leftrightarrow \exists s\,(s \in u \land \varphi(s, y))\big) $$

In plain words: if you can replace each member of a set by something else according to a rule, what you get is still a set. Replacement is Fraenkel's main addition, and it is needed to build very large sets such as \(\{\mathbb{N}, \mathcal{P}(\mathbb{N}), \mathcal{P}(\mathcal{P}(\mathbb{N})), \dots\}\).


## Power Set Axiom

```
  ∀x∃y∀z[z ∈ y ≡ z ⊆ x]
```

For every set there is a set of all its subsets, \(\mathcal{P}(x)\). From a 3-element set you get 8 subsets. Cantor's theorem says \(\mathcal{P}(x)\) is always strictly bigger than \(x\), so this axiom is the engine that produces ever larger infinities.

## Axiom of Foundation (Regularity)

*(Also missing originally.)* Every non-empty set has a member that shares no members with it:

$$ \forall x\,\big(x \neq \varnothing \Rightarrow \exists y\,(y \in x \land y \cap x = \varnothing)\big) $$

Its main consequence: no set contains itself, and there are no infinite descending chains \(\dots \in x_2 \in x_1 \in x_0\). Every set is built up from the empty set in stages.


## Axiom of Choice - An add on Axiom

For every,

```
  e ∈ C f (e) ∈ e.
```

```
  ∀C∃f∀e[(e ∈ C ∧ e = ∅) → f (e) ∈ e]
```

A correction to my formula above: the condition should be that \(e\) is **non-empty**, otherwise there is nothing to choose:

$$ \forall C\,\Big(\varnothing \notin C \Rightarrow \exists f\,\forall e\,\big(e \in C \Rightarrow f(e) \in e\big)\Big) $$

Given any collection of non-empty sets, there is a function that picks one element from each. Bertrand Russell's illustration: from infinitely many pairs of shoes you can choose one from each pair with a rule ("take the left one"), but for infinitely many pairs of socks you need the axiom. Choice is independent of ZF (Gödel 1938, Cohen 1963), and it has surprising consequences such as the Banach–Tarski paradox, which is why it is often flagged when used.

## Common misconceptions

- **"ZF is the only foundation."** It is the standard one, but type theories (used by Lean and Coq) and category-theoretic foundations are serious alternatives.
- **"The axioms are self-evident truths."** Some are (Extensionality); others, like Infinity and Choice, are choices that turned out to be useful.
- **"ZF proves it is consistent."** By Gödel's second incompleteness theorem it cannot, if it is consistent.
- **"Mathematicians check every proof against ZF."** In practice almost never, though proof assistants are making this increasingly possible.

## How it connects

- [Set Theory](settheory.md): the intuitive story these rules formalise.
- [Logic](logic.md): the axioms are written in first-order predicate logic.
- [Set Relations](setrelations.md): relations and functions are built from ordered pairs, as above.
- [Category Theory](categorytheory.md) and [Abstract Algebra](abstractalgebra.md): what gets built on top.

The truth revealed: the foundation of mathematics isn't a single certainty but a short, carefully chosen list of permissions.
