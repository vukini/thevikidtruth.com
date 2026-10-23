---
title: 'PicoLisp'
date: '2016-05-12T01:09:25+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A24}'
original_name: picolisp
original_blob: blob/B/12/254.txt
revisions: 51
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: picolisp
draft: false
topics:
- lisp
---

![picos](/assets/picos.png)
{.right}
[Penti](penti.md)

# PicoLisp

If you have always been interested in Lisp and its variants, such as **Common Lisp, Scheme, [Racket](https://racket-lang.org)** or **[newLISP](http://www.newlisp.org)**, I think you are really going to love **[PicoLisp](https://picolisp.com)**.

Here is the truth about PicoLisp: **it is a Lisp that removed nearly everything other Lisps added, and found it lost almost nothing.** It is an interpreter on purpose, with one data structure, dynamic binding and a built-in database. And it is very much alive: as I write this (October 2026) the current release is **26.9**, and Alexander Burger still ships a new one every quarter.

### Where PicoLisp is in 2026

When I first wrote these notes (2016–17) there were two implementations: the original 32-bit one written in **C** (pil32), and a 64-bit one written in a generic **assembler that was itself written in PicoLisp** (pil64). Both are history now.

The current PicoLisp is **pil21**:

- It has been the only maintained implementation since 2020. pil32 and pil64 are archived.
- It is written in **PicoLisp itself**. `src/*.l` is compiled by PicoLisp into **LLVM IR**, and `clang`/`llvm` turn that into a native 64-bit binary. So it runs anywhere LLVM does: x86-64, ARM64 (including Raspberry Pi and Android/Termux), RISC-V, and on Linux, the BSDs and macOS.
- Releases are named **YY.M** and come out quarterly (x.3, x.6, x.9, x.12). The rolling `pil21.tgz` on software-lab.de is always the latest; `(version)` on my build prints `26.9.25`.
- It added **namespaces**: `symbols`, `private`, `local`, `import`, and the `ns~sym` syntax. Libraries such as `@lib/simul.l` now live in their own namespace (see [Life](pillife.md)).
- It ships **Vip**, a vi-style editor written in PicoLisp, which is what `(vi 'foo)` opens.
- New in 2025–26 is **`@lib/ai.l`**, a small client for OpenAI-style LLM APIs (the `ai` namespace: `models`, `chat`, `agent`, `search`), wired into Vip as `:ai`, `:web` and `:models`.
- Recent language additions include `tco`/`tc` for tail-call loops, `recur`, `this`, and an `e` notation for reading fixed-point numbers.

I no longer use PicoLisp every day, but I still think it is one of the best ways to really understand how a Lisp works.

### What it is, in plain words

It has exactly three kinds of data:

1. **Numbers**: arbitrary-precision integers. There are no floats; you use *fixed-point* with a scale (`*Scl`), which is honest about decimals. See [Working With Numbers](pilnumbers.md).
2. **Symbols**: names with a value and a property list. They can be internal (`foo`), transient (`"strings"`), or external (`{A1}`, objects that live in the database).
3. **Lists**: chains of two-slot cells. See [Find Boxes in Lists](findboxes.md).

On top of that sit a built-in **object system**, a built-in **database** with entities and relations, **Pilog** (a Prolog inside Lisp), and libraries for HTTP, HTML forms, JSON, SVG and now LLM APIs. A full web application with persistence fits in a few hundred lines.

### Why it matters

- **You can hold it in your head.** The whole reference fits in one browser tab. That makes it a superb language for learning how a Lisp actually works.
- **It is practical.** Alexander Burger and Software Lab have shipped commercial database applications in it for decades.
- **It shows the power of fewer concepts.** Dynamic binding, no compiler and one data structure sound like limitations. In practice they make metaprogramming and debugging extremely direct.

### An everyday analogy: a Swiss army knife versus a toolbox

Common Lisp is a full workshop toolbox, with hundreds of specialised tools, each perfect for something. PicoLisp is a really good Swiss army knife. It has fewer blades, but they all fold out of the same handle, and you always have it in your pocket.

### A hands-on taste

Tested on PicoLisp 26.9:

```picolisp
$ pil +
: (version)
26.9.25
-> (26 9 25)
: (de fact (N) (if (=0 N) 1 (* N (fact (dec N)))))
-> fact
: (fact 30)
-> 265252859812191058636308480000000
: (mapcar '((X) (* X X)) (range 1 5))
-> (1 4 9 16 25)
: (scl 2) (format (*/ 1.25 3.0 1.0) *Scl)    # fixed-point: 3 x 1.25
-> "3.75"
: (pp 'fact)                                # code is data
(de fact (N)
   (if (=0 N)
      1
      (* N (fact (dec N))) ) )
```

A tiny class, using the built-in object system:

```picolisp
(class +Pt)
(dm T (X Y) (=: x X) (=: y Y))
(dm len> () (sqrt (+ (* (: x) (: x)) (* (: y) (: y)))))
(len> (new '(+Pt) 3 4))   # -> 5
```

### Getting it

See [PicoLisp Installation](../languages/picolispinstallation.md) for the full INSTALL text. In short, build from source:

```bash
sudo apt install binutils make clang llvm libreadline-dev libffi-dev libssl-dev pkg-config
wget https://software-lab.de/pil21.tgz && tar xfz pil21.tgz
cd pil21/src && make && cd ..
./pil +          # REPL with debugging on
```

Many distributions package it (`apt install picolisp` on Debian/Ubuntu, Alpine, Arch AUR, FreeBSD ports, Termux, Guix, Nix), but versions lag behind, often by a year or more. **Void Linux and Homebrew have no package**, so build from source there.

### Common misconceptions

- **"No compiler means slow."** For list processing and database work it is surprisingly quick, because the interpreter is tiny and evaluation is direct. And since pil21 the interpreter itself is optimised by LLVM. Heavy number crunching belongs elsewhere, or in C via `native`.
- **"No floats means no decimals."** Fixed-point gives exact decimals, which is what money needs anyway.
- **"Dynamic binding is dangerous."** It needs a naming convention (capitalised locals, `*Globals`, `+Classes`), and since pil21 namespaces and `private` help further. In return you get simple, inspectable programs.
- **"It is a dead hobby language."** It has had quarterly releases for years, an active mailing list and IRC/Matrix channel, and it runs real business applications.

### Connections

- Tutorials: [The Vikid PicoLisp Tutorial](pltutorial.md), [PicoLisp Tutorials](piltutorials.md), [PicoLisp By Example](picolispbyexample.md), [Input/Output](plio.md), [quote](pilquote.md), [box](plbox.md), [new](plnew.md), [Working With Numbers](pilnumbers.md), [Going MAD with Files and Directories](filesanddirectories.md).
- Applications: [PicoLisp DB](pildb.md), [Application Development](appdev.md), [The Health Application](pilhealth.md), [http.l](httpl.md), [httpGate](httpgatec.md).
- Examples: [PicoLisp Examples Examined](pilexamplesexamined.md), [Life](pillife.md), [Chat](pilchat.md).
- Under the hood: [The PicoLisp Machine](pilmachine.md), [PicoLisp Sources](pilsource.md), [Makefile](makefile.md), [pico.h](picoh.md), [vers.l](versh.md), [PicoLisp ASM (pil64, historical)](pilasm.md).
- Cousins: [Common Lisp](commonlisp.md), [Scheme](scheme.md), [Racket](racket.md), [Lambda Calculus](lambdacalculus.md), [Functional Programming](functional.md).

### External links

- [picolisp.com](https://picolisp.com) and its [wiki](https://picolisp.com/wiki/?home)
- [Reference manual](https://software-lab.de/doc/ref.html) and [tutorial](https://software-lab.de/doc/tut.html)
- [Download pil21.tgz](https://software-lab.de/pil21.tgz) and the [ChangeLog](https://software-lab.de/doc/ChangeLog)
- [The 5 transaction steps](https://software-lab.de/doc/ref.html#trans)
