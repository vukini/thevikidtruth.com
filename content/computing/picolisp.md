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
