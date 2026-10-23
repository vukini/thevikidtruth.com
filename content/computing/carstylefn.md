---
title: "car-Style Functions"
date: '2016-11-26T23:07:05+04:00'
lastmod: '2016-11-26T23:08:07+04:00'
original_id: '{A407}'
original_name: carstylefn
original_blob: blob/B/2/237.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: carstylefn
draft: false
topics:
- lisp
---

[Back to subr.l](subrl.md)


> **Reading this in 2026.** This page reproduces `the c[ad]r family from src64/subr.l` from the PicoLisp sources (pil64), as I studied them around 2017. These are the assembly implementations of `caar`, `cadr`, `cdar` and the other combinations. PicoLisp is MIT-licensed, © Software Lab, Alexander Burger. Since 2020 the current PicoLisp is **pil21**, which is written in PicoLisp itself and compiled through LLVM, so the line-by-line details here belong to the older 64-bit assembly implementation; the ideas carry over. Current sources are at [software-lab.de](https://software-lab.de/down.html).

```
(code 'doCaar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCadr 2)
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
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCdar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCddr 2)
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
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCaaar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCaadr 2)
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
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCadar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCaddr 2)
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
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCdaar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCdadr 2)
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
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCddar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCdddr 2)
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
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCaaaar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCaaadr 2)
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
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCaadar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCaaddr 2)
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
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCadaar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCadadr 2)
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
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCaddar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCadddr 2)
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
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   pop X
   ret

(code 'doCdaaar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCdaadr 2)
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
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCdadar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCdaddr 2)
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
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCddaar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCddadr 2)
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
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCdddar 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval
   num E  # Need variable
   jnz varErrEX
   ld E (E)  # Take CAR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret

(code 'doCddddr 2)
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
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   cmp E Nil  # Need list
   if ne
      atom E
      jnz lstErrEX
   end
   ld E (E CDR)  # Take CDR
   pop X
   ret
```
