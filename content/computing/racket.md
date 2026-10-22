---
title: Racket
date: '2022-08-17T01:06:30+04:00'
lastmod: '2022-09-20T01:18:34+04:00'
original_id: '{A1701}'
original_name: racket
original_blob: blob/B/11/417.txt
revisions: 9
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: racket
draft: false
topics:
- lisp
---

# Racket

Racket is an evolution of the Scheme Language. A Scheme with Batteries and more.
[Read R6RS Scheme Specs. It always helps.](https://docs.racket-lang.org/r6rs/r6rs-std/index.html)


### What it is, in plain words

Here is the truth about Racket: **it is not really one language. It is a factory for making languages, which happens to ship with a very good Scheme as its default product.** Every Racket file starts with a `#lang` line that tells the system which language the rest of the file is written in.

Racket began in 1995 as PLT Scheme, a teaching environment from a group of universities led by Matthias Felleisen. It was renamed Racket in 2010 once it had grown well beyond standard Scheme. Since version 8 it runs on **Chez Scheme** underneath ("Racket CS"), which made it much faster. In 2026 the 8.x series is current, and there is also **Rhombus**, a new language built on Racket with a conventional, indentation-based syntax but the same macro power.

Out of the box you get:

- `#lang racket` – the full language, with modules, contracts, structs, classes, threads and a large standard library.
- `#lang typed/racket` – gradual static typing.
- `#lang htdp/bsl` and friends – the student languages from *How to Design Programs*, where `check-expect` (below) comes from.
- `#lang scribble`, `#lang datalog`, `#lang r7rs` and many more, all just libraries.
- **DrRacket**, a beginner-friendly IDE, and `raco` for packages and building executables.

### Why it matters

- **Language-oriented programming.** When a problem has its own vocabulary (configuration, music, tests, documentation), you can build a small language for it with macros and give it its own `#lang`. Racket is the best place to learn how that is done.
- **Teaching.** *How to Design Programs* is one of the clearest introductions to programming there is, and the student languages give error messages a beginner can actually read.
- **Batteries included.** Web server, GUI toolkit, plotting, a math library and a package catalogue mean a Scheme you can use for real projects.

### An everyday analogy: a kitchen that builds kitchens

Most languages are a kitchen: you cook in it. Racket is a kitchen that also contains the tools to build a new kitchen, a pastry kitchen or a sushi bar, each with its own layout. The `#lang` line on the door tells you which one you are walking into.

### A hands-on example

Install on Vikix with `xbps-install -S racket`, then:

```racket
#lang racket
;; squares.rkt
(define (square x) (* x x))

(define (sum-of-squares lst)
  (for/sum ([x lst]) (square x)))

(module+ test
  (require rackunit)
  (check-equal? (sum-of-squares '(1 2 3)) 14))

(module+ main
  (printf "~a\n" (map square (range 1 6))))
```

```bash
racket squares.rkt        # prints (1 4 9 16 25)
raco test squares.rkt     # runs the test submodule
raco exe squares.rkt      # builds a standalone executable
```

And a taste of the language factory, a macro that adds a `swap!` form:

```racket
(define-syntax-rule (swap! a b)
  (let ([tmp a]) (set! a b) (set! b tmp)))

(define x 1) (define y 2)
(swap! x y)               ; x = 2, y = 1
```

The macro is hygienic: its `tmp` cannot clash with a variable called `tmp` in your code.

### Common misconceptions

- **"Racket is just for students."** The student languages are one corner. Racket is used for research, tooling and real applications, and it is the reference platform for macro systems.
- **"Racket is Scheme."** It started as one. Today `#lang racket` is its own language, with immutable pairs by default and many extensions. Use `#lang r7rs` or `#lang r6rs` for standard Scheme.
- **"It is slow."** On the Chez Scheme back end it is competitive with other dynamic languages, often well ahead of them.
- **"You need DrRacket."** Emacs with `racket-mode` is excellent, and `racket` works fine from a terminal.

### Connections

- [Scheme](scheme.md), [Common Lisp](commonlisp.md), [PicoLisp](picolisp.md), [Lambda Calculus](lambdacalculus.md).
- [Functional Programming](functional.md), [Haskell](haskell.md), [PureScript](purescript.md).
- [Computer Languages](computerlanguages.md) – where Racket fits.

### Notes from my early Racket sessions

## Initial Grammar

```
   program ::= {expr | test | def}*
       def ::= (define <variable name> expr)
      test ::= (check-expect expr expr)
      expr ::= string
           ::= number
           ::= (<function> expr*)
           ::= <variable name>
    string ::= "<character>"
    number ::= positive
           ::= negative
  positive ::= mag
  negative ::= -mag
       mag ::= int
           ::= real
           ::= fraction
       int ::= digit*
     digit ::= 0|1|2|3|4|5|6|7|8|9
      real ::= digit*.digit*
  fraction ::= int/nonzero-int
non-zeroint::= <1|2|3|4|5|6|7|8|9>int
```

## DrRacket

If using DrRacket as an IDE. You can get auto-complete while typing "ctrl-/"

### Functions to Explore

```
(quote 1 2 3)
```

Testing:

```
(check-expect val val-expected)
(check-within val val-expected tolerance)
```

Lists

```
(list 'a 'b 'c)
(list? x)
(pair? y)
(cons a b)
(a . b)
(car L)
(first L)
(cdr L)
(rest L)
(second L)
(third L) ;; upto tenth
(list-ref L index) ;; (list-ref '(0 1 2 3 4 5 6) 3)
(length L)
(reverse L)
(sort L <)
(sort L >)
(append L1 L2 ...)
> (range 10)
'(0 1 2 3 4 5 6 7 8 9)
> (range 4 10)
'(4 5 6 7 8 9)
> (range 4 10 2)
'(4 6 8)
(make-list 10 'Vikid)
(null? '())
(index-of L member-searched-for)
```

## Links

[Eric Clack - Racket Examples](https://github.com/ericclack/racket-examples)
[Rash - The Reckless Racket Shell](https://rash-lang.org/)
[ Fear of Macros](https://www.greghendershott.com/fear-of-macros/)
[ 5 Advanced Racket Macros](https://school.racket-lang.org/2019/plan/tue-mor-lecture.html)
[ Fancy App: Scala-Style Magic Lambdas](https://docs.racket-lang.org/fancy-app/index.html)
[ Beautiful Racket by Matthew Butterick](https://beautifulracket.com/)
