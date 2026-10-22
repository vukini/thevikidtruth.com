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
---

[Computing](computing.md) | [Picolisp](picolisp.md) | [ASM](pilasm.md) |
[Pil Tutorials](piltutorials.md) |

# box

Here is the truth about `box` in PicoLisp: **it is a tiny mutable cell – a cons whose purpose is to hold something that changes while the identity of the cell stays put.** When you need a shared, updatable place without inventing a class, you reach for a box.

### What it is, in plain words

`(box Val)` creates a new cell with `Val` as its value. Access and update with `val` and `set` (or related patterns). Because PicoLisp is dynamically typed and list-oriented, a box is often enough where another language would demand an object or an `IORef`.

```lisp
(setq Cnt (box 0))
(set Cnt (inc (val Cnt)))
(val Cnt)   # 1
```

### Why it matters

Closures, GUIs and servers all need "a place to keep the current thing". Boxes give you that place without ceremony. They also teach something deeper about PicoLisp: mutation is available, explicit and usually localised – functional style by default, cells when you need them.

### An everyday analogy: a labelled tray

A number written on the blackboard gets erased when replaced. A tray labelled "count" stays the tray even when you swap the card inside. Code that holds the tray still holds the right thing after an update. That tray is a box.

### A hands-on example

```lisp
# Counter factory
(de make-counter ()
   (let C (box 0)
      (list
         (cons 'inc  (curry (C) () (set C (inc (val C)))))
         (cons 'get  (curry (C) () (val C)))
         (cons 'reset (curry (C) () (set C 0))) ) ) )

(setq Ctr (make-counter))
((cdr (assoc 'inc Ctr)))
((cdr (assoc 'inc Ctr)))
((cdr (assoc 'get Ctr)))   # 2
```

A simpler everyday use – caching a computed value:

```lisp
(setq Cache (box))
(de expensive ()
   (or (val Cache)
      (set Cache (long-computation)) ) )
```

You'll also meet boxes in GUI and form code when a field needs a stable identity while its contents change across requests.

### Common misconceptions

- **"Boxes are hash tables."** They're single cells. Use indexes / `idx` or the DB for maps.
- **"Mutation means the language isn't functional."** PicoLisp lets you choose. Prefer pure functions; box when state is the point.
- **"`setq` already mutates."** `setq` rebinds a symbol. A box mutates through an indirection you can pass around.
- **"I need boxes everywhere."** Most Pil code never touches them. That's healthy.

### Boxes versus DB entities

If the value must survive process restart or be shared across users, it belongs in the [PicoLisp DB](pildb.md), not a box. Boxes are for in-memory, per-process state: counters, caches, UI selection, "current request" scratch. Mixing the two up is how people lose data on restart and blame the language.

### Connections

- [PicoLisp](picolisp.md), [Pil I/O](plio.md), [PicoLisp Tutorials](piltutorials.md).
- [JavaScript Variables](jsvariable.md) – a different take on mutable bindings.

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
