---
title: My Emacs Config Tour
date: '2026-10-22T15:00:00+04:00'
lastmod: '2026-10-22T15:00:00+04:00'
tags:
- computing
categories:
- computing
draft: false
topics:
- tools
---

[Computing](computing.md) |
[Emacs Notes](emacsnotes.md) |
[My Emacs Config Tour](myemacsconfig.md) |
[Emacs on Vikix & StumpWM](emacsvikix.md) |
[Common Lisp](commonlisp.md) | [vim](vim.md) | [Git](git.md)

Here is the truth about my Emacs config: **it is one Org file that explains itself, and a tiny `init.el` that turns it into Lisp.** No framework, no Doom, no Spacemacs. Just `use-package` declarations, each with a sentence saying why it is there, and a few scars from things that broke.

It lives in public at [vukini/emacs-void](https://github.com/vukini/emacs-void/blob/main) ("Simple Emacs Config that works on Void Linux"). Everything quoted on this page is copied from that repo; I have not tidied it up for the page. It targets Emacs 30.

### The core idea, in plain words

Emacs reads `~/.emacs.d/init.el` at start. Mine does three jobs:

1. Switch off the noise (splash screen, bell, menu, tool and scroll bars).
2. Turn on a few built-ins: `save-place-mode`, `desktop-save-mode` and `windmove-default-keybindings` (Shift + arrows moves between windows).
3. Load the real config:

```elisp
(require 'org)  ;; ensure Org is available
(org-babel-load-file (expand-file-name "config.org" user-emacs-directory))
```

[`init.el`](https://github.com/vukini/emacs-void/blob/main/init.el)

`org-babel-load-file` *tangles* every `elisp` source block in [`config.org`](https://github.com/vukini/emacs-void/blob/main/config.org) into `config.el` and loads it. It only re-tangles when `config.org` is newer, so start-up stays fast. This is literate programming: the prose and the code sit side by side, and `config.el` is generated output that I never edit by hand.

### How the file is laid out

`config.org` is organised in load order, and its own table of contents says so:

| Section    | Contents                                        |
|------------|-------------------------------------------------|
| Bootstrap  | load-path, package archives, use-package        |
| Core       | custom file, backups, appearance, global keys   |
| Completion | vertico, corfu and the rest of the stack        |
| Navigation | avy, projectile, speedbar                       |
| Editing    | paredit, yasnippet, input methods               |
| Languages  | eglot plus per-language setup                   |
| Tools      | magit, pdf-tools, nov, gptel                    |
| Attic      | disabled config, kept for reference             |

The **Attic** is my favourite habit. Old setups (lsp-mode, an Obsidian package, an earlier gptel backend) are kept as `:tangle no` blocks. They never load, but when I wonder "how did I do that before?", the answer is right there.

Packages come from MELPA, and `use-package-always-ensure` is on, so a plain declaration installs the package on a fresh machine. Built-ins say `:ensure nil`.

### The packages, and why

**Completion: two independent stacks.** In the minibuffer: [Vertico](https://github.com/minad/vertico) shows candidates in a vertical list, [Orderless](https://github.com/oantolin/orderless) lets space-separated words match in any order, [Marginalia](https://github.com/minad/marginalia) adds notes in the margin, [Consult](https://github.com/minad/consult) gives better search and switch commands, and [Embark](https://github.com/oantolin/embark) acts on whatever is under the cursor. In the buffer: [Corfu](https://github.com/minad/corfu) pops up completions as you type, with Cape for extra sources and kind-icon for the little icons. `savehist` (built in) remembers minibuffer history.

**Navigation.** [Avy](https://github.com/abo-abo/avy) for jumping to anything visible, Projectile (deferred, only loads when used) with my project folders `~/p/`, `~/apps/` and `~/repos`, and the built-in Speedbar.

**Editing.** Paredit in every Lisp buffer (Emacs Lisp, Common Lisp, Racket and its REPL), and Yasnippet with my own snippets in [`snippets/`](https://github.com/vukini/emacs-void/blob/main/snippets) (Org source blocks, an HTML skeleton, a C `main`, a Makefile). There is also a Haskell Unicode input method installed straight from GitHub with `use-package :vc`.

**Languages.** Eglot (built in) is the one LSP client. All the server mappings live in one place:

```elisp
(use-package eglot
  :ensure nil
  :custom
  (eglot-events-buffer-size 0)         ; 0 = unlimited event log
  :config
  (add-to-list 'eglot-server-programs '(zig-mode . ("zls")))
  (add-to-list 'eglot-server-programs '((odin-mode odin-ts-mode) . ("ols"))))
```

C and C++ use `ccls`, JavaScript and TypeScript use `typescript-language-server`, and Python, Odin and Zig hook `eglot-ensure` themselves. Common Lisp goes through **SLIME** with `sbcl` and a local copy of the HyperSpec when it is on disk. Racket mode only loads if `racket` is actually installed. Python uses `ipython` as its shell plus `pyvenv`. There are modes for Odin (tree-sitter), Zig, Jinja, CSV, Markdown, Lua, Go, PHP and even RFCs.

**Tools.** Magit for Git, vterm for a real terminal, pdf-tools and nov.el so PDFs and EPUBs open inside Emacs, gptel for chatting with language models, agent-shell for coding agents, and org-roam for linked notes.

### My keybindings

Nothing exotic: I keep the Emacs defaults and add a handful.

| Key | Does | From |
|---|---|---|
| `C-=` / `C--` | bigger / smaller text | core |
| `M-\` | previous window | core |
| `S-<arrows>` | move between windows | windmove, `init.el` |
| `C-x b` | buffers, recent files, bookmarks | consult |
| `C-s` | search lines in this buffer | consult |
| `M-s r` / `M-s f` | ripgrep / find file in the project | consult |
| `M-g i` | jump to a definition or heading | consult |
| `C-.` / `C-;` | act on the thing at point / do the obvious | embark |
| `C-:` / `C-'` | jump to a char / two chars | avy |
| `M-g f`, `M-g w`, `M-g e` | jump to a line / word | avy |
| `C-c p` | Cape's completion menu | cape |
| `C-x g` | Magit status | magit |
| `C-c g` / `C-c G` | gptel chat / gptel menu | gptel |
| `C-c a` | an agent chat | agent-shell |

One honest note: in Python buffers on Vikix, `C-c p` is taken over by the Python IDE keys (see [Emacs on Vikix](emacsvikix.md)), because a mode's own map wins over the global one.

`which-key` is turned on too. Since Emacs 30 it ships with Emacs, so the config just says `:ensure nil`. Press `C-c` and wait, and it shows what can follow.

### Notable snippets

**Comments that remember the bug.** My vterm block explains why the shell is pinned:

```elisp
(use-package vterm
  :ensure t
  :commands (vterm vterm-other-window)
  :custom
  ;; Not `shell-file-name': under the runit daemon $SHELL is unset, so that
  ;; resolves to /bin/sh (dash), which never sources ~/.bashrc.
  (vterm-shell "/bin/bash")
  (vterm-max-scrollback 10000))
```

[`config.org`, Tools › vterm](https://github.com/vukini/emacs-void/blob/main/config.org)

The Emacs daemon runs under runit with a bare `PATH`, so vterm got dash, which never reads `~/.bashrc`, so tools in `~/.npm-global/bin` were "not found". One line fixes it, and the paragraph above it in the Org file says why.

**Being careful with Emacs 30's new defaults.** Emacs 30 completes words in text buffers from a dictionary. Void has no `/usr/share/dict/words`, so with Corfu's auto popup every word logged an ispell error:

```elisp
(unless (seq-some #'file-readable-p '("/usr/share/dict/words" "/usr/dict/words"))
  (setq text-mode-ispell-word-completion nil))
```

**Coming back to where I left off.** The bottom of `init.el` remembers the window layout of the last frame I closed, and a new `emacsclient -c` frame comes back looking the same; with nothing to come back to, you get `*scratch*` in `~`:

```elisp
(add-hook 'delete-frame-functions #'my/remember-frame)
(setq initial-buffer-choice #'my/last-frame-or-scratch)
```

**No secrets in the repo.** gptel's OpenAI and Perplexity keys are read from the environment (pulled in from the login shell with `exec-path-from-shell`) through a lambda, so nothing private is ever written into the config.

### Common misconceptions

- **"A literate config is slow."** It is tangled once; after that Emacs loads plain `config.el`.
- **"You need lsp-mode."** Eglot is built in since Emacs 29 and does all I need. lsp-mode sits in my Attic.
- **"You need Doom to get a modern UI."** Vertico, Orderless, Marginalia, Consult, Embark and Corfu are small, separate packages that work with the standard completion API.

### Connections

- [Emacs Notes](emacsnotes.md): the basics and my older notes.
- [Emacs on Vikix & StumpWM](emacsvikix.md): how this config fits my desktop.
- [Emacs Lisp](emacslisp.md), [Common Lisp](commonlisp.md), [Racket](racket.md), [Git](git.md).
