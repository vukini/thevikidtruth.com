---
title: 'PicoLisp Life Program'
date: '2017-06-15T12:08:43+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A1120}'
original_name: pillife
original_blob: blob/B/5/612.txt
revisions: 23
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pillife
draft: false
topics:
- lisp
---

# PicoLisp Life Program

# A Study

**Conway's Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician [John Horton Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in 1970. For all its simplicity it raises really deep questions in philosophy and about our understanding of the Universe, and it has been a topic of intense research by computer scientists and physicists ever since. [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a good place to get oriented.

The rules are simple. Every cell in a grid is alive or dead. At each step:

- A live cell with **2 or 3** live neighbours survives.
- A dead cell with **exactly 3** live neighbours becomes alive.
- Every other cell dies or stays dead.

When I first wrote this study, a `life.l` program came packaged in the `misc/` folder of the PicoLisp sources. I confessed then that **I didn't understand it myself**, and learned it as I wrote. Current PicoLisp (pil21) no longer ships `misc/life.l`, so below is a complete version that I rewrote and tested on **PicoLisp 26.9** in October 2026. It keeps the original's idea: a grid from `@lib/simul.l`, where every cell is a symbol with a `life` property.

## The program

Save this as `life.l` and run it with `pil life.l`:

```picolisp
# life.l -- Conway's Game of Life on pil21
(load "@lib/simul.l")
(symbols '(simul pico))                 # simul.l lives in its own namespace
(seed (in "/dev/urandom" (rd 8)))

(let Grid (grid 26 26)
   (for Col Grid                         # random start
      (for This Col
         (=: life (rand T)) ) )
   (do 3                                 # three generations
      (disp Grid NIL
         '((This) (if (: life) "X " "  ")) )
      (wait 100)
      (for Col Grid                      # compute the next state
         (for This Col
            (let N
               (cnt
                  '((Dir) (get (Dir This) 'life))
                  (quote
                     west east south north
                     ((X) (south (west X)))
                     ((X) (north (west X)))
                     ((X) (south (east X)))
                     ((X) (north (east X))) ) )
               (=: next
                  (if (: life)
                     (>= 3 N 2)
                     (= N 3) ) ) ) ) )
      (for Col Grid                      # then switch all at once
         (for This Col
            (=: life (: next)) ) ) ) )
(bye)
```

It prints the board with row numbers on the left and letters a–z along the bottom, like a chess board:

```
 26 X X   X   X     X   X         X     X X   X   X   X
 25   X X X X     X   X X X   X X   X X X   X X     X X
 ...
  1 X     X     X X     X   X X   X X X X X
    a b c d e f g h i j k l m n o p q r s t u v w x y z
```

## Making head and tail of it

**`(load "@lib/simul.l")` and `(symbols '(simul pico))`.** `simul.l` is a small simulation library: `grid`, `disp`, and the direction functions `west`, `east`, `south` and `north`. In pil21 it defines its own namespace, `simul`. Without the `symbols` line you get `grid -- Undefined`. That was the first thing that broke when I re-ran my old notes.

**`(grid 26 26)`** returns a list of columns, and each column is a list of fresh symbols, one per cell. Each cell symbol knows its neighbours, so `(west This)` is the cell to the left. At the edge it is `NIL`, and `(get NIL 'life)` is simply `NIL`, which is why the edges need no special code. `(grid 26 26 T T)` would wrap around into a torus.

**`This` and `=:` / `:`.** This is the trick that I found impenetrable at first. `(=: life X)` means "set the `life` property of whatever `This` is", and `(: life)` reads it. By binding `This` with `(for This Col ...)`, every cell is treated like an object, without any class.

**Counting neighbours with `cnt`.** The quoted list holds eight "directions". Four are plain functions (`west`…) and four are little lambdas that combine two steps for the diagonals. `cnt` calls the test once per direction and counts how many neighbours are alive.

**`(>= 3 N 2)`** is PicoLisp's chained comparison: it is true when 3 ≥ N ≥ 2. That is the survival rule in one expression.

**Two passes.** The new state goes into `next` first and is copied into `life` only after every cell has been computed. Otherwise early cells would see their neighbours' *future* state.

**`disp`** draws the grid, calling our lambda for each cell to get a two-character string.

## Things to try

- Seed a glider instead of random noise: set `life` on just five cells, such as `(with (get Grid 2 24) (=: life T))`.
- Make the board wrap with `(grid 26 26 T T)`.
- Increase `(do 3 ...)` and clear the screen between generations with `(prin "\e[H\e[2J")`.

See also: [PicoLisp Examples Examined](pilexamplesexamined.md), [Chat](pilchat.md), [PicoLisp](picolisp.md).
