---
title: The MINIX Book by Tanebaum & Woodhull
date: '2016-11-26T05:48:56+04:00'
lastmod: '2016-11-26T06:12:52+04:00'
original_id: '{A353}'
original_name: theminixbook
original_blob: blob/B/2/036.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: theminixbook
draft: false
topics:
- os-hardware
---

# The MINIX Book by Tanebaum & Woodhull

[Books](books.md) | [Operating Systems](os.md)

![minix](/assets/minix.jpg)
{.right}

### About the book

*Operating Systems: Design and Implementation* by Andrew S. Tanenbaum and Albert S. Woodhull, usually just called "the MINIX book", is the companion to Tanenbaum's [Modern Operating Systems](modernoperatingsystems.md). Where that book explains OS *theory*, this one teaches by showing a complete, working operating system you can read line by line: **MINIX**, a small Unix-like system Tanenbaum wrote for teaching. The book walks through the real source code for processes, memory management, the file system and I/O, so the abstractions become concrete.

MINIX has a famous place in history: as a student, Linus Torvalds used it and was frustrated by its limits, which prompted him to write his own kernel, Linux, in 1991. MINIX itself went on to pioneer a **microkernel** design (keeping the kernel tiny and running drivers as ordinary, restartable processes for reliability), and MINIX 3 was later adopted, surprisingly, inside Intel's Management Engine, making it for a while one of the most widely shipped operating systems in the world.

The section links below are chapters and topics I intend to write up in my own words as time allows.

### Why it is worth reading

Reading *about* operating systems only takes you so far; reading a real one takes you the rest of the way. This book is the bridge between theory and the actual code that makes a computer manage itself, and it pairs naturally with Tanenbaum's more theoretical volume.



- [Processes](processes.md "MISSING PAGE")
- [Threads](threads.md "MISSING PAGE")
- [Interprocess Communication](ipc.md "MISSING PAGE")
- [Scheduling](scheduling.md "MISSING PAGE")
- [Memory](osmemory.md "MISSING PAGE")
- [Virtual Memory](virtualmemory.md "MISSING PAGE")
- [Paging](paging.md "MISSING PAGE")
- [Segmentation](segmentation.md "MISSING PAGE")
- [File Systems](filesystems.md "MISSING PAGE")
- [I/O](io.md "MISSING PAGE")
- [Clocks](clocks.md "MISSING PAGE")
- [Deadlocks](deadlocks.md "MISSING PAGE")
- [Encoding](encoding.md "MISSING PAGE")
- [Compression](compression.md "MISSING PAGE")
- [Caching](caching.md "MISSING PAGE")
- [Virtualization](virtualization.md)
- [Distributed Systems](ds.md "MISSING PAGE")
- [Security](security.md "MISSING PAGE")
- [Cryptography](cryptography.md "MISSING PAGE")
- [Authentication](authentication.md "MISSING PAGE")
- [Attacks](attacks.md "MISSING PAGE")
- [Exploits](exploits.md "MISSING PAGE")
- [Malware](malware.md "MISSING PAGE")
