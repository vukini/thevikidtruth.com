---
title: (cdr 'lst) -> any
date: '2016-11-26T23:22:48+04:00'
lastmod: '2016-11-26T23:22:48+04:00'
original_id: '{A411}'
original_name: cdrdocdr
original_blob: blob/B/2/245.txt
revisions: 1
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: cdrdocdr
draft: false
topics:
- lisp
---

[subr.l](subrl.md)


> **Reading this in 2026.** This page reproduces `doCdr from src64/subr.l` from the PicoLisp sources (pil64), as I studied them around 2017. It is the assembly implementation of `cdr`. PicoLisp is MIT-licensed, © Software Lab, Alexander Burger. Since 2020 the current PicoLisp is **pil21**, which is written in PicoLisp itself and compiled through LLVM, so the line-by-line details here belong to the older 64-bit assembly implementation; the ideas carry over. Current sources are at [software-lab.de](https://software-lab.de/down.html).

```
# (cdr 'lst) -> any
(code 'doCdr 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret
```
