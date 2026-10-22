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
draft: true
review: update
topics:
- c-systems
---

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
