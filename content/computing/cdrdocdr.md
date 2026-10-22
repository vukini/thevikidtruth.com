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
draft: true
review: update
---

[subr.l](subrl.md)

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
