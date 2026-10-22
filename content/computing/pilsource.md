---
title: Picolisp Sources
date: '2016-11-26T21:48:16+04:00'
lastmod: '2017-06-29T02:04:04+04:00'
original_id: '{A375}'
original_name: pilsource
original_blob: blob/B/6/070.txt
revisions: 24
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pilsource
draft: false
topics:
- lisp
---

# Picolisp Sources

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

### The plain idea

PicoLisp has been implemented three times, and this page indexes my reading of the first two:

- **pil32**, written in C. Small, readable and the easiest place to start. Its files (`pico.h`, `main.c`, `sym.c` and the rest) are listed below. Its spirit lives on in *miniPicoLisp*, a minimal C version still available from Software Lab.
- **pil64**, written in a generic assembly language that is itself defined in PicoLisp (`asm.l`), then translated to x86-64, ARM64, PowerPC and others. Fast, with a full 64-bit object database.
- **pil21**, the current PicoLisp since 2020. Alexander Burger rewrote the system again, this time in PicoLisp itself, generating LLVM intermediate code. It keeps the same language and libraries (`@lib/http.l`, `form.l`, the database) while being portable to any platform LLVM supports. If you download PicoLisp today, this is what you get.

### Why read interpreter sources at all?

Because PicoLisp is small enough to read. The whole of pil32 is a few thousand lines. You can see exactly how a cell is laid out, how a symbol stores its value and properties, how the garbage collector marks and sweeps, and how `eval` walks a list. Few languages let you hold the entire machine in your head, and doing it once changes how you write code in any language.

### An analogy

Reading a novel tells you the story. Reading the author's drafts tells you how stories are built. These pages are the drafts.

### How to use this page

Start with [pico.h](picoh.md) for the data structures, then [main.c](mainc.md) and [flow.c](flowc.md) to see evaluation, then [sym.c](symc.md) and [subr.c](subrc.md) for symbols and lists. Each source page has a short note saying what the file does. When you are ready for the current system, download pil21 from [software-lab.de](https://software-lab.de/down.html) and compare: the ideas are the same, written a third time.

## [Examples Examined](pilexamplesexamined.md)

- [misc/life.l](pillife.md)
- [misc/chat](pilchat.md)

## [32 Bit C Source](32bitcsource.md)

- [pico.h](picoh.md)
- [main.c](mainc.md)
- [apply.c](applyc.md)
- [balance.c](balancec.md)
- [big.c](bigc.md)
- [ext.c](extc.md)
- [flow.c](flowc.md)
- [gc.c](gcc.md)
- [ht.c](htc.md)
- [httpGate.c](httpgatec.md)
- [io.c](ioc.md)
- [lat1.c](lat1c.md)
- [Makefile](makefile.md)
- [mkVers](mkvers.md)
- [net.c](netc.md)
- [ssl.c](sslc.md)
- [start.c](startc.md)
- [subr.c](subrc.md)
- [sym.c](symc.md)
- [tab.c](tabc.md)
- [TAGS](tags.md "MISSING PAGE")
- [utf2.c](utf2c.md)
- [vers.h](versh.md)

## [64 Bit Asm Source](64bitasmsource.md)

- [apply.l](apply-l.md "MISSING PAGE")
- [arch](arch.md "MISSING PAGE")
- [big.l](big-l.md "MISSING PAGE")
- [db.l](db-l.md "MISSING PAGE")
- [defs.l](defs-l.md "MISSING PAGE")
- [err.l](err-l.md "MISSING PAGE")
- [ext.l](ext-l.md "MISSING PAGE")
- [flow.l](flow-l.md "MISSING PAGE")
- [gc.l](gc-l.md "MISSING PAGE")
- [glob.l](glob-l.md "MISSING PAGE")
- [ht.l](ht-l.md "MISSING PAGE")
- [io.l](io-l.md "MISSING PAGE")
- [lib](lib.md "MISSING PAGE")
- [main.l](main-l.md "MISSING PAGE")
- [Makefile](makefile.md)
- [mkAsm](mkasm.md "MISSING PAGE")
- [mkAsm.l](mkasm-l.md "MISSING PAGE")
- [net.l](net-l.md "MISSING PAGE")
- [src-list](src-list.md "MISSING PAGE")
- [subr.l](subrl.md)
- [sym.l](sym-l.md "MISSING PAGE")
- [sys](sys.md "MISSING PAGE")
- [sysdefs.c](sysdefs-c.md "MISSING PAGE")
- [tags](tags.md "MISSING PAGE")
- [version.l](version-l.md "MISSING PAGE")
- [x86-64.linux.base.o](x86-64-linux-base-o.md "MISSING PAGE")
- [x86-64.linux.base.s](x86-64-linux-base-s.md "MISSING PAGE")
- [x86-64.linux.ext.o](x86-64-linux-ext-o.md "MISSING PAGE")
- [x86-64.linux.ext.s](x86-64-linux-ext-s.md "MISSING PAGE")
- [x86-64.linux.ht.o](x86-64-linux-ht-o.md "MISSING PAGE")
- [x86-64.linux.ht.s](x86-64-linux-ht-s.md "MISSING PAGE")

## [Picolisp Libraries](pillibraries.md "MISSING PAGE")

- [adm.l](adm-l.md "MISSING PAGE")
- [android.l](android-l.md "MISSING PAGE")
- [app.l](app-l.md "MISSING PAGE")
- [bash_completion](bash-completion.md "MISSING PAGE")
- [boss.l](boss-l.md "MISSING PAGE")
- [btree.l](btree-l.md "MISSING PAGE")
- [cal.l](cal-l.md "MISSING PAGE")
- [canvas.js](canvas-js.md "MISSING PAGE")
- [canvas.l](canvas-l.md "MISSING PAGE")
- [complete.l](complete-l.md "MISSING PAGE")
- [conDbgc.l](condbgc-l.md "MISSING PAGE")
- [db32-64.l](db32-64-l.md "MISSING PAGE")
- [dbase.l](dbase-l.md "MISSING PAGE")
- [db.l](db-l.md "MISSING PAGE")
- [debug.l](debug-l.md "MISSING PAGE")
- [edit.l](edit-l.md "MISSING PAGE")
- [ed.l](ed-l.md "MISSING PAGE")
- [eedit.l](eedit-l.md "MISSING PAGE")
- [el](el.md "MISSING PAGE")
- [eled.l](eled-l.md "MISSING PAGE")
- [ext](ext.md "MISSING PAGE")
- [form.js](form-js.md "MISSING PAGE")
- [form.l](form-l.md "MISSING PAGE")
- [frac.l](frac-l.md "MISSING PAGE")
- [gcc.l](gcc-l.md "MISSING PAGE")
- [gis.l](gis-l.md "MISSING PAGE")
- [glyphlist.txt](glyphlist-txt.md "MISSING PAGE")
- [head.ps](head-ps.md "MISSING PAGE")
- [heartbeat.l](heartbeat-l.md "MISSING PAGE")
- [ht](ht.md "MISSING PAGE")
- [http.l](httpl.md)
- [import.l](import-l.md "MISSING PAGE")
- [json.l](json-l.md "MISSING PAGE")
- [led.l](led-l.md "MISSING PAGE")
- [led.min.l](led-min-l.md "MISSING PAGE")
- [lint.l](lint-l.md "MISSING PAGE")
- [list](list.md "MISSING PAGE")
- [map](map.md "MISSING PAGE")
- [math32.l](math32-l.md "MISSING PAGE")
- [math64.l](math64-l.md "MISSING PAGE")
- [math.l](math-l.md "MISSING PAGE")
- [misc.l](misc-l.md "MISSING PAGE")
- [native.l](native-l.md "MISSING PAGE")
- [nodroid.l](nodroid-l.md "MISSING PAGE")
- [note.l](note-l.md "MISSING PAGE")
- [openGl.l](opengl-l.md "MISSING PAGE")
- [phone.css](phone-css.md "MISSING PAGE")
- [pilog.l](pilog-l.md "MISSING PAGE")
- [plio.js](plio-js.md "MISSING PAGE")
- [prof.l](prof-l.md "MISSING PAGE")
- [ps.l](ps-l.md "MISSING PAGE")
- [readline.l](readline-l.md "MISSING PAGE")
- [role.l](role-l.md "MISSING PAGE")
- [rsa.l](rsa-l.md "MISSING PAGE")
- [scrape.l](scrape-l.md "MISSING PAGE")
- [simul.l](simul-l.md "MISSING PAGE")
- [socialshareprivacy](socialshareprivacy.md "MISSING PAGE")
- [sq.l](sq-l.md "MISSING PAGE")
- [svg.l](svg-l.md "MISSING PAGE")
- [term.l](term-l.md "MISSING PAGE")
- [test.l](test-l.md "MISSING PAGE")
- [tex.l](tex-l.md "MISSING PAGE")
- [tinymce.l](tinymce-l.md "MISSING PAGE")
- [too.l](too-l.md "MISSING PAGE")
- [tsm.l](tsm-l.md "MISSING PAGE")
- [user.l](user-l.md "MISSING PAGE")
- [vim](vim.md)
- [xhtml.l](xhtml-l.md "MISSING PAGE")
- [xm.l](xm-l.md "MISSING PAGE")
- [xml.l](xml-l.md "MISSING PAGE")
- [xmlrpc.l](xmlrpc-l.md "MISSING PAGE")
- [z3d.l](z3d-l.md "MISSING PAGE")
- [zahlwort.l](zahlwort-l.md "MISSING PAGE")
