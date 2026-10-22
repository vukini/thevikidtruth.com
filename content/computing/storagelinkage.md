---
title: Sorting the Confusion between Storage Classes, Linkage, Duration & Scope
date: '2016-11-21T06:28:18+04:00'
lastmod: '2016-11-21T09:47:52+04:00'
original_id: '{A312}'
original_name: storagelinkage
original_blob: blob/B/1/477.txt
revisions: 31
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: storagelinkage
draft: false
topics:
- c-systems
---
### The plain idea, up front

Four C concepts, **scope**, **duration** (lifetime), **linkage** and **storage class**, are endlessly confused because they overlap and sound alike. The one-line summary: *scope* is **where** a name is visible, *duration* is **how long** the data lives, *linkage* is **whether the same name in different files means the same thing**, and *storage class* specifiers (`auto`, `static`, `extern`, `register`) are the keywords you use to control the first three. This page untangles them one at a time.

### Why it matters

Getting these wrong produces some of C's most baffling bugs: a variable that mysteriously keeps its value between calls, a "multiple definition" linker error, a name that is visible where you did not expect, or memory that vanishes while you are still using it. Once the four ideas are separated in your head, `static` and `extern` stop being mysterious and the linker's complaints start making sense.

### An everyday analogy

Think of a company. *Scope* is which rooms a person is allowed into. *Duration* is how long they are employed. *Linkage* is whether "Sam in Accounts" and "Sam" mentioned in another department are the same Sam. *Storage class* is the type of contract (permanent, temporary, on-loan) that sets all of that. A person can be permanently employed (duration) but only allowed in one room (scope), which is exactly what `static` does to a variable.


# Sorting the Confusion between Storage Classes, Linkage, Duration & Scope

[Back to C Programming](cprogramming.md)

There are four distinct ideas that we need to master:

- The **Duration** of an object describes whether its storage is allocated once only,
  at program start-up, or is more transient in its nature, being allocated and
  freed as necessary.
- **Scope** describes **where** an [identifier](identifier.md) has meaning and what
  meaning it has. The scope of a declaration is the part of the code
  where the declaration is seen and can be used.
- **Linkage**
   is used to determine what makes the same name declared in different
   scopes refer to the same thing.
   **Storage class** specifiers help you to specify the type of storage used for data
  objects.

[Objects](object.md) have storage duration, not linkage; and identifiers have linkage, not storage duration.

#### Duration

There are two kinds of duration:

- **automatic**
- **static**

#### Storage Classes

During the execution of a program, each object exists as a physical location
in memory for a certain period, called its **lifetime**.
The lifetime is determined by its **storage duration** which have corresponding
**storage class specifiers**.

There are four kinds of storage duration **static, thread, automatic and
allocated**.

Typically

- static & thread storage objects are stored in the **Data Segment**.
- Automatic storage objects are stored on the **Stack**.
- Allocated objects are stored on the **Heap**.

The are five storage class specifiers: **static, extern, auto, register and typedef**.

- Static objects
    - 
    - 
    -
- Thread Duration
    - 
    - 
    -

 Automatic Duration
  
- 
- 
- 

  
Each declaration can only have a single storage class specifier.

#### Linkage

There are three kinds of linkage:

- **no linkage**
    - All identifiers which are **not internal** or **external**. Such as:
    - **Labels, tags, typedef's**
    - **Function parameters**
- **internal linkage**
    - Identifiers with **internal linkage** represent the **same** object
             within the same **translation unit / Module**.
    - use storage class specifier **static** on function or object **outside** all function
              definitions
- **external linkage**
    - Identifiers with **external linkage** represent the **same** object
              throughout the program.
    - functions are **extern** by default.
    - use storage class specifier **extern** on function or object.
    - once an identifier has been declared intern, you cannot change it back
              to extern.

#### Sources

- [cs-fundamentals.com](http://cs-fundamentals.com/c-programming/storage-classes-in-c-and-storage-class-specifiers.php)
- [norswap.com](http://norswap.com/c_scope_duration_linkage/)
- [gbdirect](http://publications.gbdirect.co.uk/c_book/chapter8/declarations_and_definitions.html)

### A worked example: the many faces of `static`

```c
int  globalCounter;          // external linkage, static duration, file scope
static int fileCounter;      // INTERNAL linkage: private to this file

void tick(void) {
    static int calls = 0;    // static duration, but block scope:
    calls++;                 //   keeps its value between calls,
    int local = calls;       //   while `local` is created fresh each call
}

extern int globalCounter;    // a *declaration*: "defined elsewhere"
```

Notice `static` means two different things depending on where it sits: at file level it hides a name (internal linkage); inside a function it makes a variable persist for the whole program (static duration) while staying privately scoped to that block. That double meaning is the single biggest source of confusion, and seeing it laid out is half the battle.

### Common misconceptions

- **"`static` means constant."** It does not; a static variable can change. It controls lifetime and/or linkage, not mutability (that is `const`).
- **"Scope and duration are the same."** A function's `static` variable has tiny scope but whole-program lifetime, exactly because they are independent.
- **"`extern` allocates memory."** `extern` usually just *declares* that something is defined elsewhere; the definition (and the storage) lives in one place.

### How it connects

- [Tokens](tokens.md) and [The Compiler](thecompiler.md): where identifiers and declarations are processed.
- [Identifiers](identifier.md): the names these rules govern.
- [C Programming](cprogramming.md) and the systems-level pages.

The truth revealed: C's storage rules only look tangled because four separate ideas share a handful of keywords, and once you ask of every variable "where, how long, and is it shared?", the confusion dissolves.
