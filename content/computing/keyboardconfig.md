---
title: Keyboard Config
date: '2016-11-30T04:23:36+04:00'
lastmod: '2016-12-13T20:59:51+04:00'
original_id: '{A531}'
original_name: keyboardconfig
original_blob: blob/B/5/253.txt
revisions: 13
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: keyboardconfig
draft: false
topics:
- linux
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [pil sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) | [SimpleLinuxConfig](simplelinuxconfig.md) | [Keyboard Config](keyboardconfig.md)

# Keyboard Config

I usually don't make too many changes to my keyboards, but swapping the left-control key and caps has become a must. It
is very annoying for the first few days, your mind has to physically remap itself to reflect the change. However the long
term you won't regret it.

- This command swaps the left-control into the left caps, your normal left-control still works.
  ```
     setxkbmap -option ctrl:nocaps
  ```
- This command swaps the left-control into the left-caps, and left-caps into left control. Im preference
  ```
     setxkbmap -option ctrl:swapcaps
  ```
- A simple mnemonic to remember these commands is:
  ```
     set x keyboard map with -option ctrl: is swap to caps
     --- - -  -     ---      ------- ------    ----    ----
  ```
- I also use the following alias to reset the keyboard if any funny happens:
  ```
    alias rkb="/bin/bash -c 'setxkbmap -layout us -option ctrl:nocaps'"
  ```
  rsb stands for **Reset Key Board**
- When things are not going well and you need a full reconfiguration you can use:
  ```
    dpkg-reconfigure keyboard-configuration
  ```

#### Reading List & Source

- [Keyboard Switches by Gist](https://gist.github.com/Spoygg/3122226)
- [Don't Swap Ctrl and Caps!](http://ergoemacs.org/emacs/swap_CapsLock_Ctrl.html)

### The plain idea

This page is about remapping keys in Linux, chiefly the classic move of swapping Caps Lock with Control. On Linux the quick, session-level tool is `setxkbmap` (under X11), which can turn Caps Lock into another Control key with a single option. It is one of those tiny changes that pays back for years.

### Why it matters

Control is one of the most-pressed keys for anyone who lives in [Emacs](emacs.md), [vim](vim.md) or a shell, and on most keyboards it sits awkwardly in the bottom corner, straining your little finger. Caps Lock, meanwhile, occupies prime home-row real estate and does almost nothing useful. Swapping them is the single best ergonomic tweak for a keyboard-driven workflow.

### An everyday analogy

It is like moving the most-used tool in your workshop from a high back shelf to the bench right in front of you, and putting the dust-collecting gadget up on the shelf instead. A few days of reaching to the wrong place, then it feels obvious forever.

### A 2026 note

`setxkbmap` works under **X11**. If you are on a **Wayland** desktop (now the default on Ubuntu, Fedora and others), `setxkbmap` may not apply; use your desktop's keyboard settings, or a tool like `keyd` or a `localectl` XKB option, to make the Caps-to-Ctrl swap. The idea and the key names are identical; only the mechanism differs. For a permanent, display-server-independent remap, `keyd` is the modern favourite.

### A note on the counter-argument

I link "Don't Swap Ctrl and Caps!" above on purpose. Some people prefer remapping Caps to Escape (handy in vim) or to a dual-role key (Escape when tapped, Control when held). There is no universal right answer; the point is that Caps Lock is wasted space you can reclaim for whatever *you* press most.

### How it connects

- [Emacs](emacs.md) and [vim](vim.md): the editors that make this swap worthwhile.
- [Linux](linux.md) and [Bash](bash.md): where the aliases live.

The truth revealed: the keyboard is the one tool you touch every single minute at a computer, and spending ten minutes to move your most-used key under a resting finger is among the highest-return tweaks you will ever make.
