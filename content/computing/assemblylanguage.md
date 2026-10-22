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
