---
title: Goto line Vim
date: '2017-06-27T03:44:52+04:00'
lastmod: '2017-06-27T03:46:57+04:00'
original_id: '{A1163}'
original_name: gotolinevim
original_blob: blob/B/6/046.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: gotolinevim
draft: true
review: update
topics:
- tools
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) |
  [The Compiler](thecompiler.md) |
  [Identifiers](identifier.md) |
  [Literals](literals.md) |
  [storage_linkage](storagelinkage.md) |
  [emacs](emacs.md) | [computing](computing.md) | [vim notes](vikidvim.md)

# [Goto line Vim](gotolinevim.md)

You your program crashes on line 282, how do you get there quickly?

If your in the file already use:

**method 1**

```
282G
```

**method 2**

```
282gg
```

**method 3**

```
:282<CR>
```

**If you need to open the file on the command line, use:**

```
$ vim +282 file
```

you can even try

```
$ vim +/symbolName file
```

and it will get you to the first place `symbolName` is found in the file.

```

```

  [back to vim notes](vikidvim.md)
