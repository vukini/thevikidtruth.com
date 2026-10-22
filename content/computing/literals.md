---
title: Literals
date: '2016-11-21T22:08:27+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A314}'
original_name: literals
original_blob: blob/B/11/631.txt
revisions: 14
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: literals
draft: false
topics:
- c-systems
---

# Literals

Here is the truth about literals: **they are how values show up in source code before they have a name.** Every language has them; C's are small, strict and easy to get subtly wrong – especially once suffixes and escape sequences enter.

### What it is, in plain words

A **literal** is a notation that writes a value directly: `42`, `3.14`, `'a'`, `"hello"`, `true`. In C (and C-like languages) the form of the literal decides its **type** and how it's stored. Related pages cover each family in depth: [integers](cints.md), [floats](cfloats.md), [characters](cchars.md), [strings](cstrings.md).

### Why it matters

Write `1 << 32` on a machine where `int` is 32 bits and you've wandered into undefined behaviour – the literal `1` was too narrow. Write `"café"` without knowing the source encoding and you ship mojibake. Literals look trivial; they are load-bearing.

### An everyday analogy: coins on the table

A variable is a labelled jar. A literal is a coin you put on the table right now: a 1-euro coin, a 50-cent coin. The *shape* of the coin (the notation) tells everyone its value and denomination (the type). Put the wrong coin in the jar and the totals come out wrong.

### A hands-on example (C)

```c
#include <stdio.h>
int main(void) {
    /* Integer literals */
    int d = 42;            /* decimal */
    int h = 0x2A;          /* hex */
    int o = 052;           /* octal – easy to write by mistake */
    int b = 0b101010;      /* binary – standard in C23 */
    long L = 42L;
    unsigned long long big = 1ULL << 40;
    int million = 1'000'000;   /* digit separators – C23 */

    /* Floating literals */
    double pi = 3.14159;
    float  f  = 1.0f;
    double sci = 6.022e23;
    double hexf = 0x1.8p1;     /* 3.0 */

    /* Character and string */
    char c = 'A';
    char nl = '\n';
    char *s = "Void Linux";    /* static storage, don't free */
    char *u = u8"café";        /* UTF-8 string literal (C11/C23) */

    printf("%d %d %llu %s\n", d, b, big, s);
    return 0;
}
```

```bash
gcc -std=c23 -Wall literals.c -o literals && ./literals
```

In Python the same ideas feel softer – `1_000_000`, `0x2A`, `0b101010`, `"café"`, `b"bytes"`, `True` – and the type is the object's, not the literal's bit-width. In JavaScript, watch for octal legacy forms in non-strict mode; prefer `0o52` and `0b101010`.

### Boolean and null-ish literals across languages

| Language | True/False | Empty / null |
|----------|------------|--------------|
| C23 | `true` `false` (`bool`) | `NULL` |
| Python | `True` `False` | `None` |
| JavaScript | `true` `false` | `null`, `undefined` |
| Lisp | `T` / `NIL` (PicoLisp: `T` / `NIL`) | `NIL` |
| Rust | `true` `false` | `None` (Option) |

Knowing what your language treats as a literal versus a built-in name avoids the classic Python mistake of writing `true` (NameError) or the C mistake of assuming `TRUE` exists without a header.

### Common misconceptions

- **"Leading zero means decimal."** In C, leading zero means *octal*. `010 == 8`.
- **"String literals are `char *` you can write through."** They have static storage and must be treated as read-only. Use `char buf[] = "hi";` if you need a mutable copy.
- **"`'AB'` is a character."** In C it's an *integer* character constant (implementation-defined value); not a string.
- **"Binary literals aren't portable."** They're in C23 and have been a GCC/Clang extension for years.
- **"Literals and constants are the same."** A literal is notation in source; a constant (`const`, `enum`, `#define`) is a named binding. Related, not identical.

### What C23 changed

C23 is the biggest update to C literals in decades:

```c
#include <stdio.h>

int main(void) {
    bool ok = true;               /* bool, true, false are keywords now */
    int *p = nullptr;             /* typed null pointer constant */
    unsigned mask = 0b1111'0000;  /* binary literal with a digit separator */
    long big = 9'223'372'036'854'775'807;
    auto x = 42u;                 /* auto infers unsigned int from the literal */
    constexpr double tau = 6.283'185'307;   /* a compile-time constant object */

    printf("%d %p %u %ld %u %.3f\n", ok, (void *)p, mask, big, x, tau);
    printf("%zu\n", sizeof(u8"é"));          /* char8_t array: 3 bytes */
}
```

So the table above should read `nullptr` (or `NULL`) for C23. `nullptr` has its own type, `nullptr_t`, which avoids the old ambiguity where `NULL` might be plain `0` and match the wrong overload in generic code. `u8"..."` literals now have type `char8_t[]`-compatible `unsigned char` elements, which matters when you pass them to functions expecting `char *`.

### Literals in Lisp: the reader decides

In C, the *compiler* decides what a literal means. In Lisp, the *reader* does, and you can watch it:

```picolisp
: (read)
123456789012345678901234567890     # arbitrary-size integer, no suffix needed
-> 123456789012345678901234567890
: (scl 2) (read)
3.14                                # fixed-point: stored as the integer 314
-> 314
: '(a "b" 7)                        # symbol, transient symbol (string), number
-> (a "b" 7)
```

PicoLisp numbers have no size suffixes because they never overflow, and decimals are integers scaled by `*Scl`. That is the honest version of what C's `3.14` really is: an approximation chosen by the literal's type.

### Connections

- [Integers in C](cints.md), [Floating-point numbers in C](cfloats.md), [Characters in C](cchars.md), [Strings in C](cstrings.md).
- [C Programming](cprogramming.md), [Tokens](tokens.md), [Identifier](identifier.md).
- [Binary](binary.md).

[C Programming](cprogramming.md)

A **literal** is a [token](tokens.md) that denotes a **fixed value**, which may be:

- an [integer](cints.md),
- a [floating-point number](cfloats.md),
- a [character](cchars.md),
- or [string](cstrings.md).

This **fixed value** actually sits in the **source file** and must be **copied into
memory** when [the compiler](thecompiler.md) finally gets to work.
