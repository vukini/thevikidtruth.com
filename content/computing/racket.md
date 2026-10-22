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
---

# Racket

Racket is an evolution of the Scheme Language. A Scheme with Batteries and more.
[Read R6RS Scheme Specs. It always helps.](https://docs.racket-lang.org/r6rs/r6rs-std/index.html)

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
