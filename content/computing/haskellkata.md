---
title: Haskell Kata
date: '2023-04-06T04:16:37+04:00'
lastmod: '2023-04-06T04:16:57+04:00'
original_id: '{A1755}'
original_name: haskellkata
original_blob: blob/B/12/044.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: haskellkata
draft: false
topics:
- functional
---

[Haskell](haskell.md) | [Haskell Kata](haskellkata.md) |

# Haskell Kata

Here is the truth about learning Haskell: **you do not learn it by reading. You learn it by typing small things into GHCi until the type errors stop surprising you.** A *kata* is a martial-arts drill repeated until it becomes reflex. This page is a set of drills.

### What it is, in plain words

[Haskell](haskell.md) is a purely functional, lazily evaluated, statically typed language. Each of those words shows up in these katas:

- **Pure** – a function given the same input always returns the same output, and does nothing else. `dbl 3` is always `6`.
- **Lazy** – nothing is computed until it is needed, which is why `take 5 [40, 45..]` works on an infinite list.
- **Statically typed with inference** – every expression has a type, checked before the program runs, but you rarely have to write it. Ask GHCi with `:t`.

The katas below cover functions, `if` expressions, lists, ranges and list comprehensions: the vocabulary for everything else.

### Why it matters

These few operations (`map`, `filter`, folds, comprehensions, ranges) are the core of functional programming in *every* language. Python's list comprehensions came from Haskell. JavaScript's `map` and `filter`, Rust's iterators and Lisp's `mapcar` are the same ideas. Drilling them in Haskell, where there is no loop to fall back on, makes them stick.

### An everyday analogy: scales on a piano

Nobody performs scales at a concert. But a pianist who has played them a thousand times can sight-read anything, because their fingers already know the shapes. `take`, `drop`, `zip`, `foldr` and comprehensions are the scales of functional code.

### Getting set up in 2026

The recommended installer is **GHCup**, which manages GHC (the 9.x series), `cabal` and the Haskell Language Server. On Vikix you can also use the distribution package: `xbps-install -S ghc cabal-install`. Then start the REPL:

```bash
ghci
```

Useful GHCi commands while you drill:

```
:t expr        -- show the type of an expression
:i name        -- info about a function or type class
:l file.hs     -- load a file
:r             -- reload after editing
:set +s        -- show time and memory for each evaluation
```

### How to drill

For each block below: type it in, predict the result *before* pressing Enter, then ask for the type with `:t`. If you were wrong, change one thing and try again. Some examples are deliberate traps, for instance `head [ ]` throws an exception (and GHC 9.8+ warns that `head` is partial), which is the lesson: prefer pattern matching or `Data.List.uncons` for lists that may be empty.

A few extra katas to finish each session:

```haskell
-- Write these yourself, then check with the answers
myLength :: [a] -> Int
myLength []     = 0
myLength (_:xs) = 1 + myLength xs

myMap :: (a -> b) -> [a] -> [b]
myMap _ []     = []
myMap f (x:xs) = f x : myMap f xs

-- FizzBuzz with guards
fizz :: Int -> String
fizz n | n `mod` 15 == 0 = "FizzBuzz"
       | n `mod` 3  == 0 = "Fizz"
       | n `mod` 5  == 0 = "Buzz"
       | otherwise       = show n

main :: IO ()
main = mapM_ (putStrLn . fizz) [1..15]
```

Compare `myMap` with the PicoLisp equivalent, `(de myMap (F L) (when L (cons (F (car L)) (myMap F (cdr L)))))`. Same recursion over the same list shape, a cons cell at a time (see [Find Boxes in Lists](findboxes.md)).

### Common misconceptions

- **"You need to understand monads first."** You need none of that for these katas. `IO` can wait until you want to print things.
- **"Lists are arrays."** Haskell lists are linked lists. `nL!!3` walks three cells; `length` walks the whole list.
- **"Lazy means slow."** Laziness lets you write `take 20 (cycle nL)` against an infinite list and pay only for what you use. It can cause memory build-up in folds; use `foldl'` from `Data.List` for big sums.
- **"`if` without `else` is fine."** In Haskell `if` is an expression and must always have both branches.

### Connections

- [Haskell](haskell.md), [PureScript](purescript.md), [Functional Programming](functional.md), [Lambda Calculus](lambdacalculus.md).
- [Scheme](scheme.md), [Racket](racket.md), [PicoLisp](picolisp.md) – the same drills in Lisp.
- [Algorithms](algorithms.md) and [Data Structures and Algorithms](datastructuresandalgorithms.md).

## Getting Started

min 1 2
max 1 2
}

```
dbl x = x + x
dbls x y = dbl x + dbl y

dsn x = if x > 100
  then x
  else x*2
dsn' x = (if x > 100 then x else x*3) + 1
```

```
nL = [0,1,2,3,4,5,6,7,8,9]
nL ++ [10,11,12]
0:nL
nL!!3
nLL= [nL,nL,nL]
nLL ++ [[0,2]]
[10,11,12]:nLL
```

```
length nL
null nL
take 5 nL
drop 5 nL
head [ ]
head nL
tail nL
last nL
init nL
reverse nL
maximum nL
minimum nL
sum nL
product nL
5 `elem` nL
elem 5 nL
```

```
[1..10]
['a'..'l']
[3, 4..12]
take 5 [40, 45..]
take 20 (cycle nL)
take 10 (repeat 5)
replicate 4 10
```

```
[ dsn x | x <- nL, x > 5 ]
beepBop xs = [ if x < 5 then "beep" else "bop" | x <- xs, odd x]
[ x*y | x <- [2,5,10], y <- [8,10,11]]
```
