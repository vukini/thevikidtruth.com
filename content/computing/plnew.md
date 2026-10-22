---
title: new
date: '2021-08-28T06:47:27+04:00'
lastmod: '2021-08-28T06:53:26+04:00'
original_id: '{A1501}'
original_name: plnew
original_blob: blob/B/7/576.txt
revisions: 6
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: plnew
draft: false
topics:
- lisp
---

[Computing](computing.md) | [Picolisp](picolisp.md) | [The Picolisp Reference](http://software-lab.de/doc/ref.html#vm) | [ASM](pilasm.md) |
[Pil Tutorials](piltutorials.md) |

# new

Here is the truth about objects in PicoLisp: **an object is just a symbol.** Its value is a list of classes, and its properties hold the data. `new` is the function that makes one, and it is short enough that you can understand the whole object system from it.

### What it is, in plain words

`(new)` with no arguments creates a fresh **anonymous symbol** (it prints like `$177305325561003`). Give it a list of classes and it sets the symbol's value to that list, then sends the object the special `T` message, which plays the role of a constructor. Give it a flag first and the new symbol is **external**: it lives in the database and survives a restart.

So `new` does three jobs depending on the arguments:

| Call | Result |
|---|---|
| `(new)` | a bare anonymous symbol, like [box](plbox.md) with no value |
| `(new '(+Pt) 3 4)` | an in-memory object of class `+Pt`, initialised by its `T` method |
| `(new T '(+Item) 'nm "Nut")` | a persistent database object in file 1 |

The reference text below gives the full signature.

### Why it matters

PicoLisp's object system is *message passing* in the Smalltalk tradition, but with no extra machinery. Methods are functions stored in the class symbol; inheritance is the class list; properties are the symbol's property list. Once you see that `new` only builds a symbol and sends `T`, you can debug any object with `show`, and you understand how the database's entities are just the same objects made persistent.

### An everyday analogy: a blank name badge

`new` hands you a blank name badge (the symbol). If you also say which club it belongs to (the class list), the club secretary immediately fills in your details on the back (the `T` message). If you ask for a permanent membership (`T` flag), your badge is also filed in the club's records (the database) and will still be there next year.

### A hands-on example

```picolisp
$ pil +
: (class +Pt)
-> +Pt
: (dm T (X Y)            # the constructor, run by new
   (=: x X)
   (=: y Y) )
-> T
: (dm len> ()
   (sqrt (+ (* (: x) (: x)) (* (: y) (: y)))) )
-> len>
: (setq P (new '(+Pt) 3 4))
-> $177305325561100
: (len> P)
-> 5
: (show P)
$177305325561100 (+Pt)
   y 4
   x 3
-> $177305325561100
: (type P)
-> (+Pt)
: (isa '+Pt P)
-> $177305325561100
```

`=:` stores a property on `This` (the current object) and `:` reads one. `show` reveals the truth: an object is a symbol whose value is `(+Pt)` and whose properties are `x` and `y`.

Without a `T` method, `new` treats the remaining arguments as key/value pairs:

```picolisp
: (class +Tag)
: (show (new '(+Tag) 'name "lisp" 'count 3))
$177305325561200 (+Tag)
   count 3
   name "lisp"
```

For the database you normally use `new!`, which wraps the creation in a transaction (`dbSync`, create, `commit 'upd`) so concurrent processes stay consistent. See [PicoLisp DB](pildb.md).

### Common misconceptions

- **"Objects need a special heap."** No, they are ordinary symbols, garbage collected like any other.
- **"`T` is a boolean here."** In `(dm T ...)` it is the name of the initialisation message, and as the first argument to `new` it means "external, in database file 1". Context decides.
- **"Methods live in the object."** They live in the class symbols. The object only points at its classes.
- **"`new` and `box` are unrelated."** `(box Val)` is essentially `new` that also sets the value. Both create anonymous symbols.

### Connections

- [box](plbox.md), [PicoLisp](picolisp.md), [PicoLisp DB](pildb.md), [Application Development](appdev.md).
- [Objects in C](object.md) – the word "object" meaning raw memory, for contrast.
- [Cuis Smalltalk](cuissmalltalk.md) and [JS Objects](jsobjects.md) – other message and prototype models.

### Reference


```
(new ['flg|num] ['typ ['any ..]]) -> obj 
```

Creates and returns a new object.

If **flg** is given and **non-NIL**, the new object will be an **external symbol**
(created in database file 1 if T, or in the corresponding database file if num is given).

**typ** (typically a list of classes) is assigned to the VAL,
and the *initial T message* is sent with the arguments any to the new object.

*If no T message is defined for the classes in typ or their superclasses*,
the any arguments should evaluate to alternating keys and values for the initialization of the new object.

```
: (new)
-> $134426427
: (new T '(+Address))
-> {A3}
```

```
(new! 'typ ['any ..]) -> obj
```

Transaction wrapper function for new.
` (new! '(+Cls) 'key 'val ...) ` is equivalent to ` (dbSync) (new (db: +Cls) '(+Cls) 'key 'val ...) (commit 'upd).`

See also request!, set!, put! and inc!.

```
: (new! '(+Item)  # Create a new item
   'nr 2                      # Item number
   'nm "Spare Part"           # Description
   'sup (db 'nr '+CuSu 2)     # Supplier
   'inv 100                   # Inventory
   'pr 12.50 )                # Price
```

see also [box](plbox.md), object, class, type, isa, send and Database.
