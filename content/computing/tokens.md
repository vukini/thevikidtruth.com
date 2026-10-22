---
title: Tokens
date: '2016-11-21T04:48:26+04:00'
lastmod: '2016-11-21T05:39:34+04:00'
original_id: '{A310}'
original_name: tokens
original_blob: blob/B/1/410.txt
revisions: 7
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: tokens
draft: false
topics:
- c-systems
---

# Tokens

[Back to The Compiler](thecompiler.md)

A token is:

- a keyword
- an [identifier](identifier.md)
- a constant
- a string literal
- a symbol
    - one or more punctuations
    - that function as operators or digraphs
    - something of syntactic importance, like semicolons or braces

## Parsing a Token

As a rule, while parsing tokens, the compiler will

**append each successive non-white character**

**to the existing token unless**

**it would make the valid token invalid.**

### The plain idea

A token is the smallest meaningful piece of a program, a single "word" in the language. Before a [compiler](thecompiler.md) can understand your code, it must first chop the raw stream of characters into these words: keywords, [identifiers](identifier.md), constants, string literals and symbols. That chopping step is called *lexical analysis* or *tokenizing*, and it is the very first thing any compiler or interpreter does.

### Why it matters

Everything downstream, parsing, type-checking, code generation, works on tokens, not on raw text. Understanding tokens explains a hundred small mysteries: why `int x;` and `intx;` mean completely different things, why whitespace usually does not matter but sometimes does, why a missing quote can produce a baffling error far from the real mistake. It is also the gateway concept to writing your own parsers, linters and little languages.

### An everyday analogy: reading a sentence

When you read "The cat sat.", your eye does not see fourteen separate letters; it sees four units, three words and a full stop. You do that splitting so automatically you forget it is happening. A tokenizer is a program doing that same splitting deliberately: turning `x = 42;` into the tokens `x`, `=`, `42`, `;`.

### A worked example: tokenizing a line

Take this C line:

```c
total = price * 2;
```

The lexer scans left to right and emits:

| Token    | Kind              |
|----------|-------------------|
| `total`  | identifier        |
| `=`      | operator          |
| `price`  | identifier        |
| `*`      | operator          |
| `2`      | integer constant  |
| `;`      | punctuator        |

The rule from my note above, "append each non-white character to the current token until a character arrives that cannot belong to it", is exactly how the lexer knows `total` ends and `=` begins. This is also the "maximal munch" rule: `>>=` is read as one token, not three, because the lexer grabs the longest valid token it can.

### Common misconceptions

- **"Whitespace is just for humans."** Usually it only *separates* tokens, but it is essential where removing it would merge two tokens into one (`int x` versus `intx`). Some languages (Python) make indentation itself a token.
- **"The compiler reads line by line."** It reads a stream of tokens; line breaks are mostly just whitespace in C.
- **"A string is many tokens."** A whole string literal `"hello world"` is a *single* token, spaces and all.

### How it connects

- [The Compiler](thecompiler.md): tokenizing is its first phase.
- [Identifiers](identifier.md) and [Literals](literals.md): two kinds of token.
- [Digraphs](digraphs.md) and [Trigraphs](trigraphs.md): alternate spellings the lexer recognises.
- [Regular Expressions](regularexpressions.md): the usual tool for describing token patterns.

The truth revealed: before a program can mean anything, it first has to be cut into words, and that humble cutting step quietly decides what your code is allowed to say.
