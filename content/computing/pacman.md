---
title: pacman
date: '2022-08-23T00:11:07+04:00'
lastmod: '2022-08-23T00:20:11+04:00'
original_id: '{A1703}'
original_name: pacman
original_blob: blob/B/11/015.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pacman
draft: false
---

[Read This!](caveatemptor.md) | | [Quick Links](quicklinks.md) | [Algorithms](algorithms.md) | [AssemblyLanguage](assemblylanguage.md) | [BASH](bash.md) |   [C-Programmming](cprogramming.md) |
[Computer Security](computersecurity.md) |  [Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) |
[Functional Programming](functional.md) |
[Firewalls](firewalls.md) |   [Git](git.md) | [Haskell](haskell.md) | [Javascipt](javascript.md) | [Julia](julia.md) | [Social Engineering](internetexploitation.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) |
[Linux](linux.md) |
[Python](python.md) |
[Operating Systems](os.md) |
[Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |  [Open Data Science](opendatascience.md) |
[Networking](networking.md) | [Machine Learning](machinelearning.md) | [Racket](racket.md) | [Scheme](scheme.md) |
[Unity](unity.md) | [vim](vim.md) |
[Web Development](webdevelopment.md) | [Windows WSL](windowswsl.md)

# pacman

```
pacman -Syu
```

S stands for sync,
y is for refresh (local cache),
u is for system update.

```
pacman -R package_name_ ;to remove a package
```

To remove a package and its dependencies which are not required by any other installed package:

```
pacman -Rs _package_name_
```

```
pacman -Qdtq | pacman -Rs -
```

Search Packages Locally

```
pacman -Q  boost-libs    #Display version
pacman -Ql boost-libs    #Display file list provided by local package
pacman -Qk boost-libs    #Check the local package database
pacman -Qo /path/to/file #Check if the file is owned by any package
```

Search For Package on Net

```
pacman -Ss package
```

To search for package file names in remote packages:

```
pacman -F _string1_ _string2_ ...
```

To view the dependency tree of a package:

```
pactree _package_naenter code hereme_
```

Clear the Cache:

```
paccache -r
```

To remove all the cached packages that are not currently installed, and the unused sync database, execute:

```
pacman -Sc
```

To remove all files from the cache, use the clean switch twice, this is the most aggressive approach and will leave nothing in the cache folder:

```
pacman -Scc
```

#### Sources

[Pacman-Command](https://itsfoss.com/pacman-command/)
