---
title: Picolisp Life Program
date: '2017-06-15T12:08:43+04:00'
lastmod: '2017-06-17T05:38:56+04:00'
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
draft: true
review: update
topics:
- lisp
---

# Picolisp Life Program

[Computing](computing.md) | [Picolisp](picolisp.md) | [ASM](pilasm.md) | [pil sources](pilsource.md)

# A Study

**Conway's Game of Life**, also known simply as **Life**, was a [cellular automaton](cellularautomaton.md "MISSING PAGE")
devised by the British mathematician [John Horton Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in 1970. For all its simplicity it raises really deep
questions in philosophy and our understanding of the Universe. It has been a topic of intense research by Computer
Scientists and Physicists ever since. Read about it
[here](http://web.stanford.edu/~cdebs/GameOfLife/) to get orientated.

This particular instance is coded in picolisp and comes packaged in the source.

Once you have downloaded the picolisp sources you will find a folder called `  misc  ` inside the main `  picoLisp  ` folder.
This has various example programs that are great to study.

In this article we are going to study the code inside the **life.l** program. To tell you the truth, as I write this
article **I don't understand it myself.** So whatever I glean from the code, I will be learning it with you. So, let's
get stuck in, try and make head and tail, of what looks to me like impenetrable code.

The whole source for this is at the bottom of the article for reference.

## Running Life.l

Assuming you are in the source folder, in bash type:

```
 $ pil life.l
```

You should see this output:

[life (ogg)](/assets/life.ogg)

We can make it a little more exciting by speeding up the rendering. This way you can really intuit what the program
is doing much better.

Go to **line 15** and change it to:
` (wait 50) `.
This will shorten how long picolisp waits between each pass of the loop.

The output will now be:

[life-fast (ogg)](/assets/life-fast.ogg)

That's all there is to it. You have basically just done what **Genetic Engineers** do all around the world. You have
tweaked **the code of life** and produced a better producing variant!

## Understanding the Code

This code is complex, and will take to the heart of many of picolisp's most powerful functions. So it may be best
looking at some of these in a little detail as we parse the code.

However, firstly, let's make a sweep of the whole source to understand it's structure from a high level.

#### First Sweep

**Line 1 - 2:** Are simple comments telling you who wrote this code and when.

**Line 4:** We load simul.l

```
(load "@lib/simul.l")
```

In **load** the **@** (within a string) just acts as a shortcut the home directory of the picolisp process.
So it is effectively like writing,

`(load "/home/of/picolisp/lib/simul.l")`.

Which will then effectively load that file and all it's definitions, etc, as if you had written them right here, in
the file.

Libraries such as this are good practice for code that you except you might use for other similar programs.
Unfortunately for us, this means we will have to dive into the library, if we are to understand what is going on in
**life.l**

**line 6:** We want some extra level of randomness in our code, so that it starts afresh each time we load the game.

**line 8-11:** We create a 26 x 26 grid and temporarily set it to the variable **Grid**. If you remember from running
 **life** as we did above, the stage was set within a **grid**. So it looks like that's what we are doing here.
It then appears that we populate the **elements / cells** of this **grid** with a **random boolean** (i.e. T or NIL). Which will set
each cell either **on or off**. This way each time the game starts in a new state.

**line 12 - 33:** We will change the state of the display the grid (**line 13**), wait (`line 15`), and then, depending
on whether **each cell and its neighbours** are on or off, we will be the rules of the game, **change its state**.

And we will do this in a continuous loop. Hence we will get the output we just experienced.

#### Getting Stuck in

###### Line6: Randomness

```
(seed (in "/dev/urandom" (rd 8)))
```

[seed](https://picolisp.com/wiki/@doc/refS.html#seed) is used to initialize our random generators. What it
does **internally** is to set a number **Seed** within the code, which is then used by
[rand](https://picolisp.com/wiki/@doc/refR.html#rand) to generate its output.

In Linux, **/dev/random is a special file that serves as a blocking pseudorandom number generator.**

So we utilize this OS feature and use it **"as if it were a file"** and **"binary read"
([rd](https://picolisp.com/wiki/@doc/refR.html#rd)) 8 bytes of the file as a single number**.

To understand the next block of code (**Line 8-11**), we need to have a look at the definition of **grid**
as it is central to what happens next.

###### simul.l Lines 89 - 117, Setting up the Grid

Remember the call to **grid** in **life.l, line 8**, is

```
 (grid 26 26)
```

This means we are only using 2 out of the 4 formal arguments. **DX = DY = 26, FX = FY = NIL**

```
 89 (de grid (DX DY FX FY)
 90    (let Grid

 91       (make
 92          (for X DX
 93             (link
 94                (make
 95                   (for Y DY
 96                      (set
 97                         (link
 98                            (if (> DX 26)
 99                               (box)
100                               (intern (pack (char (+ X 96)) Y)) ) )
101                         (cons (cons) (cons)) ) ) ) ) ) )

102       (let West (and FX (last Grid))
103          (for (Lst Grid  Lst)
104             (let
105                (Col (++ Lst)
106                   East (or (car Lst) (and FX (car Grid)))
107                   South (and FY (last Col)) )
108                (for (L Col  L)
109                   (with (++ L)
110                      (set (: 0 1) (++ West))  # west
111                      (con (: 0 1) (++ East))  # east
112                      (set (: 0 -1) South)     # south
113                      (con (: 0 -1)            # north
114                         (or (car L) (and FY (car Col))) )
115                      (setq South This) ) )
116                (setq West Col) ) ) )
117       Grid ) )
```

It's best to think what a grid is and how one could represent it in a program.

For simplicity consider a 3 x 3 grid.

```
   X1 X2 X3
   X4 X5 X6
   X7 X8 X9
```

We can easily see a grid has 3 x 3 = 9 elements. But labeling them X1 to X9 is not as helpful as perhaps:

```
  a1 a2 a3
  b1 b2 b3
  c1 c2 c3
```

Here we know instantly the exact position of the element of the grid as we differentiate row by letters and
columns by numbers.

I hope that you would agree it is just a small step for then concluding that a list structure such as:

```
  ((a1 a2 a3) (b1 b2 b3) (c1 c2 c3))
```

Could represent such a grid. I.e. **A list of lists**.

Please appreciate the following results.

```
: (intern (pack (char (+ 1 96)) 1))
-> a1
: (intern (pack (char (+ 2 96)) 1))
-> b1
: (intern (pack (char (+ 2 96)) 2))
-> b2
```

and study [intern](https://picolisp.com/wiki/@doc/refI.html#intern),
[pack](https://picolisp.com/wiki/@doc/refP.html#pack) and
[char](https://picolisp.com/wiki/@doc/refC.html#char), to figure out how this works.

Now appreciate this following code:

```
? (make (for X 3 (link (make (for Y 3 (link 'X))))))
-> ((X X X) (X X X) (X X X))
```

and,

```
: (make (for X 3 (link (make (for Y 3 (link (intern (pack (char (+ X 96)) Y))))))))
-> ((a1 a2 a3) (b1 b2 b3) (c1 c2 c3))
```

I think you can appreciate what this code is doing. Explaining each line is tedious, you need to spend some
time thinking about it.

Essentially, when we enter the function we start with a [let](https://picolisp.com/wiki/@doc/refL.html#let)
 expression which sets **Grid** to **NIL**.

*(It is a picolisp convention
to use Capitalized Variable names for function local variables)*

We then proceed to construct a list of lists (to represent the grid) using the picolisp make procedure
 in conjunction with 2 for loops. One for the outer list, the second for each consecutive in inner list.

Finally we name each element of the list as demonstrated above and **set** its value to:

```
: (cons (cons) (cons))
-> ((NIL) NIL)
```

a straight call to ` (cons) ` in picolisp returns **NIL**.

Try pasting the following code into a normal pil repl, and see the result.

```
(setq Grid
       (make
          (for X 3
             (link
                (make
                   (for Y 3
                      (set
                         (link
                            (if (> DX 26)
                               (box)
                               (intern (pack (char (+ X 96)) Y)) ) )
                         (cons (cons) (cons)) ) ) ) ) ) ))
```

and you will see that **we have made a 3 x 3 grid with element a1, a2, ..., c3 with each element set to ((NIL) NIL).**

The rest of the grid function is not import right now. Except the Last Line, which return Grid. So a call to **grid**
returns a **list of list structure that represents the Grid**.

Returning to **life.l, Lines 8 - 11**.

```
  8 (let Grid (grid 26 26)
  9    (for Col Grid
 10       (for This Col
 11          (=: life (rand T)) ) )
```

Here we are adding a property called **life** randomly to each element.

- **line 8**, The call to **grid** returns a list of **columns**.
- **Line 9**, Then for each for each **column** of **Grid** and,
- **Line 10**,for each **cell** in the column. (notice how we clever set the cell to **This**
- **Line 11**we set a new property **( := uses This)** called **life** to a **randomly chosen Boolean (T or NIL)**

###### Line 131-156, (disp), simul.l

The next section of code needs us to understand **disp** (short for display), which is defined in **simul.l**.
The best way to understand how it works is to look at a sample output.

```
: (disp Grid NIL '((X) "X "))

 4 X X X X
 3 X X X X
 2 X X X X
 1 X X X X
   a b c d

-> NIL
```

Here's the code in full:

```
131 (de disp (Grid How Fun X Y DX DY)
132    (setq Grid
133       (if X
134          (mapcar
135             '((L) (flip (head DY (nth L Y))))
136             (head DX (nth Grid X)) )
137          (mapcar reverse Grid) ) )
138    (let (N (+ (length (cdar Grid)) (or Y 1))  Sp (length N))
139       (border north)
140       (while (caar "Grid")
141          (prin   (align Sp N)
142             (and How (if (and (nT How) (west (caar Grid)))   '|)) )
143          (for L Grid
144             (prin
145                (Fun (car L))
146                (and How (if (and (nT How) (east (car L)))   '|)) ) )
147          (prinl)
148          (border south)
149          (map pop Grid)
150          (dec 'N) )
151       (unless (> (default X 1) 26)
152          (space (inc Sp))
153          (for @ Grid
154             (prin   (and How   ) (char (+ 96 X)))
155             (T (> (inc 'X) 26)) )
156          (prinl) ) ) )
```

The argument signature of **disp** is **(Grid How Fun X Y DX DY)**, in **life.l** the call is:

```
 13       (disp Grid NIL
 14          '((This) (if (: life) "X " "  ")) )
```

this maps out as

- **Grid =** `Grid`
- **How =** `NIL`
- **Fun =** `'((This) (if (: life) X    )) )`
- **X = Y = DX = DY =** Not set hence NIL

As X = NIL, **Line 133** the if will go directly to the **else** clause.

` (mapcar reverse Grid)`

Which has the following effect for a 4 x 4 grid:

```
: Grid
-> ((a1 a2 a3 a4) (b1 b2 b3 b4) (c1 c2 c3 c4) (d1 d2 d3 d4))
: (mapcar reverse Grid)
-> ((a4 a3 a2 a1) (b4 b3 b2 b1) (c4 c3 c2 c1) (d4 d3 d2 d1))
```

**Line 138**,  `(cdar Grid) is effectively (car (cdr Grid)`h and,
set **Sp** to (length of N in Bytes, i.e. 1)

**line 139:**The line can be effectively ignored as **How** is **NIL** when we called grid.

```
(de "border" (Dir)
   (when "How"
      (space Sp)
      (prin "  +")
      (for L "Grid"
         (prin (if (and (nT "How") (Dir (car L))) "   +" "---+")) )
      (prinl) ) )
```

**Line 140 - 150, the while loop**

`(caar Grid)` will always return some **cell** while there is at least some column in **Grid** else it return **NIL**.

**lines 141 -142:**

```
 (prin " " (align Sp N) " "
            (and "How" (if (and (nT "How") (west (caar "Grid"))) " " '|)) )
```

**Line 142:** can be effectively ignored as **"How"** in **NIL**. **Sp**

## The Sources

#### life.l

```
# 31dec13abu
# (c) Software Lab. Alexander Burger

(load @lib/simul.l)

(seed (in /dev/urandom (rd 8)))

(let Grid (grid 26 26)
   (for Col Grid
      (for This Col
         (=: life (rand T)) ) )
   (loop
      (disp Grid NIL
         '((This) (if (: life) X    )) )
      (wait 1000)
      (for Col Grid
         (for This Col
            (let N  # Count neighbors
               (cnt
                  '((Dir) (get (Dir This) 'life))
                  (quote
                     west east south north
                     ((X) (south (west X)))
                     ((X) (north (west X)))
                     ((X) (south (east X)))
                     ((X) (north (east X))) ) )
               (=: next  # Next generation
                  (if (: life)
                     (>= 3 N 2)
                     (= N 3) ) ) ) ) )
      (for Col Grid  # Update
         (for This Col
            (=: life (: next)) ) ) ) )

# vi:et:ts=3:sw=3
```

#### simul.l

```
# 24nov16abu
# (c) Software Lab. Alexander Burger

(de permute (Lst)
   (ifn (cdr Lst)
      (cons Lst)
      (mapcan
         '((X)
            (mapcar
               '((Y) (cons X Y))
               (permute (delete X Lst)) ) )
         Lst ) ) )

(de subsets (N Lst)
   (cond
      ((=0 N) '(NIL))
      ((not Lst))
      (T
         (conc
            (mapcar
               '((X) (cons (car Lst) X))
               (subsets (dec N) (cdr Lst)) )
            (subsets N (cdr Lst)) ) ) ) )

(de shuffle (Lst)
   (by '(NIL (rand)) sort Lst) )

(de samples (Cnt Lst)
   (make
      (for (N (length Lst) (n0 Cnt) (++ Lst) (dec N))
         (when (>= Cnt (rand 1 N))
            (link (car Lst))
            (dec 'Cnt) ) ) ) )

# Genetic Algorithm
(de gen (Pop Cond Re Mu Se)
   (until (Cond Pop)
      (for (P Pop P (cdr P))
         (set P
            (maxi Se  # Selection
               (make
                  (for (P Pop P)
                     (rot P (rand 1 (length P)))
                     (link  # Recombination + Mutation
                        (Mu (Re (++ P) (++ P))) ) ) ) ) ) ) )
   (maxi Se Pop) )

# Alpha-Beta tree search
(de game (Flg Cnt Moves Move Cost)
   (let (Alpha '(1000000)  Beta -1000000)
      (recur (Flg Cnt Alpha Beta)
         (let? Lst (Moves Flg)
            (if (=0 (dec 'Cnt))
               (loop
                  (Move (caar Lst))
                  (setq *Val (list (Cost Flg) (car Lst)))
                  (Move (cdar Lst))
                  (T (>= Beta (car *Val))
                     (cons Beta (car Lst) (cdr Alpha)) )
                  (when (> (car Alpha) (car *Val))
                     (setq Alpha *Val) )
                  (NIL (setq Lst (cdr Lst)) Alpha) )
               (setq Lst
                  (sort
                     (mapcar
                        '((Mov)
                           (prog2
                              (Move (car Mov))
                              (cons (Cost Flg) Mov)
                              (Move (cdr Mov)) ) )
                        Lst ) ) )
               (loop
                  (Move (cadar Lst))
                  (setq *Val
                     (if (recurse (not Flg) Cnt (cons (- Beta)) (- (car Alpha)))
                        (cons (- (car @)) (cdar Lst) (cdr @))
                        (list (caar Lst) (cdar Lst)) ) )
                  (Move (cddar Lst))
                  (T (>= Beta (car *Val))
                     (cons Beta (cdar Lst) (cdr Alpha)) )
                  (when (> (car Alpha) (car *Val))
                     (setq Alpha *Val) )
                  (NIL (setq Lst (cdr Lst)) Alpha) ) ) ) ) ) )

### Grids ###
(de grid (DX DY FX FY)
   (let Grid
      (make
         (for X DX
            (link
               (make
                  (for Y DY
                     (set
                        (link
                           (if (> DX 26)
                              (box)
                              (intern (pack (char (+ X 96)) Y)) ) )
                        (cons (cons) (cons)) ) ) ) ) ) )
      (let West (and FX (last Grid))
         (for (Lst Grid  Lst)
            (let
               (Col (++ Lst)
                  East (or (car Lst) (and FX (car Grid)))
                  South (and FY (last Col)) )
               (for (L Col  L)
                  (with (++ L)
                     (set (: 0 1) (++ West))  # west
                     (con (: 0 1) (++ East))  # east
                     (set (: 0 -1) South)     # south
                     (con (: 0 -1)            # north
                        (or (car L) (and FY (car Col))) )
                     (setq South This) ) )
               (setq West Col) ) ) )
      Grid ) )

(de west (This)
   (: 0 1 1) )

(de east (This)
   (: 0 1 -1) )

(de south (This)
   (: 0 -1 1) )

(de north (This)
   (: 0 -1 -1) )

(de disp (Grid How Fun X Y DX DY)
   (setq Grid
      (if X
         (mapcar
            '((L) (flip (head DY (nth L Y))))
            (head DX (nth Grid X)) )
         (mapcar reverse Grid) ) )
   (let (N (+ (length (cdar Grid)) (or Y 1))  Sp (length N))
      (border north)
      (while (caar Grid)
         (prin   (align Sp N)
            (and "How" (if (and (nT "How") (west (caar "Grid"))) " " '|)) )
         (for L Grid
            (prin
               (Fun (car L))
               (and How (if (and (nT How) (east (car L)))   '|)) ) )
         (prinl)
         (border south)
         (map pop Grid)
         (dec 'N) )
      (unless (> (default X 1) 26)
         (space (inc Sp))
         (for @ Grid
            (prin   (and How   ) (char (+ 96 X)))
            (T (> (inc 'X) 26)) )
         (prinl) ) ) )

(de border (Dir)
   (when How
      (space Sp)
      (prin   +)
      (for L "Grid"
         (prin (if (and (nT How) (Dir (car L)))    + ---+)) )
      (prinl) ) )
```
