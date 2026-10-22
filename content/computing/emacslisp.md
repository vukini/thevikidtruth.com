---
title: Emacs Lisp Notes
date: '2022-08-28T12:43:04+04:00'
lastmod: '2022-08-28T13:35:22+04:00'
original_id: '{A1714}'
original_name: emacslisp
original_blob: blob/B/11/117.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: emacslisp
draft: false
topics:
- lisp
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

# Emacs Lisp Notes

Some Functions to explore:

```
    (switch-to-buffer-other-window "buffer-name")
    (erase-buffer)
    (search-forward)
    (re-search-forward)
    (replace-match "Some-text")
    (other-window 1)
    (goto-char (point-max))
    (add-text-properties)
    (match-beginning)
    (match-end)
    (other-window)
```

### The plain idea

Emacs Lisp (Elisp) is the language Emacs is written in and the language you speak to it in. Every key you press runs a Lisp function. `C-f` runs `forward-char`; `C-x C-s` runs `save-buffer`. Elisp is a Lisp: code is written as lists in parentheses, the first item is the function, and the rest are its arguments. `(+ 1 2)` is 3. `(insert "hello")` puts "hello" in the current buffer.

What makes Elisp unusual is that it is a language built around editing. Its basic objects include buffers (the text you are working on), points (cursor positions), markers, windows and frames. The functions listed above, `erase-buffer`, `search-forward`, `replace-match`, `goto-char`, are the verbs of that world.

### Why it matters

Without Elisp, Emacs is a capable editor. With it, Emacs is whatever you need. Small bits of Elisp remove the repetitive chores from your day: renaming things across a file, inserting templates, tidying a log, opening the three files you always open together. And because the whole editor is written in the same language, you can read the source of any command (`C-h f`, then follow the link) and learn by example from the people who built it.

It has also improved a lot. Lexical binding, switched on by the cookie `;;; -*- lexical-binding: t -*-` at the top of a file (Emacs 30 warns when a file lacks it), makes closures behave the way they do in other modern languages. Native compilation turns Elisp into machine code for speed, and `cl-lib` supplies Common Lisp conveniences such as `cl-loop`.

### An everyday analogy: talking to a very literal assistant

Imagine an assistant sitting at your desk who knows exactly where your cursor is and can follow simple instructions: go to the end, search for this word, replace it with that, switch to the other window. Elisp is how you write those instructions down so the assistant can repeat them forever without you.

### A worked example: clean a buffer in one keystroke

Suppose you often paste text with trailing spaces and runs of blank lines. Here is a command that fixes both, using several of the functions from my list:

```elisp
(defun vikid/tidy-buffer ()
  "Remove trailing spaces and collapse runs of blank lines."
  (interactive)
  (save-excursion
    (goto-char (point-min))
    (while (re-search-forward "[ \t]+$" nil t)
      (replace-match ""))
    (goto-char (point-min))
    (while (re-search-forward "\n\\{3,\\}" nil t)
      (replace-match "\n\n"))))

(global-set-key (kbd "C-c t") #'vikid/tidy-buffer)
```

Read it line by line:

1. `defun` defines a function; the string is its documentation, shown by `C-h f`.
2. `(interactive)` makes it a command you can run with `M-x` or a key.
3. `save-excursion` remembers where the cursor was and puts it back afterwards.
4. `goto-char (point-min)` jumps to the start of the buffer.
5. `re-search-forward` finds the next match of a [regular expression](regularexpressions.md); `nil t` means "no limit, and don't complain if nothing is found".
6. `replace-match` swaps the matched text for the new text.

Put the cursor after the last parenthesis and press `C-x C-e` to evaluate it. It is now part of your editor.

### Common misconceptions

- **"Elisp is just a config language."** It is a full programming language. Org mode, Magit and whole mail clients are written in it.
- **"Elisp is the same as Common Lisp."** They are cousins. Elisp is simpler, has no package-level namespaces (hence the `vikid/` prefix habit), and is tied to the editor. `cl-lib` borrows some Common Lisp features.
- **"Dynamic scope makes Elisp weird."** That was true for years. With lexical binding on, which is what all new code should use, variables behave the way you expect, while special variables can still be dynamically bound when that is useful.
- **"You need to learn it all at once."** You need about ten functions to be dangerous. The rest you look up with `C-h f` as you go.

### How it connects

- [Emacs](emacs.md): the environment Elisp lives in.
- [My .emacs file](dotemacs.md) and [init.org](initorg.md): where your Elisp usually ends up.
- [PicoLisp](picolisp.md), [Common Lisp](commonlisp.md) and [Scheme](scheme.md): the rest of the Lisp family.
- [Regular Expressions](regularexpressions.md): the search language Elisp uses for most text work.

The truth revealed: you start writing Elisp to fix one small annoyance, and a few years later the editor is a portrait of how you think.

## Tutorials & Links

- [Emergency Lisp by Steve Yegge](http://steve-yegge.blogspot.com/2008/01/emergency-elisp.html)
- [Elisp Guide by Chris Done](https://github.com/chrisdone/elisp-guide)
- [How to Read Emacs Lisp by Sacha Chua](http://emacslife.com/how-to-read-emacs-lisp.html)
- [elisp by Xah Lee](http://xahlee.info/emacs/emacs/elisp.html)
- [Elisp Cookbook](https://www.emacswiki.org/emacs/ElispCookbook)
- [Practical Elisp by Xah Lee](http://xahlee.info/emacs/emacs/practical_elisp.html)
- [Example Config](https://www.emacswiki.org/emacs/ExampleConfigurations)
- [System Crafters Emacs Lisp intro](https://www.youtube.com/watch?v=RQK_DaaX34Q)
- [Emacs Lisp Tutorial by Sacha Chua](http://www.emacslife.com/emacs-lisp-tutorial.html)
- [Emacs Lisp by Fincher](https://www.fincher.org/tips/Languages/Emacs.shtml)
- [Introduction by Christian Johansen](https://cjohansen.no/an-introduction-to-elisp)
- [Getting Started by Ben Windsor](https://benwindsorcode.github.io/Getting-Started-With-Emacs-Lisp/)
- [GNU Emacs Lisp Reference Manual](https://www.gnu.org/software/emacs/manual/html_node/elisp/)
- [An Introduction to Programming in Emacs Lisp](https://www.gnu.org/software/emacs/manual/html_node/eintr/)
