---
title: Emacs Notes
date: '2022-08-28T12:15:52+04:00'
lastmod: '2022-09-15T06:05:53+04:00'
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
