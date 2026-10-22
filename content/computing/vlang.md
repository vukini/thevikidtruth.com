---
title: The V Programming Language
date: '2022-08-25T02:35:41+04:00'
lastmod: '2022-08-25T02:37:45+04:00'
original_id: '{A1707}'
original_name: vlang
original_blob: blob/B/11/066.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: vlang
draft: false
---

[Read This!](caveatemptor.md) | | [Quick Links](quicklinks.md) | [Algorithms](algorithms.md) | [AssemblyLanguage](assemblylanguage.md) | [BASH](bash.md) |   [C-Programmming](cprogramming.md) |
[CommonLisp](commonlisp.md) |
[Computer Security](computersecurity.md) |  [Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) |
[Functional Programming](functional.md) |
[Firewalls](firewalls.md) |   [Git](git.md) | [Haskell](haskell.md) | [Javascript](javascript.md) | [Julia](julia.md) | [Social Engineering](internetexploitation.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) |
[Linux](linux.md) |
[Python](python.md) |
[Operating Systems](os.md) |
[Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |  [Open Data Science](opendatascience.md) |
[Networking](networking.md) | [Machine Learning](machinelearning.md) | [Racket](racket.md) | [Scheme](scheme.md) |
[Unity](unity.md) | [vim](vim.md) | [V](vlang.md) |
[Web Development](webdevelopment.md) | [Windows WSL](windowswsl.md)

# The V Programming Language

## Variable

Variable are **immutable** by default

```
  x:= 100
```

use the ` mut ` keyword to make it mutable.

### Naming Convetions

- start with lower case
- no uppercase alphabet
- no special chars except _
- names can end in numbers or _
- use snake_case

Declare variable with ` := `, use ` = ` to reassign.

#### Parallel Declaration and Assignment

```
  a, b, c := 1, 2 3
    mut d, mut e := "hello" , "hi"
```

reassign with the same type only:

```
d, e = "what" , "who"
```
