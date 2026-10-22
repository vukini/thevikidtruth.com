---
title: Binary Systems
date: '2016-05-19T01:35:27+04:00'
lastmod: '2016-11-29T00:31:08+04:00'
original_id: '{A34}'
original_name: binary
original_blob: blob/B/2/651.txt
revisions: 14
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: binary
draft: false
topics:
- os-hardware
---

[Math](math.md) | [CS](computerscience.md) | [bciyh](bciyh.md) | [Philosophy](philosophy.md)

# Binary Systems

![binary-600](/assets/binary-600.jpg)
{.center}

It is no secret that at the bottom of all computing abstractions lies the **Binary**.

I believe that **Binary Systems** lie at the heart of the **Universe** and
moreover, that we have **Quatum Mechanics** because the universe is **Binary**.

Grokking this system is probably the most important thing that you will need to do today. So I say put down **whatever**
you are doing. It can wait. Getting Binary is priority.

## Distinguishing

Think about this...

```
        What Makes One Thought Different From Another?
```

If you think about it hard, I think you will find that at a very minimum, the difference between any two thoughts
can only be the difference between a **state** being is one of two positions, call them **On & Off**.

### The plain idea, in order

Binary is simply counting with two symbols instead of ten. We write numbers in base ten because we have ten fingers; a computer "counts" with switches that are either **on** or **off**, so it uses base two: 0 and 1. A single such switch is a **bit**; eight of them make a **byte**, which can hold 256 different patterns (2⁸). That is the whole foundation on which every photo, song, program and message is built.

### Why it matters

Underneath every abstraction, numbers, text, colour, sound, instructions, is a pattern of bits. Grasp binary and the machine stops being magic: you see why a byte maxes out at 255, why colours are written like `#FF8800`, why "kilobyte" is sometimes 1000 and sometimes 1024, and how the same pattern of bits can be a number, a letter, or a command depending only on how it is read.

### An everyday analogy: a row of light switches

Picture a row of light switches on a wall. Each is up or down. With three switches you can make eight distinct patterns (down-down-down, down-down-up, …). Add a switch and you double the patterns. That doubling with each new bit is why small numbers of bits reach huge numbers so fast: ten switches already give 1,024 patterns, thirty-two give over four billion.

### A worked example: reading and writing binary

Each position is a power of two, doubling from right to left: 1, 2, 4, 8, 16, 32, 64, 128. To read a binary number, add up the positions that are "on":

```
 1 0 1 1 0 1
32 .  8 4 . 1   ->  32 + 8 + 4 + 1 = 45
```

To go the other way, subtract the largest power of two you can, repeatedly: 45 − 32 = 13, 13 − 8 = 5, 5 − 4 = 1, 1 − 1 = 0, which lights up the 32, 8, 4 and 1 positions: `101101`. Counting up in binary, 0, 1, 10, 11, 100, 101, is the same "carry when you run out of symbols" trick you learned in base ten, just with the roll-over happening at two instead of ten.

### Misconceptions

- **"Computers understand binary because it's natural."** It is a practical choice: a switch reliably tells two states apart far more cheaply than ten voltage levels. Base two is engineering, not metaphysics.
- **"Binary and hexadecimal are different worlds."** Hex (base 16) is just shorthand for binary, one hex digit stands for exactly four bits, which is why programmers use it.
- **"A byte is always a character."** A byte is 256 patterns; what they *mean*, a number, an ASCII letter, part of a UTF-8 character, is a matter of interpretation. See [Unicode in C](unicodeinc.md).

### A note on the big claim above

My intro makes a bold leap, that the universe is binary and that is why we have quantum mechanics. I will be honest that this is my own speculation, not established physics. There is a real and fascinating idea nearby, John Wheeler's "it from bit" and the information-theoretic view of physics, and quantum computing really does rest on the *qubit*, which (unlike a bit) can be in a blend of 0 and 1 until measured. But that is almost the opposite of a simple on/off universe. Take my opening as enthusiasm, and the arithmetic below as solid ground.

### How it connects

- [Mathematics](math.md): number bases and powers.
- [Unicode in C](unicodeinc.md) and [Tokens](tokens.md): how bits become text.
- [Computing](computing.md) and [bciyh](bciyh.md): building up from the bottom.

The truth revealed: every towering abstraction in computing rests on the humblest of facts, a switch that is either on or off, and learning to read those switches is learning to read the machine itself.

## Sources and Links
- [Binary number - Wikipedia](https://en.wikipedia.org/wiki/Binary_number)
- [Code, by Charles Petzold](https://www.charlespetzold.com/code/) - the classic book on this idea
