---
title: Trigraphs
date: '2016-11-21T04:30:32+04:00'
lastmod: '2016-11-21T04:30:48+04:00'
original_id: '{A307}'
original_name: trigraphs
original_blob: blob/B/1/365.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: trigraphs
draft: false
topics:
- c-systems
---

# Trigraphs

[Back to The Compiler](thecompiler.md)

C also provides a 3 char representation of punctuation marks all starting with two
question marks.

```
??( is translated into [

??) is translated into ]

??< is translated into \{

??> is translated into \}

??= is translated into #

??/ is translated into \\

??! is translated into !

??' is translated into ^

??- is translated into ~
```

### The plain idea

Trigraphs are three-character stand-ins for punctuation marks that some very old or non-English keyboards and character sets could not type. In the 1980s not every terminal had `{`, `}`, `[`, `]`, `#`, `\`, `^`, `~` or `|` available, so C let you write, for example, `??(` wherever you meant `[`. The compiler replaced every trigraph before doing anything else, in the very first translation step.

### Why it matters

Mostly as history and as a trap. You will almost never *want* a trigraph, but because the replacement happened so early and so blindly, an innocent `??` inside a string could change your program's meaning without warning, which is exactly why they are worth knowing about.

### An everyday analogy: a typewriter workaround

Old typewriters without a "1" key taught typists to use a lowercase "l" instead. It looked right on paper but confused anything that read the text literally. Trigraphs were that workaround, baked into the C language itself for keyboards missing certain symbols.

### A worked example: the surprise

```c
printf("What??!\n");   // prints: What|
```

That is not a typo in the output. `??!` is the trigraph for `|`, so the compiler silently rewrote the string. This kind of accidental substitution is the whole reason trigraphs became infamous.

### A 2026 update

**Trigraphs were removed from C in C23** (and from C++ in C++17). Modern compilers ignore them by default and often warn if they spot a sequence that used to be one. Today, with Unicode keyboards everywhere, they are purely a historical curiosity, and that is good news: one fewer silent surprise.

### Common misconceptions

- **"They're still active in C."** Not since C23. Even before that, GCC and Clang disabled them unless you asked.
- **"They're the same as [digraphs](digraphs.md)."** No. Trigraphs are replaced character-by-character anywhere, even inside strings; digraphs are proper tokens and never touch string contents.

### How it connects

- [Digraphs](digraphs.md): the safer, token-level alternative.
- [Tokens](tokens.md) and [The Compiler](thecompiler.md): where this substitution sits in translation.
- [Unicode in C](unicodeinc.md): why the problem trigraphs solved no longer exists.

The truth revealed: trigraphs are a fossil from an age of limited keyboards, kept alive just long enough to bite the unwary, and finally retired in C23.
