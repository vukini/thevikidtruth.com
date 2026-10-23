---
title: 'PicoLisp Examples Examined'
date: '2017-06-19T03:09:19+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A1127}'
original_name: pilexamplesexamined
original_blob: blob/B/5/634.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pilexamplesexamined
draft: false
topics:
- lisp
---

# PicoLisp Examples Examined

[Open Data Science](opendatascience.md)

There are many PicoLisp example files and snippets around the internet. I believe one good way to learn a new language, and to see the patterns and idiomatic expressions the community uses, is to read and run real source code. That is what we do on the pages below.

### What changed since I first wrote these studies

When I wrote these in 2017, the PicoLisp tarball had a `misc/` folder full of demo programs: `life.l`, `chat`, `crc.l`, `fibo.l` and more. In today's **pil21** (I checked 26.9, October 2026), `misc/` holds only the `bigtest` and `stress.l` test scripts. The demos are gone from the distribution. So each study page now contains a complete, working program that I re-tested on 26.9, along with my original walk-through.

The other big difference is **namespaces**. Some libraries (`@lib/simul.l`, `@lib/ai.l`) now define their own namespace, so old code that calls `grid` or `disp` straight after `(load "@lib/simul.l")` fails with `grid -- Undefined`. Add `(symbols '(simul pico))` or write `simul~grid`.

### The studies

- [Life](pillife.md): Conway's Game of Life on a `simul.l` grid. It shows properties as state, `=:`/`:` with `This`, and namespaces.
- [Chat](pilchat.md): a multi-user chat server in about 25 lines. It shows `port`/`listen`/`fork`, `tell` for inter-process messages, and `task` for event handling.
- [The Health Application](pilhealth.md): a tiny database web app using `http.l`, `xhtml.l` and `form.l`.

### Where to find more examples today

- **The pil21 tarball itself**: `lib/*.l` is idiomatic code by the author, `test/` exercises nearly every built-in, and `@lib/vip.l` is a whole editor.
- **[Rosetta Code, PicoLisp category](https://rosettacode.org/wiki/Category:PicoLisp)**: hundreds of tasks.
- **[PicoLisp by Example](https://github.com/tj64/picolisp-by-example)**: the book form of the above (see [PicoLisp By Example](picolispbyexample.md)).
- **[picolisp.com wiki](https://picolisp.com/wiki/?home)**: articles and small apps by the community.

### How I read an example

1. Run it first, unchanged, and see what it does.
2. `(pp 'fn)` each function and guess what it does before reading the docs.
3. Look up anything unfamiliar with `(doc 'fn)` in `pil +`.
4. Change one thing and run it again.
