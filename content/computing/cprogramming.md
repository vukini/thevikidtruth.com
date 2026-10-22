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
