---
title: Vikid's Bash Cookbook
date: '2017-06-29T06:21:51+04:00'
lastmod: '2023-04-04T22:31:37+04:00'
original_id: '{A1177}'
original_name: vikidsbashcookbook
original_blob: blob/B/11/761.txt
revisions: 12
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: vikidsbashcookbook
draft: false
topics:
- linux
---

[BASH](bash.md)  |   [Bash Cookbook](vikidsbashcookbook.md)  |

# [Vikid's Bash Cookbook](vikidsbashcookbook.md)

Here is the truth about the shell: **most of what people call "Linux skills" is really a dozen shell habits, repeated until they are automatic.** This cookbook is where I keep the recipes I actually reach for, with the reasons behind them, so they make sense rather than just work.

### What it is, in plain words

Bash (the "Bourne Again SHell", by Brian Fox for the GNU project in 1989) is both an interactive command line and a programming language. Bash 5.3 is the current version in 2026. When you type a line, Bash:

1. splits it into words, honouring quotes;
2. expands variables (`$USER`), command substitutions (`$(date)`), arithmetic (`$((1+2))`), braces (`{a,b}`) and globs (`*.md`);
3. sets up redirections (`>`, `<`, `|`);
4. finds the command (alias, function, builtin, or a program on `$PATH`) and runs it.

Nearly every shell surprise is one of those four steps doing something you did not expect. The recipes below are grouped so that each one exercises one of them.

### Why it matters

- **Glue.** The shell joins small programs into big results: `find`, `grep`, `sort`, `awk`, `xargs`. That is the Unix philosophy in practice.
- **Automation.** Anything you type twice can become a script, then a cron job or a runit service.
- **Portability of knowledge.** Bash is on nearly every Linux box, in WSL, in macOS (as an option; zsh is the default there), and inside most containers.

### An everyday analogy: a kitchen with good knives

You do not need a gadget for every job if you have three good knives and know how to use them. `grep`, `sed`, `awk`, `find`, `xargs` and pipes are the knives. Recipes are just the ways cooks combine them.

### A hands-on example: recipes I use weekly

```bash
# Which shell am I in, and which bash?
echo "$0"; bash --version | head -1

# What is this command, really? (alias, function, builtin or file)
type -a ls

# Find big files under the current directory
find . -type f -size +100M -exec ls -lh {} + 2>/dev/null

# Search code, skipping .git, then count matches per file
grep -rIn --exclude-dir=.git 'TODO' . | cut -d: -f1 | sort | uniq -c | sort -rn

# Rename *.jpeg to *.jpg safely (parameter expansion, no external tools)
for f in *.jpeg; do [ -e "$f" ] && mv -n -- "$f" "${f%.jpeg}.jpg"; done

# Run something on every file, NUL-separated so spaces in names are safe
find . -name '*.md' -print0 | xargs -0 wc -w | tail -1

# Repeat the last command with sudo
sudo !!

# Quick backup with a date stamp
cp -a notes.org "notes.org.$(date +%F)"
```

The quoting examples further down are the most important on the page. The rule: **double-quote every variable expansion unless you have a reason not to.** `"$f"` survives a file called `my notes.txt`; `$f` becomes two words.

A safe script header I start everything with:

```bash
#!/usr/bin/env bash
set -euo pipefail          # stop on errors, unset vars, and failed pipes
IFS=$'\n\t'                # split only on newlines and tabs
```

Run `shellcheck script.sh` (`xbps-install -S shellcheck` on Vikix) before trusting a script. It catches most quoting mistakes for you.

### Common misconceptions

- **"`ls` is the way to list files in a script."** Parsing `ls` output breaks on unusual names. Use globs (`for f in *`) or `find -print0`.
- **"Single and double quotes are the same."** Single quotes are literal; double quotes still expand `$var`, `$(cmd)` and backslashes. See the quoting recipe below.
- **"`which` tells you what will run."** `type` is the shell's own answer and also knows about aliases, functions and builtins.
- **"Bash and sh are the same."** On Void and Debian `/bin/sh` is `dash`, a much smaller POSIX shell. Arrays, `[[ ]]` and `${var//x/y}` are Bash-only, so use `#!/usr/bin/env bash` when you need them.
- **"The interactive check below works."** It needs `;;` at the end of each `case` branch to be valid. See [Bash case statements](bashcase.md).

### Connections

- [Using Variables in Bash](bashvariables.md), [Bash if statements](bashif.md), [Bash case statements](bashcase.md), [Reserved Words](bashreservewords.md).
- [awk](awk.md), [Linux Tools](linuxtools.md), [ncdu](ncdu.md), [Linux Introspection](linuxinstrospection.md).
- [vim](vim.md), [Emacs Notes](emacsnotes.md), [Git](git.md).

## The recipes


#### Some Simple Stuff

```
bash --version

ls -adFlLQrRS1

pwd -L, pwd -P

type which, type -a which

apropos zip => man -k, locate which

find

stat, file -b

chsh -s /bin/bash

passwd -el

sudo cat /etc/shells
```

#### Common Shell Variables

```
$USER
$-             list all current option flags
```

#### Download a website

```
wget -r -np -k http://somesite.com
```

Options:

- -r (recursive)
- -np (don't follow links to parent directories)
- -k to make links in downloaded HTML or CSS point to local files
- -nd (no directories): download all files to the current directory
- -e robots.off: ignore robots.txt files, don't download robots.txt files
- -A png,jpg: accept only files with the extensions png or jpg
- -m (mirror): -r --timestamping --level inf --no-remove-listing
- -nc, --no-clobber: Skip download if files exist

#### Quoting

```
echo value is $3?!
echo "value is $3?!"
echo 'value is $3?!'
```

`!" is history substitution`

## Sources and Links

- [download a website](https://apple.stackexchange.com/questions/100570/getting-files-all-at-once-from-a-web-page-using-curl)
- [wget-command-examples](https://www.hostinger.com/tutorials/wget-command-examples/#Using_Wget_Command_to_Download_Single_Files)

#### Builtin Commands

```
ls () {
    builtin ls "@"
    echo "using defined ls"
}
```

#### Interactive

```
#!/usr/bin/env bash

case "$-" in
   *i*)
      echo "interative"
   *)
      echo "not interactive"
esac
```
