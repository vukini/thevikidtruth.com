---
title: vers.h
date: '2017-06-29T02:06:42+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1175}'
original_name: versh
original_blob: blob/B/6/112.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: versh
draft: false
topics:
- lisp
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
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
  [Open Data Science](opendatascience.md)

# [vers.h](versh.md)

Here is a small truth hidden in a tiny file: **in PicoLisp, the version number is a date.** `vers.h` is the whole of it in the old C sources, one line telling you the day the interpreter was cut. Reading it is a nice first step into the [PicoLisp sources](pilmachine.md), because it shows how little ceremony the system needs.

### What it is, in plain words

`vers.h` is a header file from the C-based PicoLisp sources (pil32 and the older miniPicoLisp lineage). It declares one array:

```
static byte Version[4] = {17,6,13};
```

Three numbers: **year, month, day**. `{17,6,13}` means 13 June 2017. The fourth slot is spare. When the interpreter starts and you call `(version)`, it prints those numbers joined by dots.

In today's PicoLisp (pil21, the 64-bit version written in PicoLisp itself and compiled through LLVM), the same idea lives in `src/vers.l`:

```picolisp
(pico~de *Version 25 3 29)
```

Same date format, now as Lisp. Releases still follow the date: the stable versions you see in package managers in 2025 and 2026 are numbered like `25.3` or `25.12`, the year and month of the release.

### Why it matters

- **Debugging.** When you ask on the mailing list or IRC why something behaves oddly, the first answer is "which version?" A date tells you exactly which source tree you have, and which changes in the change log apply.
- **Compatibility.** Code written for pil32 (the C interpreter) and pil21 differs in places, for example in how the native call interface works. Knowing your version tells you which manual to read.
- **Simplicity as a design value.** Most projects need a build system plugin to generate a version string. PicoLisp needs one array. That is the PicoLisp attitude in miniature.

### An everyday analogy: a "baked on" stamp

A loaf of bread from a good bakery has a date on it, not a marketing number. You know immediately how fresh it is and which batch it came from. `vers.h` is that stamp. "Version 3.1.7" tells you little on its own; "13 June 2017" tells you where it sits in history.

### A hands-on example

Ask the running interpreter, from the shell or the REPL:

```bash
$ pil -version -bye
25.3.29
```

```picolisp
: (version)       # prints and returns the list
25.3.29
-> (25 3 29)
: (version T)     # just return it, no printing
-> (25 3 29)
```

Because it returns a list, you can test it in code, for example to refuse to run on an interpreter that is too old:

```picolisp
(unless (>= (version T) (24 6 1))
   (quit "Need PicoLisp 24.6 or newer") )
```

PicoLisp compares lists element by element, so `(25 3 29)` is greater than `(24 6 1)`. Dates sort naturally, which is another quiet benefit of the format.

On Vikix I also keep a tiny shell script that prints the versions of the tools I depend on, so I can paste them into notes or bug reports:

```bash
#!/bin/sh
uname -sr
xbps-query -p pkgver picolisp 2>/dev/null
pil -version -bye
emacs --version | head -1
```

Finding the file itself in the C sources:

```bash
grep -rn Version src/vers.h src/*.c | head
```

You will see `Version` used by the `version` built-in function and nowhere else. The type `byte` it uses is defined in `pico.h` (see below).

### Common misconceptions

- **"The date is the day I installed it."** It is the day the source was released, not your install or build date.
- **"Newer pil21 numbers mean a rewrite each time."** No. The format just tracks dates; most releases are small fixes and additions.
- **"`vers.h` configures the build."** It configures nothing. It is purely informational.

### Connections

- [PicoLisp](picolisp.md), [The PicoLisp Machine](pilmachine.md), [PicoLisp Assembly](pilasm.md).
- [C Programming](cprogramming.md), [Identifiers](identifier.md) and [Literals](literals.md) – to read the C line above with confidence.
- [new](plnew.md) and [box](plbox.md) – more built-ins worth reading in the source.

### The C line itself

```
static byte Version[4] = {17,6,13};
```

remember that `byte` is defined in [pico.h](picoh.md) line 50 as `typedef unsigned char byte;`.
