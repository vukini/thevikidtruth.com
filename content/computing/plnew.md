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
