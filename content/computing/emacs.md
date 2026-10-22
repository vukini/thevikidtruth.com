---
title: Emacs
date: '2016-05-19T02:22:37+04:00'
lastmod: '2023-05-20T03:43:20+04:00'
original_id: '{A46}'
original_name: emacs
original_blob: blob/B/12/272.txt
revisions: 38
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: emacs
draft: false
topics:
- tools
---

[Readinglist](readinglist.md)  | [Quick Links](quicklinks.md) | [Algorithms](algorithms.md) | [Apple](apple.md) | [AssemblyLanguage](assemblylanguage.md) |
[BASH](bash.md) |   [C-Programmming](cprogramming.md) | [CommonLisp](commonlisp.md) | [Computer Security](computersecurity.md) | [CuisSmalltalk](cuissmalltalk.md) |
[Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) |
[Functional Programming](functional.md) |
[Firewalls](firewalls.md) |   [Git](git.md) | [GNUSmalltalk](gnusmalltalk.md) | [Haskell](haskell.md) | [Javascript](javascript.md) |  [Julia](julia.md) |
[Linux](linux.md) | [Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |[Machine Learning](machinelearning.md) |
[Networking](networking.md) | [Operating Systems](os.md) |[Open Data Science](opendatascience.md) | [Odin](odin.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) | [Purescript](purescript.md) |
[Python](python.md) |
[Racket](racket.md) | [Scheme](scheme.md) | [Social Engineering](internetexploitation.md) |
[Unity](unity.md) | [vim](vim.md) | [V](vlang.md) |
[Web Development](webdevelopment.md) | [Windows WSL](windowswsl.md) | [Zig](ziglang.md)

# Emacs

![emacs-400](/assets/emacs-400.jpg)
{.right}

**Emacs, Shemacs!** Emacs is the most wonderful editor in existence. To be sure I use
**[vim](vim.md)** too, when the situation arises. And in being a computer polyglot I think
it is quite useful to have a few skills, but in terms of pleasure, Emacs wins!

The real problem with emacs is that it takes years to get into it. You have to
persevere, you have to learn elisp and you have to spend time cultivating a
gargantuan .emacs file.

Theres tonnes of information out there, plenty of starter kits to get you off the
ground. But I would avoid them. Craft your own. It is the zen of emacs.

In the months and years that follow, I will be posting many of my emacs exploits,
 tip and tricks here on these pages. I hope that they will help you on your
journey.

### The plain idea

Emacs is a text editor the way a workshop is a hammer. Underneath the windows and buffers sits a small core written in C and a large Lisp interpreter, and almost everything you touch, from the way a key moves the cursor to the mail client, is a Lisp function you can read, change or replace while the editor is running. You do not so much use Emacs as grow it.

In 2026 that core is in good health. The Emacs 29 and 30 releases folded in things people used to bolt on by hand: `use-package` is built in, Eglot gives you language-server support (completion, go-to-definition, renames) out of the box, tree-sitter powers fast and accurate syntax highlighting for many languages, native compilation of Lisp to machine code is a standard build option, and `which-key` ships with the editor. A fresh Emacs is far less bare than the one I first met.

### Why it matters

Most tools ask you to adapt to them. Emacs adapts to you. Once your editing, notes, agenda, Git, shell and writing all live in one programmable place, the friction between them disappears. A keyboard macro you record for code works just as well in an email. A function you write to clean up a log file can clean up a chapter of a book.

It also matters because it lasts. Emacs has been around since the 1970s and GNU Emacs since 1985. The hours you put into it are not thrown away when a company changes its pricing or a plugin store closes. Your config is a text file you own.

### An everyday analogy: a kitchen you build yourself

A modern IDE is a fitted kitchen from a showroom: everything is where the designer put it, and it works well until you want the sink somewhere else. Emacs is an empty room with excellent plumbing and a pile of good timber. The first week you cook on a camping stove. A year later every drawer is exactly where your hand reaches for it, and nobody else's kitchen feels right.

### A worked example: making Emacs yours in ten lines

Here is a tiny but real start, the kind of thing that goes in `~/.emacs.d/init.el` (or in an [init.org](initorg.md) file if you like literate configs):

```elisp
;; Show line numbers in programming buffers
(add-hook 'prog-mode-hook #'display-line-numbers-mode)

;; Remember recently opened files
(recentf-mode 1)

;; Language servers via the built-in Eglot
(add-hook 'python-mode-hook #'eglot-ensure)

;; A command of my own, bound to a key
(defun vikid/insert-date ()
  "Insert today's date at point."
  (interactive)
  (insert (format-time-string "%Y-%m-%d")))
(global-set-key (kbd "C-c d") #'vikid/insert-date)
```

Evaluate the buffer with `M-x eval-buffer` and the changes take effect immediately, no restart. That last function is the whole point: four lines of [Emacs Lisp](emacslisp.md) and the editor has a new feature that nobody shipped. Use `C-h f` on any function or `C-h k` on any key to see its documentation and jump to its source.

### Common misconceptions

- **"Emacs is just for old-timers."** It has a lively community: Protesilaos Stavrou's themes and packages, System Crafters, and a steady stream of new packages for completion (Vertico, Corfu, Consult) keep it modern.
- **"You must use a starter kit."** Doom Emacs and Spacemacs are excellent if you want a ready-made setup, and Crafted Emacs is a gentle middle ground. I still think you learn far more by crafting your own, a little at a time.
- **"Emacs vs Vim is a war."** Plenty of people use both. Evil mode gives Emacs Vim's keys, and I reach for [vim](vim.md) on servers without a second thought.
- **"Emacs needs a giant config."** A useful setup can be fifty lines. Mine is gargantuan because I enjoy it, not because it must be.

### How it connects

- [Emacs Lisp](emacslisp.md): the language that makes all of this possible.
- [My .emacs file](dotemacs.md) and [init.org](initorg.md): how I organise my own configuration.
- [PicoLisp](picolisp.md) and [Common Lisp](commonlisp.md): Emacs is many people's first Lisp, and a good doorway to the rest of the family.
- [Git](git.md): Magit, the Emacs Git interface, is reason enough to install Emacs.
- [vim](vim.md): the other great editor, and a fine companion.

The truth revealed: Emacs is not hard because it is old. It is hard because it hands you the keys to the whole machine, and learning to drive takes time.

## Links

- [Emacs Notes](emacsnotes.md)
- [EmacsLisp](emacslisp.md)
- [My .emacs file - an exploration](dotemacs.md)

- [Doom Tutorials by Distrotube](https://www.youtube.com/playlist?list=PLyy8KUDC8P7X6YkegqrnEnymzMWCNB4bN)
- [Doom Cast](https://www.youtube.com/playlist?list=PLhXZp00uXBk4np17N39WvB80zgxlZfVwj)
- [Ergomacs - Xah's amazing emacs site](http://ergoemacs.org/index.html)
- [Emacs Manual](https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html#SEC_Contents)
- [GitHub - emacs-dashboard/emacs-dashboard: An extensible emacs dashboard](https://github.com/emacs-dashboard/emacs-dashboard)
- [ Emacs: display ugly ^L page breaks as tidy horizontal lines](https://github.com/purcell/page-break-lines)
- [A utility package to collect various Icon Fonts and propertize them within Emacs.](https://github.com/domtronn/all-the-icons.el)
- [Next-generation, purely functional package manager for the Emacs hacker.](https://github.com/radian-software/straight.el)
- [exwm-x](https://github.com/tumashu/exwm-x)
- [Emacs from Scratch](https://github.com/daviwil/emacs-from-scratch)
- [Skewer-mode](https://github.com/skeeto/skewer-mode)
- [Doom Emacs](https://github.com/doomemacs/doomemacs)
- [A Life Configuring Emacs](https://alhassy.github.io/emacs.d/)
- [Common Lisp on Emacs](https://www.gnu.org/software/emacs/manual/html_mono/cl.html)
- [using-straight-el](https://systemcrafters.cc/advanced-package-management/using-straight-el/)
- [emacs manual on CL](https://www.gnu.org/software/emacs/manual/html_mono/cl.html)
- [crafted-emacs](https://github.com/SystemCrafters/crafted-emacs)
- [https://dawranliou.com/blog/rewriting-my-emacs-config](https://dawranliou.com/blog/rewriting-my-emacs-config)
- [A Life Configuring Emacs](https://alhassy.github.io/emacs.d/)
- [Beacon](https://github.com/Malabarba/beacon)
- [clippy.el](https://github.com/Fuco1/clippy.el)
- [use-package](https://github.com/jwiegley/use-package)
- [denote](https://protesilaos.com/emacs/denote)
- [latex-emacs](https://ejenner.com/post/latex-emacs/)
- [EmacsCommonLisp](https://www.emacswiki.org/emacs/EmacsCommonLisp)
- [LSP Dart](https://emacs-lsp.github.io/lsp-dart/)
- [publishing-with-org-mode-export](https://lucidmanager.org/productivity/publishing-with-org-mode-export/)
- [Fastmail setup in Emacs](https://rakhim.org/fastmail-setup-with-emacs-mu4e-and-mbsync-on-macos/)
- [Emacs Lisp](https://www.fincher.org/tips/Languages/Emacs.shtml)
- [steve yegge - effective-emacs](https://sites.google.com/site/steveyegge2/effective-emacs)
- [Excellent Free Tutorials to Learn Emacs Lisp - LinuxLinks](https://www.linuxlinks.com/excellent-free-tutorials-learn-emacs-lisp/)
- [Protesilaos Stavrou](https://protesilaos.com/)
- [Emacs Lisp](https://www.fincher.org/tips/Languages/Emacs.shtml)
- [Stevey's Blog Rants: Emergency Elisp](http://steve-yegge.blogspot.com/2008/01/emergency-elisp.html?m=1)
- [chrisdone/elisp-guide: A quick guide to Emacs Lisp programming](https://github.com/chrisdone/elisp-guide)
- [EmacsWiki: Online Resources](https://www.emacswiki.org/emacs/OnlineResources)
- [GitHub - jwiegley/use-package: A use-package declaration for simplifying your .emacs](https://github.com/jwiegley/use-package)
- [Top (Magit User Manual)](https://magit.vc/manual/magit/)
- [macs-eaf/emacs-application-framework: EAF, an extensible framework that revolutionizes the graphical capabilities of Emacs](https://github.com/emacs-eaf/emacs-application-framework)
- [how to open *.info file in emacs in info mode?](https://stackoverflow.com/questions/1921049/how-to-open-info-file-in-emacs-in-info-mode)
- [What is a easy way to view texi files?](https://askubuntu.com/questions/433807/what-is-a-easy-way-to-view-texi-files)
