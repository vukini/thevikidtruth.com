---
title: (car 'var) -> any
date: '2016-11-26T23:20:29+04:00'
lastmod: '2016-11-28T22:28:19+04:00'
original_id: '{A410}'
original_name: cardocar
original_blob: blob/B/2/600.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: cardocar
draft: false
topics:
- lisp
---

[subr.l](subrl.md) | [pilAsm](pilasm.md)


> **Reading this in 2026.** This page reproduces `doCar from src64/subr.l` from the PicoLisp sources (pil64), as I studied them around 2017. It is the assembly implementation of `car`, annotated line by line. PicoLisp is MIT-licensed, © Software Lab, Alexander Burger. Since 2020 the current PicoLisp is **pil21**, which is written in PicoLisp itself and compiled through LLVM, so the line-by-line details here belong to the older 64-bit assembly implementation; the ideas carry over. Current sources are at [software-lab.de](https://software-lab.de/down.html).

```
# (car 'var) -> any
(code 'doCar 2)
   push X                         #push whatever value was here onto the stack
   ld X E                         #load pointer to expression E, into X
   ld E ((E CDR))  # Get arg      #load the value
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret
```

```
   CPU Registers:

      +---+---+---+---+---+---+---+---+
      |               A           | B |  \\      [A]ccumulator
      +---+---+---+---+---+---+---+---+   D     [B]yte register
      |               C               |  /      [C]ount register
      +---+---+---+---+---+---+---+---+         [D]ouble register
      |               E               |         [E]xpression register
      +---+---+---+---+---+---+---+---+

      +---+---+---+---+---+---+---+---+
      |               X               |         [X] Index register
      +---+---+---+---+---+---+---+---+         [Y] Index register
      |               Y               |         [Z] Index register
      +---+---+---+---+---+---+---+---+
      |               Z               |
      +---+---+---+---+---+---+---+---+

      +---+---+---+---+---+---+---+---+
      |               L               |         [L]ink register
      +---+---+---+---+---+---+---+---+         [S]tack pointer
      |               S               |
      +---+---+---+---+---+---+---+---+

      +-------------------------------+
      |  [z]ero  [s]ign  [x,b,c]arry  |         [F]lags
      +-------------------------------+
```
