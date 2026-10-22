---
title: Mathematics on Computers
date: '2016-11-29T11:16:47+04:00'
lastmod: '2016-12-10T23:02:18+04:00'
original_id: '{A474}'
original_name: mathoncomputers
original_blob: blob/B/5/171.txt
revisions: 9
author: admin
last_editor: admin
tags:
- math
categories:
- math
wikislug: mathoncomputers
draft: false
topics:
- math-physics
---

[Abstract Algebra](abstractalgebra.md) | [ZF Axioms](zf.md) | [Math on Computers](mathoncomputers.md)

![math-800](/assets/math-800.jpg)
{.center}

# Mathematics on Computers

[MathJax](https://www.mathjax.org)
[typeit math!](http://math.typeit.org)

∀(x, y ∈ A ∪ B; x ≠ y) x² − y² ≥ 0

### The plain idea

Computers do mathematics in four very different ways, and most confusion comes from mixing them up:

1. **Typesetting** – making maths *look* right on a page or screen (LaTeX, MathJax, the line of symbols above).
2. **Numerical computing** – crunching approximate numbers very fast (NumPy, MATLAB, Julia, a spreadsheet).
3. **Symbolic computing** – manipulating exact expressions the way you would on paper: \(\frac{d}{dx}\sin x = \cos x\), \(\sqrt{8} = 2\sqrt{2}\) (SageMath, SymPy, Maxima, Mathematica).
4. **Proof checking** – verifying, line by line, that a proof is correct (Lean, Coq/Rocq, Isabelle).

### Why it matters

A modern mathematician, physicist or engineer uses all four, often in the same afternoon. Numerical computing put men on the Moon and forecasts tomorrow's weather. Symbolic systems take the drudgery out of algebra. And proof assistants are quietly changing what counts as certain: in 2005 Georges Gonthier formally verified the Four Colour Theorem in Coq, and Lean's community library, Mathlib, now holds a very large and growing body of formalised mathematics. Since 2024 AI systems have joined in too, with Google DeepMind's AlphaProof reaching silver-medal standard at the International Mathematical Olympiad in 2024 and AI models reaching gold-medal standard in 2025.

### An everyday analogy: calculator versus algebra teacher

A pocket calculator tells you \(\sqrt{2} \approx 1.41421356\). An algebra teacher tells you \(\sqrt{2} \times \sqrt{2} = 2\) *exactly*. Numerical software is the calculator; symbolic software is the teacher; a proof assistant is the examiner who refuses to let you skip a single step.

### A worked example: why 0.1 + 0.2 isn't 0.3

Ask almost any programming language:

```python
>>> 0.1 + 0.2
0.30000000000000004
```

This is not a bug. Computers store numbers in binary floating point (the IEEE 754 standard), and \(0.1\) in binary is an endless repeating fraction, just as \(\tfrac13 = 0.333\ldots\) is in decimal. The machine keeps 53 binary digits and rounds, so tiny errors appear. Now ask Sage or SymPy with exact rationals:

```python
>>> from fractions import Fraction
>>> Fraction(1, 10) + Fraction(2, 10)
Fraction(3, 10)
```

Exact. The lesson: numerical answers are fast and approximate; symbolic answers are exact and slower. Know which one you are holding, especially with money (banks use decimal or integer cents for this reason).

## Sage

I am currently experimenting on [Sage](http://www.sagemath.org/). Sage is primarily written in [Python](python.md).
Which I will now need to get familiar with.

```
   Sage is free, open-source math software that supports

   research and teaching in algebra, geometry, number theory, cryptography,
   numerical computation, and related areas.
```

The main reason I want sage is so that I can run the server here on the site
serving up my mathematical requirements dynamically to you the reader.
[Sage Server Config](https://wiki.sagemath.org/SageServer)

An update: the public Sage server ("Sage notebook") route described above has been retired in favour of the **SageMathCell** service and Jupyter notebooks. Sage itself is very much alive (the 10.x series), runs inside Jupyter, and the simplest way to embed live computation on a page like this today is a SageMathCell widget or a hosted notebook. For display, this site uses MathJax, which renders \( \)-style inline maths and `$$` display maths in the browser.

### A taste of symbolic computing

In Sage (or Python with SymPy), exact answers come back as exact objects:

```python
sage: factor(x^4 - 1)
(x - 1)*(x + 1)*(x^2 + 1)
sage: integrate(sin(x)^2, x, 0, pi)
1/2*pi
sage: factor(30031)
59 * 509
```

That last line is the [Euclid example](numbertheory.md) from the number theory page, done in a millisecond.

### Common misconceptions

- **"Computers can't make maths mistakes."** They make rounding mistakes constantly, and software has bugs. Results you depend on should be checked a second way.
- **"Symbolic systems are always right."** They sometimes simplify under assumptions you didn't make, such as treating \(\sqrt{x^2}\) as \(x\) when \(x\) might be negative.
- **"Proof assistants make mathematicians obsolete."** They check proofs; humans still decide what is worth proving. AI tools are getting genuinely good at finding proofs too, but formal checking is what makes their output trustworthy.

### How it connects

- [Abstraction](abstraction.md): computing and mathematics as two towers of the same idea.
- [Abstract Algebra](abstractalgebra.md) and [Number Theory](numbertheory.md): the bread and butter of computer algebra systems.
- [Python](python.md): the glue language of modern scientific computing, and Sage's own language.
- [Computing](computing.md) for the rest of the machine.

The truth revealed: a computer doesn't know any mathematics. It follows rules extremely fast, and the art is knowing which rules you asked it to follow.

### Links

- [SageMath](https://www.sagemath.org) and [SageMathCell](https://sagecell.sagemath.org)
- [SymPy](https://www.sympy.org)
- [Lean and Mathlib](https://leanprover-community.github.io)
- David Goldberg, "What Every Computer Scientist Should Know About Floating-Point Arithmetic" (1991)
