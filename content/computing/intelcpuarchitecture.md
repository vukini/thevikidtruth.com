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
draft: true
review: update
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
