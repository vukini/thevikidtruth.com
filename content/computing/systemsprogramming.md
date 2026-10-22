---
title: Systems Programming
date: '2016-11-29T09:50:10+04:00'
lastmod: '2016-12-04T12:24:17+04:00'
original_id: '{A471}'
original_name: systemsprogramming
original_blob: blob/B/4/164.txt
revisions: 3
author: admin
last_editor: admin
tags: []
categories:
- computing
wikislug: systemsprogramming
draft: false
topics:
- c-systems
aliases:
- /about/systemsprogramming/
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [pil sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md)

# Systems Programming

### The plain idea

Systems programming is writing software that talks directly to the operating system and hardware, rather than to a user. Where application programming builds things *people* use (apps, websites), systems programming builds the layer *underneath*: operating systems, device drivers, databases, network servers, language runtimes. The key tool is the **system call**: a request your program makes to the kernel to do something privileged, open a file, create a process, send data over the network. The `select` call linked here, for instance, lets one program wait efficiently on many network connections at once.

### Why it matters

Every application rests on this layer, so understanding it demystifies performance, concurrency and the strange bugs that leak up from below. It is also where the most durable, foundational software lives: the kernel, the C library, the tools that everything else depends on. Languages like C, and now Rust and Zig, exist largely to make this work safe and fast.

### An everyday analogy

If applications are the shops on a high street, systems programming is the plumbing, wiring and roads underneath: invisible when it works, catastrophic when it fails, and requiring a very different kind of care to build. System calls are the regulated junctions where a shop can tap into the mains, you cannot just help yourself to electricity; you ask the utility (the kernel) through a controlled interface.

### A 2026 note

The classic reference, Linux system calls, is as relevant as ever (the definitive-guide link below still holds up). What has changed is the language: **Rust** has become a serious systems language, even entering the Linux kernel, because it offers C-level control without C's memory-safety pitfalls, exactly the bugs ([stack](stacks.md) overflows and the like) that plague low-level code. Newer interfaces like `io_uring` have also started to replace older ones like `select` for high-performance I/O.

### How it connects

- [Modern Operating Systems](modernoperatingsystems.md): the theory behind what system calls do.
- [C Programming](cprogramming.md), [Linux](linux.md) and [Bash](bash.md): the traditional tools.
- [Stacks](stacks.md): the low-level memory model you must understand here.

The truth revealed: systems programming is building the floor everyone else stands on, which is why it rewards caution, and why the industry is slowly moving it to languages that catch mistakes before they ship.


## System Calls of Interest

- [select system call](http://www.tutorialspoint.com/unix_system_calls/_newselect.htm)

#### Reading List & Source

[TDLP Linux Guides and Howto's](http://www.tldp.org)
[The Kernel (2.6) Module Programming Guide](http://www.tldp.org/LDP/lkmpg/2.6/lkmpg.pdf)
[https://blog.packagecloud.io/eng/2016/04/05/the-definitive-guide-to-linux-system-calls/
the-definitive-guide-to-linux-system-calls](https://blog.packagecloud.io/eng/2016/04/05/the-definitive-guide-to-linux-system-calls/
the-definitive-guide-to-linux-system-calls)
[syscalls manpage](http://man7.org/linux/man-pages/man2/syscalls.2.html)
