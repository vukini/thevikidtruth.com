---
title: 'PicoLisp Tutorials'
date: '2017-06-24T03:42:32+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A1147}'
original_name: piltutorials
original_blob: blob/B/7/561.txt
revisions: 14
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: piltutorials
draft: false
topics:
- lisp
---

# PicoLisp Tutorials

Here is the truth about learning PicoLisp: **the language is small enough that tutorials can take you from zero to a working app without a 900-page book.** The hard part is not the syntax. It is learning to trust that lists, symbols and a handful of forms really are enough.

### What it is, in plain words

This page is the hub for the PicoLisp tutorials on this site. They are short, concrete paths into the language, the database and the application style Alexander Burger designed. The official docs at [software-lab.de](https://software-lab.de/doc/ref.html) remain the source of truth; everything here was re-checked against **PicoLisp 26.9** (pil21) in October 2026.

### Why it matters

PicoLisp rewards apprenticeship. A weekend with `quote`, `fill` and a tiny DB-backed form teaches more about interactive systems than a month of framework tutorials elsewhere.

### An everyday analogy: a workshop tour

The tutorials are stations on a workshop tour. First you learn how to hold the tools (`quote`), then you do a small project (the Health app), then you start inventing. Skip the tour and the tools look like clutter. Take it, and the clutter becomes a kit.

### Start here (2026)

1. **Install pil21 from source.** It needs `clang` and `llvm`; see [PicoLisp Installation](../languages/picolispinstallation.md). Distro packages exist for Debian/Ubuntu, Arch (AUR), Alpine, FreeBSD, Termux and others, but they often lag a year or more behind. Void Linux and Homebrew have no package at all.
2. Run `./pil +` in the source directory (or `pil +` after a global install). The `+` turns on debug mode, which gives you `doc`, `vi`, `trace`, `debug` and friends.
3. Read the official [tutorial](https://software-lab.de/doc/tut.html) alongside these pages.

### A hands-on path

1. Work through [quote](pilquote.md): why quoting exists and how evaluation walks lists.
2. Do [The Vikid PicoLisp Tutorial](pltutorial.md): REPL tools, defining functions, debugging.
3. Retype the problems in [PicoLisp By Example](picolispbyexample.md). Don't just glance at them.
4. Dip into [Working With Numbers](pilnumbers.md), [Input/Output](plio.md), [box](plbox.md) and [new](plnew.md) as those topics come up.
5. Build or study [The Health Application](pilhealth.md): entities, forms and persistence.
6. Keep [PicoLisp Sources](pilsource.md) and [The PicoLisp Machine](pilmachine.md) nearby for when you wonder how deep the rabbit hole goes.

```picolisp
(de square (N) (* N N))
(mapcar square (range 1 5))   # -> (1 4 9 16 25)
(load "@lib/http.l" "@lib/xhtml.l" "@lib/form.l")
```

When something surprises you, `(doc 'mapcar)` (in debug mode it opens the reference in a browser) and the REPL are the tutors.

### A four-week path that actually works

This is the route I would give a friend starting today:

1. **Week one: the REPL and lists.** Learn `de`, `let`, `if`, `cond`, `mapcar`, `filter`, `make`/`link`, and the cell model on [Find Boxes in Lists](findboxes.md). Do small exercises: reverse a list by hand, count words in a file, flatten a nested list.
2. **Week two: symbols and evaluation.** Learn quoting, transient versus internal symbols, property lists, [box](plbox.md), and why PicoLisp uses dynamic binding. In pil21 also learn **namespaces** (`symbols`, `private`, `ns~sym`), because the libraries use them.
3. **Week three: objects and I/O.** Learn `class`, `dm`, [new](plnew.md) and `show`, then streams with `in`, `out` and `pipe` from [Input/Output](plio.md). Write a tiny command-line tool that reads a CSV and prints a report. `@lib/json.l` (`readJson`, `printJson`) is handy here.
4. **Week four: the database and the GUI.** Learn entities and relations, `+Ref` and `+Key` indexes, `db`, `collect` and Pilog queries, then the form library. Build something small but real: a reading log, a recipe box, a link collection. See [PicoLisp DB](pildb.md) and [Application Development](appdev.md).

Each week ends with one small program you would actually use. That is the whole trick.

### A worked mini exercise: word frequency

Retype this, run it on any text file, then change it. It is tested on 26.9.

```picolisp
(de words (File)
   (in File
      (make
         (until (eof)
            (let W (lowc (till " \t\n.,;:!?\"()" T))
               (and W (link W)) )
            (char) ) ) ) )

(de freq (File)
   (let Idx NIL
      (for W (words File)
         (accu 'Idx W 1) )
      (head 10 (flip (by cdr sort Idx))) ) )

(freq "README")
```

On the text "the cat and the dog. The end, the cat!" it returns `(("the" . 4) ("cat" . 2) ...)`.

Things to try: what happens with an empty file? How would you ignore short words? Can you replace the association list with an `idx` tree for big files? Each question sends you back to the reference, which is exactly where you want to end up.

### How I take notes while learning

I keep a `scratch.l` open next to the tutorial. After every example, change one thing (a name, a boundary, a wrong input) and see what the REPL says. Paste the survivors into your own file. Tutorials explain; your scratch file remembers.

When an example app exists (Health, Chat, Life), run it before reading the source. Predicting what a click does, then confirming it, wires the concepts in faster than reading alone.

### Common misconceptions

- **"I need a big framework first."** You need `pil +` and curiosity.
- **"Tutorials replace the docs."** They don't. They sequence them.
- **"Old tutorials still apply unchanged."** Mostly they do, but examples written for pil32/pil64 may break on pil21. Typical causes: namespaced libraries, `misc/` demos that are no longer shipped, and removed functions.
- **"I must memorise every function."** You must learn how to ask the system (`doc`, `show`, `pp`, `what`, `who`).

### Where to ask

The PicoLisp mailing list and the `#picolisp` channel on Libera.Chat are small and friendly, and the author, Alexander Burger, is often there in person. Before you post, include your `(version)` output and the smallest piece of code that shows the problem.

### Tutorial index

- [quote](pilquote.md): evaluation and quoting
- [The Vikid PicoLisp Tutorial](pltutorial.md)
- [PicoLisp By Example](picolispbyexample.md) · [PicoLisp Examples Examined](pilexamplesexamined.md)
- [Working With Numbers](pilnumbers.md) · [Input/Output](plio.md) · [box](plbox.md) · [new](plnew.md)
- [PicoLisp DB](pildb.md) · [Chat](pilchat.md) · [Life](pillife.md)
- [The Health Application](pilhealth.md): an end-to-end app

### Connections

- [PicoLisp](picolisp.md), [The PicoLisp Machine](pilmachine.md), [PicoLisp Sources](pilsource.md).
- [Databases](databases.md), [Lambda Calculus](lambdacalculus.md).
