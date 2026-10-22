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
draft: true
review: update
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
