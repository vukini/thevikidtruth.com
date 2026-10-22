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
draft: true
review: update
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
