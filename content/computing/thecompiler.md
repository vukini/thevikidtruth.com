---
title: The Compiler
date: '2016-11-21T04:06:50+04:00'
lastmod: '2021-08-27T01:39:17+04:00'
original_id: '{A305}'
original_name: thecompiler
original_blob: blob/B/7/461.txt
revisions: 23
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: thecompiler
draft: false
topics:
- c-systems
---

[Back to C programming](cprogramming.md)

# The Compiler

The C compiler translates **C-source-code** into **machine code**.

The Compiler translates each *source file* into an *object file* also known as
a **module**.

If there are more that 1 *object files*, these are then *linked* by the
**linker** which outputs a **executable**.

The **executable** is what we normally run as a program in the system.

## The Translation Phases

The compilation takes place in 8 steps.

1. **Read Source**
    - Convert the *File Charset* into *Source Charset* if necessary
    - Convert *end-of-line indicators* to *newline chars* if needed
    - [Trigraphs](trigraphs.md) are converted to their single char versions
    - [Digraphs](digraphs.md) are left as they are.
1. **whenever a backslash is followed by a newline character, it is deleted**
1. **Source is Broken in [Tokens](tokens.md).**
    - each Comment is converted into a space.
1. **Preprocessor Directives are carried out and macro calls are expanded**
1. **It is the converted into the Execution Character Set**
    - all character and escape sequences in char constants and strings converted.
1. **Adjacent String Literals are concatenated**
1. **Compiling Begins** and the tokens are converted into Machine Code
1. **The Linker** is invoked
    - it resolves references to external objects and functions
    - generates the executable file
    - External objects and functions should not be defined more than once

## Compiling Programs

use make when you can. Assume you have a file, file.c, then:

```
make file
```

or

```
CFLAGS="-Wall" make file
```

use a makefile named "Makefile":

```
CFLAGS=-Wall -g

clean:
  rm -f file
```
