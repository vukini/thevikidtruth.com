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
draft: false
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

### The plain idea and why it matters

Jumping to a specific line is one of the most common things you do in an editor, especially when a compiler or stack trace says "error on line 282". [Vim](vikidvim.md) gives you several quick ways to get there, both from inside the file and when first opening it, so you never scroll hunting for a line number.

### The methods, explained

- `282G` and `282gg` both jump to line 282. `G` on its own goes to the end of the file, `gg` to the top; prefix either with a number to land exactly there.
- `:282` then Enter is the command-line way, the same mechanism scripts and plugins use.
- `vim +282 file` opens the file already sitting on line 282, perfect straight from an error message.
- `vim +/symbolName file` opens the file at the first match of `symbolName`, handy when you know *what* broke but not *where*.

A tip that pairs with these: turn on line numbers with `:set number` (or relative numbers with `:set relativenumber`), so the counts a compiler reports line up with what you see.

### An everyday analogy

It is the difference between flipping through a book page by page and simply saying "page 282" to a librarian who opens it there instantly. The line number is the page number; these commands are how you tell Vim the page.

### How it connects

- [Vikid's Vim Notes](vikidvim.md): the rest of my Vim tips.
- [Linux](linux.md): where you will most often meet Vim, on remote servers.

The truth revealed: the fastest way through a file is never to travel it at all, but to name your destination, and a good editor should take you straight there.
