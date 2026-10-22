---
title: C Standard Library
date: '2017-06-29T02:39:49+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1176}'
original_name: cstandardlibrary
original_blob: blob/B/11/620.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: cstandardlibrary
draft: false
topics:
- c-systems
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
  [Picolisp By Example](picolispbyexample.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md) | [Networking](networking.md) | [Machine Learning](machinelearning.md) |
  [Git](git.md) |
  [Machine Learning](machinelearning.md) |
  [Algorithms](algorithms.md) |
  [Open Data Science](opendatascience.md) |

## [C Standard Library](cstandardlibrary.md)

Here is the truth about the C standard library: **it is a small, sharp toolkit – I/O, memory, strings, maths, time – that every hosted C program leans on, and its sharpest edges are still the string and unchecked I/O functions.** Knowing what is in ISO C versus what your OS adds is half of reading real code.

### What it is, in plain words

The **C standard library** (libc) is defined by the ISO C standard and implemented by projects like **glibc** (GNU), **musl** (Void's default option), **dietlibc**, and the BSD libcs. Headers you'll use constantly:

| Header | Role |
|--------|------|
| `<stdio.h>` | `printf`, `fopen`, `fread`, `snprintf` |
| `<stdlib.h>` | `malloc`, `free`, `atoi`, `exit`, `qsort` |
| `<string.h>` | `strlen`, `memcpy`, `memcmp`, `memset` |
| `<ctype.h>` | `isdigit`, `tolower` |
| `<math.h>` | `sin`, `sqrt`, `fma` (link `-lm` on many systems) |
| `<time.h>` | `time`, `strftime`, `clock` |
| `<stdint.h>` / `<inttypes.h>` | fixed-width integers |
| `<stdbool.h>` | `bool` (keyword in C23) |
| `<assert.h>` | `assert` |
| `<errno.h>` | `errno` values |
| `<stdarg.h>` | variadic helpers |

POSIX and Linux add much more (`<unistd.h>`, `<pthread.h>`, `<sys/socket.h>`…) – useful, but not ISO C.

### Why it matters

You can write C without libc (freestanding kernels, some embedded), but almost everything else calls it. Understanding ownership of `malloc` memory, the difference between `size_t` and `int`, and why `scanf("%s", buf)` is a trap makes you fluent in the language as it's actually used.

### An everyday analogy: a workshop's communal drawers

Every workshop shares a drawer of tape measures, pencils and utility knives. Libc is that drawer. Some tools (the utility knives – `gets`, `strcpy`) will cut you; safer tools (`snprintf`, `memcpy` with lengths) do the same job. musl versus glibc is two shops stocking slightly different brands of the same tools.

### A hands-on example

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(void) {
    size_t n = 64;
    char *buf = malloc(n);
    if (!buf) return 1;

    time_t now = time(NULL);
    struct tm *t = localtime(&now);
    strftime(buf, n, "%Y-%m-%d %H:%M:%S", t);
    printf("now: %s\n", buf);

    /* Grow a buffer the hard way */
    const char *extra = " – Vikix";
    size_t need = strlen(buf) + strlen(extra) + 1;
    char *p = realloc(buf, need);
    if (!p) { free(buf); return 1; }
    buf = p;
    memcpy(buf + strlen(buf), extra, strlen(extra) + 1);
    puts(buf);

    free(buf);
    return 0;
}
```

Compile with warnings as errors when you can: `gcc -std=c23 -Wall -Wextra -Werror`.

### Common misconceptions

- **"libc is the OS."** It's a user-space library that *calls* the OS.
- **"All Linuxes share glibc."** Alpine and Void-musl use musl; behaviour differs at the edges (`printf` of long doubles, locale, DNS stubs).
- **"`malloc` zeroes memory."** It doesn't. Use `calloc` or `memset`.
- **"`errno` is always set."** It's only meaningful when a function documents setting it and signals failure.
- **"ISO C includes networking."** Networking is POSIX / OS-specific.

### Freestanding versus hosted

ISO C defines **hosted** environments (with full libc) and **freestanding** ones (kernel, bootloader, some embedded) where only a handful of headers are required (`<stddef.h>`, `<limits.h>`, `<stdint.h>`, `<stdarg.h>`, …) and you provide your own I/O. Knowing which world you're in stops you from calling `printf` in a kernel module and wondering why linking fails.

When reading man pages, check whether a function is ISO C, POSIX, or a GNU extension – portability depends on it.

### What C23 added to the library

The library grows slowly, but C23 brought several genuinely useful additions. GCC 15 and recent glibc and musl support most of them:

| Header / function | What it gives you |
|---|---|
| `<stdckdint.h>`: `ckd_add`, `ckd_sub`, `ckd_mul` | integer arithmetic that **reports overflow** instead of silently wrapping or invoking undefined behaviour |
| `<stdbit.h>`: `stdc_count_ones`, `stdc_leading_zeros`, `stdc_bit_width` | portable bit operations that compile to single CPU instructions |
| `memccpy` | copy until a byte (such as `'\0'`) is found, with a size limit: the building block for safe string concatenation |
| `strdup`, `strndup` | duplicate a string onto the heap (finally standard, after decades in POSIX) |
| `memset_explicit` | clear memory (passwords, keys) in a way the optimiser may not remove |
| `timespec_getres`, `gmtime_r`, `localtime_r` | thread-safe time functions |

Overflow checking is the one I would adopt today:

```c
#include <stdckdint.h>
#include <stdio.h>
#include <stdint.h>

int main(void) {
    int32_t total;
    if (ckd_mul(&total, 70000, 70000))           /* true means it overflowed */
        puts("overflow: refusing to continue");
    else
        printf("%d\n", total);
}
```

### Reading the library like a map

You do not need to memorise libc. You need to know where to look:

```bash
man 3 snprintf          # section 3 = library functions
man 3 stdio             # overview of a whole header
man 2 open              # section 2 = system calls underneath
apropos -s 3 string     # search library pages by keyword
```

On Void, install `man-pages` and `man-pages-devel`; pick between `glibc` and `musl` at install time, which is why some of the edge-case behaviour above can differ between two Vikix machines. If a program behaves differently on musl, the first question is "does it rely on something glibc-specific?"

Compared with PicoLisp, which provides its own I/O, strings and bignums, C's library is deliberately bare: it is the thin layer that languages like PicoLisp, Python and Node are themselves built on.

### Connections

- [C Programming](cprogramming.md), [Strings](cstrings.md), [Literals](literals.md).
- [Integers](cints.md), [Floats](cfloats.md), [Characters](cchars.md).
- [GCC](gcc.md), [objdump](objdump.md).

###### External Links

- [n843.pdf](http://std.dkuug.dk/JTC1/SC22/WG14/www/docs/n843.pdf)
- [The C Library Reference Guide by Eric Huss](https://eecs.wsu.edu/~aofallon/cpts122/CLibraryReferenceGuide.pdf)
- [ISO/IEC Committee Draft — April 12, 2011](http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1570.pdf)
- [IEC/ISO JTC1/SC22/WG14 - C main page](http://www.open-std.org/JTC1/SC22/WG14/)
- [The GNU C Library Reference Manual](https://www.gnu.org/software/libc/manual/pdf/libc.pdf)
- [A Brilliant reference from devdocs.io](http://devdocs.io/c/)
