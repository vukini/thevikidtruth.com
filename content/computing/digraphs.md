---
title: Digraphs
date: '2016-11-21T04:20:07+04:00'
lastmod: '2016-11-21T04:26:19+04:00'
original_id: '{A306}'
original_name: digraphs
original_blob: blob/B/1/363.txt
revisions: 9
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: digraphs
draft: false
topics:
- c-systems
---

# Digraphs

[Back to The Compiler](thecompiler.md)

Not some punctuation marks are not available on all keyboards. In this case we
can use the following Digraphs in our source files.

```
<:   is translated into [

:>   is translated into ]

<%   is translated into \{

%>   is translated into \}

%:   is translated into \#

%:%: is translated into \##
```

### The plain idea

Digraphs, like [trigraphs](trigraphs.md), are alternate spellings for punctuation that some keyboards lacked, this time two characters instead of three. `<:` means `[`, `%>` means `}`, and so on. The crucial difference from trigraphs is that digraphs are real *tokens*: the compiler treats `<:` as the `[` token, but it never reaches inside a string literal to change your text.

### Why it matters

They are safer than trigraphs for exactly that reason, and unlike trigraphs they are **still part of C and C++**. You will rarely write them, but you may meet them in old code, and knowing they are harmless, equivalent spellings saves confusion.

### An everyday analogy: spelling "and" as "&"

Writing "fish & chips" instead of "fish and chips" is a shorthand everyone understands, and it never accidentally changes a word inside a sentence. Digraphs are that kind of tidy substitution: an alternate spelling at the level of whole symbols, not stray letters.

### A worked example

These two lines compile to exactly the same program:

```c
int a<:3:> = <%1, 2, 3%>;   // with digraphs
int a[3]   = { 1, 2, 3 };   // the normal way
```

Because `<:` is a token, this works cleanly, whereas the trigraph version would risk mangling anything that happened to contain the sequence.

### Common misconceptions

- **"Digraphs and trigraphs are interchangeable."** They solve the same problem but differ in a key way: digraphs are tokens (string-safe, still in the language); trigraphs were raw character substitutions (string-unsafe, removed in C23).
- **"They slow compilation or change behaviour."** No; they are purely alternate spellings with identical meaning.

### How it connects

- [Trigraphs](trigraphs.md): the three-character, now-removed cousin.
- [Tokens](tokens.md) and [The Compiler](thecompiler.md): digraphs are recognised during tokenizing.

The truth revealed: digraphs are the civilised version of the keyboard-shortage fix, alternate spellings that mean exactly what they look like and never surprise you.
