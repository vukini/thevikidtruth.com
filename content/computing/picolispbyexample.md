---
title: 'PicoLisp By Example'
date: '2017-06-21T13:09:16+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A1145}'
original_name: picolispbyexample
original_blob: blob/B/5/701.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: picolispbyexample
draft: false
topics:
- lisp
---

# PicoLisp By Example

### The plain idea

This page is my personal problem set for learning [PicoLisp](picolisp.md) by *doing*: small, interesting programming problems, each worked through in idiomatic PicoLisp. Every solution below was re-run on **PicoLisp 26.9** (pil21) in October 2026.

### Why learning by example works

PicoLisp is small and unusually consistent, which makes it ideal for this. Each problem shows a pattern (recursion, `make`/`link`, `filter`, `fish`, `tco`) that you will meet again and again in real code.

### An everyday analogy

You do not learn a language from a phrasebook; you learn it by having real little conversations. These problems are those conversations: short enough to finish, real enough to teach.

### A note on the sources

[PicoLisp by Example](https://github.com/tj64/picolisp-by-example) (by Alexander Burger and Thorsten Jolitz) is a book. Its first part solves the **99 Lisp Problems**, which began as a **Prolog** problem list by Werner Hett ([P-99](https://www.ic.unicamp.br/~meidanis/courses/mc336/problemas-prolog/)). Its second part collects 600+ [Rosetta Code](https://rosettacode.org/wiki/Category:PicoLisp) tasks. Rosetta Code is still the biggest public collection of PicoLisp solutions. The book was written in the pil32/pil64 era, so a few examples need small changes on pil21: library namespaces, and demos that were dropped from `misc/`.

I am not trying to copy that fine piece of work. I use it as inspiration and a guide for my own list of problems and solutions.

### The problems

Start the REPL with `pil +` and type along.

**1. Last element of a list** (P-99 #1). The recursive version first, then the built-in:

```picolisp
(de myLast (L)
   (if (cdr L) (myLast @) (car L)) )   # @ holds the result of (cdr L)
(myLast (1 2 3 4))   # -> 4
(last (1 2 3 4))     # -> 4
```

**2. Reverse a list** (#5), by pushing onto an accumulator:

```picolisp
(de myRev (L)
   (let R NIL
      (for X L (push 'R X))
      R ) )
(myRev (1 2 3))   # -> (3 2 1)
```

**3. Palindrome** (#6). A string becomes a list of characters with `chop`:

```picolisp
(de pal? (L) (= L (reverse L)))
(pal? (chop "racecar"))   # -> T
```

**4. Flatten a nested list** (#7). `fish` collects every element that satisfies a test:

```picolisp
(fish atom '(a (b (c d) e)))   # -> (a b c d e)
```

**5. Eliminate consecutive duplicates** (#8). `make`/`link` build a list, and `made` lets you look at it while it grows:

```picolisp
(de compress (L)
   (make
      (for X L
         (unless (= X (last (made))) (link X)) ) ) )
(compress '(a a a b c c a a d e e e))   # -> (a b c a d e)
```

**6. Pack runs into sublists, then run-length encode** (#9, #10):

```picolisp
(de pack2 (L)
   (make
      (while L
         (let X (car L)
            (link (make (while (= X (car L)) (link (pop 'L))))) ) ) ) )
(pack2 '(a a b c c c))   # -> ((a a) (b) (c c c))

(de encode (L)
   (mapcar '((G) (list (length G) (car G))) (pack2 L)) )
(encode '(a a a b c c))  # -> ((3 a) (1 b) (2 c))
```

**7. Primes** (#31, #39). A `loop` with two exit clauses:

```picolisp
(de prime? (N)
   (and (> N 1)
      (let D 2
         (loop
            (T (> (* D D) N) T)
            (T (=0 (% N D)) NIL)
            (inc 'D) ) ) ) )
(filter prime? (range 1 30))   # -> (2 3 5 7 11 13 17 19 23 29)
```

**8. Fibonacci with bignums.** `swap` sets a variable and returns its old value:

```picolisp
(de fib (N)
   (let (A 0 B 1)
      (do N (setq B (+ (swap 'A B) B)))
      A ) )
(fib 100)   # -> 354224848179261915075
```

**9. FizzBuzz** (Rosetta Code):

```picolisp
(for I 15
   (prin
      (cond
         ((=0 (% I 15)) "FizzBuzz")
         ((=0 (% I 3)) "Fizz")
         ((=0 (% I 5)) "Buzz")
         (T I) )
      " " ) )
```

**10. Deep recursion without stack growth.** This uses `tco`/`tc`, which were added in pil21. Plain recursion a million levels deep would exhaust the stack; this runs as a loop:

```picolisp
(de sumTo (N)
   (let Acc 0
      (tco (N Acc)
         (if (=0 N)
            Acc
            (tc (dec N) (+ Acc N)) ) ) ) )
(sumTo 1000000)   # -> 500000500000
```

**11. GCD.** There is no built-in `gcd`, so write Euclid's algorithm:

```picolisp
(de gcd (A B) (if (=0 B) A (gcd B (% A B))))
(gcd 36 60)   # -> 12
```

### Patterns worth noticing

- **`@`** holds the result of the last test (`if`, `and`, `while`…), which saves a `let`.
- **`make`/`link`/`made`** are the idiomatic way to build lists front to back.
- **Numbers are bignums**, so `fib`, `fact` and friends never overflow.
- **No `gcd`, no `odd?`.** The core stays small; you write the two-liners yourself (`(bit? 1 N)` tests oddness).

### More

- [Find Boxes in Lists](findboxes.md): the cell model behind all of the above.
- [PicoLisp Examples Examined](pilexamplesexamined.md): reading bigger programs.
- [PicoLisp Tutorials](piltutorials.md).
