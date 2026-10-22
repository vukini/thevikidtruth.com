---
title: Regular Expressions
date: '2016-12-06T03:59:49+04:00'
lastmod: '2016-12-08T00:45:18+04:00'
original_id: '{A714}'
original_name: regularexpressions
original_blob: blob/B/4/747.txt
revisions: 12
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: regularexpressions
draft: false
topics:
- linux
---

[Read This!](caveatemptor.md)

# Regular Expressions

Regular Expressions are really a language in themselves. If you read any code online you will see them
everywhere. So in this light it is best to get familiar with them and the most common patterns. I am
hoping to develop my own [little library](regexplibrary.md) of expressions over the next few years. I hope this page will be of
use to you.

## Introduction

A regular expression ("regex") is a tiny pattern language for describing text. Instead of searching for one fixed word, you describe a *shape*: "three digits, a dash, four digits", "a word starting with a capital", "anything between quotes". A regex engine then finds, checks or replaces every piece of text matching that shape. They turn up in search-and-replace, [Bash](bash.md) and grep, log analysis, form validation, and nearly every programming language.

The basics: most characters match themselves, so `cat` matches "cat". A few characters are *special*:

```
  .        any single character
  \d       a digit (0-9)        \w   a word character (letter/digit/_)
  \s       whitespace           \D \W \S   the opposite of each
```

So `\d\d:\d\d` matches a time like `09:30`.

## Boundaries

Boundaries match a *position*, not a character:

```
  ^        start of the line (or string)
  $        end of the line (or string)
         a word boundary (edge of a word)
  \B       not a word boundary
```

`^Error` matches only lines that begin with "Error"; `cat` matches "cat" but not the "cat" inside "category".

## Alternation

```
  (a|b)        a or b
```

## Groups and Subpatters

```
  (...)        Anything between (brackets) is a group
  (?..)        Passive (non-c­apt­uring) group
  \n           Group / Sub­pattern number "­n"
```

## Backreferences

A backreference matches the same text a group captured earlier:

```
  (\w+)\s+     a word repeated, e.g. "the the"
```

`` means "whatever group 1 matched". Capture groups also power search-and-replace, where `$1` or `` inserts the captured text into the result.

## Character Classes & Ranges

```
  [rst]        r or s or t
  [^rst]       NOT r or s or t
  [a-z]        Lower case letter from a to z
  [A-Z]        Upper case letter from A to Z
  [0-9]        Digit from 0 to 9
```

## Unicode

Modern regex engines understand [Unicode](unicodeinc.md), not just ASCII:

```
  \p{L}        any Unicode letter (any alphabet)
  \p{N}        any Unicode number
  \p{Lu}       an uppercase letter
```

So `\p{L}+` matches a word in any language, where plain `[a-z]+` would miss "café" or "Москва". Many engines need a flag (such as `u` in JavaScript) to turn Unicode mode on.

## Quantifiers

Quantifiers say *how many* of the preceding thing to match:

```
  *        zero or more        +    one or more
  ?        zero or one         {3}  exactly 3
  {2,5}    between 2 and 5      {2,} 2 or more
```

By default they are *greedy* (match as much as possible); add `?` to make them *lazy* (as little as possible): `<.+?>` matches one `<tag>` rather than everything from the first `<` to the last `>`.

## Lookaround

Lookaround checks what is beside your match without consuming it:

```
  (?=foo)      lookahead: followed by "foo"
  (?!foo)      negative lookahead: NOT followed by "foo"
  (?<=foo)     lookbehind: preceded by "foo"
  (?<!foo)     negative lookbehind: NOT preceded by "foo"
```

For example `\d+(?= USD)` matches the number in "100 USD" but not the "USD" itself.

## Sites About Regexp & Engines

- [Regexpal](http://regexpal.com)
- [Composability](http://www.thaiopensource.com/relaxng/design.html#section:5)
- [GSkinner's Regexr](http://gskinner.com/regexr)
- [RegExp @ Cheatography](https://www.cheatography.com/davechild/cheat-sheets/regular-expressions/)

### An everyday analogy: a stencil

A regex is a stencil you lay over text. The stencil's shape, "three letters then two digits", lets through only the parts that fit and blocks the rest. Change the stencil and you change what passes. Learning regex is learning to cut stencils.

### A worked example: validating and extracting

Say you want to pull dates like `2026-10-22` out of a log:

```
\b(\d{4})-(\d{2})-(\d{2})\b
```

Read it piece by piece: a word boundary, four digits captured as group 1 (the year), a dash, two digits (month), a dash, two digits (day), another boundary. In Python:

```python
import re
for y, m, d in re.findall(r"\b(\d{4})-(\d{2})-(\d{2})\b", text):
    print(y, m, d)
```

### A caution, and a 2026 note

Two hard-won lessons. First, **do not parse HTML or deeply nested structures with regex**; use a real parser. Regex matches patterns, not grammar. Second, beware **catastrophic backtracking**: a pattern like `(a+)+$` on a long non-matching string can hang for seconds or minutes (a "ReDoS" denial-of-service bug). Keep patterns simple, avoid nested quantifiers, and prefer linear-time engines like Google's RE2 (used in Go, and the syntax several of my tools expect) when running regex on untrusted input.

### Common misconceptions

- **"All regex engines are identical."** They differ: POSIX, PCRE, JavaScript, Python and RE2 vary in features (lookbehind, `\p{}`, backreferences).
- **"Regex can match anything."** It handles *regular* patterns; balanced brackets and nested tags are beyond it.
- **"More clever is better."** A readable pattern you can fix beats a dense one-liner nobody understands.

### How it connects

- [Bash](bash.md): grep, sed and awk live on regex.
- [Tokens](tokens.md): lexers describe tokens with regex.
- [Unicode in C](unicodeinc.md): why `\p{L}` beats `[a-z]`.
- [Knowledge Representation](krep.md) and text processing more broadly.

The truth revealed: a regular expression is not magic, it is a stencil for text, and most of the skill is cutting a shape just specific enough and no more.
