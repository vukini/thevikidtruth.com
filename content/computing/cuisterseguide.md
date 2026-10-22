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
