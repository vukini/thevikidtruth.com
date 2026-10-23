---
title: 'PicoLisp ASM'
date: '2016-11-26T11:39:51+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A360}'
original_name: pilasm
original_blob: blob/B/11/306.txt
revisions: 6
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pilasm
draft: false
topics:
- lisp
---

# PicoLisp ASM

[The PicoLisp Reference](https://software-lab.de/doc/ref.html#vm) | [ASM](pilasm.md)

### A page about history (updated October 2026)

From about 2009 to 2020, 64-bit PicoLisp (**pil64**) was written in its own **generic assembly language**. The instruction set below was defined in PicoLisp (`src64/arch/*.l`), and PicoLisp itself translated those generic instructions into real x86-64, ARM64, PowerPC or emulated code. It was a brilliant way to get a fast, portable interpreter with complete control over the machine: registers, stack layout and the tagged-pointer tricks described in [The PicoLisp Machine](pilmachine.md).

**pil64 is no longer maintained.** Since 2020 PicoLisp is **pil21** (current release 26.9). Alexander Burger kept the idea of writing the system in PicoLisp, but swapped his own assembler for **LLVM**. The sources (`src/*.l`) are written in a PicoLisp DSL defined in `src/lib/llvm.l`, which emits LLVM IR. LLVM then handles register allocation, optimisation and code generation for every CPU it supports. The result runs on more platforms (including Linux on ARM, Android/Termux and macOS) with far less machine-specific code.

To see the difference, here is the whole of `car` in pil21 (`src/subr.l`). In pil64 the same function was a dozen hand-written VM instructions that evaluated the argument, tested the tag bits and jumped to an error handler:

```picolisp
(de _Car (Exe)
   (chkA (eval (cadr Exe))) )
```

The data model is unchanged: same cells, same tag bits, same symbols. What changed is that nobody has to write register moves by hand any more.

### Why I keep this page

I studied this VM when I first went deep into PicoLisp, and it is still the clearest picture I know of what a Lisp interpreter *does* at the machine level: registers named for their role (**A**ccumulator, **C**ount, **E**xpression, **X**/**Y**/**Z** index), a stack (**S**), and a carry/zero/sign flag model that maps directly onto real CPUs. If you want to understand LLVM IR or real assembly, this is a friendly stepping stone. The original reference follows, unchanged.

## The pil64 VM reference (archive)

 [Quicklinks](quicklinks.md) | [Readinglist](readinglist.md) |  [Computing](computing.md) | [Picolisp](picolisp.md) |
[The Picolisp Reference](http://software-lab.de/doc/ref.html#vm) | [ASM](pilasm.md)

```
   CPU Registers:

      +---+---+---+---+---+---+---+---+
      |               A           | B |  \\      [A]ccumulator
      +---+---+---+---+---+---+---+---+   D     [B]yte register
      |               C               |  /      [C]ount register
      +---+---+---+---+---+---+---+---+         [D]ouble register
      |               E               |         [E]xpression register
      +---+---+---+---+---+---+---+---+

      +---+---+---+---+---+---+---+---+
      |               X               |         [X] Index register
      +---+---+---+---+---+---+---+---+         [Y] Index register
      |               Y               |         [Z] Index register
      +---+---+---+---+---+---+---+---+
      |               Z               |
      +---+---+---+---+---+---+---+---+

      +---+---+---+---+---+---+---+---+
      |               L               |         [L]ink register
      +---+---+---+---+---+---+---+---+         [S]tack pointer
      |               S               |
      +---+---+---+---+---+---+---+---+

      +-------------------------------+
      |  [z]ero  [s]ign  [x,b,c]arry  |         [F]lags
      +-------------------------------+
```

```
   Source Addressing Modes:
      ld A 1234            # Immediate
      ld A "(a+b-c)"
      ld A R               # Register
      ld A Global          # Direct
      ld A (R)             # Indexed
      ld A (R 8)           # Indexed with offset
      ld A (R OFFS)
      ld A (R Global)
      ld A (Global)        # Indirect
      ld A (Global OFFS)   # Indirect with offset
      ld A ((R))           # Indexed indirect
      ld A ((R 8))         # Indexed with offset indirect
      ld A ((R 8) OFFS)
      ld A ((R Global) OFFS)
      ld A ((R OFFS) Global)
      ...

   Destination Addressing Modes:
      ld R A               # Register
      ld (R) A             # Indexed
      ld (R 8) A           # Indexed with offset
      ld (R OFFS) A
      ld (R Global) A
      ld (Global) A        # Indirect
      ld (Global OFFS) A   # Indirect with offset
      ld ((R)) A           # Indexed indirect
      ld ((R 8)) A         # Indexed with offset indirect
      ld ((R 8) OFFS) A
      ld ((R Global) OFFS) A
      ld ((R OFFS) Global) A
      ...

   Target Addressing Modes:
      jmp 1234             # Absolute
      jmp Label
      jmp (R)              # Indexed
      jmp (R T)            # Indexed SUBR
      jmp (Global)         # Indirect

========================================================================

   Instruction set:
      nop               # No operation

   Move Instructions:
      ld dst src        # Load 'dst' from 'src' [---]
      ld2 src           # Load 'A' from two bytes 'src' (unsigned) [---]
      ld4 src           # Load 'A' from four bytes 'src' (unsigned) [---]
      ldz dst src       # Load if Zero 'dst' from 'src' [---]
      ldnz dst src      # Load if not Zero 'dst' from 'src' [---]
      lea dst src       # Load 'dst' with effective address of 'src' [---]
      st2 dst           # Store two bytes from 'A' into 'dst' [---]
      st4 dst           # Store four bytes from 'A' into 'dst' [---]
      xchg dst dst      # Exchange 'dst's [---]
      movn dst src cnt  # Move 'cnt' bytes from 'src' to 'dst' (non-overlapping or src < dst)
      mset dst cnt      # Set 'cnt' bytes of memory to B
      save src end dst  # Save 'src'..'end' to 'dst' (aligned, non-overlapping or src < dst)
      load dst end src  # Load 'dst'..'end' from 'src' (aligned, non-overlapping)

   Arithmetics:
      add dst src       # Add 'src' to 'dst' [zsc]
      addc dst src      # Add 'src' to 'dst' with Carry [zsc]
      sub dst src       # Subtract 'src' from 'dst' [zsb]
      subb dst src      # Subtract 'src' from 'dst' with Borrow [zsb]

      inc dst           # Increment 'dst' [zs.]
      dec dst           # Decrement 'dst' [zs.]
      not dst           # One's complement negation of 'dst' [z..]
      neg dst           # Two's complement negation of 'dst' [zs.]

      and dst src       # Bitwise AND 'dst' with 'src' [zs.]
      or dst src        # Bitwise OR 'dst' with 'src' [zs.]
      xor dst src       # Bitwise XOR 'dst' with 'src' [zs.]
      off dst src       # Clear 'src' bits in 'dst' [zs.]
      test dst src      # Bit-test 'dst' with 'src' [zs.]

      shl dst src       # Shift 'dst' left into x-bit by 'src' bits [zsx]
      shr dst src       # Shift 'dst' right into x-bit by 'src' bits [zsx]
      rol dst src       # Rotate 'dst' left by 'src' bits [...]
      ror dst src       # Rotate 'dst' right by 'src' bits [...]
      rxl dst src       # Rotate 'dst' with x-bit left by 'src' bits [zsx]
      rxr dst src       # Rotate 'dst' with x-bit right by 'src' bits [zsx]

      mul src           # Multiplication of 'A' and 'src' into 'D' [...]
      div src           # Division of 'D' by 'src' into 'A', 'C' [...]

      zxt               # Zero-extend 'B' to 'A' [...]
      eq                # Set Zero and clear Borrow [z._]
      gt                # Clear Zero and Borrow [_._]
      lt                # Clear Zero and set Borrow [_.b]
      setx              # Set x-bit [--x]
      clrx              # Clear x-bit [--_]

   Comparisons:
      cmp dst src       # Compare 'dst' with 'src' [zsc]
      cmpn dst src cnt  # Compare 'cnt' bytes 'dst' with 'src' [z..]
      slen dst src      # Set 'dst' to the string length of 'src' [...]
      memb src cnt      # Find B in 'cnt' bytes of 'src' memory [z..]
      null src          # Compare 'src' with 0 [zs_]
      nulp src          # Check 'src' for null-pointer [z..]
      nul4              # Compare four bytes in 'A' with 0 [zs_]

   Byte addressing:
      set dst src       # Set 'dst' byte to 'src' [---]
      nul src           # Compare byte 'src' with 0 [z..]

   Types:
      cnt src           # Non-'z' if small number [z..]
      big src           # Non-'z' if bignum [z..]
      num src           # Non-'z' if number [z..]
      sym src           # Non-'z' if symbol [z..]
      atom src          # Non-'z' if atom [z..]

   Floating point:
      ldd               # Load double value pointed to by 'C'
      ldf               # Load float value pointed to by 'C'
      fixnum            # Convert double with scale 'E' to fixnum in 'E'
      float             # Convert fixnum with scale 'A' pointed to by 'X'
      std               # Store double value at address 'Z'
      stf               # Store float value at address 'Z'

   Flow control:
      jmp adr           # Jump to 'adr' [---]
      jz adr            # Jump to 'adr' if Zero [---]
      jnz adr           # Jump to 'adr' if not Zero [---]
      js adr            # Jump to 'adr' if Sign [---]
      jns adr           # Jump to 'adr' if not Sign [---]
      jc adr            # Jump to 'adr' if Carry set [---]
      jnc adr           # Jump to 'adr' if Carry not set [---]
      jb adr            # Jump to 'adr' if Borrow set [---]
      jnb adr           # Jump to 'adr' if Borrow not set [---]
      jx adr            # Jump to 'adr' if x-bit set [---]
      jnx adr           # Jump to 'adr' if x-bit not set [---]

      call adr          # Call 'adr'
      cc adr(src ..)    # C-Call to 'adr' with 'src' arguments
      cc adr reg        # C-Call to 'adr' with top of stacked args in 'reg'

      ret               # Return [---]
      catch             # Prepare non-local jump [---]
      throw             # Resolve non-local jump [---]
      func              # Convert 'E' to function pointer
      begin             # Called from foreign function
      return            # Return to foreign function

   Stack Manipulations:
      push src          # Push 'src' [---]
      pop dst           # Pop 'dst' [---]
      tos dst           # Get return entry [---]
      link              # Setup frame [---]
      tuck src          # Extend frame [---]
      drop              # Drop frame [---]

   Evaluation:
      eval              # Evaluate expression in 'E'
      eval+             # Evaluate expression in partial stack frame
      eval/ret          # Evaluate expression and return
      exec reg          # Execute lists in 'reg', ignore results
      prog reg          # Evaluate expressions in 'reg', return last result

   System:
      initData          # Init runtime data
      initCode          # Init runtime code
      initMain          # Command in X, arguments in Y, last pointer in Z
      initLib           # Library function pointer in A
      stop              # Stop (system-dependent)

========================================================================

   Naming conventions:

   Lisp level functions, which would be all of the form 'doXyzE_E', are written
   as 'doXyz' for brevity.
```
