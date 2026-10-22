---
title: gc.c
date: '2017-06-19T03:30:25+04:00'
lastmod: '2017-06-29T01:56:32+04:00'
original_id: '{A1137}'
original_name: gcc
original_blob: blob/B/6/055.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: gcc
draft: false
topics:
- lisp
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
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

# [gc.c](gcc.md)

### What gc.c does

This file is PicoLisp's **garbage collector**: the part of the interpreter that automatically reclaims memory no longer in use. In a language like Lisp you never call `free()`; you just make cells (`cons`, symbols, numbers) and let them go. The garbage collector periodically finds everything still reachable from the program's roots, keeps it, and recycles the rest. PicoLisp uses a classic **mark-and-sweep** collector: a first pass *marks* every cell reachable from the stack and global symbols, and a second pass *sweeps* the heap, returning unmarked cells to the free list. Reading it is a wonderfully compact way to see how automatic memory management actually works, in a few hundred lines rather than the tens of thousands a production JVM collector takes.

> **Reading this in 2026.** This page reproduces a file from the PicoLisp sources, as I studied them around 2017 (the 32-bit C / pil32 implementation). PicoLisp is MIT-licensed, © Software Lab, Alexander Burger. Since 2020 the current PicoLisp is **pil21**, written in PicoLisp itself and compiled through LLVM, so the line-by-line details here belong to the older implementation; the ideas carry over. Current sources are at [software-lab.de](https://software-lab.de/down.html).

```
/* 01may14abu
 * (c) Software Lab. Alexander Burger
 */

#include "pico.h"

/* Mark data */
static void mark(any x) {
   cell *p;

   while (num((p = cellPtr(x))->cdr) & 1) {
      *(word*)&cdr(p) &= ~1;
      if (!isNum(x))
         mark(p->car);
      x = p->cdr;
   }
}

/* Garbage collector */
static void gc(long c) {
   any p, *pp, x;
   heap *h;
   int i;

   val(DB) = Nil;
   h = Heaps;
   do {
      p = h->cells + CELLS-1;
      do
         *(word*)&cdr(p) |= 1;
      while (--p >= h->cells);
   } while (h = h->next);
   /* Mark */
   mark(Nil+1);
   mark(Alarm),  mark(Sigio),  mark(Line),  mark(Zero),  mark(One);
   for (i = 0; i < IHASH; ++i)
      mark(Intern[i]),  mark(Transient[i]);
   mark(ApplyArgs),  mark(ApplyBody);
   for (p = Env.stack; p; p = cdr(p))
      mark(car(p));
   for (p = (any)Env.bind;  p;  p = (any)((bindFrame*)p)->link)
      for (i = ((bindFrame*)p)->cnt;  --i >= 0;) {
         mark(((bindFrame*)p)->bnd[i].sym);
         mark(((bindFrame*)p)->bnd[i].val);
      }
   for (p = (any)CatchPtr; p; p = (any)((catchFrame*)p)->link) {
      if (((catchFrame*)p)->tag)
         mark(((catchFrame*)p)->tag);
      mark(((catchFrame*)p)->fin);
   }
   for (i = 0; i < EHASH; ++i)
      for (p = Extern[i];  isCell(p);  p = (any)(num(p->cdr) & ~1))
         if (num(val(p->car)) & 1) {
            for (x = tail1(p->car); !isSym(x); x = cdr(cellPtr(x)));
            if ((x = (any)(num(x) & ~1)) == At2  ||  x == At3)
               mark(p->car);  // Keep if dirty or deleted
         }
   if (num(val(val(DB) = DbVal)) & 1) {
      val(DbVal) = cdr(numCell(DbTail)) = Nil;
      tail(DbVal) = ext(DbTail);
   }
   for (i = 0; i < EHASH; ++i)
      for (pp = Extern + i;  isCell(p = *pp);)
         if (num(val(p->car)) & 1)
            *pp = (cell*)(num(p->cdr) & ~1);
         else
            *(word*)(pp = &cdr(p)) &= ~1;
   /* Sweep */
   Avail = NULL;
   h = Heaps;
   if (c) {
      do {
         p = h->cells + CELLS-1;
         do
            if (num(p->cdr) & 1)
               Free(p),  --c;
         while (--p >= h->cells);
      } while (h = h->next);
      while (c >= 0)
         heapAlloc(),  c -= CELLS;
   }
   else {
      heap **hp = &Heaps;
      cell *av;

      do {
         c = CELLS;
         av = Avail;
         p = h->cells + CELLS-1;
         do
            if (num(p->cdr) & 1)
               Free(p),  --c;
         while (--p >= h->cells);
         if (c)
            hp = &h->next,  h = h->next;
         else
            Avail = av,  h = h->next,  free(*hp),  *hp = h;
      } while (h);
   }
}

// (gc ['cnt]) -> cnt | NIL
any doGc(any x) {
   x = cdr(x),  x = EVAL(car(x));
   val(At) = val(At2) = Nil;
   gc(isNum(x)? CELLS*unBox(x) : CELLS);
   return x;
}

/* Construct a cell */
any cons(any x, any y) {
   cell *p;

   if (!(p = Avail)) {
      cell c1, c2;

      Push(c1,x);
      Push(c2,y);
      gc(CELLS);
      drop(c1);
      p = Avail;
   }
   Avail = p->car;
   p->car = x;
   p->cdr = y;
   return p;
}

/* Construct a symbol */
any consSym(any v, any x) {
   cell *p;

   if (!(p = Avail)) {
      cell c1, c2;

      Push(c1,v);
      Push(c2,x);
      gc(CELLS);
      drop(c1);
      p = Avail;
   }
   Avail = p->car;
   p = symPtr(p);
   tail(p) = x;
   val(p) = v;
   return p;
}

/* Construct a string */
any consStr(any x) {
   cell *p;

   if (!(p = Avail)) {
      cell c1;

      Push(c1,x);
      gc(CELLS);
      drop(c1);
      p = Avail;
   }
   Avail = p->car;
   p = symPtr(p);
   tail(p) = x;
   val(p) = p;
   return p;
}

/* Construct a number cell */
any consNum(word n, any x) {
   cell *p;

   if (!(p = Avail)) {
      cell c1;

      Push(c1,x);
      gc(CELLS);
      drop(c1);
      p = Avail;
   }
   Avail = p->car;
   p->car = (any)n;
   p->cdr = x;
   return numPtr(p);
}
```
