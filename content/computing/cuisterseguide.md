---
title: Cuis Terse Guide
date: '2023-03-30T20:31:26+04:00'
lastmod: '2023-03-30T20:46:12+04:00'
original_id: '{A1741}'
original_name: cuisterseguide
original_blob: blob/B/11/650.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: cuisterseguide
draft: false
topics:
- other-languages
---

[Read This!](caveatemptor.md) | | [Quick Links](quicklinks.md) | [Algorithms](algorithms.md) | [AssemblyLanguage](assemblylanguage.md) | [BASH](bash.md) |   [C-Programmming](cprogramming.md) |
[CommonLisp](commonlisp.md) |
[Computer Security](computersecurity.md) | [CuisSmalltalk](cuissmalltalk.md) | [Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) |
[Functional Programming](functional.md) |
[Firewalls](firewalls.md) |   [Git](git.md) | [GNUSmalltalk](gnusmalltalk.md) | [Haskell](haskell.md) | [Javascript](javascript.md) |  [Julia](julia.md) |
[Linux](linux.md) | [Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |[Machine Learning](machinelearning.md) |
[Networking](networking.md) | [Operating Systems](os.md) |[Open Data Science](opendatascience.md) | [Odin](odin.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) | [Purescript](purescript.md) |
[Python](python.md) |
[Racket](racket.md) | [Scheme](scheme.md) | [Social Engineering](internetexploitation.md) |
[Unity](unity.md) | [vim](vim.md) | [V](vlang.md) |
[Web Development](webdevelopment.md) | [Windows WSL](windowswsl.md) | [Zig](ziglang.md)

[Terse Guide](cuisterseguide.md)

# Cuis Terse Guide


Here is the truth about Smalltalk syntax: **it fits on a postcard.** There are no `if` statements, no loops and no operators built into the language. There are only objects and messages, and everything else, including conditionals and loops, is just messages sent to objects. This guide is the postcard, written out long-hand for [Cuis Smalltalk](cuissmalltalk.md).

### What it is, in plain words

A terse guide is a page of runnable snippets you can paste into a **Workspace** and evaluate, one line at a time, to remind yourself how something is spelled. The tradition comes from the Squeak community; this is my Cuis version.

Everything in it uses three kinds of message, which differ only in how they look and in precedence:

| Kind | Example | Precedence |
|---|---|---|
| **Unary** – a single word | `3 factorial`, `x class` | highest |
| **Binary** – symbols | `3 + 4`, `a = b`, `x @ y` | middle |
| **Keyword** – words ending in colons | `x between: 1 and: 10`, `d at: #k put: 5` | lowest |

Evaluation is strictly left to right within each level, so `3 + 4 * 2` is **14**, not 11. Use parentheses when you mean otherwise.

A few more marks complete the grammar: `.` separates statements, `;` cascades several messages to the same receiver, `^` returns a value, `[ ... ]` is a block (a closure), `#sym` is a symbol, `$a` is a character, `'text'` is a string, and `"double quotes"` are comments.

### A note on `_`

Many lines below use `_` for assignment, as in `x _ 4.` That is the original Smalltalk-80 left-arrow assignment; Cuis still accepts it and displays it as `←`. The portable spelling that works in Pharo, Squeak and GNU Smalltalk is `:=`, as in `z := 5.` Use `:=` in code you share.

### Why it matters

Because there are no special forms, once you know how messages are sent you can read *any* Smalltalk code. `ifTrue:` is a method on `Boolean`; `whileTrue:` is a method on blocks; `do:` is a method on collections. You can browse to their source with one click and see that they are ordinary Smalltalk. That is the opposite of most languages, where control structures are locked inside the compiler. It is also the same lesson Lisp teaches, from the other direction.

### An everyday analogy: a phrasebook

A traveller's phrasebook does not teach grammar. It gives you the twenty sentences you actually need, in a form you can say right now. This guide is a phrasebook for the Cuis image: you point at the line you need, evaluate it, and the image answers.

### A hands-on example: how to use this page

In Cuis 7, open a Workspace from the World menu, paste a block of lines, select one and press:

- **Ctrl-D** – *do it*: evaluate for its effect;
- **Ctrl-P** – *print it*: evaluate and paste the result after the selection;
- **Ctrl-I** – *inspect it*: open an inspector on the result;
- **Ctrl-B** – *browse it*: open the class browser on the selected class name.

Try this first, so the precedence rules become muscle memory:

```smalltalk
3 + 4 * 2.                          "print it -> 14"
3 + (4 * 2).                        "print it -> 11"
(1 to: 10) inject: 0 into: [:a :b | a + b].   "-> 55"
#(3 1 2) asSortedCollection asArray.          "-> #(1 2 3)"
(3 > 2) ifTrue: ['yes'] ifFalse: ['no'].      "-> 'yes'"
Transcript show: 'hello'; cr; show: 'world'; cr.   "a cascade"
```

Then browse the implementation of `ifTrue:ifFalse:` in class `True` and see that it is one line of Smalltalk.

### Common misconceptions

- **"Arithmetic follows maths precedence."** It does not. Binary messages go strictly left to right.
- **"`x _ 4` is a typo."** It is the historical assignment arrow; `:=` is the modern spelling.
- **"`ifTrue:` is a keyword of the language."** It is a message understood by `true` and `false`.
- **"Copy means a deep copy."** `copy` is usually `shallowCopy` plus `postCopy`; `veryDeepCopy` follows the whole object graph. Pick deliberately.

### Connections

- [Cuis Smalltalk](cuissmalltalk.md), [GNU Smalltalk](gnusmalltalk.md), [Objects in C](object.md) for the contrasting meaning of "object".
- [JS Objects](jsobjects.md), [Prototypal Inheritance](jsprototypalinheritance.md), [new](plnew.md) – PicoLisp's message-passing objects.
- [Lambda Calculus](lambdacalculus.md) – blocks are closures, the same idea in its purest form.

## The guide


```
x _ 4.

z := 5.

x _ y _ z _ 6.

x _ (y _ 6) + 1.

x _ Object new.

x _ 123 class.
x _ Object allInstances.

x _ Integer allInstances.
x _ Integer allSuperclasses.

w _ 1.2 hash.

t _ x copy.
y _ x shallowCopy.
y _ x veryDeepCopy.

TranscriptWindow openTranscript. Transcript
Transcript clear.
Transcript show: 'hello world'.
Transcript nextPutAll: 'Hello World'.
Transcript nextPut: $A.
Transcript space.
Transcript tab; nextPut: $A; space; tab; nextPut: $B.
Transcript newLine.

'Hello' printOn: Transcript.
'Yellow' storeOn: Transcript.
Transcript endEntry.

'Literals are objects that are created when you compile a method'

| b x |

b _ true.
b _ false.
x _ nil.
x _ 1.

x _ 3.14.
x _ 2e-1.
x _ 2.0e-2.

x _ 7/8.

x _ 16r0F.
x _ 16rFFFFFFFF.
x _ 16rFFFFFFFF negated.
x _ -1.

x _ 'hello'.
x _ 'I''m here'.
x _ $A.
x _ $ .
x _ #aSymbol.
x _ #(3 2 1).
x _ #('abc' 1 $a).
x _ #[3 2 1 0].
x _ #[1.0 3.12 6.03e23].

x _ {'hello' size. Float pi. 1.0 arcTan}.
x _ `{'hello' size. Float pi. 1.0 arcTan}`.

x _ `{ 1. 3. 5. 7. 11. 13. 17} asSet`.

"Booleans"
| b x y |
x _ 1. y _ 2.
b _ ( x = y).
b _ ( x ~= y).
b _ ( x == y).
b _ ( x ~~ y).
b _ ( x > y ).
b _ ( x < y).
b _ ( x >= y).
b _ ( x <= y).
b _ b not.
b _ (x < 5) & ( y > 1).
b _ (x < 5) | (y > 1).
b _ (x < 5) and: (y > 1).
b _ (x < 5) or: (y > 1).
b _ (x < 5) eqv: (y > 1).
b _ (x < 5) xor: (y > 1).
b _ 5 between: 3 and: 12.
b _ 123 isKindOf: Number.
b _ 123 isMemberOf: SmallInteger.
b _ 123 respondsTo: #sqrt.
b _ x isNil.
b _ x isZero.
b _ x positive.
b _ x strictlyPositive.
b _ x negative.
b _ x even.
b _ x odd.
b _ x isInteger.
b _ x isLiteral.
b _ x isNumber.
b _ x isSymbol.
b _ $A isUppercase.
```

#### "Bit-Wise"

```
x _ 16rFF bitAnd: 16r0F.     "and bits"
x _ 16rF0 bitOr: 16r0F.       "or bits"
x _ 16rFF bitXor: 16r0F.      "xor bits"
x _ 16rFF bitInvert.             "invert bits"
x _ 16r0F bitShift: 4.          "left shift "
x _ 16rF0 bitShift: -4.         "right shift"
x _ 16r80 bitAt: 8.             "bit at position (0|1)"
x _ 16r80 highBit.              "position of highest bit set"
b _ 16rFF allMask: 16r0F.    "test if all bits set in mask are set in receiver"
b _ 16rFF anyMask: 16r0F.  "test if any bits set in mask are set in receiver"
b _ 16rFF noMask: 16r0F. "test if all bits set in mask are clear in receiver"
```
