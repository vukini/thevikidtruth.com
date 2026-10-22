---
title: Vikid's Vim Notes
date: '2017-06-27T03:34:25+04:00'
lastmod: '2017-06-27T03:48:18+04:00'
original_id: '{A1162}'
original_name: vikidvim
original_blob: blob/B/6/047.txt
revisions: 6
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: vikidvim
draft: false
topics:
- tools
---

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
  [storage_linkage](storagelinkage.md) |
  [emacs](emacs.md) | [computing](computing.md) |
  [vim notes](vikidvim.md)

# Vikid's Vim Notes

Here below are the various notes that I take time to time on vim. It's not intended to be complete but a quick help about
certain vim functions or operations that are helpful.

###### [Goto line Vim](gotolinevim.md)

### The plain idea

Vim is a *modal* text editor: unlike most editors, where the keys always type letters, Vim has different modes, chiefly **Normal** mode (where keys are commands: move, delete, copy) and **Insert** mode (where keys type text). That split is Vim's whole secret. Your fingers spend most of their time issuing fast, composable commands from the home row, and only drop into Insert mode to actually write. This page collects my running notes on those commands.

### Why it matters

Vim (and its modern successor **Neovim**) is everywhere: it is installed on virtually every server, so when you SSH into a remote machine, Vim is the editor you can count on. Its editing "language", verbs (`d` delete, `c` change, `y` yank) combined with motions (`w` word, `}` paragraph, `G` end of file), lets you express complex edits in a few keystrokes, without ever reaching for a mouse. Even people who live in other editors use Vim *keybindings* inside them (Emacs has Evil mode, VS Code has a Vim plugin) because the grammar is that good.

### An everyday analogy

Most editors are like writing with a pen: you can only ever write. Vim is like having a pen *and* a full set of editing tools, scissors, highlighter, ruler, always in hand, and a single button to switch between "writing" and "editing". The brief awkwardness of remembering which mode you are in is the price for never having to move your hands to a mouse or arrow keys.

### A worked example: the grammar of editing

The power is that commands *compose* like a language, verb + motion:

```
dw     delete to the next word
d$     delete to the end of the line
ci"    change the text inside the quotes
y5j    yank (copy) the next 5 lines
.      repeat the last change
```

Learn ten verbs and ten motions and you can express a hundred edits, which is why the [Goto line](gotolinevim.md) tricks below (`282G`, `vim +282 file`) feel so natural once the pattern clicks.

### How it connects

- [Goto line Vim](gotolinevim.md): jumping straight to a line or symbol.
- [Emacs](emacs.md): the other great editor, and a friendly rivalry.
- [Linux](linux.md) and [Bash](bash.md): where you will meet Vim most.

The truth revealed: Vim feels baffling for a week and then becomes invisible, because once editing is a language your fingers speak, you stop thinking about the editor and think only about the text.
