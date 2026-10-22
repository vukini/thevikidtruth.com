---
title: with-output-to-string
date: '2023-04-09T22:39:59+04:00'
lastmod: '2023-04-09T22:45:24+04:00'
original_id: '{A1761}'
original_name: withoutputtostring
original_blob: blob/B/12/147.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: withoutputtostring
draft: false
topics:
- lisp
---

[commonlisp](commonlisp.md) | [Functions](clfunctions.md) | [with-output-to-string](withoutputtostring.md)

# with-output-to-string

[External Link: Macro WITH-OUTPUT-TO-STRING](http://clhs.lisp.se/Body/m_w_out_.htm).

The macro WITH-OUTPUT-TO-STRING can be used to create a string output stream, and return the resulting string at the end.

```
with-output-to-string (var &optional string-form &key element-type)
declaration* form*

=> result*
```

```
element-type specifier is defaulted to character.
form* is implicit progn
```

**with-output-to-string** creates a character output stream
and performs a series of operation that output to the result.
automatically closed on exit
side effect: the string is modified

```
(with-output-to-string (str)
  (write-line "Foobar!" str)
  (write-string "Barfoo!" str))
;=> "Foobar!
;   Barfoo!"
```

```
(let ((str (make-string-output-stream)))
  (write-line "Foobar!" str)
  (write-string "Barfoo!" str)
  (get-output-stream-string str))
```
