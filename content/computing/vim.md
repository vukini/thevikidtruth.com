---
title: vim
date: '2016-11-22T22:30:18+04:00'
lastmod: '2022-09-15T02:15:51+04:00'
original_id: '{A335}'
original_name: vim
original_blob: blob/B/11/317.txt
revisions: 11
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: vim
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
  [emacs](emacs.md) | [computing](computing.md)

# vim

vim is one of the tools that you will want to get familiar with in linux. Just like Emacs, vim has it's adherents who
evangelize endlessly about its virtues.

I happen to love both [emacs](emacs.md) & [vim](vim.md) finding that I happen to pop in and out of both continuously while working. You
can do everything you want in either one of them, but like many things in life, having multi options you are fairly
competent in, is very useful, fun and keeps life interesting.

To get started in vim, once you have it on your system just type this in the shell:

```
$ vimtutor
```

and your away!

My notes on vim, [vikid's vim notes](vikidvim.md)

## What it is, in plain words

Here is the truth about vim: **it is not an editor with strange shortcuts. It is a small language for talking about text, and the shortcuts are its words.** Once you see that, it stops being a memory test.

vim ("Vi IMproved") was written by Bram Moolenaar in 1991 as a clone of Bill Joy's `vi` from 1976. Bram passed away in 2023 and the project is now maintained by a team of volunteers; Vim 9.1 is the current line, with its own faster scripting language, **Vim9 script**. Its big sibling **Neovim** (0.11 and newer in 2026) forked in 2014 and adds built-in LSP, Tree-sitter parsing and Lua configuration. Both share the same core: **modal editing**.

- **Normal mode** – keys are commands. You spend most of your time here.
- **Insert mode** – keys type text. Enter with `i`, `a`, `o`; leave with `Esc`.
- **Visual mode** – select text with `v`, `V` or `Ctrl-v`, then act on it.
- **Command-line mode** – `:` commands such as `:w`, `:q`, `:%s/old/new/g`.

### Why it matters

- **It is everywhere.** Some `vi` is on every Linux server, router, container and rescue disk. When the GUI is gone, it is still there.
- **It is fast once learned.** Editing becomes composing commands rather than holding keys down.
- **Its language spreads.** Vim keys work in Emacs (Evil mode), VS Code, JetBrains IDEs, browsers (Vimium, Tridactyl), `less`, `man`, and window managers. StumpWM and [i3](i3.md) users often bind vim-style `hjkl` for window movement too.

### An everyday analogy: speaking in sentences

In most editors you point and drag, like gesturing at things in a shop. Vim lets you *say* what you want: "delete inside the quotes", "change to the end of the sentence", "yank three paragraphs". Commands are **verb + count + noun**:

| Verb | Meaning | Noun (motion or text object) | Meaning |
|---|---|---|---|
| `d` | delete | `w` | to next word |
| `c` | change | `$` | to end of line |
| `y` | yank (copy) | `ip` | inner paragraph |
| `>` | indent | `i"` | inside quotes |
| `gU` | uppercase | `t,` | up to the next comma |

So `d2w` deletes two words, `ci"` changes everything inside the quotes, `yip` copies a paragraph, `gUiw` uppercases a word. Learn five verbs and ten nouns and you know fifty commands. And `.` repeats the last change, which is where the real speed comes from.

### A hands-on example

Start with the built-in tutorial (`vimtutor`, 30 minutes, really do it). Then try this in any file:

```
/TODO<Enter>     search for TODO
cwDONE<Esc>      change the word to DONE
n.               jump to the next TODO and repeat the change
:%s/foo/bar/gc   replace foo with bar everywhere, confirming each
qa ... q         record a macro into register a; @a plays it, 10@a ten times
:g/^$/d          delete every empty line
```

A minimal, modern `~/.vimrc` to start from:

```vim
vim9script
set number relativenumber      # line numbers relative to the cursor
set ignorecase smartcase incsearch hlsearch
set expandtab shiftwidth=4 tabstop=4
set clipboard=unnamedplus      # share the X clipboard (needs vim with +clipboard)
syntax on
filetype plugin indent on
nnoremap <Space>w :w<CR>
```

On Vikix, a vim build with `+clipboard` is what you want (check with `vim --version | grep clipboard`; the `gvim` package provides one); `neovim` is packaged too. For Lisp work, plugins like vim-sexp or Conjure make parentheses as easy to edit as in Emacs.

### Common misconceptions

- **"You can't quit vim."** `:q` quits, `:q!` quits without saving, `:wq` or `ZZ` saves and quits.
- **"Vim users memorise hundreds of shortcuts."** They learn a grammar of a few dozen words and combine them.
- **"Vim versus Emacs is a war."** I use both every day. Emacs is a Lisp machine that edits text; vim is a text-editing language. Evil mode lets you have both at once.
- **"You need lots of plugins."** Stock vim with a 10-line config does most things. Add plugins when you feel a specific need.
- **"Arrow keys are forbidden."** They work fine. `hjkl` is simply faster because your hands stay on the home row.

### Connections

- [Emacs Notes](emacsnotes.md), [The i3 Window Manager](i3.md), [Penti](penti.md), [KMonad](kmonad.md).
- [Vikid's Bash Cookbook](vikidsbashcookbook.md), [Linux Tools](linuxtools.md), [Git](git.md) (vim is the default commit-message editor on many systems).
- [Simple Linux Configuration](simplelinuxconfig.md) – dotfiles on Vikix.

# Links & Sources

- [SpaceVim Docs](https://spacevim.org/documentation/#window-manager)
- [SpaceVim tutorial](https://spacevim.org/quick-start-guide/#online-tutorials)
- [vim movement](http://naleid.com/blog/2010/10/04/vim-movement-shortcuts-wallpaper)
- [How to Copy and Paste](https://linuxize.com/post/how-to-copy-cut-paste-in-vim/)
- [NeatVi](https://github.com/aligrudi/neatvi.git)
- [Windows Management](http://vimdoc.sourceforge.net/htmldoc/windows.html#window-resize)
