---
title: 'PicoLisp Sources'
date: '2016-11-26T21:48:16+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
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

# PicoLisp Sources

### The plain idea

PicoLisp has been implemented three times. This page is the index of my reading of all three, updated in October 2026:

- **pil32**, written in C. It is small, readable, and the easiest place to start. Its files (`pico.h`, `main.c`, `sym.c` and the rest) are listed below as I studied them in 2017. They are kept here as an archive. pil32 is no longer maintained, but its spirit lives on in *miniPicoLisp*, a minimal C version.
- **pil64**, written in a generic assembly language that was itself defined in PicoLisp, then translated to x86-64, ARM64, PowerPC and others. It was fast and had a full 64-bit object database. It is also archived now (see [PicoLisp ASM](pilasm.md)).
- **pil21**, the current PicoLisp since 2020 (latest release **26.9**). Alexander Burger rewrote the system again, this time in PicoLisp itself, generating **LLVM IR**. It keeps the same language and libraries (`@lib/*.l`) and adds namespaces. If you want to read the code that actually runs today, read this one.

### Why read interpreter sources at all?

Because PicoLisp is small enough to read. All of pil21's `src/*.l` is about 16,000 lines. You can see exactly how a cell is laid out, how a symbol stores its value and properties, how the garbage collector marks, and how `eval` walks a list. See [The PicoLisp Machine](pilmachine.md) for the data model.

### An analogy

Reading a novel tells you the story. Reading the author's drafts tells you how stories are built. These pages are the drafts.

### The pil21 source tree (src/)

From `pil21.tgz`, version 26.9:

| File | What it holds |
|---|---|
| `lib/llvm.l` | The **LLVM front end**: a PicoLisp DSL that emits LLVM IR. Everything else is written in it. |
| `vers.l` | The version, `(pico~de *Version 26 9 25)`. See [vers.l](versh.md). |
| `defs.l`, `glob.l`, `dec.l` | Constants, global symbols and the symbol table, and declarations. |
| `main.l` | Startup, the REPL, `eval`/`apply`, error handling, signals. |
| `gc.l` | The mark-and-sweep garbage collector and heap. |
| `big.l` | Numbers: short numbers and bignums, arithmetic. |
| `sym.l` | Symbols, names, namespaces, properties, list functions. |
| `io.l` | The reader, printer, files, sockets and pipes. |
| `db.l` | External symbols: the database engine. |
| `apply.l`, `flow.l`, `subr.l` | Function application, control flow (`if`, `loop`, `co`…), and list built-ins. |
| `ext.l`, `ht.l` | The `ext.so` and `ht.so` extension libraries (`ht.so` speeds up HTTP and HTML output). |
| `lib.c`, `pico.h` | A small C helper layer for things easier done in C (terminal, signals, `native` calls). See [pico.h](picoh.md). |
| `httpGate.c`, `ssl.c`, `balance.c`, `sysdefs.c` | Standalone tools in C: the HTTPS proxy ([httpGate](httpgatec.md)), the SSL client, a load balancer, and the generator for `lib/sysdefs`. |
| `Makefile` | Builds it all with `clang`, `opt`, `llc` and `llvm-link`. See [Makefile](makefile.md). |

A built-in function in pil21 looks like this (from `src/subr.l`):

```picolisp
# (cdr 'lst) -> any
(de _Cdr (Exe)
   (chkD (eval (cadr Exe))) )
```

That is PicoLisp code, but it is compiled, not interpreted: `lib/llvm.l` turns it into LLVM IR (`base.ll`), and LLVM optimises it into machine code. The tarball ships the generated `.ll` files, so you can build pil21 without having PicoLisp installed first.

### How to use this page

For **today's PicoLisp**, start with `src/defs.l` and `src/glob.l` for the data structures, then `main.l` for evaluation, then `sym.l` and `subr.l`. Read the [reference VM section](https://software-lab.de/doc/ref.html#vm) alongside.

For the **historical C version**, start with [pico.h](picoh.md), then [main.c](mainc.md) and [flow.c](flowc.md) to see evaluation, then [sym.c](symc.md) and [subr.c](subrc.md) for symbols and lists.

## [Examples Examined](pilexamplesexamined.md)

- [Life](pillife.md)
- [Chat](pilchat.md)
- [The Health Application](pilhealth.md)

## Libraries (current)

- [http.l](httpl.md): the HTTP server.
- [httpGate](httpgatec.md): the HTTPS front-end proxy.

## [32 Bit C Source (pil32, archive)](32bitcsource.md)

These are my 2017 reading notes on the pil32 sources, kept as they were:

- [pico.h](picoh.md) (now also covers pil21's `pico.h`)
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
- [utf2.c](utf2c.md)
- [vers.h](versh.md)

## [64 Bit Asm Source (pil64, archive)](64bitasmsource.md)

- [PicoLisp ASM](pilasm.md): the pil64 virtual machine and its registers.
