---
title: Input / Output IO
date: '2021-08-28T07:09:06+04:00'
lastmod: '2021-08-28T07:09:06+04:00'
original_id: '{A1502}'
original_name: plio
original_blob: blob/B/7/611.txt
revisions: 1
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: plio
draft: false
---

![picos](/assets/picos.png)
{.right}
 [computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [JavaScript](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Penti](penti.md)

# Input / Output IO

Comments can be embedded in the input stream with the hash # character.
Everything up to the end of that line will be ignored by the reader.

```
: (* 1 2 3)  # This is a comment
-> 6
```

A comment spanning several lines (a block comment) may be enclosed between

```
#{ and }#
```
