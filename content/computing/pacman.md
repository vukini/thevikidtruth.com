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
topics:
- linux
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

Here is the truth about package managers: **a package manager is a database of promises.** Every package promises which files it owns, which other packages it needs and which version it is. `pacman` is the tool that keeps those promises on [Arch Linux](archlinux.md), and once you understand the database, its odd-looking flags read like sentences.

### What it is, in plain words

`pacman` is Arch Linux's package manager (also used by Manjaro, EndeavourOS, CachyOS and MSYS2 on Windows). Version 7 is current in 2026. It does three things:

1. **Syncs** a local copy of the repository databases (`core`, `extra`, `multilib`) from a mirror.
2. **Installs, upgrades and removes** packages, resolving dependencies and checking GPG signatures.
3. **Queries** the local database: what is installed, which package owns a file, what is orphaned.

The flags are grouped by *operation*, which is always a capital letter:

| Operation | Means | Example |
|---|---|---|
| `-S` | Sync (with repos) | `pacman -S git` install |
| `-R` | Remove | `pacman -Rns git` remove with unneeded deps and config |
| `-Q` | Query local database | `pacman -Qi git` info |
| `-F` | Files database | `pacman -F bin/rg` which package provides a file |
| `-U` | Upgrade from a file | `pacman -U ./pkg.tar.zst` |

Lower-case letters modify the operation: `y` refresh, `u` upgrade, `s` search or recursive, `i` info, `l` list files, `o` owner, `d` dependencies, `t` unrequired, `q` quiet.

### Why it matters

- **Arch is a rolling release.** There are no big version jumps; you update often, so you need to understand updates.
- **Partial upgrades break things.** Running `pacman -Sy foo` (refresh the database but install one package without upgrading the rest) can install a package built against newer libraries than you have. Always `-Syu`.
- **The same ideas apply everywhere.** Void's `xbps`, Debian's `apt` and Alpine's `apk` all keep the same kind of database. Learn one well and the others are translation.

### An everyday analogy: a library catalogue

The repository is a library's central catalogue; your local database is the list of books on your own shelves. `-Sy` fetches the latest catalogue. `-Su` swaps every book on your shelf for its newest edition. `-Qo /usr/bin/ls` looks at a page and tells you which book it came from. And an orphan (`-Qdt`) is a book you only borrowed because another book referenced it, and you no longer have that other book.

### A hands-on example: a safe weekly routine

```bash
# 1. Read the news first: manual interventions are announced at archlinux.org/news
# 2. Full upgrade
sudo pacman -Syu

# 3. Merge any new config files pacman saved as .pacnew
sudo pacdiff                 # from pacman-contrib

# 4. Remove orphans (check the list before saying yes)
pacman -Qdtq
sudo pacman -Rns $(pacman -Qdtq)

# 5. Keep only the last 3 versions of each package in the cache
sudo paccache -rk3
```

Some everyday questions answered:

```bash
pacman -Qo $(command -v vim)   # which package owns this binary?
pacman -Ql picolisp | grep bin # what did this package install?
pacman -Qe                     # what did *I* install explicitly?
pacman -Si sbcl                # info from the repo, before installing
sudo pacman -F -y && pacman -F libssl.so.3   # who provides this library?
```

For software outside the official repos, the **AUR** (Arch User Repository) holds build scripts (`PKGBUILD`s). Read them before building, since anyone can upload. Helpers like `paru` or `yay` automate it.

**The Vikix equivalent.** On Void the same routine is `sudo xbps-install -Su` (upgrade), `xbps-query -o /usr/bin/vim` (owner), `xbps-query -f pkg` (files), `sudo xbps-remove -o` (orphans) and `sudo xbps-remove -O` (clean cache). Different spelling, same database of promises.

### Common misconceptions

- **"`-Sy` is a good way to install the latest version of one thing."** It is the classic partial-upgrade trap. Use `-Syu` then `-S`.
- **"`-Scc` frees space safely."** It deletes *all* cached packages, so you can no longer downgrade offline. `paccache -rk3` is gentler.
- **"The AUR is part of Arch."** It is community-maintained and unsupported. Treat every `PKGBUILD` as code from a stranger.
- **"Removing a package removes its dependencies."** Only with `-s`; add `-n` to remove saved config files too.

### Connections

- [Arch Linux](archlinux.md), [Linux Tools](linuxtools.md), [Simple Linux Configuration](simplelinuxconfig.md), [Ubuntu Common Tasks](ubuntucommontask.md).
- [systemd](systemd.md), [Linux Security](linuxsecurity.md), [Operating Systems](os.md).
- [Vikid's Bash Cookbook](vikidsbashcookbook.md) – shell habits that make all of this easier.

## Command notes


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
pactree _package_name_
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
