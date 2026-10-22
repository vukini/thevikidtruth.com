---
title: Notes on the Intel CPU Cache Architecture & Attacks
date: '2017-06-15T10:32:32+04:00'
lastmod: '2017-06-15T11:03:47+04:00'
original_id: '{A1102}'
original_name: intelcpuarchitecture
original_blob: blob/B/5/534.txt
revisions: 11
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: intelcpuarchitecture
draft: false
topics:
- os-hardware
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md) | [Networking](networking.md) | [Machine Learning](machinelearning.md) |
  [Git](git.md) |
  [Machine Learning](machinelearning.md) |
  [Algorithms](algorithms.md)

# Notes on the Intel CPU Cache Architecture & Attacks

[on Intel CPU lecture @ media.ccc.de](https://media.ccc.de/v/33c3-8044-what_could_possibly_go_wrong_with_insert_x86_instruction_here#video&t=273
Caches)

Imagine a 4-core CPU, it usually has two caches per core which are private to the core and we have a
**Last Level Cache (LLC)** which is divided into slices by how many cores you have.

![cpu-cache](/assets/cpu-cache.png)
{.center}

Let us consider three instructions:

1. **mov:** accesses data in the main memory and from registers to registers
1. **clflush:** removes cache line from the cache
1. **prefetch:** prefetches cache line for future use

Data can reside in:

- **CPU Registers**
- **Different Levels of Cache**
- **Main Memory**
- **Disk Storage**

#### Flush and Reload - Cache Attack

- Attackers monitor the timing differences of memory access.
- The attack monitors which lines are accessed but not the content.
- the Attacker establishes a Covert Channel of communication between two processes.
  Which he would normally not be allowed to do so.

![Shared-Libray-Step-1](/assets/shared-libray-step-1.png)
{.center}

![Shared-Libray-Step-2](/assets/shared-libray-step-2.png)
{.center}

![Shared-Libray-Step-3](/assets/shared-libray-step-3.png)
{.center}

#### Prime & Probe - Cache Attack

![prime-probe-1](/assets/prime-probe-1.png)
{.center}

![prime-probe-2](/assets/prime-probe-2.png)
{.center}

![prime-probe-3](/assets/prime-probe-3.png)
{.center}

#### Establish a Covert Channel

You need two apps on a phone for example. The apps will use the shared cache using the above to send info between
 the apps.

### The plain idea

A modern CPU is far faster than main memory, so between the two sits the **cache**: small, very fast memory holding recently-used data. As my notes show, each core has its own small private caches (L1, L2) and all cores share a big **Last Level Cache (LLC)**, split into slices. The cache is normally invisible, it just makes things fast, but its one observable side effect, *how long* a memory access takes, turns out to leak secrets. A cache *hit* is quick; a cache *miss* is slow. By measuring that difference, an attacker can learn what another program has been touching, even without reading its data.

### Why it matters

This is the heart of an entire class of **side-channel attacks**. They do not break encryption by maths; they watch the hardware's timing and infer the secret, a key, a password, a keystroke, from the pattern of cache hits and misses. The same shared-cache trick also builds a **covert channel**: two programs that are forbidden to talk can still signal each other by deliberately causing cache hits and misses. These ideas underpinned the famous **Spectre and Meltdown** vulnerabilities disclosed in 2018, which shook the whole industry precisely because the flaw was in the CPU design, not in any one program.

### An everyday analogy: the library desk

Imagine a shared library with a small "recently requested" shelf behind the desk. You cannot see what your rival checked out, but you *can* time the librarian. Ask for a book and if it comes back instantly, it was on the quick shelf, meaning someone requested it recently. By timing which books are fast to fetch, you deduce what your rival has been reading, without ever seeing their library card. That is a cache timing attack.

### A worked example: Flush+Reload

My notes sketch the classic Flush+Reload attack, which works when two processes share memory (such as a shared library):

1. **Flush.** The attacker uses `clflush` to evict a specific shared cache line, so it is no longer cached.
2. **Wait.** Let the victim run. If the victim accesses that line, it gets pulled back into the cache.
3. **Reload.** The attacker reads the same line and *times* it. Fast means the victim touched it (a hit); slow means they did not (a miss).

Repeat this on the cache lines of, say, a cryptographic table, and the pattern of hits reveals which entries the victim used, which can reconstruct the secret key. **Prime+Probe** is the sibling technique for when there is no shared memory: the attacker fills a cache set with its own data (prime), lets the victim run, then checks which of its lines got evicted (probe), inferring where the victim accessed.

### A 2026 update

Since these conference notes, the field exploded. **Spectre** and **Meltdown** (2018) showed that CPUs' *speculative execution* could be tricked into leaving secrets in the cache for exactly these attacks to read, affecting nearly every processor made for two decades. A long line of relatives followed (Foreshadow, ZombieLoad, and more recently Downfall and Inception in 2023). Mitigations now live everywhere, in CPU microcode, operating-system kernels and compilers, often at a real cost in performance. The deep lesson stands: **performance optimisations that are invisible to software can still be very visible to an attacker with a stopwatch.**

### Common misconceptions

- **"Cache attacks read memory directly."** They do not read content; they infer it from *timing*. That indirectness is what makes them so hard to stop.
- **"Only encryption is at risk."** Keystroke timing, browsing behaviour and more have all been leaked this way.
- **"A patch fixed it."** Many variants exist; mitigation is ongoing and often trades away speed.
- **"This needs physical access."** Some variants have run from JavaScript in a web browser.

### How it connects

- [Stacks](stacks.md) and low-level memory layout.
- [Encryption](encryption.md): the keys these attacks target.
- [Exploitation](exploitation.md): where side channels fit the attacker's toolkit.
- [Modern Operating Systems](modernoperatingsystems.md): the kernel-level mitigations.

The truth revealed: the cache was built to make computers faster, and that very speed difference became a crack through which secrets leak, a reminder that in security, even time itself is a channel.
