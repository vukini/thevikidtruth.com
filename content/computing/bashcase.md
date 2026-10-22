---
title: Bash case statements
date: '2022-08-29T00:33:21+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
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
topics:
- linux
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

Here is the truth about `case` in Bash: **it is not a weaker `if` – it is a pattern matcher, and patterns are where it earns its keep.** When you find yourself writing a chain of `[[ $x == … ]]` branches, `case` is usually clearer.

### What it is, in plain words

`case` matches a string against a list of **glob patterns** and runs the commands for the first match:

```bash
case "$word" in
  pattern1) commands ;;
  pattern2|pattern3) commands ;;
  *) commands ;;          # default
esac
```

Patterns are the same style as filename globs: `*` any string, `?` any one character, `[abc]` a set, and with `shopt -s extglob`, richer forms like `+(foo|bar)`.

### Why it matters

Option parsing, file-type dispatch, answering "what kind of argument is this?" – `case` expresses these without nested `if`s. It is also POSIX, so scripts using it run under `dash` and other `/bin/sh` implementations. A surprising amount of system init and package-manager scripting is `case` all the way down.

### An everyday analogy: a sorting desk

Letters arrive. A clerk glances at the postcode pattern and drops each into a bin: "starts with SW", "ends with 4AE", "everything else". The clerk does not open the letters (`if` with complicated tests); they match the address against stencils. That's `case`.

### A hands-on example

```bash
#!/bin/bash
# greet.sh
name=${1:-world}
case "$name" in
  [Vv]ikid|VikiD) echo "Hello, me." ;;
  vikix|void)     echo "Hello, machine." ;;
  *.local)        echo "Hello, LAN host $name" ;;
  "")             echo "Hello, nobody?" ;;
  *)              echo "Hello, $name." ;;
esac
```

File-extension dispatch:

```bash
case "$file" in
  *.tar.gz|*.tgz) tar -tzf "$file" ;;
  *.tar.xz)       tar -tJf "$file" ;;
  *.zip)          unzip -l "$file" ;;
  *.md)           "${EDITOR:-nvim}" "$file" ;;
  *)              echo "unknown type: $file" >&2 ; exit 1 ;;
esac
```

Simple option parsing (for fuller needs, use `getopts`):

```bash
while [ $# -gt 0 ]; do
  case "$1" in
    -v|--verbose) verbose=1 ; shift ;;
    -o|--output)  output=$2 ; shift 2 ;;
    --)           shift ; break ;;
    -*)           echo "unknown: $1" >&2 ; exit 1 ;;
    *)            break ;;
  esac
done
```

`;;&` (Bash) falls through to test the next pattern; `;&` falls through and *runs* the next arm. Prefer explicit patterns joined with `|` unless you need fall-through.

### Patterns in detail

```bash
# character classes and ranges
case "$c" in
  [a-z]) echo lower ;;
  [A-Z]) echo upper ;;
  [0-9]) echo digit ;;
esac

# extglob (Bash)
shopt -s extglob
case "$file" in
  +(*.jpg|*.png)) echo image ;;
  !(*.tmp))       echo "not a temp file" ;;
esac
```

Nested `case` is fine; so is calling a function from each arm to keep the structure readable. When the patterns are really regular expressions, step up to `[[ $s =~ ^[0-9]+$ ]]` or pipe through `grep -E` – don't force `case` to be something it isn't.

### case versus if

Use `if` when the test is a *condition* (`-f file`, `-z "$s"`, numeric comparison). Use `case` when the test is "which of these shapes does this string match?". Mixing them – `case` for the shape, `if` inside an arm for a deeper check – is normal and clear.

### Common misconceptions

- **"`case` uses regex."** It uses globs. `*.txt` works; `.*\.txt` does not mean what you think.
- **"Quotes break patterns."** Quote the *subject* (`"$word"`), not the patterns.
- **"`*)` is required."** No, but a default that errors is good manners in scripts.
- **"`case` is slower than `if`."** Negligible. Choose the clearer form.
- **"Only Bash has it."** `case` is POSIX; it's one of the portable conditionals.

### Connections

- [BASH](bash.md), [Bash if](bashif.md), [Bash Variables](bashvariables.md).
- [Bash Reserve Words](bashreservewords.md), [Bash Cookbook](vikidsbashcookbook.md).
- [Regular Expressions](regularexpressions.md) – when you really do need regex (`[[ =~ ]]`).

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
