---
title: Unicode in C
date: '2016-11-21T22:33:37+04:00'
lastmod: '2016-11-22T22:23:18+04:00'
original_id: '{A315}'
original_name: unicodeinc
original_blob: blob/B/1/624.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: unicodeinc
draft: false
topics:
- c-systems
---

# Unicode in C

[C Programming](cprogramming.md) | [Strings](cstrings.md)

Regular C programming only deals with ascii text, however most of the world
has moved on to unicode encoding as it works fairly well.

The problem is most tutorials don't really deal with the topic very well. Please
below the sources and thoughts of Vikid.

## Sources

- [Unicode - Options in C](http://www.cprogramming.com/tutorial/unicode.html)

### The plain idea

C grew up when text meant ASCII: 128 characters, one byte each, enough for English. The rest of the world needs tens of thousands of characters, which is what **Unicode** provides, and the near-universal way to store Unicode in bytes is **UTF-8**. The awkward truth is that C's `char` is still just a byte, so a single visible character may span several `char`s. Handling text correctly in C means keeping the ideas of *byte*, *code point* and *character* firmly apart.

### Why it matters

Get this wrong and you produce the classic bugs: counting "café" as five characters, truncating a string in the middle of a multi-byte character and corrupting it, or mangling anyone's name that is not plain English. In a connected world where every program meets every language and emoji, UTF-8 competence is not optional.

### An everyday analogy: letters versus envelopes

Think of a code point as a *letter* (the abstract character "é") and a byte as part of an *envelope* that carries it. ASCII letters fit in one envelope. Many letters need two, three or four envelopes taped together. If you count envelopes and call it letters, your sums come out wrong. UTF-8 is the taping scheme, cleverly designed so the old ASCII letters still travel in a single, unchanged envelope.

### A worked example: bytes versus characters

```c
#include <stdio.h>
#include <string.h>
int main(void) {
    const char *s = "café";        // é is two bytes in UTF-8
    printf("bytes: %zu\n", strlen(s));   // prints 5, not 4
    return 0;
}
```

`strlen` counts bytes, and "é" (U+00E9) is encoded as two bytes (0xC3 0xA9). To count actual characters you must decode UTF-8, or use a library. The design virtue of UTF-8 shows here too: every byte of a multi-byte character has its high bit set, so plain ASCII text is byte-for-byte identical to its UTF-8 form, which is why so much old C code kept working.

### A 2026 update

The modern advice is clear: **use UTF-8 everywhere** ("UTF-8 everywhere" is now the consensus). Keep text as UTF-8 `char` arrays and only decode to code points when you must. For heavy work use a dedicated library such as **ICU** or **utf8proc**; avoid the old `wchar_t`/`setlocale` path, which is portable in theory and painful in practice (notably `wchar_t` is 16-bit on Windows but 32-bit elsewhere). C11 added `char16_t`/`char32_t` and `u8"..."` literals, and C23 made `u8` strings `char8_t`-friendly, but for most programs "store UTF-8, be careful when you count" is the whole lesson.

### Common misconceptions

- **"One `char` is one character."** Only for ASCII. In UTF-8 a character is one to four bytes.
- **"`strlen` gives the character count."** It gives the byte count.
- **"`wchar_t` solves everything."** It is inconsistent across platforms; UTF-8 in `char` is simpler and more portable.
- **"Reversing a string is easy."** Reversing bytes corrupts multi-byte characters; you must reverse by code point (and even then, combining marks complicate it).

### How it connects

- [C Programming](cprogramming.md) and [Strings](cstrings.md): where byte-vs-character bites.
- [Tokens](tokens.md): source files themselves are usually UTF-8 now.
- [Encryption](encryption.md): encoding is not encryption; UTF-8 hides nothing.

The truth revealed: in C, text is just bytes, and all the trouble, and all the skill, lies in remembering that a byte is not a letter.
