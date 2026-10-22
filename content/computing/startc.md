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
draft: true
review: update
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
