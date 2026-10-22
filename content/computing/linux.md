---
title: Linux
date: '2016-05-12T01:15:56+04:00'
lastmod: '2023-03-30T09:21:05+04:00'
original_id: '{A25}'
original_name: linux
original_blob: blob/B/11/633.txt
revisions: 52
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: linux
draft: false
topics:
- linux
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |   [C Programmming](cprogramming.md) |  [Computer Security](computersecurity.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [i3](i3.md) |
  [Javascipt](javascript.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [Tools and Software](linuxtoolsandsoftware.md)
  [Operating Systems](os.md) |
 [Pharo Smalltalk](pharo.md) |
 [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [pil sources](pilsource.md) |
  [Python](python.md) | [SimpleLinuxConfig](simplelinuxconfig.md) |

# Linux

I haven't used Windows as my primary system for over 10 years, using Mac mostly
in the mean time. Through the years, Apple and the OSX environment also began to
trouble me. Apple kept making changes that made it difficult for me, in the
Free Software Movement, to work *freely!*

I had to change and have now moved
almost exclusively on Linux. My Favourite distros are **Ubuntu** (for its sheer
ubiquitousness) and **Manjaro** (for being an easy **Arch** distro).

### The plain idea

Linux is a free, open-source operating system: the core software that sits between your hardware and your programs, managing the processor, memory, files and devices. Strictly, "Linux" is just the *kernel* (the part Linus Torvalds started in 1991); the full systems people install are *distributions* ("distros") that wrap that kernel with a package manager, desktop and tools, Ubuntu, Arch, Manjaro, Debian, Fedora and hundreds more. What they share is a Unix heritage: small composable tools, a powerful shell, and the freedom to see and change every line.

### Why it matters

Linux quietly runs the modern world. It powers almost every web server, the top 500 supercomputers, most cloud infrastructure, Android phones (an Android is a Linux kernel underneath), cars, routers and Raspberry Pis. Learning it means you can work anywhere software runs, automate your machine with [Bash](bash.md), and, as my intro says, work *freely*, owning your tools rather than renting them.

### An everyday analogy

If a computer were a restaurant, the operating system is the kitchen management: it decides which cook (process) uses which stove (CPU core), how the pantry (memory) is shared, and how orders (your programs) get what they need without colliding. A Linux distro is a particular restaurant's way of running that kitchen, same core idea, different house style.

### A worked example: the shape of the system

A few commands reveal how Linux is put together:

```bash
uname -a            # the kernel: version and architecture
cat /etc/os-release # the distro: which flavour this is
ps aux              # the processes currently running
ls /                # the single file tree everything hangs off
```

Notice the last one: unlike Windows drive letters, Linux has *one* tree starting at `/`, and even devices and settings appear as files within it. That "everything is a file" idea is the heart of the Unix philosophy Linux inherits.

### A 2026 note

The links and distro notes below are a few years old. Two practical updates: **Ubuntu 16.04 is long past end-of-life** (use a current LTS such as 24.04), and the old kernel-module and partitioning guides still teach the right concepts but reference dated versions. The fundamentals, the shell, the file tree, [systemd](systemd.md), processes and memory, are unchanged, which is exactly why Linux rewards learning deeply once.



[Linux Processes and Memory](linuxprocessesandmemory.md)
This is an area I have really struggled with but it is the heart of Linux. What this section will try to do is explain
the subject to the would be linux beginner. [Read more here...](linuxprocessesandmemory.md)

[Tools to Learn](linuxtools.md)
[Display Modes and Virtual Consoles](displaymodesandvirtualconsoles.md)
[Linux Introspection](linuxinstrospection.md)
[Ubuntu Common Tasks](ubuntucommontask.md)
[Tools and Software](linuxtoolsandsoftware.md)
[The Vikid Arch Linux Wiki!](archlinux.md)
[systemd](systemd.md)
[Burn an Iso to USB](burniso.md)
[xrandr](xrandr.md)
[The Linux Process Manager](thelinuxprocessmanager.md)

#### Reading List & Source

[Dive into Systems Programming Book](https://diveintosystems.org/singlepage/) | [Source Code](https://github.com/madmax440/gists)
[difference-between-gpt-and-mbr](https://www.howtogeek.com/193669/whats-the-difference-between-gpt-and-mbr-when-partitioning-a-drive)
[Gdisk and Booting Linux](https://www.rodsbooks.com/gdisk/)
[TDLP Linux Guides and Howto's](http://www.tldp.org)
[The Kernel (2.6) Module Programming Guide](http://www.tldp.org/LDP/lkmpg/2.6/lkmpg.pdf)
[Inspecting Hardware - openGL](https://www.opengl.org/wiki/Platform_specifics:_Linux)
[Todo After installing Ubuntu 16.04](http://www.omgubuntu.co.uk/2016/04/10-things-to-do-after-installing-ubuntu-16-04-lts)
[Critix Remote Applications](https://www.citrix.com/)
[GNU Docs](http://www.delorie.com/gnu/docs/)
[Dealing with IO, sigio & C10K Problem](http://kegel.com/c10k.html#nb.sigio)
[Single Unix Specification](http://www.unix.org/online.html)
[AppImage | Linux apps that run anywhere](https://appimage.org/)
[How to Store Dotfiles](https://www.atlassian.com/git/tutorials/dotfiles)
[Kernel Newbies](https://kernelnewbies.org)
[Insallaion guide - ArchWiki](https://wiki.archlinux.org/index.php/insallaion_guide)
[How o Insall Arch Linux {Comprehensive Sep-by-Sep Guide](https://phoenixnap.com/kb/arch-linux-insall)
[How to Install Arch Linux in 2020 Step by Step Guide](https://itsfoss.com/install-arch-linux/)
[Arch Linux Full Installation Walkthrough](https://www.youtube.com/watch?v=a00wbjy2vns)
[Arch Linux Installation Guide 2020](https://www.youtube.com/watch?v=PQgyW10xD8s)
[Arch Linux Installation (2021)](https://www.youtube.com/watch?v=UiYS8xWFXLY)
[LVM - ArchWiki](https://wiki.archlinux.org/index.php/LVM)
[Unified Extensible Firmware Interface - ArchWiki](https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface)
[EFI system partition - ArchWiki](https://wiki.archlinux.org/index.php/EFI_system_partition)
[Partitioning - ArchWiki](https://wiki.archlinux.org/index.php/Partitioning)
[genfstab(8) — Arch manual pages](https://man.archlinux.org/man/genfstab.8)
[System time - ArchWiki](https://wiki.archlinux.org/index.php/System_time#Time_zone)
[Arch Linux - Package Search](https://archlinux.org/packages/?name=linux-firmware)
[File systems - ArchWiki](https://wiki.archlinux.org/index.php/File_systems)
[Network configuration - ArchWiki](https://wiki.archlinux.org/index.php/Network_configuration)
[List of applications - ArchWiki](https://wiki.archlinux.org/index.php/List_of_applications#Text_editors)
[Arch Linux - Package Search](https://archlinux.org/packages/?name=man-db)
[Check if Your Computer Uses UEFI or BIOS in Linux & Windows](https://itsfoss.com/check-uefi-or-bios/)
