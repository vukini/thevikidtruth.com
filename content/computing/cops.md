---
title: Operators
date: '2021-08-27T00:40:19+04:00'
lastmod: '2021-08-27T00:46:41+04:00'
original_id: '{A1456}'
original_name: cops
original_blob: blob/B/7/440.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: cops
draft: false
topics:
- c-systems
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) |
  [The Compiler](thecompiler.md) |
  [Identifiers](identifier.md) |
  [Literals](literals.md) |
  [storage_linkage](storagelinkage.md) |

# Operators

Here is the truth about operators in C: **they are just functions in disguise, and two things about them trip up everyone: precedence (who binds tighter) and evaluation order (who runs first), which are not the same question.** The tables below (as images) are the quick reference; the prose here is what the tables cannot show.

### What it is, in plain words

An **operator** is a symbol that combines values into a new value: `+`, `*`, `=`, `&&`, `<<`, `?:`. C has an unusually rich set, grouped by job:

- **Arithmetic**: `+ - * / %` and the unary `+ -`.
- **Relational and equality**: `< > <= >= == !=`, each giving `1` or `0`.
- **Logical**: `&& || !`, which short-circuit.
- **Bitwise**: `& | ^ ~ << >>`, which work on the individual bits.
- **Assignment**: `=` and its compound forms `+= -= *= &= <<=` and so on.
- **Others**: `?:` (ternary), `,` (comma), `sizeof`, `&` (address-of), `*` (dereference), `->` and `.` (member access), `[]` and `()`.

Each operator has a **precedence** (how tightly it binds) and an **associativity** (which way it groups when precedences tie). `a + b * c` is `a + (b * c)` because `*` binds tighter; `a = b = c` is `a = (b = c)` because `=` groups right to left.

### Why it matters

- **Bugs hide in precedence.** `if (x & 1 == 0)` does *not* test the low bit, because `==` binds tighter than `&`; it parses as `x & (1 == 0)`, which is `x & 0`, always zero. Add parentheses: `if ((x & 1) == 0)`.
- **Short-circuiting is control flow.** `if (p && p->next)` is safe precisely because `&&` does not evaluate the right side when the left is false. The order is guaranteed.
- **Most arithmetic is not.** In `f() + g()`, C does not say whether `f` or `g` runs first. Relying on it, or on `a[i] = i++`, is undefined behaviour.

### An everyday analogy: order of operations at the till

A supermarket till applies discounts in a fixed order no matter how you stack the coupons: that fixed order is precedence. Whether the cashier scans the milk or the bread first, when it makes no difference to the total, is evaluation order; the shop does not promise one. Problems come when you assume the scan order changes the total, as with `a[i] = i++`.

### A hands-on example

```c
#include <stdio.h>
int main(void) {
    int x = 6;
    printf("%d\n", x & 1 == 0);     /* prints 0: parsed as x & (1==0), the trap */
    printf("%d\n", (x & 1) == 0);   /* 1: x is even, so its low bit really is 0 */

    int flags = 0;
    flags |= 1 << 2;                /* set bit 2  -> 4 */
    flags |= 1 << 4;                /* set bit 4  -> 20 */
    printf("flags = %d, bit2 set? %d\n", flags, (flags >> 2) & 1);

    int a = 5;
    int b = (a > 3) ? 100 : -100;   /* ternary: a small if-expression */
    printf("%d\n", b);
}
```

```bash
gcc -std=c23 -Wall -Wextra ops.c -o ops && ./ops
```

Turn on `-Wall` and GCC warns about the precedence trap on the first line before it ever runs. That warning has saved more programs than any table.

Compare PicoLisp, which sidesteps the whole problem: there are no operators and no precedence, only functions in prefix form. `(+ a (* b c))` says exactly what it means, and `(& x 1)` cannot be misread. The parentheses *are* the precedence, which is one reason Lispers stop worrying about it.

### Common misconceptions

- **"Precedence decides evaluation order."** It decides *grouping*, not *timing*. `&&`, `||`, `?:` and `,` are the only operators that fix an order.
- **"`=` compares."** `=` assigns; `==` compares. `if (x = 5)` assigns 5 and is always true.
- **"`++i` and `i++` differ in speed."** For an `int` they are identical after optimisation; they differ only in the *value* the expression yields.
- **"`&` is always logical AND."** `&` is bitwise, `&&` is logical. Mixing them up is the trap above.

### Connections

- [C Programming](cprogramming.md), [Literals](literals.md), [C Syntax](csytanx.md), [Objects in C](object.md), [Identifiers](identifier.md).
- [Assembly Language](assemblylanguage.md) and [Build a Computer in Your Head](bciyh.md) – what bitwise operators map to.
- [JavaScript Control Flow](jscontrolflow.md) – the same operators, plus `===` and `??`.

### The reference tables


![arithmetic](/assets/arithmetic.png)
{.center}

![ass](/assets/ass.png)
{.center}

![bit](/assets/bit.png)
{.center}

![dat](/assets/dat.png)
{.center}

![log](/assets/log.png)
{.center}

![mis](/assets/mis.png)
{.center}

![rel](/assets/rel.png)
{.center}
