---
title: Strings in C Programming
date: '2016-11-22T21:52:26+04:00'
lastmod: '2016-11-22T22:23:38+04:00'
original_id: '{A331}'
original_name: cstrings
original_blob: blob/B/1/625.txt
revisions: 9
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: cstrings
draft: true
review: update
---

# Strings in C Programming

[Literals](literals.md) | [C Programming](cprogramming.md)
| [Unicode](unicodeinc.md)

The C11 standard provides a new prefix, u8, which allows you to define a UTF-8
string literal

A wide-string literal is defined using the prefix L:
L"This String is Wide."

and of the type **wchar_t**.

Although C does not strictly prohibit modifying string literals, you should not
attempt to do so.
