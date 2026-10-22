---
title: mkVers
date: '2017-06-29T02:03:06+04:00'
lastmod: '2017-06-29T02:07:30+04:00'
original_id: '{A1165}'
original_name: mkvers
original_blob: blob/B/6/100.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: mkvers
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

# [mkVers](mkvers.md)

> **Reading this in 2026.** This page reproduces `mkVers` from the PicoLisp sources (PicoLisp build tools), as I studied them around 2017. It is the script that stamps the current version number into the source files. PicoLisp is MIT-licensed, © Software Lab, Alexander Burger. Since 2020 the current PicoLisp is **pil21**, which is written in PicoLisp itself and compiled through LLVM, so the line-by-line details here belong to the older implementations; the ideas carry over. Current sources are at [software-lab.de](https://software-lab.de/down.html).


```
#!../bin/picolisp ../lib.l
# 07mar11abu
# (c) Software Lab. Alexander Burger

(load "../src64/version.l")

(out "vers.h"
   (prinl
      "static byte Version[4] = {"
      (glue "," *Version)
      "};" ) )

(bye)

# vi:et:ts=3:sw=3
```
