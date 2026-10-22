---
title: start.c
date: '2017-06-29T02:04:42+04:00'
lastmod: '2017-06-29T02:10:14+04:00'
original_id: '{A1170}'
original_name: startc
original_blob: blob/B/6/104.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: startc
draft: false
topics:
- lisp
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
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
  [Open Data Science](opendatascience.md)

# [start.c](startc.md)

> **Reading this in 2026.** This page reproduces `start.c` from the PicoLisp sources (pil32), as I studied them around 2017. It is the tiny wrapper that hands control to `main2`, the real start-up routine. PicoLisp is MIT-licensed, © Software Lab, Alexander Burger. Since 2020 the current PicoLisp is **pil21**, which is written in PicoLisp itself and compiled through LLVM, so the line-by-line details here belong to the older 32-bit C implementation; the ideas carry over. Current sources are at [software-lab.de](https://software-lab.de/down.html).


```
/* 03sep06abu
 * (c) Software Lab. Alexander Burger
 */

extern void main2(int ac, char *av[]) __attribute__ ((noreturn));
int main(int ac, char *av[]) __attribute__ ((noreturn));

int main(int ac, char *av[]) {
   main2(ac,av);
}
```
