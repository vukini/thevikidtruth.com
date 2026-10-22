---
title: Cuis Smalltalk
date: '2022-09-12T01:39:35+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1727}'
original_name: cuissmalltalk
original_blob: blob/B/12/006.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: cuissmalltalk
draft: false
topics:
- other-languages
---

[Read This!](caveatemptor.md) | | [Quick Links](quicklinks.md) | [Algorithms](algorithms.md) | [AssemblyLanguage](assemblylanguage.md) | [BASH](bash.md) |   [C-Programmming](cprogramming.md) |
[CommonLisp](commonlisp.md) |
[Computer Security](computersecurity.md) | [CuisSmalltalk](cuissmalltalk.md) | [Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) |
[Functional Programming](functional.md) |
[Firewalls](firewalls.md) |   [Git](git.md) | [GNUSmalltalk](gnusmalltalk.md) | [Haskell](haskell.md) | [Javascript](javascript.md) |  [Julia](julia.md) |
[Linux](linux.md) | [Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |[Machine Learning](machinelearning.md) |
[Networking](networking.md) | [Operating Systems](os.md) |[Open Data Science](opendatascience.md) | [Odin](odin.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) | [Purescript](purescript.md) |
[Python](python.md) |
[Racket](racket.md) | [Scheme](scheme.md) | [Social Engineering](internetexploitation.md) |
[Unity](unity.md) | [vim](vim.md) | [V](vlang.md) |
[Web Development](webdevelopment.md) | [Windows WSL](windowswsl.md) | [Zig](ziglang.md)

[Terse Guide](cuisterseguide.md)

# Cuis Smalltalk

Here is the truth about Cuis: **it is Smalltalk stripped back to something one person can understand completely – a personal computing environment that still fits in a single mind.** If Pharo is a bustling city, Cuis is a well-kept village with excellent roads.

### What it is, in plain words

**Cuis Smalltalk** (often just **Cuis**) is a free Smalltalk-80 descendant maintained by Juan Vuletich and contributors, focused on:

- a **small, clean image** you can read;
- excellent vector graphics (VectorEngine);
- faithfulness to classic Smalltalk ideas without decades of accretion;
- running on OpenSmalltalk / CuisVM across platforms.

You live inside the image: browser, workspace, transcript, debugger – the classic Smalltalk tools. Packages extend it without turning the core into a jungle.

### Why it matters

Most modern environments bury you under abstractions you can't finish reading. Cuis is a bet that a comprehensible personal system still matters – the same bet I recognise in PicoLisp and Void. Studying Cuis teaches OOP as message passing, not as a keyword museum, and it is pleasant.

### An everyday analogy: a hand-built bicycle

Pharo is an e-bike with a app store. Cuis is a steel-frame road bike you can strip and rebuild on the kitchen table. Slower to acquire gadgets; faster to understand every click.

### A hands-on example

Download the image and VM from the Cuis site, start it, and in a Workspace evaluate:

```smalltalk
3 + 4 * 2.                         "14 – left to right"
(1 to: 10) sum.                    "55"
Morph new openInWorld.             "a rectangle you can drag"

Object subclass: #Counter
  instanceVariableNames: 'count'
  classVariableNames: ''
  poolDictionaries: ''
  category: 'Demo'.

Counter compile: 'initialize
  count := 0'.
Counter compile: 'inc
  count := count + 1'.
Counter compile: 'count
  ^ count'.

c := Counter new inc inc.
c count.                           "2"
```

Browse the class with the Browser, set a breakpoint, and enjoy a debugger that *is* the environment. Compare with [GNU Smalltalk](gnusmalltalk.md) (file-oriented) and [Pharo](pharo.md) (larger ecosystem).

### Common misconceptions

- **"Smaller means abandoned."** Cuis is actively maintained with a clear philosophy.
- **"You can't ship apps."** People do; the path is different from `npm init`.
- **"It's only for nostalgia."** Message-passing OOP remains a sharp tool.
- **"Cuis and Pharo packages are interchangeable."** Ecosystems differ; ideas transfer.

### Living in the image

Save often. Use commits of the image or FileOut packages when you experiment. The debugger is not a failure state – it is the normal way to understand a running object. If you come from file-oriented languages, schedule a week to unlearn "edit-compile-restart" and learn "change-the-object-while-it-runs". That week is the whole point of Smalltalk.

### Getting Cuis running on Vikix

Cuis is distributed as a Git repository containing the image, the sources and a script to fetch the right OpenSmalltalk VM:

```bash
git clone --depth 1 https://github.com/Cuis-Smalltalk/Cuis-Smalltalk-Dev.git cuis
cd cuis
./RunCuisOnLinux.sh            # downloads the VM on first run, then starts the image
```

The image opens as one X window, which StumpWM treats like any other application; giving it its own group (virtual desktop) works well, since you will live inside it for a while. Packages are loaded from `.pck.st` files in the repository with `Feature require: #PackageName`, for example `Feature require: #'VectorGraphics'` for the newer anti-aliased graphics.

### How Cuis differs from Pharo and Squeak

All three descend from the same Squeak image of the late 1990s:

| | Cuis | Pharo | Squeak |
|---|---|---|---|
| Goal | small and understandable | modern industrial platform | the classic, education and research |
| Size | a few thousand classes | many more | in between |
| Source in Git | text files (`.pck.st`) | Iceberg / Tonel format | Monticello |
| Style | stability, careful pruning | fast-moving, many tools | conservative |

If you want to *understand* a whole Smalltalk system, Cuis is the one. If you want many libraries and a large community, Pharo is. The language is nearly the same, so moving between them is easy; see the [Cuis Terse Guide](cuisterseguide.md) for the syntax.

### A tiny class, from start to finish

In a System Browser, create a category `Vikid`, then define:

```smalltalk
Object subclass: #Counter
    instanceVariableNames: 'count'
    classVariableNames: ''
    poolDictionaries: ''
    category: 'Vikid'

Counter >> increment
    count := (count ifNil: [0]) + 1.
    ^ count
```

Then in a Workspace, `c := Counter new. c increment; increment. c increment` prints **3**. Change `increment` to add 10, accept with Ctrl-S, and the *same* `c` object immediately behaves the new way. No restart, no recompiling: that live change is what people mean when they say Smalltalk is a living system. Compare PicoLisp's `(class +Counter)` and [new](plnew.md), which give you the same message-passing style in a Lisp.

### Connections

- [Pharo](pharo.md), [Learn Pharo](learnpharo.md), [GNU Smalltalk](gnusmalltalk.md).
- [Objects and Messages](objectsandmessagespharo.md), [JavaScript Objects](jsobjects.md).

[Terse Guide](cuisterseguide.md)

#### External Links

- [Get Cuis](https://github.com/Cuis-Smalltalk/Cuis-Smalltalk-Dev)
- [https://github.com/Cuis-Smalltalk/Learning-Cuis](https://github.com/Cuis-Smalltalk/Learning-Cuis)
- [https://github.com/Cuis-Smalltalk/Learning-Cuis/blob/master/LayoutTour.md](https://github.com/Cuis-Smalltalk/Learning-Cuis/blob/master/LayoutTour.md)
- [The Cuis Book](https://cuis-smalltalk.github.io/TheCuisBook/index.html)
- [The Cuis Book - Github](https://github.com/Cuis-Smalltalk/TheCuisBook)

#### Videos

- [Cuis on YouTube](https://www.youtube.com/playlist?list=PLbevs6Mp0MMMaR5gSYzJQXQ56OplFSCJk)
- [Build a simple but realistic Class into your own Package](https://youtu.be/u31DaOEqiG0)
- [Playlist with many tutorials](https://www.youtube.com/playlist?list=PLu8vLCSA-4hklsvT9W6ruintbdx_K0DYW)

## Historical

- [Dan Ingalls - Object Oriented Programming](https://www.youtube.com/watch?v=P2mh92d-T3Y)
