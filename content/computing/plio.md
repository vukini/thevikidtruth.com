---
title: Input / Output IO
date: '2021-08-28T07:09:06+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
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
topics:
- lisp
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

Here is the truth about I/O in PicoLisp: **everything is a stream or a list of characters, and the same functions that print to your terminal can print into a socket, a file or a string.** Once you meet `in`, `out` and `prin`, the rest is composition.

### What it is, in plain words

PicoLisp I/O is built from a few ideas:

- **Current input / output** – redirected with `in` and `out` for the dynamic extent of a body.
- **Characters and lines** – `char`, `line`, `read`, `skip`.
- **Printing** – `prin`, `prinl`, `print`, `println`, `space`, `pack`.
- **Files and processes** – pathnames, `pipe`, HTTP via `@lib/http.l`.
- **Binary** – `rd`, `wr` for raw bytes when text isn't enough.

There is no separate "file object" API to memorise – you bind the current stream and use the same readers and writers.

### Why it matters

Web handlers, CGI, templating and DB dumps in PicoLisp are all I/O redirection plus printing. Understanding `out`/`in` means understanding how Pil apps talk to the world without a maze of classes.

### An everyday analogy: a funnel you can aim

Instead of every tool having its own hose, PicoLisp gives you one funnel (`prin`) and lets you aim it at the sink, the bucket or the neighbour's tank (`out "file"`, `out (pipe …)`, HTTP response). Same funnel, different target.

```mermaid
flowchart LR
  B[body of code] --> P[prin / print]
  P --> C[current output]
  O["(out target …)"] --> C
```

### A hands-on example

```lisp
# Write a file
(out "hello.txt"
   (prinl "Hello from Vikix")
   (println (date) (time)) )

# Read it back
(in "hello.txt"
   (until (eof)
      (println (line T)) ) )

# Capture into a string
(pack
   (list
      (print "x=" 3)
      (prin " ")
      (print "y=" 4) ) )

# Pipe
(in '(pipe (exec "uname" "-a"))
   (prinl (line T)) )

# HTTP server fragment (after loading http/xhtml)
(de go ()
   (html 0 "Hi" NIL NIL
      (<h1> "Hello")
      (<p> "Uptime thoughts go here") ) )
```

`print` produces a readable, `read`-able representation (with quotes); `prin` prints raw. Choose consciously – especially when emitting HTML (where `@lib/xhtml.l` helpers already escape).

### Common misconceptions

- **"`prin` and `print` are synonyms."** They differ on quoting and separators.
- **"You must close files."** `in`/`out` close when the body returns (even on throw).
- **"Binary needs a different language."** Use `rd`/`wr` and sizes.
- **"HTTP is separate."** It's streams plus libraries.

### Pretty-printing and debugging

`(pretty Expr)` and friends help you see structure. During HTTP development, temporarily `(out 2 (println …))` to write traces to stderr without corrupting the response body. For large dumps, prefer writing files with `out` over flooding the console.

Remember that `read` reads one Pil expression – great for config files written as s-expressions, surprising if you expected line-oriented text (use `line` for that).

### Connections

- [PicoLisp](picolisp.md), [PicoLisp Tutorials](piltutorials.md), [Pil Box](plbox.md).
- [PicoLisp DB](pildb.md), [with-output-to-string](withoutputtostring.md) (CL cousin).

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
