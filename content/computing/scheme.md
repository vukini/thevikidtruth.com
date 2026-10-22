---
title: Scheme
date: '2016-11-30T08:50:15+04:00'
lastmod: '2022-09-15T05:44:33+04:00'
original_id: '{A540}'
original_name: scheme
original_blob: blob/B/11/356.txt
revisions: 16
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: scheme
draft: false
topics:
- lisp
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Racket](racket.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md)

# Scheme

I am partial to scheme, I always really appreciated it.

```
   (define (max-of-list lst)
     (foldr max (first lst) (rest lst)))
```

That little function says why. It finds the largest number in a list by *folding* `max` across it, in one line, with no loop counter and no temporary variable. That is Scheme's whole character: small, sharp ideas that combine.

### What it is, in plain words

Here is the truth about Scheme: **it is the Lisp that was designed by subtraction.** Guy Steele and Gerald Sussman created it at MIT in 1975 to understand the actor model, and found that a tiny Lisp with lexical scope and first-class functions already did everything they needed.

Scheme gives you:

- **Lexical scope and closures** – a function remembers the variables around where it was defined.
- **Proper tail calls** – a recursive call in tail position is a jump, so recursion *is* iteration and never blows the stack.
- **First-class continuations** (`call/cc`) – you can capture "the rest of the computation" as a value, which is how generators, coroutines and exceptions can be built in the language itself.
- **Hygienic macros** (`syntax-rules`) – macros that cannot accidentally capture your variable names.
- **One namespace** for functions and variables (a "Lisp-1"), unlike Common Lisp.

The standards are the **RnRS** reports. R5RS (1998) is tiny and still widely taught. R6RS (2007, see below) is larger and stricter. **R7RS-small** (2013) is what most implementations target today; R7RS-large is being built piece by piece through SRFIs (Scheme Requests for Implementation).

### Why it matters

- **It teaches computation itself.** *SICP*, the most famous programming textbook ever written, uses Scheme because the language gets out of the way of the ideas.
- **It is everywhere quietly.** GNU Guile is the extension language of GNU Guix and GnuCash; Chez Scheme is the engine under [Racket](racket.md); Scheme dialects script GIMP (Script-Fu) and LilyPond.
- **Its ideas spread.** Closures in [JavaScript](jsfunctions.md), tail calls in functional languages, hygienic macros in Rust: all owe something to Scheme.

### An everyday analogy: Lego Technic

Scheme is a small box of Lego Technic pieces: beams, pins, gears and axles. There is no pre-moulded car body in the box. But because the pieces connect in every direction, you can build a gearbox, a crane or a car, and you understand exactly how each one works because you built it.

### A hands-on example

Install a Scheme on Vikix: `xbps-install -S chez-scheme` (R6RS, very fast) or `guile` (R7RS mostly, GNU), or use Racket's `#lang r7rs`.

```scheme
;; Tail recursion: this loop runs in constant stack space
(define (sum-to n)
  (let loop ((i 0) (acc 0))
    (if (> i n)
        acc
        (loop (+ i 1) (+ acc i)))))

(sum-to 1000000)          ; => 500000500000

;; Closures: a counter that remembers its own state
(define (make-counter)
  (let ((n 0))
    (lambda () (set! n (+ n 1)) n)))

(define c (make-counter))
(c) (c)                   ; => 2

;; Higher-order functions
(map (lambda (x) (* x x)) '(1 2 3 4))    ; => (1 4 9 16)

;; The fold from the top of the page, in portable R7RS
(define (max-of-list lst)
  (let loop ((best (car lst)) (rest (cdr lst)))
    (if (null? rest)
        best
        (loop (max best (car rest)) (cdr rest)))))
(max-of-list '(3 9 2 7))  ; => 9
```

Note `foldr` is a Racket name; portable Scheme gets folds from SRFI 1 (`fold`, `fold-right`). The PicoLisp version of the same idea is just `(apply max '(3 9 2 7))`.

### Common misconceptions

- **"Scheme is only for teaching."** Chez Scheme is one of the fastest dynamic language implementations around, and Guix is a whole Linux distribution configured in Guile.
- **"Recursion is slow and dangerous."** Not with proper tail calls, which the standard *requires*.
- **"Scheme and Common Lisp are the same thing."** They share parentheses. Scheme is minimal, Lisp-1 and standard-driven; [Common Lisp](commonlisp.md) is large, Lisp-2 and industrial.
- **"`call/cc` is just a curiosity."** It is how you understand every control structure as a special case of one idea.

### Connections

- [Racket](racket.md), [Common Lisp](commonlisp.md), [PicoLisp](picolisp.md), [Lambda Calculus](lambdacalculus.md).
- [Functional Programming](functional.md), [Haskell](haskell.md), [Data Structures and Algorithms](datastructuresandalgorithms.md).
- [Computer Languages](computerlanguages.md) – where Scheme sits in the family tree.

## [R6RS - Revision 6 Scheme Standard](r6rs.md)

Programming languages should be designed not by piling feature on top of feature, but by removing
the weaknesses and restrictions that make additional features appear necessary. Scheme demonstrates
that a very small number of rules for forming expressions, with no restrictions on how they are composed,
suffice to form a practical and efficient programming language that is flexible enough to support most of the major ...
[Read more.](r6rs.md)

## Links, Sources and Reading List

- [The Scheme Programming Language, Edition](https://www.scheme.com/tspl4/)
- [Learn Scheme by Jared Krinke](https://jaredkrinke.github.io/learn-scheme/)
- [r6rs specs home](http://www.r6rs.org)
- [r6rs specs pdf](http://www.r6rs.org/final/r6rs.pdf)
- [Racket](https://racket-lang.org)
- [Tutorial A](https://classes.soe.ucsc.edu/cmps112/Spring03/languages/scheme/SchemeTutorialA.html)
- [ schemeprogramming.blogspot.ae](http://schemeprogramming.blogspot.ae)
- [SICP - Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sicp/)
- [Gambit Scheme](https://gambitscheme.org/latest/manual/)
- [Chicken-Scheme](https://call-cc.org)
