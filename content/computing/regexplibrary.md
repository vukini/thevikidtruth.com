---
title: VikiD's RegExp Library
date: '2016-12-08T00:47:41+04:00'
lastmod: '2026-10-22T21:30:00+04:00'
original_id: '{A772}'
original_name: regexplibrary
original_blob: blob/B/4/754.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: regexplibrary
draft: false
topics:
- linux
---

[Read This!](caveatemptor.md) | [Back to Regular Expressions](regularexpressions.md)

# VikiD's RegExp Library

The library is no longer empty! Below is a working collection of regular expressions I actually use, with a note on each. For the theory, go [back to Regular Expressions](regularexpressions.md).

## The core idea in plain words

A regular expression is a tiny pattern language for describing **shapes of text**: "three digits, a dash, four digits", "a word at the start of a line followed by a colon". A regex engine slides your pattern along the text and reports where it fits.

The catch is that there are several dialects. The ones you meet daily:

- **POSIX ERE** — `grep -E`, `sed -E`, `awk`. No `\d`; use `[0-9]` or `[[:digit:]]`.
- **PCRE / Perl-style** — `grep -P`, Perl, PHP, and (close enough) Python's `re`, JavaScript and Rust's `regex` crate, which [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) uses. Has `\d`, `\w`, `\s`, non-greedy `*?`.
- **Emacs regexps** — groups and alternation are backslashed: `\(`, `\|`. Or skip the backslash soup with the `rx` macro.

Unless noted, patterns below are PCRE-style and work in `rg`, Python and JavaScript.

## An analogy: a stencil

A regex is a stencil you slide over a page. Literal characters are solid cut-outs that must match exactly; `.` is a hole that lets any character through; `[aeiou]` is a hole shaped to fit only vowels; `+` and `*` say "this hole can stretch". Anchors (`^`, `$`, `\b`) pin the stencil to the edge of a line or a word.

## The library

### Whitespace and lines

| Pattern | Matches |
|---|---|
| `^\s*$` | blank (or whitespace-only) line |
| `\s+$` | trailing whitespace |
| `^\s*#` | a comment line in shell/conf files |
| `^(?!\s*#).+` | a non-comment, non-empty line (PCRE lookahead) |

### Numbers

| Pattern | Matches |
|---|---|
| `^-?\d+$` | an integer |
| `^-?\d+(\.\d+)?$` | an integer or decimal |
| `^0x[0-9A-Fa-f]+$` | a hex literal |
| `\b\d{1,3}(,\d{3})+\b` | thousands with commas: `1,234,567` |

### Dates and times

| Pattern | Matches |
|---|---|
| `\b\d{4}-\d{2}-\d{2}\b` | ISO date shape `2026-10-22` (shape only; doesn't reject month 13) |
| `\b\d{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[12]\d\|3[01])\b` | ISO date with valid month/day ranges |
| `\b([01]\d\|2[0-3]):[0-5]\d\b` | 24-hour time `21:30` |

(The `\|` above is just a table escape; in real use it is a bare `|`.)

### Network bits

| Pattern | Matches |
|---|---|
| `\b(?:\d{1,3}\.){3}\d{1,3}\b` | IPv4 shape (allows 999) |
| `\b(?:(?:25[0-5]\|2[0-4]\d\|1?\d?\d)\.){3}(?:25[0-5]\|2[0-4]\d\|1?\d?\d)\b` | strict IPv4, 0–255 |
| `https?://[^\s)>\]]+` | URLs in prose, stopping at a space or closing bracket |
| `^[^@\s]+@[^@\s]+\.[^@\s]+$` | "looks like an email" — good enough for a sanity check; don't try to be RFC-perfect |

### Code and config

| Pattern | Matches |
|---|---|
| `^\s*(def\|class)\s+(\w+)` | Python definitions; group 2 is the name |
| `^\(def(un\|var\|custom\|macro)\s+(\S+)` | Emacs Lisp top-level definitions |
| `\bTODO\b\|\bFIXME\b` | the things I promised myself |
| `^([A-Za-z_][A-Za-z0-9_]*)=(.*)$` | `KEY=value` lines (env files, Void's `/etc/rc.conf`) |
| `"(?:[^"\\]\|\\.)*"` | a double-quoted string with escapes |

### Logs

| Pattern | Matches |
|---|---|
| `\b(ERROR\|FATAL\|panic)\b` | trouble |
| `^\S+ \S+ (\S+)\[(\d+)\]:` | syslog-style `host prog[pid]:`; groups are program and PID |

## A worked example: tidy a file, three ways

Task: in `notes.org`, find every ISO date and swap it from `2026-10-22` to `22/10/2026`.

**sed (POSIX ERE):**

```sh
sed -E 's/\b([0-9]{4})-([0-9]{2})-([0-9]{2})\b/\3\/\2\/\1/g' notes.org
```

(GNU sed understands `\b`; add `-i` to edit in place once you're happy.)

**ripgrep, to preview first:**

```sh
rg -n '\b(\d{4})-(\d{2})-(\d{2})\b' -r '$3/$2/$1' notes.org
```

`-r` only shows the replacement; it never touches the file.

**Emacs:** `M-x replace-regexp`, then

```
\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\)  →  \3/\2/\1
```

or, readably, build the pattern with `rx`:

```elisp
(rx (group (= 4 digit)) "-" (group (= 2 digit)) "-" (group (= 2 digit)))
```

## Common misconceptions

- **"`.*` is harmless."** It is greedy: in `<a><b>`, `<.*>` matches the whole thing. Use `<[^>]*>` or the non-greedy `<.*?>`.
- **"Regex can parse HTML/JSON."** Not reliably — nesting defeats it. Use `jq`, `pup` or a real parser.
- **"All regex engines are the same."** `\d` does nothing in POSIX grep; `|` needs a backslash in Emacs. Know your dialect.
- **"A validation regex proves the data is valid."** It proves the *shape*. `2026-02-31` passes the date pattern above.
- **"Complex regex is clever."** It's a liability. Comment it, or use `rx` or Python's `re.VERBOSE`.

## Connections

- [Regular Expressions](regularexpressions.md) — the theory and syntax.
- [awk](awk.md) and [Bash](bash.md) — where many of these live.
- [VikiD's Bash Cookbook](vikidsbashcookbook.md) — more one-liners.
- [Emacs](emacs.md) — `rx`, `occur`, `replace-regexp`.
- [Linux Tools](linuxtools.md) — grep, sed, ripgrep and friends.
