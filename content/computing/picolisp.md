---
title: PicoLisp
date: '2016-05-12T01:09:25+04:00'
lastmod: '2023-04-14T02:10:16+04:00'
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
 [computingFreedom](computingfreedom.md) |
 [Quicklinks](quicklinks.md) | [Readinglist](readinglist.md) |   [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [JavaScript](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Penti](penti.md)

# PicoLisp

If you have always been interested in Lisp and its variant forms such as **Common
Lisp, Scheme, [Racket](https://racket-lang.org), **[newLISP](http://www.newlisp.org)** and the like, I think that you are really going to
love **[Picolisp](http://picolisp.com)**.

The original 32 bit implementation is written in **C**, and supports 32bit programming.
Over the years the language has grown and is now available in 64 bit. The really cool
things is this time the language is implemented by a [assembler written in picolisp](http://software-lab.de/doc64/asm
generic).
The [picolisp website](http://picolisp.com) has all the
[documentation](http://picolisp.com/wiki/?Documentation) that you
need to get setup and running. It also has an extensive [tutorial](http://software-lab.de/doc/tut.html) on the
language. So you can get started there.

What I want to do here, is examine the sources and the implementation details
so that we can get a low level / deep understanding of how the language actually
works.


### An update for 2026

Since I first wrote that, the story moved on again. The current PicoLisp is **pil21**: a 64-bit implementation written in PicoLisp itself, which generates LLVM IR and is compiled by LLVM into a native binary. That means it runs on x86-64, ARM64 (Raspberry Pi, Apple Silicon, Android via Termux) and RISC-V from one code base. The old hand-written assembler version (pil64) and the C version (pil32) are history, though their sources are still a great read. Releases are named by date, for example `25.3` or `25.12`; see [vers.h](versh.md).

On Vikix it is one command: `sudo xbps-install -S picolisp`, then `pil +` for a REPL with debugging on.

### What it is, in plain words

Here is the truth about PicoLisp: **it is a Lisp that removed nearly everything other Lisps added, and found it lost almost nothing.** It is an *interpreter* on purpose, with no compiler, because when code is data you want to be able to build, inspect and change it at run time.

It has exactly three kinds of data:

1. **Numbers** – arbitrary-precision integers. No floats; you use *fixed-point* with a scale (`*Scl`), which is honest about decimals.
2. **Symbols** – names with a value and a property list. Internal (`foo`), transient (`"strings"`) and external (`{A1}`, objects that live in the database).
3. **Lists** – chains of two-slot cells. See [Find Boxes in Lists](findboxes.md).

On top of that sit a built-in **object system**, a built-in **database** with entities and relations, **Pilog** (a Prolog inside Lisp), and libraries for HTTP, HTML forms and JSON. A full web application with persistence can be a few hundred lines.

### Why it matters

- **You can hold it in your head.** The whole reference fits in one browser tab. That makes it a superb language for learning how a Lisp actually works.
- **It is practical.** Alexander Burger and Software Lab have shipped commercial database applications in it for decades.
- **It shows the power of fewer concepts.** Dynamic binding, no compiler and one data structure sound like limitations. In practice they make metaprogramming and debugging extremely direct.

### An everyday analogy: a Swiss army knife versus a toolbox

Common Lisp is a full workshop toolbox: hundreds of specialised tools, each perfect for something. PicoLisp is a really good Swiss army knife. Fewer blades, but they all fold out of the same handle, and you always have it in your pocket.

### A hands-on taste

```picolisp
$ pil +
: (de fact (N) (if (=0 N) 1 (* N (fact (dec N)))))
-> fact
: (fact 30)
-> 265252859812191058636308480000000
: (mapcar '((X) (* X X)) (range 1 5))
-> (1 4 9 16 25)
: (scl 2) (format (* 3 1.25) *Scl)    # fixed-point: 3 x 1.25
-> "3.75"
: (pp 'fact)                         # code is data: pretty-print it
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

### Common misconceptions

- **"No compiler means slow."** For list processing and database work it is surprisingly quick, because the interpreter is tiny and evaluation is direct. Heavy number crunching belongs elsewhere.
- **"No floats means no decimals."** Fixed-point gives exact decimals, which is what money needs anyway.
- **"Dynamic binding is dangerous."** It needs a naming convention (PicoLisp's capitalised locals and `*Globals`), and in return gives you simple, inspectable programs.
- **"It is a toy."** It runs real business applications, and its database has transactions, indexes and replication.

### Connections

- Tutorials: [The Vikid PicoLisp Tutorial](pltutorial.md), [PicoLisp Tutorials](piltutorials.md), [Input/Output](plio.md), [box](plbox.md), [new](plnew.md), [PicoLisp DB](pildb.md), [Application Development](appdev.md).
- Under the hood: [The PicoLisp Machine](pilmachine.md), [PicoLisp Assembly](pilasm.md), [vers.h](versh.md).
- Cousins: [Common Lisp](commonlisp.md), [Scheme](scheme.md), [Racket](racket.md), [Lambda Calculus](lambdacalculus.md), [Functional Programming](functional.md).


- [Application Development](appdev.md)
- [Going MAD with Files and Directories](filesanddirectories.md)
- [Vikid Picolisp Tutorial](pltutorial.md)
- #### Topics
- [picolisp website](http://picolisp.com)
- [The PicoLisp Machine](pilmachine.md)
- [Input/Output](plio.md)
- [Working With Numbers](pilnumbers.md)
- Symbols
- NIL
- Internal Symbols
- Transient Symbols
- External Symbols
- Lists
- Read-Macros
- Evaluation
- Shared Libraries
- Coroutines
- Interrupt
- Error Handling
- @ Result
- Comparing
- OO Concepts
- Database
- Transactions
- [The 5 Transaction Steps](http://software-lab.de/doc/ref.html#trans)
- [Updating the Database](upd.md)
- Entities / Relations
- Pilog (PicoLisp Prolog)
- Naming Conventions
- Breaking Traditions
- ### External Links
- [A Beginner's Blog](https://picolisp-blog.hashnode.dev)
- [Web-application Series](https://picolisp-explored.com/series/web-app)**
