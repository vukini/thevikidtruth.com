---
title: C Programming
date: '2016-11-21T03:47:35+04:00'
lastmod: '2023-05-19T01:10:07+04:00'
original_id: '{A303}'
original_name: cprogramming
original_blob: blob/B/12/262.txt
revisions: 51
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: cprogramming
draft: false
topics:
- c-systems
---

[C-Programmming](cprogramming.md) | [The Compiler](thecompiler.md)  | [Identifiers](identifier.md) | [Literals](literals.md) |
[linkage](storagelinkage.md) | [C Operators](cops.md) | [C Syntax Structures](csytanx.md) | [GBD Debugger](gbddebugger.md) |
[Operating Systems](os.md) | [devdocs.io](https://devdocs.io)

# C Programming

![cprog](/assets/cprog.jpg)
{.right}

The C programming language is at the heart of GNU/Linux - it is the programming language
most of the Linux Kernel and GNU tools is written in.

There are many outstanding books and online resources where you can learn C and as
such this site will not try and duplicate these efforts.

What I will try to do here is try to complement other sources, trying to explain
parts which are easily overlooked by beginners or are difficult to remember.
I hope that you like what is on offer and if you do, please bookmark these pages
and spread the word.


### What C is, in plain words

C is a small, compiled, statically typed language designed by Dennis Ritchie at Bell Labs in the early 1970s to write Unix. Here is the truth that makes it click: **C is a thin, portable description of what the machine actually does.** You get numbers, memory addresses, functions and very little else. There is no garbage collector, no built-in string type, no classes, no exceptions. What you write is close to what runs.

The language is defined by an ISO standard. **C23** (ISO/IEC 9899:2024) is the current one. It added `true`/`false`/`bool` as real keywords, `nullptr`, `typeof`, `constexpr` objects, `#embed`, binary literals like `0b1010`, digit separators (`1'000'000`) and `[[attributes]]`. GCC 15 and Clang 19+ default to it or close to it, so in 2026 you can use these freely on Vikix.

### Why it matters

- **It is underneath everything.** The Linux kernel, glibc and musl, Python's interpreter, Git, SQLite, PicoLisp's older pil32 interpreter, the runtimes of most languages: C. When something low down breaks, you end up reading C.
- **It teaches the machine.** Pointers, stack frames, memory layout and calling conventions stop being abstractions. That knowledge transfers to [Rust](rust.md), [Zig](ziglang.md), [Odin](odin.md) and even to performance work in Python.
- **It is everywhere hardware is.** Microcontrollers, firmware, [Raspberry Pi](rasberrypi.md) projects and embedded systems still speak C first.
- **Its sharp edges are the security story.** Buffer overflows and use-after-free bugs in C code are a large share of real-world vulnerabilities. That is why [Computer Security](computersecurity.md) people learn C, and why newer kernel code is starting to appear in Rust.

### An everyday analogy: a manual car

Python is an automatic with lane assist. C is a manual gearbox with no traction control. You can drive more efficiently and you feel exactly what the engine is doing, but nobody stops you from stalling, or from redlining it into a wall. Most people who learn to drive manual become better drivers in automatics too.

### A hands-on first program

```c
/* hello.c */
#include <stdio.h>

int main(int argc, char *argv[]) {
    const char *who = argc > 1 ? argv[1] : "world";
    printf("Hello, %s!\n", who);
    return 0;
}
```

```bash
gcc -std=c23 -Wall -Wextra -O2 hello.c -o hello   # compile and link
./hello VikiD                                    # Hello, VikiD!
gcc -std=c23 -E hello.c | tail -5                # see the preprocessor output
gcc -std=c23 -S -O2 hello.c -o - | less          # see the assembly
```

Those last two lines are the habit I recommend most. Look at what the [compiler](thecompiler.md) actually produced. On Void, `xbps-install -S gcc make gdb` gets you everything you need; add `clang` and `clang-tools-extra` for `clangd`, which gives Emacs or vim real code completion through LSP.

When the program grows, add a `Makefile`, turn on `-fsanitize=address,undefined` while developing, and learn [GDB](gbddebugger.md). Those three tools catch most beginner mistakes before they become mysteries.

### Common misconceptions

- **"C is a subset of C++."** It is not. They split decades ago. Valid C (for example implicit `void *` conversion from `malloc`) can be invalid C++, and C has features C++ lacks.
- **"C is fast, so my C is fast."** Bad algorithms are slow in every language. C just removes the excuses.
- **"Undefined behaviour means it crashes."** It means *anything*, including working perfectly today and failing after an optimiser upgrade. Compile with warnings and sanitizers.
- **"Strings are a type in C."** They are arrays of `char` ending in a zero byte. See [Strings in C](cstrings.md).
- **"C is dead because of Rust."** Rust is growing in new code, including in the kernel. The world's existing C is not going anywhere, and someone has to read it.

### Connections

The pages below go deeper. Start with [The Compiler](thecompiler.md), [Identifiers](identifier.md), [Objects in C](object.md) and [Literals](literals.md), then [C Syntax](csytanx.md), the types ([integers](cints.md), [floats](cfloats.md), [chars](cchars.md)), [Strings](cstrings.md) and the [Standard Library](cstandardlibrary.md). For the level below C see [Assembly Language](assemblylanguage.md) and [objdump](objdump.md); for the level beside it, [Operating Systems](os.md).

### The pages in this section


1. **The C Language**
    - [The Compiler](thecompiler.md)
    - [Identifiers](identifier.md)
    - [Literals](literals.md)
    - [Sorting the confusion between Storage Classes and Linkage](storagelinkage.md)
    - [C Operators](cops.md)
    - [C Syntax Structures](csytanx.md)
    - [GBD Debugger](gbddebugger.md)
1. **[Standard Library](cstandardlibrary.md)**
    - The Standard Headers
    - - stdarg.h - variadic functions
          - ```
            Macros:
            va_start             enables access to variadic function arguments (function macro)
            va_arg               accesses the next variadic function argument(function macro)
            va_copy              (C99) makes a copy of the variadic function arguments (function macro)
            va_end               ends traversal of the variadic function arguments (function macro)
            Type:
            va_list              holds the information needed by va_start, va_arg, va_end, and va_copy (typedef)
            #include <stdio.h>
            #include <stdarg.h>
            void simple_printf(const char* fmt, ...)
            {
                va_list args;
                va_start(args, fmt);
                while (*fmt != '\0') {
                    if (*fmt == 'd') {
                        int i = va_arg(args, int);
                        printf("%d\n", i);
                    } else if (*fmt == 'c') {
                        // A 'char' variable will be promoted to 'int'
                        // A character literal in C is already 'int' by itself
                        int c = va_arg(args, int);
                        printf("%c\n", c);
                    } else if (*fmt == 'f') {
                        double d = va_arg(args, double);
                        printf("%f\n", d);
                    }
                    ++fmt;
                }
                va_end(args);
                }
            ```
          - Functions at a Glance
  **Basic Tools**
    - Compiling with GCC
    - Using make to Build C Programs
    - Debugging C Programs with GDB
    - Using an IDE with C
    - [Unicode in C](unicodeinc.md)
  **Problem Solving**
    - [StackOverflow: how-to-check-if-an-initialised-struct-is-empty-or-not](https://stackoverflow.com/questions/30422539/how-to-check-if-an-initialised-struct-is-empty-or-not)
    - [TutorialsPoint: c_type_casting](https://www.tutorialspoint.com/cprogramming/c_type_casting.htm)
    - <!-- 
      -{^{}}
      -{^{}}
       -->
  ### Videos
    - [Learning C by VertoStudio3D](https://www.youtube.com/watch?v=JPAyj85tJ5E&list=PLT6WFYYZE6uLMcPGS3qfpYm7T_gViYMMt)
    - [Intro to C by Molly Rocket Playlist](https://www.youtube.com/watch?v=F3ntGDm6hOs&list=PLEMXAbCVnmY6RverunClc_DMLNDd3ASRp)
  ### Books
    - [The-C-Programming-Language-2nd-Edition Source Code on Github](https://github.com/Heatwave/The-C-Programming-Language-2nd-Edition)
    - [Build Your Own Lisp in C](https://www.buildyourownlisp.com/)
    - [Dive Into Systems](https://diveintosystems.org/book/index.html)
  ### Other External Links
    - [devdocs.io](https://devdocs.io)
    - [cppreference](https://en.cppreference.com/w/c)
    - [Excellent Free Tutorials to Learn C - LinuxLinks](https://www.linuxlinks.com/excellent-free-tutorials-learn-c/)
    - [richard-stallman-c-reference](https://www.i-programmer.info/news/184-cc/15705-richard-stallman-announces-c-reference.html)
    - [Programming Simplified: C programming Examples](https://www.programmingsimplified.com)
    - [Thee Geek Stuff: Variadic Functions](http://www.thegeekstuff.com/2017/05/c-variadic-functions/)
    - [Wikibooks: Programming Termios](https://en.wikibooks.org/wiki/Serial_Programming/termios)
    - [CHL - Create a Webapps in C](https://github.com/it4e/CHL/wiki/Tutorial)
    - [libc manual](https://www.gnu.org/software/libc/manual/html_mono/libc.html#File-Positioning)
    - [c-programming-projects-with-source-code-coding-projects-ideas](https://www.cselectricalandelectronics.com/c-programming-projects-with-source-code-coding-projects-ideas)
