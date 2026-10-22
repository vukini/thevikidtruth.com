---
title: Identifiers in C
date: '2016-11-21T05:40:07+04:00'
lastmod: '2023-03-28T07:47:44+04:00'
original_id: '{A311}'
original_name: identifier
original_blob: blob/B/11/630.txt
revisions: 23
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: identifier
draft: false
topics:
- c-systems
---

# Identifiers in C

Here is the truth about names in C: **a name is not one thing. The same spelling can mean four different things at once, and the compiler keeps them in separate drawers.** Most "why does this even compile?" moments come from not knowing which drawer you are in.

### What it is, in plain words

An **identifier** is a name you invent: for a variable, a function, a type tag, a struct member, a label, an enumeration constant or a macro. The rules for spelling are simple:

- letters, digits and underscore, not starting with a digit (`count`, `_tmp`, `point2d`);
- case sensitive (`Count` and `count` are different);
- not a keyword (`int`, `return`, and in C23 also `bool`, `true`, `false`, `nullptr`, `typeof`, `constexpr`);
- C23 also allows many Unicode letters, so `π` is a valid identifier if your compiler and editor agree on UTF-8.

Names beginning with an underscore followed by a capital letter (`_Bool`, `_Foo`) or with two underscores (`__x`) are **reserved** for the implementation. Do not use them.

Every identifier has three properties the rest of this page explains: its **namespace** (which drawer), its **scope** (where in the text it is visible) and its **linkage** (whether the same name in another file refers to the same thing).

### Why it matters

Large C programs are many files glued together by names. Clashing names, accidentally shadowed variables and globals that leak between files are some of the hardest bugs to see, because the code *looks* right. Understanding namespaces and scope also lets you read idioms such as `struct stat stat;` without flinching.

### An everyday analogy: names in a building

In an office block "Ali" can be a person in reception, a meeting room called Ali, and the Ali project on the whiteboard. Nobody gets confused because context tells you which list to look in (namespace). A visitor badge only works on certain floors (scope). And a company-wide "Ali" on the staff directory is the same person in every branch, while a nickname used only in one team is not (linkage).

### A hands-on example

```c
#include <stdio.h>

struct tag { int tag; };          /* tag namespace AND member namespace */

static int hidden = 1;            /* file scope, internal linkage */
int shared = 2;                   /* file scope, external linkage */

int count(struct tag *tag) {      /* parameter 'tag': ordinary namespace */
    int shared = 10;              /* shadows the global inside this block */
    if (tag->tag > 0)
        goto done;                /* label: function scope */
    shared++;
done:
    return tag->tag + shared + hidden;
}

int main(void) {
    struct tag t = { .tag = 5 };
    printf("%d\n", count(&t));    /* prints 16 */
}
```

Compile with `gcc -Wall -Wextra -Wshadow` and GCC points out the shadowed `shared`. `-Wshadow` is not in `-Wall`; I add it to every project.

To see which names a compiled file exports, use `nm`:

```bash
gcc -c ident.c && nm ident.o
# T count   T main   D shared   d hidden
```

Capital letters are external linkage, lower case internal. `hidden` stays private to the file because of `static`.


[Back to Tokens](tokens.md) | [Back to C Programming](cprogramming.md) | [The Compiler](thecompiler.md)

There are 4 types of Identifiers and each type gets its own namespace.

- Label Names, are names that end in a **colon, :**
- Tags for structure, union, and enumeration types
- Names of Structure or Union **members**
- Ordinary Identifiers (all others)

```
struct tag { char tag; ...}
```

Here you can see we have created a structure with the tag **tag**, which also has
a member **tag** of the type char.

```
int count( struct tag *tag)
{
 int len = length( tag->tag)
}
```

Here you can see we defined the function **count** with a parameter named **tag**
which is a pointer to **struct tag**.

In all cases the name **tag** is in different namespaces and do not conflict.

## Identifier Scope

Scopes can confusing, so lets hope we can putthe confusion to rest here.

The scope of an identifier generally begins **after** the declaration except when we
define **structures, union and enumeration types**.

In these cases, the identifier goes into scope **immediately**, within the declaration itself. So you can used the
identifier for **recursive** definitions.

#### File Scope

If you declare the identifier outside of all blocks and parameter lists.
you can use the identifier **anywhere** within the **translation unit / module**.

#### Block Scope

Ignoring **lables**.

An Identifier declared in a block has the scope of the smallest block it is
declared in from its location to the end of the block.

The **parameters** in the function also have block scope.

#### Function Prototype Scope

Identifiers within parameters of the prototype only have scope in the prototype.

#### Function Scope

Labels are special. They take the full scope of the function, no matter if they
are nested within blocks.

i.e. you can use them as **goto** statements.

## Linkage, briefly

- **External linkage** – file-scope names without `static` (and all functions by default). The same name in another translation unit refers to the same object or function. Declare it with `extern` in a header, define it in exactly one `.c` file.
- **Internal linkage** – file-scope names marked `static`. Private to this file.
- **No linkage** – everything at block scope, parameters, typedef names, tags and labels.

Storage classes and linkage together are the most confusing corner of C for beginners.

## Common misconceptions

- **"A struct tag is a type name."** In C, `struct point` is the type; `point` alone means nothing unless you `typedef` it. (C++ differs here.)
- **"Shadowing is an error."** It is legal and silent. Use `-Wshadow`.
- **"`static` makes a variable constant."** It changes lifetime or linkage, never mutability. That is `const`.
- **"Long names slow the program."** Names vanish at compile time (except as debug info and exported symbols).
- **"Any name is fine if it compiles."** Reserved names (leading `_` plus capital, double underscore, `str...` and `mem...` prefixes from the [standard library](cstandardlibrary.md)) can break on the next compiler upgrade.

## Connections

- [C Programming](cprogramming.md), [Objects in C](object.md) – a variable is an object with an identifier.
- [Literals](literals.md), [C Syntax](csytanx.md), [The Compiler](thecompiler.md) – where tokens and names get sorted out.
- [objdump](objdump.md) and [Using the C Debugger](gbddebugger.md) – seeing names after compilation.
- [Scope in JavaScript](jsscope.md) – the same ideas in a very different language.
