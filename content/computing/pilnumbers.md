---
title: Working With Numbers
date: '2016-11-27T23:42:57+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A423}'
original_name: pilnumbers
original_blob: blob/B/2/365.txt
revisions: 6
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pilnumbers
draft: false
topics:
- lisp
---

[Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [pil sources](pilsource.md)

# Working With Numbers

There are a few in built functions that help us deal effectively with Numbers

The ones I use most: `*/`, `format`, `round`, `pad`, `hex`, `oct` and `bin`.

### The plain idea

[PicoLisp](picolisp.md) handles numbers in a way that trips up newcomers: it has **no floating-point type at all**. Instead it uses arbitrary-precision integers (bignums) and does "decimals" with **fixed-point** arithmetic, scaled integers. A price of 19.95 is stored as the integer 1995 with an understanding that there are two decimal places. The built-in helpers, `format`, `round`, `*/`, and the base converters `hex`, `oct`, `bin`, `pad`, are how you work with and display these numbers.

### Why it matters

Floating point is fast but *inexact*: the classic `0.1 + 0.2` does not equal `0.3` on most systems (see [Mathematics on Computers](mathoncomputers.md)). That rounding error is unacceptable for money and accounting, which is exactly what PicoLisp was built for. By using scaled integers, PicoLisp gives you *exact* decimal arithmetic, 19.95 + 0.05 is precisely 20.00, every time. It is a deliberate design choice that trades a little convenience for a lot of correctness.

### An everyday analogy

Instead of measuring in metres and fractions of a metre (where the fractions get fuzzy), PicoLisp measures everything in whole millimetres and just remembers where the decimal point goes. There are no "half-millimetres" to round awkwardly; every quantity is a clean whole number of the smallest unit, and the display puts the point back in at the end.

### A worked example: fixed-point in action

```lisp
(scl 2)                 # work to 2 decimal places
(+ 1995 5)              # -> 2000  (that's 19.95 + 0.05)
(format 2000 2)         # -> "20.00"   (format inserts the point)
(format 123456 2 ".")   # -> "1234.56"
(*/ 1995 3 1)           # fixed-point multiply/divide with rounding
```

`scl` sets the scale (how many decimal places the reader applies to literals like `19.95`), `format` turns a scaled integer back into a human string, and `*/` multiplies then divides with proper rounding, the workhorse for percentages and tax. For base conversions, `(hex 255)` gives `"FF"` and `(bin 5)` gives `"101"`.

### More examples, tested on PicoLisp 26.9

```picolisp
(scl 2)
19.95                       # -> 1995    the reader scales literals
(*/ 19.95 1.5 1.0)          # -> 2993    19.95 x 1.5 = 29.93 (rounded)
(format (*/ 19.95 1.05 1.0) 2)   # -> "20.95"  add 5% tax
(round 1234567 2)           # -> "12,345.67"  thousands separator included
(format 1234567 2 "." ",")  # -> "12,345.67"  same, explicit separators
1.5e3                       # -> 150000  e-notation works too (1500.00)
(format (sqrt 2.0 1.0) *Scl)     # -> "1.41"  sqrt with a scale factor
(= (+ 0.1 0.2) 0.3)         # -> T       exact, unlike floating point
(pad 5 42)                  # -> "00042"
(oct 8)                     # -> "10"
```

The rule of thumb for multiplying two scaled numbers is `(*/ A B 1.0)`: multiply, then divide by one unit of the scale to put the decimal point back, with rounding. To divide, use `(*/ A 1.0 B)`. If you really need IEEE floats (for example, to call a C library), the `native` FFI can pass and return doubles, converting to and from scaled integers at the boundary.

The old blog post I used to link here about fixed-point arithmetic is gone. The best current explanation is the [Numbers section of the reference](https://software-lab.de/doc/ref.html#number) and the [`*/`](https://software-lab.de/doc/refS.html#*/) and [`format`](https://software-lab.de/doc/refF.html#format) entries.

### Common misconceptions

- **"PicoLisp just lacks floats."** It is a feature, not a gap: exact decimals beat fast-but-fuzzy floats for the business use PicoLisp targets.
- **"Fixed-point limits the size of numbers."** No, the integers are arbitrary precision; you can compute factorials of huge numbers exactly.
- **"`format` does the maths."** `format` only *displays*; the arithmetic happens on the underlying scaled integers.

### How it connects

- [Mathematics on Computers](mathoncomputers.md): why floating point is inexact in the first place.
- [PicoLisp](picolisp.md) and [big.c](bigc.md): the bignum implementation underneath.
- [Binary](binary.md): base conversion and how numbers are stored.

The truth revealed: PicoLisp refuses floating point on purpose, and once you see that it is counting in whole smallest-units and only painting the decimal point on at the end, its arithmetic stops being odd and starts looking wiser than the default.
