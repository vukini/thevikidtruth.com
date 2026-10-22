---
title: box
date: '2021-08-28T06:45:21+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1500}'
original_name: plbox
original_blob: blob/B/7/601.txt
revisions: 7
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: plbox
draft: false
topics:
- lisp
---

[Computing](computing.md) | [Picolisp](picolisp.md) | [ASM](pilasm.md) |
[Pil Tutorials](piltutorials.md) |

# box

Here is the truth about `box` in PicoLisp: **it hands you a brand-new symbol that nobody else can name.** That sounds like nothing, but a symbol is PicoLisp's universal container: it has a value, a property list and an identity. A box is a private, mutable place you can pass around.

### What it is, in plain words

`(box Val)` creates and returns a new **anonymous symbol** whose value is `Val`. It is not interned, so it has no name you can type. It prints as something like `$177305325560446`, which is simply its address. You read the value with `val` and change it with `set`, `inc`, `dec`, `push` and friends. Because it is a full symbol, you can also hang properties off it with `put` and `get`.

```picolisp
: (setq Cnt (box 0))
-> $177305325560446
: (sym? Cnt)
-> T
: (inc Cnt)
-> 1
: (val Cnt)
-> 1
```

`box` is a close cousin of [new](plnew.md): `(new)` makes the same kind of anonymous symbol with no value. Objects are just anonymous symbols whose value is a class list, so a box is "an object without a class".

### Why it matters

- **Shared state without globals.** Two functions can both hold the same box and see each other's updates, without polluting the global namespace with a `*Counter`.
- **Avoiding dynamic-binding surprises.** PicoLisp uses dynamic binding, so a closure that refers to a variable by name can see the wrong binding later. Capturing a box (with `curry` or `job`) captures the *container*, not the name.
- **It shows how simple the object system is.** Values, properties and identity are all a symbol already gives you.

### An everyday analogy: a labelled tray

A number written on a whiteboard is gone once someone erases it. A tray with no label of its own, that you carry around, stays the same tray even when you swap the card inside. Anyone you hand the tray to sees the current card. The tray is a box; the card is its value.

### A hands-on example: a counter factory

```picolisp
(de make-counter ()
   (let C (box 0)
      (list
         (cons 'inc (curry (C) () (inc C)))
         (cons 'get (curry (C) () (val C))) ) ) )

(setq Ctr (make-counter))
((cdr (assoc 'inc Ctr)))
((cdr (assoc 'inc Ctr)))
((cdr (assoc 'get Ctr)))   # -> 2
```

`curry` builds a new function with `C` replaced by the actual box, so every counter has its own private box even though they all came from the same code.

A box with properties, a quick record without defining a class:

```picolisp
: (setq S (box))
: (put S 'name "Ali")
: (put S 'lang 'picolisp)
: (show S)
$177305325561003 NIL
   lang picolisp
   name "Ali"
```

And a lazily computed cache:

```picolisp
(setq *Cache (box))
(de config ()
   (or (val *Cache)
      (set *Cache (in "config.l" (read))) ) )
```

### Common misconceptions

- **"A box is a cons cell."** No. A cons cell is a list cell with a CAR and CDR (see [Find Boxes in Lists](findboxes.md)). A `box` is a *symbol*, with a value, properties and a name slot.
- **"`setq` would do the same."** `setq` changes what a *named* variable holds. A box is a container you can hand to other code, and it keeps its identity wherever it goes.
- **"Boxes are a hash table."** One box holds one value plus properties. For key/value maps use `idx` trees, association lists, or the [PicoLisp DB](pildb.md).
- **"Boxes persist."** They live in memory and vanish when the process ends. For data that must survive, use external symbols created with `(new T ...)`.

### Boxes versus DB entities

If the value must survive a restart or be shared between processes, it belongs in the database. Boxes are for per-process state: counters, caches, the current selection in a GUI, scratch space for one request.

### Connections

- [new](plnew.md), [PicoLisp](picolisp.md), [Input/Output](plio.md), [PicoLisp Tutorials](piltutorials.md).
- [Find Boxes in Lists](findboxes.md) – the other kind of "box": cells.
- [JavaScript Variables](jsvariable.md) and [JS Scope](jsscope.md) – closures and mutable bindings elsewhere.

### Reference

```
: (box 'any) -> sym 
```

Creates and returns a new anonymous symbol. The initial value is set to the any argument.

```
: (show (box '(A B C)))
$134425627 (A B C)
-> $134425627
```

see [new](plnew.md)
