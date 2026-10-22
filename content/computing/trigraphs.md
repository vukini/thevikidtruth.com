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
draft: true
review: update
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
