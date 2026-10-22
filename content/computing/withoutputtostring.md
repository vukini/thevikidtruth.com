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

Here is the truth about `with-output-to-string`: **it lets any code that "prints" produce a string instead, without changing that code at all.** Printing and building strings turn out to be the same job pointed at different places.

### What it is, in plain words

In Common Lisp, output goes to a **stream**. `*standard-output*` is usually your terminal, but a stream can just as well be a file, a socket or a growing string in memory. `with-output-to-string` creates a string output stream, binds a variable to it, runs the body, and returns everything written to it as a fresh string.

The variable can be any name you like. The very common idiom `(with-output-to-string (*standard-output*) ...)` rebinds standard output itself, so even plain `(print ...)` and `(format t ...)` calls inside the body get captured.

### Why it matters

- **Testing.** You can check what a function prints by capturing it and comparing strings.
- **Reuse.** A function written to print a report can also produce the report as a string for a web page or an email, with no second version.
- **Performance and clarity.** Building a big string by repeated `concatenate` copies the string again and again. Writing to a string stream appends efficiently and reads naturally.

### An everyday analogy: a dictation machine

You can say a letter out loud to a room (print to the terminal) or say exactly the same words into a dictaphone (a string stream). The words do not change. At the end you take the tape out and you have the letter, ready to be posted somewhere else.

### A hands-on example

Try these in SBCL (`sbcl` on Vikix after `xbps-install -S sbcl`), ideally through SLY or SLIME in Emacs:

```lisp
;; Write to the stream variable directly
(with-output-to-string (s)
  (write-string "Hello, " s)
  (format s "~a! You have ~d messages." "VikiD" 3))
;; => "Hello, VikiD! You have 3 messages."

;; Capture code that only knows how to print
(defun report (items)
  (dolist (i items)
    (format t "~&- ~a~%" i)))

(with-output-to-string (*standard-output*)
  (report '("lists" "symbols" "streams")))
;; => "- lists
;; - symbols
;; - streams
;; "

;; Its input-side twin
(with-input-from-string (in "10 20 30")
  (+ (read in) (read in) (read in)))
;; => 60
```

The second form is the trick worth remembering: rebinding `*standard-output*` captures output from code you did not write.

For one-off formatting, `(format nil ...)` is simpler: `(format nil "~a-~a" 1 2)` returns `"1-2"`. Reach for `with-output-to-string` when the output is produced by several calls or by other functions.

**The PicoLisp way.** PicoLisp has no string streams, but you get the same effect two ways: `pack` joins values into a string directly, and `pipe` runs code that prints and lets you read the result back.

```picolisp
: (pack "Hello, " "VikiD" "! You have " 3 " messages.")
-> "Hello, VikiD! You have 3 messages."
: (pipe (prinl "captured") (line T))
-> "captured"
```

### Common misconceptions

- **"It modifies a string I pass in."** The optional `string-form` lets you append to an existing adjustable string with a fill pointer, but normally you pass nothing and get a *new* string back.
- **"It's the same as `format nil`."** `format nil` handles one format call. `with-output-to-string` captures any amount of output from any code.
- **"The stream stays open."** It is closed automatically when the body exits, even through an error, like `with-open-file`.
- **"Strings are slow to build in Lisp."** Repeated `concatenate` is. String streams are the fast, idiomatic way.

### Connections

- [Common Lisp](commonlisp.md), [Common Lisp Functions](clfunctions.md), [Lambda Calculus](lambdacalculus.md).
- [PicoLisp Input/Output](plio.md) – the PicoLisp view of streams.
- [Emacs Notes](emacsnotes.md) – where you will be running your REPL.

### Reference


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
