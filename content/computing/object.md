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
topics:
- c-systems
---

# Objects in C

Here is the truth about "objects" in C: **they have nothing to do with classes.** When the C standard says *object*, it means something much plainer and much more useful: a chunk of memory that can hold a value. Every variable you declare, every element of an array, every block you `malloc` is an object. Once you see that, half of C's "undefined behaviour" warnings start to make sense.

### What it is, in plain words

The C standard (C23 is the current edition, with C2y in progress in 2026) defines an object as a **region of data storage in the execution environment, the contents of which can represent values**.

Every object has four properties worth knowing:

1. **Size** – how many bytes it occupies, given by `sizeof`.
2. **Type** – how those bytes are to be interpreted (`int`, `double`, `struct point`). This is the object's *effective type*.
3. **Alignment** – which addresses it may start at (`alignof`, usually 4 or 8 for `int` and `double`).
4. **Storage duration** – how long it lives:
   - **automatic**: local variables, alive until the block ends;
   - **static**: globals and `static` locals, alive for the whole program;
   - **thread**: `thread_local` (C23 spelling; `_Thread_local` before), one per thread;
   - **allocated**: from `malloc`/`calloc`/`realloc`, alive until `free`.

A **variable** is just an object that has a name, an [identifier](identifier.md). An **lvalue** is an expression that designates an object, which is why you can assign to `x`, `a[3]` or `*p` but not to `x + 1`.

### Why it matters

Most serious C bugs are object bugs:

- **Use after free** – touching an allocated object after its lifetime ended.
- **Dangling pointers to locals** – returning `&x` from a function, after `x`'s automatic lifetime is over.
- **Buffer overflows** – writing past the end of an array object into a neighbour (see [Strings in C](cstrings.md)).
- **Strict aliasing violations** – reading an object's bytes through a pointer of an unrelated type, which lets the optimiser assume things that are not true.

Each of these is "the program used memory that was not a live object of the right type". Thinking in objects is how you reason about them before the debugger has to.

### An everyday analogy: lockers

Memory is a corridor of numbered lockers. An object is a set of adjacent lockers you have been assigned, with a label on the door saying what goes inside (the type) and a rental period (the storage duration). A pointer is a slip of paper with a locker number on it. The slip can outlive the rental. Opening a locker you no longer rent is not a crime the corridor will stop. It just gives you someone else's stuff, or nothing, or a mess. That is undefined behaviour.

### A hands-on example

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdalign.h>

static int counter;              /* static storage: lives all program long */

int *bad(void) {
    int local = 42;              /* automatic storage */
    return &local;               /* dangling: local dies on return */
}

int main(void) {
    double d = 3.14;             /* an object of type double */
    int a[4] = {1, 2, 3, 4};     /* one array object holding four int objects */
    int *heap = malloc(sizeof *heap * 4);   /* allocated object */

    printf("sizeof d = %zu, alignof(double) = %zu\n", sizeof d, alignof(double));
    printf("sizeof a = %zu, elements = %zu\n", sizeof a, sizeof a / sizeof a[0]);

    a[2] = 99;                   /* a[2] is an lvalue designating an object */
    counter++;

    free(heap);                  /* heap object's lifetime ends here */
    /* heap[0] = 1;  <- would be use-after-free */
    return 0;
}
```

Compile with the sanitizers and the compiler will catch object mistakes at run time:

```bash
gcc -std=c23 -Wall -Wextra -g -fsanitize=address,undefined object.c -o object
./object
```

Uncomment the `heap[0] = 1;` line and AddressSanitizer reports `heap-use-after-free` with the exact line. Call `bad()` and dereference the result and GCC warns at compile time that you return the address of a local. Step through it in [GDB](gbddebugger.md) and `print sizeof(a)` or `ptype a` to see the object's type from the inside.

### Common misconceptions

- **"Object means OOP."** Not in C. The C++ standard uses the same plain definition too. Classes are a separate idea. If you want message-passing objects, see [Cuis Smalltalk](cuissmalltalk.md); for prototype objects, [JS Objects](jsobjects.md).
- **"A pointer is an object's address, so any address is fine."** A pointer is only valid while it points into a live object (or one past the end of an array).
- **"Arrays are pointers."** An array is one object. It *decays* to a pointer to its first element in most expressions, but `sizeof a` still sees the whole array.
- **"`malloc` gives me an `int`."** It gives you raw storage with no effective type. The first store through an `int *` gives it one.
- **"Static means private."** At file level `static` controls *linkage* (visibility); on a local it controls *storage duration*. Same keyword, two jobs.

### Connections

- [C Programming](cprogramming.md), [Identifiers](identifier.md), [Literals](literals.md), [C Syntax](csytanx.md).
- [C Integers](cints.md), [C Floats](cfloats.md), [C Chars](cchars.md) – the types objects can have.
- [The Compiler](thecompiler.md), [Using the C Debugger](gbddebugger.md), [C Standard Library](cstandardlibrary.md).
- [Data Structures and Algorithms](datastructuresandalgorithms.md) – building bigger structures out of objects and pointers.

[Back to C Programming](cprogramming.md)

In C, the term **object** refers to a location in memory whose contents can represent values.

Objects that have named [identifiers](identifier.md) are called variables.
