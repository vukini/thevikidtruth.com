---
title: Emacs Notes
date: '2022-08-28T12:15:52+04:00'
lastmod: '2026-10-22T15:00:00+04:00'
original_id: '{A1713}'
original_name: emacsnotes
original_blob: blob/B/11/363.txt
revisions: 14
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: emacsnotes
draft: false
topics:
- tools
---

[Computing](computing.md) |
[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) |
  [The Compiler](thecompiler.md) |
  [Identifiers](identifier.md) |
  [Literals](literals.md) |
  [storage_linkage](storagelinkage.md) | [Networking](networking.md)

# Emacs Notes

Here is the truth about Emacs: **it is not a text editor. It is a Lisp machine that happens to ship with a text editor written in that Lisp.** Every key you press runs an Emacs Lisp function, and you can read, change or replace any of them while it is running. These are my working notes, but first the orientation I wish I had been given.

### What it is, in plain words

GNU Emacs was started by Richard Stallman in 1984. Emacs 30 is the current major release in 2026. It is a small C core (display, I/O, a Lisp interpreter and native compiler) and over a million lines of **Emacs Lisp** on top. The key ideas:

- **Buffers** hold text: files, shells, directory listings, help, mail. "In Emacs, the buffer is the data structure."
- **Windows** show buffers; **frames** are what your window manager calls windows.
- **Modes**: one *major mode* per buffer (`python-mode`, `lisp-mode`, `org-mode`) and any number of *minor modes* (line numbers, spell checking, Evil).
- **Commands** are Lisp functions bound to keys. `C-h k` tells you which function a key runs; `C-h f` shows its documentation and a link to its source.

Recent versions made things much better out of the box: native compilation of Lisp (Emacs 28+), **Eglot** for LSP and **Tree-sitter** modes (29+), `use-package` built in (29+), and better completion and editing defaults in 30.

### Why it matters

- **One environment for everything text.** Code, notes in Org mode, Git through Magit, a REPL through SLY or `inferior-lisp`, mail, a shell. One set of keys and one way of extending them.
- **It is the best Lisp IDE.** For PicoLisp, Common Lisp, Scheme or Racket, being able to send an expression to a running REPL with one key changes how you program.
- **Freedom you can see.** Every function is inspectable and changeable while you use it. It is the most practical demonstration of [computing freedom](computingfreedom.md) I know.

### An everyday analogy: a workshop that builds its own tools

Most editors are a toolbox: you use what came in it. Emacs is a workshop with a lathe. When you need a tool that does not exist, you turn one, hang it on the wall next to the others, and it works exactly like the factory-made ones.

### A hands-on example: run it as a server on Vikix

The notes below use `systemctl --user`, which is for [systemd](systemd.md) distros. On Void with runit there is no user systemd, so the simplest approach is to start the daemon from your session, for example in `~/.xinitrc` or StumpWM's `~/.stumpwmrc`:

```bash
emacs --daemon            # start once per login
emacsclient -c            # new graphical frame, instant
emacsclient -t            # open in the terminal
export EDITOR="emacsclient -t" VISUAL="emacsclient -c -a ''"
```

`-a ''` means "if no server is running, start one". From StumpWM you can bind a key to it:

```lisp
;; ~/.stumpwmrc  (StumpWM is Common Lisp too)
(define-key *root-map* (kbd "e") "exec emacsclient -c -a ''")
```

A small, modern `init.el` to get going:

```elisp
(setq inhibit-startup-screen t
      select-enable-clipboard t)       ; share the clipboard (modern name)
(global-display-line-numbers-mode 1)
(electric-pair-mode 1)
(use-package eglot :hook (c-mode . eglot-ensure))   ; LSP for C via clangd
(use-package magit :ensure t)                       ; Git
```

Note the clipboard variable in the notes below, `x-select-enable-clipboard`, is the old name; `select-enable-clipboard` replaced it and is on by default now.

### Common misconceptions

- **"Emacs is huge and slow."** Startup with a sensible config is under a second, and with `emacsclient` new frames are instant.
- **"You must learn Emacs Lisp first."** You can use it for years with `M-x` and `C-h`. The Lisp comes when you want it.
- **"Emacs means no vim keys."** Evil mode gives you a very complete vim inside Emacs. See [vim](vim.md).
- **"Emacs pinky is inevitable."** Remap Caps Lock to Control (see [KMonad](kmonad.md)) and the problem mostly disappears.

### My own config

My real setup is public as [vukini/emacs-void](https://github.com/vukini/emacs-void): one literate `config.org` loaded by a small `init.el`. Two pages walk through it:

- [My Emacs Config Tour](myemacsconfig.md): the packages and why, my keys, how the file is laid out, and the snippets I'm proudest of.
- [Emacs on Vikix & StumpWM](emacsvikix.md): how it plugs into my desktop, including a SLIME REPL inside the running window manager.

On Vikix the daemon is started at login, and Super+x opens a frame with `emacsclient -c -a ''`.

### Connections

- [My Emacs Config Tour](myemacsconfig.md), [Emacs on Vikix & StumpWM](emacsvikix.md).
- [vim](vim.md), [Common Lisp](commonlisp.md), [PicoLisp](picolisp.md), [Scheme](scheme.md), [Racket](racket.md).
- [Git](git.md), [KMonad](kmonad.md), [Penti](penti.md), [The i3 Window Manager](i3.md).
- [with-output-to-string](withoutputtostring.md) – a Lisp idea you will use from the Emacs REPL.

## Notes


Start an emacs server.

```
systemctl --user enable emacs
```

Close an emacs client, see ` delete-frame `

Copy emacs text to the clipboard:

```
(custom-set-variables '(x-select-enable-clipboard t))

(global-set-key "\C-w" 'clipboard-kill-region)
(global-set-key "\M-w" 'clipboard-kill-ring-save)
(global-set-key "\C-y" 'clipboard-yank)
2{Notes from Mastering Emacs}
In Emacs, the buffer is the data structure.
```

## Useful tips

```
Use ‘C-x ESC ESC’ (‘repeat-complex-command’)
```

## Navigating Parenthesis

[NavigatingParentheses](http://www.emacswiki.org/emacs/NavigatingParentheses)

```
C-M-n forward-list   Move forward over a parenthetical group

C-M-p backward-list  Move backward over a parenthetical group

C-M-f forward-sexp   Move forward over a balanced expression

C-M-b backward-sexp  Move backward over a balanced expression

C-M-k kill-sexp      Kill balanced expression forward

C-M-SPC mark-sexp    Put the mark at the end of the sexp.
```

## Scale or Zoom Text

```
(text-scale-adjust 1)	C-x C-= or C-x C-+	Increase text size by one step
(text-scale-adjust -1)	C-x C–	                Decrease text-size by one step
```

## Setting Fonts

[Emacs Wiki Set Fonts](https://www.emacswiki.org/emacs/SetFonts)

## Links

- [Emacs Server GNU](https://www.gnu.org/software/emacs/manual/html_node/emacs/Emacs-Server.html)
- [Emacs DoReMi.el](https://www.emacswiki.org/emacs/DoReMi)
- [Window Resize](https://www.emacswiki.org/emacs/WindowResize)
- [Recentf](https://www.emacswiki.org/emacs/RecentFiles)
- [Installing Emacs on Windows](https://lucidmanager.org/productivity/emacs-windows/)

## Record Macros

1. Record: ctrl+x ( or 'q' in evil mode
1. Perform any actions to record
1. Stop recording by pressing ctrl+x or 'q' in evil mode)
1. Play: ctrl+x e

Naming Macros

1. Start: Ctrl+x Ctrl+k n
1. Give name-of-macro, and press ENTER
1. Play: M-x name-of-macro

Tabs and Spaces

- [emacs_delete_trailing_whitespace](http://xahlee.info/emacs/emacs/emacs_delete_trailing_whitespace.html)
