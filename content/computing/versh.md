---
title: vers.h
date: '2017-06-29T02:06:42+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1175}'
original_name: versh
original_blob: blob/B/6/112.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: versh
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

# [vers.h](versh.md)

Here is the truth about versioning shell helpers: **a tiny wrapper that prints versions of the tools you actually use saves more time than it has any right to.** When something breaks after an update, "what am I running?" should be a one-liner.

### What it is, in plain words

**versh** on this site is a personal utility idea: a shell script (or alias collection) that reports versions of the compilers, interpreters and services on a machine – the footprint of a development environment. Not a product; a habit.

### Why it matters

Bug reports without versions are guesses. Reproducing a build needs the same GCC, the same libc, the same Node. A `ver.sh` in a repo or `~/bin` turns a five-minute archaeology dig into ten seconds.

### An everyday analogy: a medical wristband

In a hospital, the wristband lists the facts that change treatment. A version script is the wristband for your toolchain.

### A hands-on example

```bash
#!/bin/sh
# ~/bin/versh – extend as you like
set -e
section() { printf '\n== %s ==\n' "$1"; }

section "OS"
uname -a
[ -f /etc/os-release ] && . /etc/os-release && echo "$PRETTY_NAME"

section "Toolchains"
command -v gcc >/dev/null && gcc --version | head -1
command -v rustc >/dev/null && rustc --version
command -v go >/dev/null && go version
command -v python3 >/dev/null && python3 --version
command -v node >/dev/null && node --version
command -v pil >/dev/null && pil -version 2>/dev/null || true

section "Userland"
git --version
vim --version | head -1
```

```bash
chmod +x ~/bin/versh
versh > ~/notes/vikix-versions.txt
```

Pin the same idea in project READMEs: "build tested with …" plus a paste from `versh`.

### Common misconceptions

- **"`--version` is enough everywhere."** Some tools use `-v`, `version`, or print to stderr. The script papers over that.
- **"Containers make this obsolete."** Images drift; recording what ran still matters.
- **"Only languages matter."** Shared libraries and package managers break builds too – add `ldd --version`, `xbps-query -v`, etc.

### Connections

- [BASH](bash.md), [Linux Introspection](linuxinstrospection.md), [Git](git.md).
- [Build](bciyh.md) – knowing what Vikix is made of.

```
static byte Version[4] = {17,6,13};
```

remember that `byte` is defined in [pico.h](picoh.md) line 50 as `typedef unsigned char byte;`.
