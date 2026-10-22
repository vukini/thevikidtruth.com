---
title: Bash case statements
date: '2022-08-29T00:33:21+04:00'
lastmod: '2023-04-04T22:40:34+04:00'
original_id: '{A1716}'
original_name: bashcase
original_blob: blob/B/11/763.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: bashcase
draft: false
---

[Quicklinks](quicklinks.md) | [Read This!](caveatemptor.md) |
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
  [Open Data Science](opendatascience.md) | [Vikid's Bash Cookbook](vikidsbashcookbook.md) |

# Bash case statements

```
#!/bin/bash

CHAR=$1

case $CHAR in
  [a-z])
        echo "Small Alphabet." ;;
  [A-Z])
        echo "Big Alphabet." ;;
  [0-9])
        echo "Number." ;;
  *)
        echo "Special Character."
esac
```
