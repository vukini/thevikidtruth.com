---
title: Stacks
date: '2016-11-30T01:30:36+04:00'
lastmod: '2016-11-30T01:31:27+04:00'
original_id: '{A525}'
original_name: stacks
original_blob: blob/B/3/115.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: stacks
draft: false
topics:
- cs-theory
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) | [encryption](encryption.md) |
[IDS/IPS](idsips.md) | [HoneyPots](honeypots.md) | [Securing Web/Apps](securingwebapps.md) | [Stacks](stacks.md)

# Stacks

```
eip
    |
    | EBP
    |
    |_
    |
    | OLD EBP
    |_
    |
    | DATA
    |_
    |
    | DATA
ebp |
```

The ebp is the entry point to the data on the stack.

## Buffer Overflows

- [IDA Pro](https://www.hex-rays.com/products/ida/)
- [You need to Understand Stacks](stacks.md)

## Sources and Links

- fuzzers
- [Appvigil](http://appvigil.co)
- ```
  ```

### The plain idea

The *call stack* is the scratchpad a program uses to keep track of function calls. Every time a function is called, the machine pushes a **stack frame** onto the stack: a block holding that function's local variables, its arguments, and, crucially, the **return address**, where to jump back to when the function finishes. When the function returns, its frame is popped off. My diagram traces the two registers that manage this: **EBP** (the base/frame pointer, marking the current frame) and **EIP** (the instruction pointer, the return address saved on the stack).

### Why it matters

This page sits in the security section for one reason: the stack's layout is the target of the most famous class of exploit in history, the **buffer overflow**. If a program writes more data into a local buffer than it has room for, the extra data spills over the neighbouring slots, including that saved return address. Overwrite the return address and you can make the program jump wherever you like, including into code you supplied. Understanding the stack is understanding how [exploitation](exploitation.md) works at the metal.

### An everyday analogy: a stack of sticky notes

Imagine doing a task that interrupts itself. You are cooking (write a note: "return to stirring"), then you answer the phone (new note on top: "return to cooking"), then the doorbell rings (another note on top). You always deal with the *top* note first and remove it, returning exactly to where you left off. The return address is "where was I?", written down so you never lose your place. A buffer overflow is someone sneaking in and rewriting your bottom note so you "return" somewhere you never meant to go.

### A worked example: the overflow

```c
void vulnerable(char *input) {
    char buffer[8];          // room for 8 bytes
    strcpy(buffer, input);   // copies with NO length check
}
```

Call `vulnerable` with 8 bytes and all is well. Call it with 50 bytes and `strcpy` keeps writing past `buffer`, over the saved EBP, and over the return address above it on the stack. Craft those overflow bytes carefully and the return address now points at attacker-chosen code. That is the classic "smashing the stack" attack.

### A 2026 update

Decades of defences have made this far harder, though not impossible:

- **Stack canaries**: a secret value placed just before the return address; if an overflow changes it, the program aborts.
- **ASLR** (address space layout randomization): the stack's location is randomised each run, so the attacker cannot predict where to jump.
- **DEP/NX** (non-executable stack): the CPU refuses to run code sitting in the stack, defeating simple payloads. Attackers answered with *return-oriented programming* (ROP), reusing existing code fragments.
- **Memory-safe languages** (Rust, Go) avoid the whole class by checking bounds.

The arms race continues, but "don't use unbounded copies like `strcpy`/`gets`" remains rule number one.

### Common misconceptions

- **"The stack and the heap are the same."** The stack is automatic, fast, LIFO, for call frames; the heap is manually managed, for long-lived data. Overflows happen in both, differently.
- **"Modern systems are immune."** Mitigations raise the bar; they do not end the problem, as ROP and ongoing CVEs show.
- **"Only C is affected."** Any language with manual memory and no bounds checks is at risk; safe languages trade a little speed to avoid it.

### How it connects

- [Exploitation](exploitation.md): buffer overflows are a core technique.
- [Intel CPU Architecture](intelcpuarchitecture.md): the registers (EBP, EIP, ESP) involved.
- [C Programming](cprogramming.md): where unsafe copies live.
- [Encryption](encryption.md) and [Securing Web Apps](securingwebapps.md): the wider defensive picture.

The truth revealed: the stack is just a tidy pile of "where was I?" notes, and almost all of low-level hacking is the art of rewriting the one note at the bottom.
