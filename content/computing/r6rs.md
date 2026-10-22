---
title: R6RS - Revision 6 Scheme Standard
date: '2016-12-04T00:07:05+04:00'
lastmod: '2016-12-04T01:26:49+04:00'
original_id: '{A632}'
original_name: r6rs
original_blob: blob/B/4/022.txt
revisions: 39
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: r6rs
draft: false
topics:
- lisp
---

### The plain idea

Scheme is a small, elegant dialect of [Lisp](commonlisp.md), prized for having very few rules that compose in very powerful ways. R6RS, the "Revised⁶ Report on the Algorithmic Language Scheme" (2007), is one of the formal standards defining what Scheme *is*. This page is my condensed, de-jargoned reading of that standard, an attempt to pull out the big ideas and skip the dense legalese.

### Why it matters

Scheme is the language of *Structure and Interpretation of Computer Programs* (SICP), the book that taught a generation to think about programming. Its design decisions, first-class functions, lexical scope, tail-call optimisation, continuations, hygienic macros, are not quirks; they are some of the deepest ideas in programming, presented in their clearest form. Understanding Scheme makes every other language easier to understand, because you see which of their features are essential and which are decoration.

### An everyday analogy

Scheme is like a set of a few perfect LEGO bricks. Other languages hand you a giant box of specialised pre-built pieces; Scheme hands you a handful of simple, beautifully made bricks and shows that *everything else can be built from them*. Loops, objects, exceptions, even new control structures, are not built in; you construct them from procedures and a few primitives.

### A worked example: tail recursion as a loop

One of the headline ideas in my notes is that **tail-recursive calls are "gotos that pass arguments"**. In most languages a function calling itself repeatedly eventually overflows the stack. In Scheme, a call in *tail position* (the last thing a function does) reuses the current stack frame, so recursion becomes a loop with no memory cost:

```scheme
(define (count-down n)
  (if (= n 0)
      'done
      (count-down (- n 1))))   ; tail call: no stack growth

(count-down 1000000)           ; -> done, uses constant memory
```

This is why Scheme needs no separate `for` or `while` keyword: proper tail calls make plain recursion *as efficient as* a loop. That single guarantee reshapes how you write everything.

### A 2026 note

R6RS was controversial for being large and was followed by the deliberately smaller **R7RS** (2013), which split Scheme into a minimal "small" language and a richer "large" standard; R7RS is what most newer implementations target today. Popular Schemes include **Racket** (which grew its own ecosystem beyond Scheme), **Chez Scheme** (fast, now open source), **Guile** (GNU's extension language) and **Chicken**. The ideas in these notes are common to all of them.

### Common misconceptions

- **"Scheme is just a teaching toy."** Its ideas power real systems, and implementations like Chez and Racket are production-grade.
- **"Lisp and Scheme are the same."** Scheme is a Lisp, but minimalist and with a single namespace for functions and values (a "Lisp-1"), unlike [Common Lisp](commonlisp.md).
- **"Parentheses make it unreadable."** The uniform `(operator operands...)` syntax is what makes code and data the same thing, enabling Scheme's famous macros.

### How it connects

- [Common Lisp](commonlisp.md) and [PicoLisp](picolisp.md): the wider Lisp family.
- [Functional Programming](functional.md): Scheme is a cornerstone of the style.
- [The Compiler](thecompiler.md): continuations and tail calls are deep compiler topics.


[Read This!](caveatemptor.md) |
  [Scheme](scheme.md) |
  [Picolisp](picolisp.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |

# [R6RS - Revision 6 Scheme Standard](r6rs.md)

**The following are my notes on the standard, which I have pretty much lifted of the standard itself. The aim is to:**
 
- Reduce both the jargon and overall text size
- To clarify difficult issues or parts of the text which seem ambiguous

## Notes

- First-class procedures (lambda calculus) prove the usefulness of static scope rules and block structure in
   a dynamically typed language.
- Scheme distinguishes
    - **procedures from lambda expressions and symbols**,
    - uses a **single lexical environment for all variables** and
    - evaluates the operator position of a procedure call in the same way as an operand position.
   By relying entirely on procedure calls to express iteration, Scheme emphasizes the fact that
    **tail-recursive procedure calls** are essentially **gotos that pass arguments.**
   uses **first-class escape procedures**, from which **all previously known sequential control structures**
    can be synthesized. 
   Has the concept of **exact and inexact number objects**, an extension of Common Lisp’s generic arithmetic.
    Supports hygienic macros, which permit the syntax of a block-structured language to be extended in a consistent and
    reliable manner.

### 1.0 Overview

- Scheme has **latent as opposed to manifest types**
- Types
  are associated with objects (also called values) rather than
  with variables.
- All objects created in the course of a Scheme computation,
  including procedures and continuations, have unlimited ex-
  tent. **They Do not HAVE to be destroyed, although they often are for practical reasons**
- Implementations of Scheme must be properly tail-
  recursive.
- In Scheme, the argument expressions of a procedure call
  are evaluated before the procedure gains control, whether
  the procedure needs the result of the evaluation or not.
- ### 1.1 Types
- In Scheme **objects** are also referred to as **values.**
- **Booleans**
- 
- ```
    #t is True
    #f is False
  ```
- **Numbers**
- 
- **Characters & Strings**
- 
- **Symbols**
- 
- 
- **Pairs & Lists**
- 
- 
- **Vectors**
- 
- 
- **Procedures**
- 
- ### 1.2. Expressions
- **Expressions**
- **values**
- - **Literal Expression**
          - #t --> #t
          - 23 --> 23
    - **Compound Expression**
          - (+ 23 42) --> 65
          - (+ 14 (* 23 42)) --> 980
- ### 1.3. Variables and binding
- - Scheme allows identifiers to stand for locations containing values.
    - These identifiers are called variables.
    - local bindings can be made with **let**, for example:
    - ```
         (Let ((x 23))
           x))
         --> 23
      ```
- ### 1.4. Definitions
- **define**
- - ```
         (define x 23)
      ```
- **define**
- **Expression**
- ### 1.5. Forms
- ### 1.6. Procedures
- - A procedure is, slightly simplified, an abstraction of an
         expression over objects.
    - A lambda expression creates a new procedure as
      an object, with no need to specify a name:
      ```
         ((lambda (x) (+ x 42)) 23) --> 65
      ```
