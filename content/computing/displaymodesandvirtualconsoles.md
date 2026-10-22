---
title: Display Modes and Virtual Consoles
date: '2016-12-08T23:15:58+04:00'
lastmod: '2016-12-08T23:15:58+04:00'
original_id: '{A1024}'
original_name: displaymodesandvirtualconsoles
original_blob: blob/B/5/106.txt
revisions: 1
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: displaymodesandvirtualconsoles
draft: false
topics:
- linux
---

# Display Modes and Virtual Consoles

There are  two primary display modes: text mode and an X Window System server
 virtual consoles are used to multiplex the display
Use the Alt-Fn keys to switch between them, or Ctrl-Alt-Fn in X

## Notes, Links & Sources

- Plymouth Boot Splash
- chvt command

### The plain idea

A Linux machine can show you a screen in two very different ways. **Text mode** is a plain, full-screen text terminal (white letters on black, no mouse). **Graphical mode** is the desktop you usually see, drawn by a display server (historically the **X Window System**, increasingly **Wayland** today). On top of this, Linux offers several **virtual consoles**: independent login sessions multiplexed onto the one physical screen, so you can flip between them like channels on a TV.

### Why it matters

Knowing this is a genuine survival skill. When the graphical desktop freezes, you are not stuck: you can switch to a text console, log in, fix or restart things, and switch back, without rebooting and losing your work. It also demystifies what the desktop actually is: just one more console, running a graphics server, among several.

### An everyday analogy

Think of your monitor as a single TV set wired to several set-top boxes. Each virtual console is a box tuned to its own channel (its own login session). The graphical desktop is simply the fanciest channel. The Alt-Fn keys are the channel buttons on the remote; the TV only ever shows one at a time.

### A worked example: switching consoles

- **Ctrl+Alt+F3** (through F6) from the desktop usually drops you to a text console, a full-screen login prompt.
- **Ctrl+Alt+F1** or **F2** typically returns you to the graphical session (the exact number varies by distro).
- From *within* text mode you can use **Alt+Fn** alone.
- `chvt 3` switches to console 3 from a script, and `who` or `w` shows who is logged in on which.

A 2026 note: on modern **systemd** distributions, text consoles are managed by `systemd` (`getty` services) and the desktop runs on its own virtual terminal, often VT1 or VT2. With **Wayland** replacing X in many desktops the user-facing experience is the same, you still switch with Ctrl+Alt+Fn, even though the graphics plumbing underneath has changed. The Plymouth boot splash my notes mention is still what hides the text console during startup.

### Common misconceptions

- **"A frozen desktop means a frozen computer."** Usually not; a text console is often still fully alive behind it.
- **"The terminal window on my desktop is a virtual console."** That is a *terminal emulator* inside the graphical session; true virtual consoles are the separate Ctrl+Alt+Fn screens.

### How it connects

- [Linux](linux.md) and [systemd](systemd.md): what manages these sessions.
- [Bash](bash.md): what you will type once you are in a text console.
- [Keyboard Config](keyboardconfig.md): remapping keys, which differs between text and graphical modes.

The truth revealed: your one screen is really several computers' worth of sessions stacked behind each other, and the Ctrl+Alt+Fn keys are the trapdoor that gets you out when the pretty one locks up.
