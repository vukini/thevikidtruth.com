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
draft: true
review: update
---

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
