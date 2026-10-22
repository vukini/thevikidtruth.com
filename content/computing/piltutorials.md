---
title: Picolisp Tutorials
date: '2017-06-24T03:42:32+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
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

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
  [Picolisp By Example](picolispbyexample.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md) | [Networking](networking.md) | [Machine Learning](machinelearning.md) |
  [Git](git.md) |
  [Machine Learning](machinelearning.md) |
  [Algorithms](algorithms.md) |
  [Open Data Science](opendatascience.md) |

# Picolisp Tutorials

Here is the truth about learning PicoLisp: **the language is small enough that tutorials can take you from zero to a working app without a 900-page book.** The hard part is not syntax – it is trusting that lists, symbols and a handful of forms really are enough.

### What it is, in plain words

This page is the hub for PicoLisp tutorials on this site: short, concrete paths into the language, the database and the application style Alexander Burger designed. Official docs at [software-lab.de](https://software-lab.de) remain the source of truth; these notes are how I keep the paths I actually walked.

### Why it matters

PicoLisp rewards apprenticeship. A weekend with `quote`, `fill` and a tiny DB-backed form teaches more about interactive systems than a month of framework tutorials elsewhere. If Vikix is a Linux you understand, PicoLisp is a language you can hold in your head.

### An everyday analogy: a workshop tour

The tutorials are stations on a workshop tour: first how to hold the tools (`quote`), then a small project (the health app), then you start inventing. Skip the tour and the tools look like clutter. Take it, and the clutter becomes a kit.

### A hands-on path

1. Install PicoLisp (`sudo xbps-install -S picolisp` on Void) and run `pil +`.
2. Work through [quote](pilquote.md) – why quoting exists and how evaluation walks lists.
3. Read [PicoLisp by Example](picolispbyexample.md) and retype the examples; don't just glance.
4. Skim [Pil Numbers](pilnumbers.md), [Pil I/O](plio.md) and [Pil Box](plbox.md) when those topics appear.
5. Build or study [The Health Application](pilhealth.md) – entities, forms, persistence.
6. Keep [Pil Sources](pilsource.md) and [Pil Machine](pilmachine.md) nearby when you wonder how deep the rabbit hole goes.

```lisp
(de square (N) (* N N))
(mapcar square (range 1 5))   # (1 4 9 16 25)
(load "@lib/http.l" "@lib/xhtml.l" "@lib/form.l")
```

When something surprises you, `(doc 'map)` and the REPL are the tutors.

### Tutorial index

- [quote](pilquote.md) – evaluation and quoting
- [The Health Application](pilhealth.md) – end-to-end app
- [PicoLisp by Example](picolispbyexample.md)
- [Pil Examples Examined](pilexamplesexamined.md)
- [Pil Numbers](pilnumbers.md) · [Pil I/O](plio.md) · [Pil Box](plbox.md)
- [PicoLisp DB](pildb.md) · [Pil Chat](pilchat.md) · [Pil Life](pillife.md)

### Common misconceptions

- **"I need a big framework first."** You need `pil +` and curiosity.
- **"Tutorials replace the docs."** They don't. They sequence them.
- **"PicoLisp is only for Retro fans."** It ships production apps today.
- **"I must memorise every function."** You must learn how to ask the image (`doc`, `show`, source).

### How I take notes while learning

Keep a `scratch.l` open next to the tutorial. After every example, change one thing – a name, a boundary, a wrong input – and see what the REPL says. Paste the survivors into your own file. Tutorials explain; your scratch file remembers.

When an official demo app exists (health, chat), run it before reading the source. Predicting what a click does, then confirming, wires the concepts faster than reading alone.

### A four-week path that actually works

Here is the route I would give a friend starting in 2026 with pil21:

1. **Week one: the REPL and lists.** Learn `de`, `let`, `if`, `cond`, `mapcar`, `filter`, `make`/`link` and the cell model on [Find Boxes in Lists](findboxes.md). Do small exercises: reverse a list by hand, count words in a file, flatten a nested list.
2. **Week two: symbols and evaluation.** Quoting, transient versus internal symbols, property lists, [box](plbox.md), and why PicoLisp uses dynamic binding. Read the [Vikid PicoLisp Tutorial](pltutorial.md) here.
3. **Week three: objects and I/O.** `class`, `dm`, [new](plnew.md), `show`, then streams with `in`, `out` and `pipe` from [Input / Output](plio.md). Write a tiny command-line tool that reads a CSV and prints a report.
4. **Week four: the database and the GUI.** Entities and relations, `+Ref` and `+Key` indexes, `collect` and Pilog queries, then the form library. Build something small but real: a reading log, a recipe box, a link collection. See [PicoLisp DB](pildb.md) and [Application Development](appdev.md).

Each week ends with one small program you would actually use. That is the whole trick.

### A worked mini exercise: word frequency

Retype this, run it on any text file, then change it.

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

(freq "README.md")
```

Things to try: what happens with an empty file? How would you ignore short words? Can you replace the association list with an `idx` tree for big files? Each question sends you back to the reference, which is exactly where you want to end up.

### Where to ask

The PicoLisp mailing list and the `#picolisp` channel on Libera.Chat are small and friendly, and the author, Alexander Burger, is often there in person. Before you post, include `(version)` output and the smallest piece of code that shows the problem.

### Connections

- [PicoLisp](picolisp.md), [PicoLisp Machine](pilmachine.md), [Pil Sources](pilsource.md).
- [Databases](databases.md), [Lambda Calculus](lambdacalculus.md).

- [quote](pilquote.md)
- [Here](pilquote.md)
- [The Health Application](pilhealth.md)
