---
title: Assembly Languagess
date: '2016-11-30T01:43:52+04:00'
lastmod: '2023-03-27T08:52:50+04:00'
original_id: '{A526}'
original_name: assemblylanguage
original_blob: blob/B/11/613.txt
revisions: 12
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: assemblylanguage
draft: false
topics:
- c-systems
---

[Algorithms](algorithms.md) | [Apple](apple.md) | [AssemblyLanguage](assemblylanguage.md) |
[BASH](bash.md)  |   [Bash Cookbook](vikidsbashcookbook.md)  |
[C-Programmming](cprogramming.md) | [CommonLisp](commonlisp.md) | [Computer Security](computersecurity.md) | [CuisSmalltalk](cuissmalltalk.md) |
[Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) | [Firewalls](firewalls.md) |
[Fortran](fortran.md) | [Functional Programming](functional.md) |
[Git](git.md) | [GNUSmalltalk](gnusmalltalk.md) | [Haskell](haskell.md) | [Social Engineering](internetexploitation.md)  | [Javascript](javascript.md) |  [Julia](julia.md) |
[Linux](linux.md) | [Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |[Machine Learning](machinelearning.md) |
[Networking](networking.md) | [Operating Systems](os.md) | [Open Data Science](opendatascience.md) | [Odin](odin.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) | [Purescript](purescript.md) | [Python](python.md) |
[Racket](racket.md) | [Scheme](scheme.md)  |
[Unity](unity.md) | [vim](vim.md) | [V](vlang.md) |
[Web Development](webdevelopment.md) | [Windows WSL](windowswsl.md) | [Zig](ziglang.md)

# Assembly Languagess

Here is the truth about assembly: **it is not a language so much as a set of labels for the machine's own instructions.** Every program you have ever run, in Python, PicoLisp or JavaScript, ends up as these instructions. Assembly is just the version written for people to read.

### What it is, in plain words

A CPU understands only **machine code**: numbers that encode instructions like "add these two registers" or "jump to this address if the last result was zero". **Assembly language** gives each instruction a short name (a *mnemonic*) such as `mov`, `add`, `cmp`, `jne`, `call`, `ret`, and lets you use labels instead of raw addresses. An **assembler** (GNU `as`, NASM, FASM) translates the text into machine code, almost one line to one instruction.

There is no single assembly language. Each CPU family has its own **instruction set architecture (ISA)**:

- **x86-64** (Intel, AMD) – most desktops and servers.
- **AArch64 / ARM64** – phones, Apple Silicon Macs, Raspberry Pi 4 and 5, and a growing share of cloud servers.
- **RISC-V** – the open ISA, now shipping in boards and microcontrollers and well worth learning in 2026.

The notes at the bottom of this page are 32-bit x86 (`ebp`, `esp`). On 64-bit x86 the same registers are `rbp` and `rsp`, there are sixteen general registers instead of eight, and function arguments arrive in registers (`rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`) rather than on the stack.

### Why it matters

- **Debugging.** When a program crashes with no source, [GDB](gbddebugger.md) and [objdump](objdump.md) show you assembly. Reading it is the last line of understanding.
- **Performance.** Seeing what the [compiler](thecompiler.md) produced shows whether a loop was vectorised or a function inlined.
- **Security.** Exploits, shellcode, reverse engineering and malware analysis all live here (see [Computer Security](computersecurity.md) and [Types of Malware](malwaretypes.md)).
- **Understanding.** Stacks, calling conventions, pointers and system calls become concrete. This is the floor of [Build a Computer in Your Head](bciyh.md).

### An everyday analogy: a calculator with a notepad

Imagine a calculator with a few memory buttons (registers), a big notepad (RAM) and a list of numbered instructions you follow one line at a time. "Copy the number from page 40 into memory A. Add memory B. If the result is zero, skip to line 12." That is all a CPU does, billions of times a second. Assembly is writing out that list of instructions yourself.

### A hands-on example: hello, world with no C library

```asm
# hello.s  -- x86-64 Linux, GNU assembler (AT&T syntax)
        .globl _start
        .section .rodata
msg:    .ascii "Hello from asm\n"
len = . - msg

        .text
_start:
        mov  $1, %rax          # syscall number 1 = write
        mov  $1, %rdi          # fd 1 = stdout
        lea  msg(%rip), %rsi   # buffer
        mov  $len, %rdx        # length
        syscall

        mov  $60, %rax         # syscall 60 = exit
        xor  %rdi, %rdi        # status 0
        syscall
```

```bash
as hello.s -o hello.o && ld hello.o -o hello && ./hello
ls -l hello          # a few hundred bytes, no libc at all
strace ./hello       # exactly two system calls
```

Then go the other way and see what C becomes:

```bash
echo 'int sq(int x){return x*x;}' > sq.c
gcc -O2 -S -masm=intel sq.c -o - | grep -A3 'sq:'
#   sq:
#       imul  edi, edi
#       mov   eax, edi
#       ret
```

The argument arrived in `edi`, the result leaves in `eax`. That is the System V calling convention used on Linux, macOS and the BSDs.

### Common misconceptions

- **"Assembly is always faster."** Modern compilers usually beat hand-written assembly for general code. Hand-tuning pays off for small hot loops, SIMD and cryptography.
- **"There is one assembly language."** There is one per ISA, plus two syntaxes for x86 alone: AT&T (`mov $1, %rax`, GNU default) and Intel (`mov rax, 1`, NASM and most manuals).
- **"Assembly is the same as machine code."** Close, but the assembler also handles labels, directives, data and relocations for the linker.
- **"Nobody writes it any more."** Kernels, bootloaders, compilers, codecs, crypto libraries and PicoLisp's own [low-level layer](pilasm.md) all contain it.

### Connections

- [Build a Computer in Your Head](bciyh.md), [Operating Systems](os.md), [Cool Hardware](coolhardware.md).
- [The Compiler](thecompiler.md), [C Programming](cprogramming.md), [objdump](objdump.md), [Using the C Debugger](gbddebugger.md).
- [PicoLisp Assembly](pilasm.md) and [The PicoLisp Machine](pilmachine.md) – a Lisp built close to the metal.
- [Forth](forth.md) – a language that feels like a portable assembler with a REPL.


## Links, Sources and Reading List

- [x86Asm Tutorial form wisc.edu](http://www.hep.wisc.edu/~pinghc/x86AssmTutorial.htm)
- [x86 Guide from Virginia.edu](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html)
- [Asm7](http://ftp.icm.edu.pl/packages/linux-uk/alpha/alpha/asm7.html)
- [ springer books pdf on Linux ASM](http://data.ceh.vn/Ebook/ebooks.shahed.biz/OS/LINUX/Springer-Verlag%20-%20Guide%20to%20Assembly%20Language%20Programming%20in%20Linux.pdf
  )
- [ spring books pdf on A Concise Guide to ASM](https://sovannarith.files.wordpress.com/2012/07/springer-guide-to-assembly-language-a-concise-introduction-2011.pdf
  )
- [Links to Linux & i586+ Assembly Programming & Doc's](http://www.lxhp.in-berlin.de/lhplinks.html#lki)
- [Excellent Free Tutorials to Learn Assembly - LinuxLinks](https://www.linuxlinks.com/excellent-free-tutorials-learn-assembly/)
- [https://en.wikipedia.org/wiki/META_II](https://en.wikipedia.org/wiki/META_II)

## Some Notes:

```
ebp is known as the base pointer or the frame pointer.

 1. On entry to your function, you push it (to save the value for the calling function).

 2. Then, you copy esp, the stack pointer, into ebp, so that ebp now points to your function's stack frame.

 3. At the end of your function, you then pop ebp so that the calling function's value is restored.

For some clarification on exactly what is going on -
the push instruction:

 1. puts the value from the specified register (ebp in this case), onto the stack, and
 2. decrements the stack pointer by the appropriate amount.

The pop operation is the opposite -

 1. it increments the stack pointer and takes a value from the stack and
 2. puts it in the specified register.
```
