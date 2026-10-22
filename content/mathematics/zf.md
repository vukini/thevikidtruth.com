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

## Axiom of Union

```
  ∀x∃y ∀z z ∈ y ≡ (∃t z ∈ t ∧ t ∈ x)
```

Given any set **x**, there is a set **y** such that, for any element **z**,
**z** is a member of **y** if and only if there is a set **t** such that **z** is a member of **t** and **t** is a member of **x**.

## Axiom of Infinity

```
  ∃x∅ ∈ x ∧ [∀y (y ∈ x) → (y ∪ {y} ∈ x)]
```

## Axiom Scheme of Replacement

```
  B(u, v) ≡ [∀r(r ∈ v ≡ ∃s[s ∈ u ∧ A n (s, r)])]
```

```
  [∀x∃!yA n (x, y)] → ∀u∃v(B(u, v))
```

## Power Set Axiom

```
  ∀x∃y∀z[z ∈ y ≡ z ⊆ x]
```

## Axiom of Choice - An add on Axiom

For every,

```
  e ∈ C f (e) ∈ e.
```

```
  ∀C∃f∀e[(e ∈ C ∧ e = ∅) → f (e) ∈ e]
```
