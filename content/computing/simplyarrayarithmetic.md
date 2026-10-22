---
title: Simply Array Arithmetic & Referencing
date: '2016-12-10T22:12:34+04:00'
lastmod: '2016-12-10T22:48:34+04:00'
original_id: '{A1031}'
original_name: simplyarrayarithmetic
original_blob: blob/B/5/166.txt
revisions: 20
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: simplyarrayarithmetic
draft: false
topics:
- lisp
---
### The plain idea

An **array** is a row of boxes ("cells") laid out next to each other in memory, each holding one value and each reachable by a number called an *index*. This page builds that picture from scratch, a cell, a value, a row of cells, and then works out the little arithmetic you keep needing: given a start and an end index, how many cells are there, and where is the middle? Those two sums turn up constantly, and getting them slightly wrong is behind a huge share of real bugs.

### Why it matters

Array index arithmetic is where "off-by-one" errors live, the most common mistake in all of programming. The midpoint calculation in particular is the heart of **binary search** and countless divide-and-conquer algorithms, and the "how many cells between m and n" sum decides loop bounds everywhere. Nail the arithmetic once, carefully, with the boundary cases checked, and whole categories of bugs disappear.

### An everyday analogy: houses on a street

Think of an array as houses numbered along one side of a street, starting at number 0. "How many houses from number 4 to number 8?" is not 8 − 4 = 4; it is 8 − 4 + 1 = 5, because you count both ends. That "+1" is the famous fencepost problem (to fence a 10-metre run with posts every metre you need 11 posts, not 10), and it is exactly why the formula on this page has its "+ 1".

### A worked example: the formulas

For cells from index `m` to index `n`:

- **Count of cells** = `|m − n| + 1` (inclusive of both ends).
- **Midpoint index** = `m + (n − m) / 2`, taking the lower value when it lands between two cells.

A practical 2026 note on the midpoint: in real code, write it as `m + (n - m) / 2` rather than the "obvious" `(m + n) / 2`. For large indices the second form can *overflow* (the sum exceeds the largest representable integer), a famous bug that lurked in many published binary-search implementations for years. The `m + (n - m) / 2` form never overflows and gives the same answer.

### Checking the boundary

As the page shows, the real test of a formula is the smallest case. With a single cell (`m = n = 0`): count = `|0 − 0| + 1 = 1` cell, and midpoint = `0 + (0 − 0)/2 = 0`, the cell is its own middle. It works, which is how you gain confidence the general formula is right.



# Simply Array Arithmetic & Referencing

I have have always been a bit confused by how do simple arithmetic on arrays.
So we are going to look at it, step by step.

This is an **empty box:**

```
   ___
   | |
   ---
```

Lets call this box a **cell**

Here is a cell:

```
   ___
   |x|
   ---
```

This cell contains an **x** lets call this the **value of the cell.**

```
  a
  |
  V___
   |x|
   ---
```

there's an **arrow labelled a**. We would like to label all cells
so that we can easily locate them. Let us call these labels the **start
address** of the cell.

```
     b
     |
   __V
   |x|
   ---
```

there's an **arrow labelled b**. Let us call this this the **end
address** of the cell.

```
   a b
   | |
   V_v__
   |x|y|
   -----
    1 2  [cell number]
```

We can put one cell adjacent to the another. You will notice the
**end address of cell 1** = **start address of cell 2**.

So we don't need **end addresses any more**, so we can use the *names*
**start address** or **address** interchangeably as there will be no confusion.

Here is a row of empty cells with a **known address, a**.

```
   a
   |
   v
   ---------------------
   | | | | | | | | | | |
   ---------------------
```

lets call a **row of cells** an **array**.

We are going to label each cell with an address, however have two
options. We can start labelling with 1 or 0, such as:

```
   a a a a a a a a a a
   1 2 3 4 5 6 7 8 9 10
   | | | | | | | | | |
   v v v v v v v v v v
   ---------------------
   | | | | | | | | | | |
   ---------------------

           OR

   a a a a a a a a a a
   0 1 2 3 4 5 6 7 8 9
   | | | | | | | | | |
   v v v v v v v v v v
   -------------------
   | | | | | | | | | |
   -------------------
```

**We will introduce a new notation. Given any cell with an address
we can label the cell in location n as a[n].**

The question is what labelling option to choose. Start with 0 or 1?

Remember the number line from maths class:

```
                     start
                     |
                     v
       7-6-5-4-3-2-1 0 1 2 3 4 5 6 7
     <---------------+--------------->
```

It is **convenient** in this view to see the **cells** starting with a **start
address** of **0**.

```
                     start
                     |
                     a a a a a a a a
                     0 1 2 3 4 5 6 7
     <---------------+--------------->
                     |r|s|t|u|v|w|x|
                     ---------------
```

Consider the cells above. **a[0] has a value of r, a[3] has a value of u.**

```
    We say a[0] = r
                     OR
           a[3] = u.

    etc...
```

i.e. the value is **immediately to the right** of the **start address**.

Also note **a[0]** is the **1st cell**. **a[3]** is the **4th cell**.

```
    Thus in any array, a[n] is the (n + 1)th cell.

    or conversely, the nth cell is labelled a[n-1]

    Oh, the horrors of labelling!
```

Now Consider the arrangment:

```
          a[4]    a[8]
   ________v_______V____
   |0|1|2|3|4|5|6|7|8|9|
   ---------------------
```

How many cells between a[8] and a[4] ?

This is more tricky than it sounds. The simple

answer would be:

```
   8-4 = 4 cells, with a mid-point of:

   4/2 = 2, thus a[4+2] -> a[6] as the mid-point.
```

However this is wrong.

a[8] is the **start address of the cell**, the cell actually
**occupies space until its end-address** which is **a[9]**.

```
       a[4]    a[8]
        _v_______V_____
   <--- 3|4|5|6|7|8|9| --->
        ---------------
                   ^
                   |
                  a[9] end address of a[8]
```

So the correct answer is:

```
   9 - 4 = 5 cells between a[8] and a[4].

   or in General for cells a[m] to a[n] :

   cell between = |m - n| + 1
                  ^     ^
                  |_____|
                  |
                  absolute value
```

And what it the **midpoint between the cells?**

```
    5 / 2 = 2.5 cells.
```

But we cant have halves (or any other fractional address or quantity)
for discrete cells.

So by convention we discard the 0.5 and consider the **lower bound**.

```
          a[4]     a[8]
   ________v_______v____
   |0|1|2|3|4|5|6|7|8|9|
   ---------------------
               ^     ^
               |     |
    a[4+2] = a[6]   a[9]  (end address)
      mid-point

 number of cells between = |8 - 4| + 1
```

In Computer Science it is always good to test your boundary conditions.

We can think about this on the boundary condition of having just the one cell

```
   a
   |
   V_
   |x|
   ---
   1   [cell number]
```

**Here the cell address is a or a[0].**

**How many cells are there?**

We are only given 1 cell with address a[0], so consider the **start cell and end cell, m = n = 0**

```
   Use the general equation:

   | m - n | + 1 =

   | 0 - 0 | + 1 = 1 Cell

   the mid-point = (1 - 0) / 2 = 0.5,

   so take the lower bound a[0]
```

**Everything works just fine. When we are given only one cell, we have only one cell and it is itself's mid-point.**

### How it connects

- [Stacks](stacks.md) and [storage/linkage](storagelinkage.md): how arrays sit in memory.
- [C Programming](cprogramming.md): where `a[i]` is literally `*(a + i)`, pointer arithmetic in disguise.
- [Algorithms](algorithms.md): binary search and divide-and-conquer live on this midpoint.

The truth revealed: most array bugs are not deep, they are a single miscounted fencepost or an overflowed midpoint, and the cure is to draw the boxes, write the formula, and test it on one cell.
