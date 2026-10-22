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
draft: true
review: update
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
