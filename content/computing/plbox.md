---
title: box
date: '2021-08-28T06:45:21+04:00'
lastmod: '2021-08-28T06:54:49+04:00'
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
