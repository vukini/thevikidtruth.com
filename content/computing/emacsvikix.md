---
title: Emacs on Vikix & StumpWM
date: '2026-10-22T15:00:00+04:00'
lastmod: '2026-10-22T15:00:00+04:00'
tags:
- computing
categories:
- computing
draft: false
wikislug: emacsvikix
topics:
- tools
---

[Computing](computing.md) |
[Vikix](vikix.md) |
[Emacs Notes](emacsnotes.md) |
[My Emacs Config Tour](myemacsconfig.md) |
[Emacs on Vikix & StumpWM](emacsvikix.md) |
[Common Lisp](commonlisp.md) | [i3](i3.md)

Here is the truth about my desktop: **the window manager and the editor are both Lisp, and they can talk to each other.** [Vikix](vikix.md) ([vikix.dev](https://vikix.dev)) is my Void Linux setup built around StumpWM, which is written in Common Lisp. Emacs is the editor. This page is about where they meet.

My Emacs config ([vukini/emacs-void](https://github.com/vukini/emacs-void/blob/main), toured in [My Emacs Config Tour](myemacsconfig.md)) works on any machine. On Vikix it picks up extra pieces. Everything here comes from those two repos.

### The core idea, in plain words

There are two owners of files:

| Where | Whose | What |
|---|---|---|
| `~/.emacs.d` | a git clone of emacs-void | the config, `config.org`; `vikix update` pulls it |
| `~/.local/share/vikix/emacs` | Vikix's | `vikix-theme.el`, `vikix-ai.el`, `vikix-notes.el`, `vikix-python.el` (and more), a link into the Vikix checkout |

(From Vikix's [editors guide](https://github.com/vukini/vikix/blob/main/docs/editors.md).)

The Vikix installer step `45-editors` clones emacs-void into `~/.emacs.d` and links [`config/emacs`](https://github.com/vukini/vikix/blob/main/config/emacs) into place. My config then loads each Vikix file *only if it is there*:

```elisp
(load (expand-file-name "~/.local/share/vikix/emacs/vikix-notes") t t)
```

The two `t`s mean "no error if missing, no message". So on a plain machine nothing happens, and on Vikix the extras switch on. That one pattern is the whole integration.

### Starting Emacs: one daemon, many frames

Emacs runs as a daemon from login, so frames open instantly with `emacsclient`. StumpWM's command registry binds it to Super+x:

```lisp
(define-vikix-command emacs "Emacs: a new window"
  :run "exec emacsclient -c -a ''" :key "s-x")
```

[`registry.lisp`](https://github.com/vukini/vikix/blob/main/config/stumpwm/vikix/registry.lisp)

`-a ''` means "start a server if there isn't one". Super+q closes the window, and the snippet at the end of my `init.el` remembers that frame's layout so the next Super+x brings it back. Vikix's built-in guide opens in Emacs's Info reader the same way, and Esploro, the Vikix file explorer, is an Emacs frame too (Super+e).

### Talking to the window manager: SLIME on port 4004

This is the part I love. StumpWM is built with Swank inside it, and Vikix starts the Swank server on 127.0.0.1 port 4004, leaving 4005 for ordinary SLIME sessions. From Emacs:

```
M-x slime-connect RET 127.0.0.1 RET 4004
```

and you are at a REPL *inside the running window manager*. Redefine a command, rebind a key, try a colour, and it takes effect immediately, no restart. Because Swank runs whatever it is sent, Vikix protects the connection with a shared-secret file that SLIME sends by itself ([`swank.lisp`](https://github.com/vukini/vikix/blob/main/config/stumpwm/vikix/swank.lisp)). My config's SLIME section (`sbcl`, `slime-fancy`, local HyperSpec) is the same one I use for normal Common Lisp, so editing the WM feels like editing any Lisp program. StumpWM's rules even say a rule defined twice (a reload, or `C-x C-e` in Emacs) simply replaces itself.

### Theme follows the desktop

`vikix theme NAME` changes the whole desktop, and `vikix-theme.el` makes a running Emacs change with it: Catppuccin for the default dark and light themes, Doom's themes for gruvbox, nord and tokyo-night, and Modus Vivendi (which ships with Emacs) for high contrast. My config falls back to gruber-darker when Vikix isn't there:

```elisp
(unless (load (expand-file-name "~/.local/share/vikix/emacs/vikix-theme") t t)
  (use-package gruber-darker-theme
    :ensure t
    :config
    (load-theme 'gruber-darker t)))
```

[`config.org`, Theme and frame appearance](https://github.com/vukini/emacs-void/blob/main/config.org)

### Notes under C-c n

[`vikix-notes.el`](https://github.com/vukini/vikix/blob/main/config/emacs/vikix-notes.el) puts my Org notes in `~/Dropbox/notes` under one prefix:

| Key | Does |
|---|---|
| `C-c n a` | the agenda: this week, then every TODO |
| `C-c n t` | every TODO in the notes |
| `C-c n c` | a note into the inbox |
| `C-c n o` | open a notes file |
| `C-c n j` | today's journal page |
| `C-c n f` | find or start a note (org-roam) |
| `C-c n i` | insert a link to another note |
| `C-c n l` | backlinks to this note |
| `C-c n g` | the notes graph in the browser (org-roam-ui, 127.0.0.1 only) |

emacs-void installs org-roam and org-roam-ui deferred, so they load only when one of these keys first needs them. org-roam's database lives in `~/.cache/vikix`, not in Dropbox.

### AI and agents

gptel is set up in my config with OpenAI and Perplexity. On Vikix, `vikix-ai.el` adds Claude and local models (Ollama) and makes the default whatever model Super+i uses (`vikix ai use`). `C-c g` opens a chat, `C-c G` the menu. For coding agents, `C-c a` opens agent-shell; on Vikix it starts *my* agent through `vikix agent` and `C-c A` runs it in a terminal:

```elisp
(if (fboundp 'vikix-ai-agent)
    (progn
      (keymap-global-set "C-c a" #'vikix-ai-agent)
      (keymap-global-set "C-c A" #'vikix-ai-agent-terminal))
  (keymap-global-set "C-c a" #'agent-shell))
```

Keys come from the environment or Vikix's secrets folder, never from the config.

### Python as an IDE under C-c p

[`vikix-python.el`](https://github.com/vukini/vikix/blob/main/config/emacs/vikix-python.el) finds the project's `.venv` by itself for pyright, the REPL, pytest and ruff, and in Python buffers gives: `C-c p t` test, `T` test the file, `P` the whole project, `r` run, `s` the REPL, `f` format, `F` format on save, `c` check, `v` the venv, `i` the IDE layout, `d` docs, `q` quit.

### Common misconceptions

- **"Vikix forks your Emacs config."** It doesn't. It clones emacs-void as is, and the Vikix parts are separate files loaded only if present.
- **"Talking to the WM from Emacs is a gimmick."** It's how I fix StumpWM: no restart, no lost windows.
- **"You need Vikix to use this config."** Without Vikix, every one of those `load` calls quietly does nothing.

### Connections

- [My Emacs Config Tour](myemacsconfig.md), [Emacs Notes](emacsnotes.md).
- [Common Lisp](commonlisp.md), [The i3 Window Manager](i3.md), [Linux](linux.md).
