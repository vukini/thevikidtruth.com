---
title: 'The PicoLisp Machine'
date: '2016-11-25T22:39:56+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A345}'
original_name: pilmachine
original_blob: blob/B/11/305.txt
revisions: 82
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pilmachine
draft: false
topics:
- lisp
---

# The PicoLisp Machine

One of the key features of PicoLisp is that high-level constructs of the language map directly onto the underlying machinery, which makes the whole system both understandable and predictable. These are my notes on that machinery. I first wrote them in the pil64 days and revised them in October 2026 against **pil21 (26.9)** and its [reference manual](https://software-lab.de/doc/ref.html#vm). The good news is that the data model described here is **the same in pil21**. Only the implementation underneath changed: from C (pil32) to a PicoLisp-written assembler (pil64) to PicoLisp-generated LLVM IR (pil21).

### Everything is a cell

The most fundamental data type is **the cell**, the building block for all other data types. On 64-bit PicoLisp a cell is two machine words, 16 bytes:

```
         +-----+-----+
         | CAR | CDR |
         +-----+-----+
```

All memory is a free list of cells. The garbage collector (mark and sweep) returns cells to it. There are no extra string spaces or special areas, except the interpreter's own code and globals and the hardware stack.

### Data types

```
                       cell
                        |
            +-----------+-----------+
            |           |           |
         Number       Symbol       Pair
        S010 S100      1000        0000
       (cnt | big)      |
                        |
   +--------+-----------+-----------+
   |        |           |           |
  NIL   Internal    Transient    External
```

The interpreter knows the type of every value from the **lowest four bits of the pointer** itself. Cells are 16-byte aligned, so those bits are free to use as tags:

```
   pair  xxxxxxxx ... xxxx 0000    points at the start of a cell
   cnt   xxxxxxxx ... xxxx S010    short number, value is IN the pointer
   big   xxxxxxxx ... xxxx S100    bignum, points 4 bytes into a cell
   sym   xxxxxxxx ... xxxx 1000    symbol, points at the CDR (8 bytes in)
```

`S` is the sign bit. A number is recognised when bit 1 (short) or bit 2 (big) is set; a symbol when bit 3 is set and bits 1 and 2 are clear. During garbage collection a spare low bit in each cell serves as the mark bit.

You can see this from the REPL with `adr`, which returns the raw address:

```picolisp
: (& 15 (adr (box 7)))       # a symbol: low bits 1000
-> 8
: (& 15 (adr (cons 1 2)))    # a pair: low bits 0000
-> 0
```

### Numbers

Values of **up to 60 bits** are "short numbers" (`cnt`). The value lives in the pointer itself and takes no heap space:

```
      xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxS010
```

Larger values are **bignums**: a chain of cells whose CARs hold 64-bit "digits", least significant first. The final CDR holds the remaining bits as a short number:

```
      +-----+-----+     +-----+-----+     +-----+-----+
      | DIG |  ---+---> | DIG |  ---+---> | DIG | CNT |
      +-----+-----+     +-----+-----+     +-----+-----+
```

That is why `(** 2 100)` just works, and why fixed-point decimals (see [Working With Numbers](pilnumbers.md)) never lose precision.

### Symbols

A symbol is a cell whose CDR is its **value** (VAL) and whose CAR is its **tail**: a property list, terminated by the symbol's name stored as a number (UTF-8 bytes packed into a short number or bignum):

```
            Symbol
            |
            V
      +-----+-----+
      |  |  | VAL |      reading a value is one memory access:
      +--+--+-----+      the pointer points straight at VAL
         | tail
         V
      +-----+-----+     +-----+-----+
      |  |  |  ---+---> | KEY |  ---+---> name
      +--+--+-----+     +-----+-----+
         |
         V
      +-----+-----+
      | VAL | KEY |       a KEY/VAL property; a lone KEY means T
      +-----+-----+
```

The four kinds of symbol all share this layout:

- **NIL** exists exactly once, and has a special structure so that both `(car NIL)` and `(cdr NIL)` are NIL. It is the empty list, false, the empty string and end-of-file all at once.
- **Internal** symbols are interned into a **namespace**, an index tree, so they can be found by name. In pil21, namespaces are first-class: `pico` is the default, and `(symbols 'myns 'pico)` creates and switches between them.
- **Transient** symbols (`"strings"`) are interned only while the current file is being read, so they act like strings and file-local statics. `box` and `new` create anonymous ones (see [box](plbox.md) and [new](plnew.md)).
- **External** symbols (`{A1}`) are database objects. Their name encodes the file and block, and they are loaded and saved transparently (see [PicoLisp DB](pildb.md)).

### Evaluation

The evaluator follows three rules:

1. A number evaluates to itself.
2. A symbol evaluates to its VAL.
3. A list is a function call: evaluate the CAR to get a function, then apply it to the rest.

A function is either a built-in (a number: the address of machine code) or a **list** `(params . body)`. That is why `(de f (X) ...)` is just `(setq f '((X) ...))` (see [quote](pilquote.md)).

Binding is **dynamic and shallow**. When a function is called, the old values of its parameter symbols are saved on the stack, the new ones are stored directly in VAL, and the old ones are restored on return. Looking up a variable therefore costs nothing; it is always "the current VAL". That is the main reason the interpreter can be fast without a compiler. It is also why naming conventions (capitalised locals, `*Globals`) and, in pil21, `private` and namespaces matter.

### Where to read further

- The official reference's [VM section](https://software-lab.de/doc/ref.html#vm), which these diagrams follow.
- [PicoLisp Sources](pilsource.md): the pil21 `src/*.l` files that implement all this (`gc.l`, `big.l`, `sym.l`, `main.l`).
- [PicoLisp ASM](pilasm.md): the pil64 virtual machine, now historical.
- [Find Boxes in Lists](findboxes.md): the cell model from the programmer's side.
