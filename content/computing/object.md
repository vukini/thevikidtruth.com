---
title: Objects in C
date: '2016-11-21T09:49:09+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A313}'
original_name: object
original_blob: blob/B/1/503.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: object
draft: false
---

# Objects in C

Here is the truth about "objects": **the word means different things in different traditions, and fights about OOP usually start from mixed definitions.** In Smalltalk an object is a living entity that answers messages; in C++ it is a region of memory with a type; in JavaScript it is a mutable property bag with a prototype link.

### What it is, in plain words

An **object** packages **state** (data) with **behaviour** (code that uses that data). Languages implement that idea differently:

- **Class-based** (Java, C++, Python) – objects are instances of classes that define their shape.
- **Prototype-based** (JavaScript, Self) – objects inherit from other objects directly.
- **Message-passing** (Smalltalk, Objective-C) – you send messages; the object decides.
- **Actor-ish** – objects as concurrent entities with mailboxes (Erlang processes are cousins).

### Why it matters

Almost every mainstream UI toolkit, game engine and business app framework speaks in objects. Knowing which object model you're in stops you from writing JavaScript as if it were Java – or Smalltalk as if it were C.

### An everyday analogy: people at a desk

You don't reach into someone's skull and change their memories. You ask them to do something ("please print this"). They may refuse, delegate or act. That is the Smalltalk view. The C++ view is more like a labelled folder of papers with procedures stapled on. Both are called "objects". Clarity demands saying which you mean.

### A hands-on contrast

```python
# Python – class-based
class Counter:
    def __init__(self): self.n = 0
    def inc(self): self.n += 1
c = Counter(); c.inc()
```

```js
// JavaScript – prototype bag
const counter = {
  n: 0,
  inc() { this.n++; },
};
counter.inc();
```

```smalltalk
"Smalltalk – message passing"
c := Counter new inc.
c count.
```

```lisp
# PicoLisp – often symbols + properties / classes when needed
(class +Counter)
(dm inc> () (inc (:: n)))
```

### Common misconceptions

- **"OOP means inheritance trees."** Composition and message passing matter more in well-designed systems.
- **"Objects require classes."** Prototypes disagree.
- **"FP and OOP are enemies."** Many languages blend them; choose per problem.

### Connections

- [JS Objects](jsobjects.md), [Prototypal Inheritance](jsprototypalinheritance.md).
- [Pharo](pharo.md), [Cuis](cuissmalltalk.md), [Common Lisp](commonlisp.md).

[Back to C Programming](cprogramming.md)

In C, the term **object** refers to a location in memory whose contents can represent values.

Objects that have named [identifiers](identifier.md) are called variables.
