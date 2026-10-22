---
title: Configuring Emacs with org-mode & init.org
date: '2016-11-22T06:51:31+04:00'
lastmod: '2016-11-22T07:23:46+04:00'
original_id: '{A330}'
original_name: initorg
original_blob: blob/B/1/574.txt
revisions: 9
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: initorg
draft: false
topics:
- tools
---

# Configuring Emacs with org-mode & init.org

[Back to .emacs](dotemacs.md)

Hopefully now you have setup your emacs to:

- **Start as a daemon** on Linux startup
- Created a shortcut to **start emacs as a client**
- Updated your **.emacs**

as per instructions in [.emacs](dotemacs.md) page. If not, do it now.

You now need to create a file **init.org** and save it in the **.emacs.d** folder.

Create them if they don't already exist.

### The plain idea

`init.org` is an Emacs configuration written as an [org-mode](https://orgmode.org) document. Prose headings explain what each part does, and the actual Emacs Lisp sits inside source blocks:

```org
* Appearance
I like a quiet screen, so no tool bar or scroll bar.
#+begin_src emacs-lisp
(tool-bar-mode -1)
(scroll-bar-mode -1)
#+end_src
```

When Emacs starts, the one line in your `.emacs` (or `init.el`), `(org-babel-load-file "~/.emacs.d/init.org")`, pulls out ("tangles") every `emacs-lisp` block into a file called `init.el` beside it and loads that. This is literate programming, the idea Donald Knuth championed: a program written primarily for people to read, which a machine can also run.

### Why it matters

Configs rot. Six months after you add a clever snippet you will not remember why it is there, and you will be afraid to delete it. In an org file, the reason sits right above the code. You can fold everything to headings with `TAB`, see the whole shape of your setup at a glance, move sections around, and disable a block by changing one tag. Org also exports, so the same file can become a web page, which is how many people share their configs.

### An everyday analogy: a recipe book, not a shopping list

A plain `init.el` is a shopping list: eggs, flour, sugar. It works if you already know what you are baking. `init.org` is a recipe book: the same ingredients, with the method and notes in the margin ("use less sugar, Mum found it too sweet"). Anyone, including future you, can cook from it.

### A worked example: a minimal setup

`~/.emacs.d/init.el` is now tiny. Note that tangling writes `init.el`, so keep the org file's output name distinct if your loader file is also called `init.el`. A common pattern is to name the loader `~/.emacs` or have `init.org` tangle to `config.el`:

```elisp
;; ~/.emacs
(require 'org)
(org-babel-load-file (expand-file-name "init.org" user-emacs-directory))
```

And `~/.emacs.d/init.org` starts like this:

```org
#+title: My Emacs configuration
#+property: header-args:emacs-lisp :lexical t

* Packages
#+begin_src emacs-lisp
(require 'package)
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/") t)
(require 'use-package)          ; built in since Emacs 29
(setq use-package-always-ensure t)
#+end_src

* Completion
#+begin_src emacs-lisp
(use-package vertico :init (vertico-mode))
#+end_src

* Org itself
#+begin_src emacs-lisp
(setq org-agenda-files '("~/org/"))
#+end_src
```

Restart Emacs, or run `M-x org-babel-load-file` on the file, and the settings take effect. To try a block without restarting, put the cursor in it and press `C-c C-c`.

### Common misconceptions

- **"Literate configs are slow to start."** Tangling happens only when `init.org` is newer than the generated file. Otherwise Emacs just loads the ordinary Elisp.
- **"You need to know org-mode well first."** You need headings (`*`), source blocks and `TAB` to fold. That is all.
- **"Everything must go in one file."** Large setups often split into several org files loaded in turn.
- **"`(require 'cl)` belongs at the top."** Older guides, including my own earlier notes, loaded `cl`. It is obsolete; use `cl-lib` if you need Common Lisp helpers.

### How it connects

- [My .emacs file](dotemacs.md): the step before this one, starting Emacs as a daemon and loading this file.
- [Emacs](emacs.md) and [Emacs Lisp](emacslisp.md): what goes inside the blocks.
- [Git](git.md): keep `init.org` under version control and every experiment is reversible.

The truth revealed: the best config is the one you can still read next year.

## Sources

- I got a major inspiration from the works of
  [Arnaud Legrand](http://mescal.imag.fr/membres/arnaud.legrand/misc/init.php).
  Rather than duplicate efforts. You can read about it by following the link.
- [Org Manual: Working with Source Code](https://orgmode.org/manual/Working-with-Source-Code.html)
- [GNU Emacs manual: The Emacs Initialization File](https://www.gnu.org/software/emacs/manual/html_node/emacs/Init-File.html)
