---
title: Groups
date: '2016-12-07T06:46:59+04:00'
lastmod: '2016-12-07T06:46:59+04:00'
original_id: '{A726}'
original_name: groups
original_blob: blob/B/4/505.txt
revisions: 1
author: admin
last_editor: admin
tags:
- math
categories:
- math
wikislug: groups
draft: false
---

[Abstract Algebra](abstractalgebra.md) | [ZF Axioms](zf.md) | [Math](math.md)
[Set Theory](settheory.md) |
[Number Theory](numbertheory.md) |
[Groups](groups.md) |
[Quotient Groups](quotientgroups.md) |
[Rings](rings.md) |
[Commutative Rings](commutativerings.md) |
[Fields](fields.md) |
[Actions](group.md) |
[Modules](modulesalegbra.md) |
[Vector Spaces](vectorspaces.md) |
[Linear Operators and Matrices](linearoperators.md) |
[Inner Product Spaces](innerproductspaces.md) |
[Tensors](tensors.md) |
[Exterior Algebras](exterioralgebras.md) |
[Theory](galois.md "MISSING PAGE") |
[Polynomial Rings](multivariable.md "MISSING PAGE") |
[Category Theory](categorytheory.md) |



Here is a truth I wish someone had revealed to me much earlier: **a group is just the mathematics of "doing and undoing".**

That's it. That's the secret. Everything else is bookkeeping.

### The core idea, in plain words

A group is a [set](settheory.md) of *actions* (or things) together with one way of *combining* them, such that four rules hold:

1. **Closure** – combine any two and you get another member of the set. You never fall out of the club.
2. **Associativity** – \((a \cdot b) \cdot c = a \cdot (b \cdot c)\). Brackets don't matter, only the order of the things.
3. **Identity** – there is a "do nothing" element \(e\), with \(e \cdot a = a \cdot e = a\).
4. **Inverses** – every \(a\) has an "undo" \(a^{-1}\), with \(a \cdot a^{-1} = a^{-1} \cdot a = e\).

Notice what is *not* on the list: nobody promised that \(a \cdot b = b \cdot a\). When that extra rule does hold, the group is called **abelian** (after Niels Abel). Most interesting groups are not.

### An everyday analogy: the Rubik's cube

Pick up a Rubik's cube. Every twist is an element. Doing one twist after another is the combining. Holding it still is the identity. And every twist can be undone by twisting the other way. Do a long scramble and the cube is still a cube (closure). That's a group – a big one, with 43,252,003,274,489,856,000 elements, all living in your hand.

And try this: turn the top face, then the right face. Now reset and do right first, then top. Different cube. **Order matters.** The Rubik's group is not abelian.

### A small worked example: the clock with four hours

Take the numbers \(\{0, 1, 2, 3\}\) and add them "on a 4-hour clock" (add, then keep the remainder after dividing by 4). Mathematicians call this \(\mathbb{Z}_4\).

- Closure: \(3 + 2 = 5\), and \(5\) on a 4-hour clock is \(1\). Still in the set. ✔
- Identity: \(0\). ✔
- Inverses: \(1 \leftrightarrow 3\) (because \(1 + 3 = 4 \equiv 0\)), \(2 \leftrightarrow 2\), \(0 \leftrightarrow 0\). ✔
- Associativity: inherited from ordinary addition. ✔

The whole group fits in one table (its *Cayley table*):

| + | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 0 | 1 | 2 | 3 |
| **1** | 1 | 2 | 3 | 0 |
| **2** | 2 | 3 | 0 | 1 |
| **3** | 3 | 0 | 1 | 2 |

Look at it: every row and every column contains each element exactly once. That's no accident – it's what having inverses *forces*. (It's a little Sudoku, and it's true for every finite group.)

### A picture in words: spinning a square

Cut a square out of paper and lay it on the table. Which moves put it back on its own outline?

- Rotations by 0°, 90°, 180°, 270° – four moves. They behave *exactly* like the 4-hour clock: rotating 90° three times then once more gets you back to start, just as \(3 + 1 = 0\).
- Add the four flips (two across the diagonals, one horizontal, one vertical) and you get 8 moves in total, the group called \(D_4\).

Now the reveal: flip then rotate 90° is **not** the same as rotate 90° then flip. The clock and the square-of-rotations are the *same group wearing different clothes*. The word for "same group, different clothes" is **isomorphic**, and it is one of the most powerful ideas in all of maths: once you understand one, you understand every one of its disguises.

### Common misconceptions

- **"A group is a set of numbers."** No – it's a set *plus* an operation. The integers under addition are a group; the integers under multiplication are not (what would you multiply \(2\) by to get back to \(1\)? Not an integer).
- **"Order doesn't matter."** Only in abelian groups. Socks then shoes ≠ shoes then socks. And notice the undo: \((a \cdot b)^{-1} = b^{-1} \cdot a^{-1}\) – to undo "socks then shoes" you take off the shoes *first*.
- **"Any operation with an undo will do."** Associativity is a real requirement. Subtraction fails it: \((5 - 3) - 1 = 1\) but \(5 - (3 - 1) = 3\).
- **"The natural numbers under addition are a group."** No inverses: there is no natural number to add to \(3\) to get \(0\). You need the negative numbers – which is, historically, one reason we invented them.

### How it connects

- **Down** to [Set Theory](settheory.md): a group is a set with structure – exactly the "sets and structures" story.
- **Sideways** to [Set Relations](setrelations.md): equivalence relations chop a group into pieces called *cosets*, which leads straight to…
- **Up** to [Quotient Groups](quotientgroups.md) (squashing a group to see its shape), [Actions](group.md) (groups *doing things* to other objects – the square above is a group acting on a square), and [Rings](rings.md) and [Fields](fields.md), which are what you get when you allow *two* operations at once.
- **Out** into the world: symmetry in [Quantum Mechanics](qm.md) and [Relativity](relativity.md) is group theory. Galois used groups to prove there is no general formula for solving degree-5 polynomial equations.

The truth revealed: wherever you can *do* something and *undo* it, a group is hiding.
