---
title: The Picolisp Machine
date: '2016-11-25T22:39:56+04:00'
lastmod: '2022-09-15T00:45:42+04:00'
original_id: '{A345}'
original_name: pilmachine
original_blob: blob/B/11/305.txt
revisions: 82
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pilmachine
draft: false
topics:
- lisp
---

[Quicklinks](quicklinks.md) | [Readinglist](readinglist.md) |  [Computing](computing.md) | [Picolisp](picolisp.md) | [The Picolisp Reference](http://software-lab.de/doc/ref.html#vm) | [ASM](pilasm.md) |
[Pil Tutorials](piltutorials.md) |

# The Picolisp Machine

One of the key features of the picolisp language is that high-level constructs
of the language directly map to the underlying machinery,
making the whole system both understandable and predictable.

**Also please note that there are still a number of possible errors in this Document, it is under active development**

#### Data Types

These are the fundamental datatypes in Picolisp:

```
                       cell
                        |
            +-----------+-----------+
            |           |           |
         Number       Symbol       Pair
        S010 S100      1000        0000
       (cnt | big)      |
                        |
   +--------+----- --------+-----------+
   |        |              |           |
  NIL   Internal       Transient    External
              \\           /            |
             0010 Short name        1010 Short name
             0100 Long name         1000 Properties
             0000 Properties
```

#### The Cell

The most fundamental datatype is **the cell** which is the building block for all
other data types.

```
         +-----+-----+
         | CAR | CDR |
         +-----+-----+
```

Consider **memory** as an array of bytes growing downwards.

```
each x, c, i is a bit (0 or 1)
x means "address  bit, unimportant if it is 0 or 1"
i mean  "special  bit for the Interpreter"
c means "contents bit"
S means "Sign bit, 1 means negative, 0 positive"

          Them Address are 64 bits in Length                                          the lowest 4 bits are used by the interpreter
                                                                                      to figure out which type the value is
                                                                                                    |
             B8       B7       B6       B5       B4       B3       B2       B1   |          ContentsV
--------------------------------------------------------------------------------------------------------
ADDRESS: xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 0000, BYTE  0: cccc iiii  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 0001, BYTE  1: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 0010, BYTE  2: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 0011, BYTE  3: cccc cccc  |__ CAR (8 Bytes long, 64 bits)
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 0100, BYTE  4: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 0101, BYTE  5: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 0110, BYTE  6: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 0111, BYTE  7: cccc cccc  |
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
ADDRESS: xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 1000, BYTE  8: cccc iiii  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 1001, BYTE  9: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 1010, BYTE 10: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 1011, BYTE 11: cccc cccc  |__ CDR (8 Bytes long, 64 bits)
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 1100, BYTE 12: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 1101, BYTE 13: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 1110, BYTE 14: cccc cccc  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx 1111, BYTE 15: cccc cccc  |
--------------------------------------------------------------------------------------------------------__ Beginning of Next Cell
ADDRESS: xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxx1 0000, BYTE 16: cccc iiii  |
         xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxx1 0001, BYTE 17: cccc cccc  |
                                                                                                       V
```

The Same Contents can be written linearly like:

```
          BYTE 7   BYTE 6   BYTE 5   BYTE 4   BYTE 3   BYTE 2   BYTE 1   BYTE 0

   pair  cccccccc cccccccc cccccccc cccccccc cccccccc cccccccc cccccccc cccc 0000

   cnt   cccccccc cccccccc cccccccc cccccccc cccccccc cccccccc cccccccc cccc S010

   big   cccccccc cccccccc cccccccc cccccccc cccccccc cccccccc cccccccc cccc S100

   sym   cccccccc cccccccc cccccccc cccccccc cccccccc cccccccc cccccccc cccc 1000
```

The **lowest bit (M)** of a cell is set for garbage collection.

```
                                                                          [bit0]
                                                                            |
         B8       B7       B6       B5       B4       B3       B2       B1  |
      xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx000M
                                                                            |
                                                                            v
                                                    [Mark for garbage collection]
```

#### Numbers

Internally, numeric values of **up to 60 bits** are stored in
**"short" numbers or count (CNT)**

```
                                                                         [bit1 set]
                                                                           |
         B8       B7       B6       B5       B4       B3       B2       B1 |
      xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxS010  - 10 = 2 in Binary
                                                                         |
                                                                         v
                                                                   [sign-bit]
```

```
 BYTE 1: xxxxS010
 BYTE 2: xxxxxxxx
 BYTE 3: xxxxxxxx
 BYTE 4: xxxxxxxx
 BYTE 5: xxxxxxxx
 BYTE 6: xxxxxxxx
 BYTE 7: xxxxxxxx
 BYTE 8: xxxxxxxx
```

i.e. the value is directly represented in the pointer, and doesn't take any
heap space.

Numbers **larger than 60 bits** are called **"big nums"** and are stored like this:

```
         Bignum
         |
         V
      +-----+-----+
      | DIG |  |  |
      +-----+--+--+
               |
               V
            +-----+-----+
            | DIG |  |  |
            +-----+--+--+
                     |
                     V
                  +-----+-----+
                  | DIG | CNT |
                  +-----+-----+
```

```
                                                                        [bit2 set]
                                                                          |
         B8       B7       B6       B5       B4       B3       B2       B1|
      xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxS100    - 100 = 4 in binary
                                                                         |
                                                                         v
                                                                   [sign-bit]
```

#### Symbols

```
           Symbol
            |
            V
      +-----+-----+
      |  /  | VAL |  Getting the Value of a symbol is super efficient as the
      +-----+-----+  pointer points directly to it.
          _____
         |     |
         V     V
      +-----+-----+
      | CAR | CDR |
      +-----+-----+
         |
         V
       'tail' is kept in the CAR
```

```
                                                                       [bit3 set]
                                                                         |
         B8       B7       B6       B5       B4       B3       B2      B1|
      xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxx1000  - 1000 = 8 in binary
                                                                         |
                                                                         v
                                                         Notice the Symbol always
                                                         points to the 8th Byte
```

##### Property Lists and Symbol Names

- A property is a **key-value pair**, represented by a **cons pair** in the
     symbol's **tail**.
- This is called a **"property list"**.
- The property list may be terminated by a **number** representing the symbol's name.
- Each property in a symbol's tail is either a **symbol**
     or a **cons pair** with the **property key in its CDR** and the
     **property value in its CAR.**
    if it is a **symbol**, then it represents the **boolean value T** and the **key is is the CAR**
   The **name** of a symbol is **stored as a number** at the end of the tail. 
   It contains the characters of the name in **UTF-8 encoding**, **using between one and seven bytes
     in a short number, or eight bytes in a bignum cell.**
   The first byte of the first character, for example, is stored in the lowest 8 bits of the number.
- ###### Sample Symbols
- ```
              Symbol
              |
              V
        +-----+-----+                                +----------+---------+
        |  |  | VAL |                                |'hgfedcba'|'onmlkji'|
        +--+--+-----+                                +----------+---------+
          tail                                          ^
           |                                            |
           |                                            |
           |                                            |
           V                                          name
           +-----+-----+     +-----+-----+     +-----+--+--+
           |  |  |  ---+---> | KEY |  ---+---> |  |  |  |  |
           +--+--+-----+     +-----+-----+     +--+--+-----+
              |                                   |
              V                                   V
              +-----+-----+                       +-----+-----+
              | VAL | KEY |                       | VAL | KEY |
              +-----+-----+                       +-----+-----+
  ```
- ###### Bit Representations in Symbol Tails
- ```
     Symbol tail
        Internal/Transient
           0010 Short name
           0100 Long name
           0000 Properties
        External
           1010 Short name
           1000 Properties
           ^
           |
     [addition tag bit]
     Name final short
        Internals, Transients
           0000.xxxxxxx.xxxxxxx.xxxxxxx.xxxxxxx.xxxxxxx.xxxxxxx.xxxxxxx0010
             60      52      44      36      28      20      12       4
  ```
- ###### The Symbol NIL
- ```
        NIL:  /
              |
              V
        +-----+-----+-----+-----+
        |'LIN'|  /  |  /  |  /  |
        +-----+--+--+-----+-----+
  ```
- #### Pairs & Lists
- ```
        |
        V
        +-----+-----+
        | any |  |  |
        +-----+--+--+
                 |
                 V
                 +-----+-----+
                 | any |  |  |
                 +-----+--+--+
                          |
                          V
                          ...
  ```
- #### Internal Symbols
- *There cannot be two different symbols with the same name in the same namespace.*
- *NIL*
- #### Transient Symbols
- - as text strings
    - as identifiers with a limited access scope (like, for example, static identifiers in the C language family)
    - as anonymous, dynamically created objects (without a name)
- **Initially, a new transient symbol's VAL is that symbol itself.**
- [box](plbox.md)
- [new](plnew.md)
- #### External Symbols
- **additional tag bit**
- **tail structure**
- **names**
- ` { and } `
- **The characters of the symbol's name itself identify the physical location of the external object.**
- - in the 64-bit version: The number of the database file minus 1 in "hax" notation
    - ```
      (i.e. hexadecimal/alpha notation, where '@' is zero, 'A' is 1 and 'O' is 15 (from
        "alpha" to "omega")),
        immediately followed (without a hyphen) the starting block in octal ('0' through '7').
      ```
- #### Memory Management
- [see: mark-and-sweep garbage collector external link](https://www.geeksforgeeks.org/mark-and-sweep-garbage-collection-algorithm/
  Please)
