---
title: Bash
date: '2016-11-22T22:36:10+04:00'
lastmod: '2023-05-22T22:01:31+04:00'
original_id: '{A336}'
original_name: bash
original_blob: blob/B/12/321.txt
revisions: 20
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: bash
draft: false
topics:
- linux
---

[BASH](bash.md)  |   [Bash Cookbook](vikidsbashcookbook.md)  |

# Bash

You must know the basics of bash if you want to do anything useful in a Linux type environment.

- [Reserve Words](bashreservewords.md)
- [Using Variables](bashvariables.md)
- [Using if Statements in Bash](bashif.md)
- [Using case Statements in Bash](bashcase.md)

### The plain idea

Bash (the Bourne Again SHell) is the program that reads what you type at a Linux terminal and makes it happen. Type `ls` and Bash finds the `ls` program and runs it. Type `ls | wc -l` and Bash starts two programs and joins the output of the first to the input of the second. Put those same lines in a file and you have a script: a little program made out of other programs.

Bash dates from 1989 and is still the default interactive shell on most Linux distributions. The current series is Bash 5 (5.3 arrived in 2025). macOS switched its default to zsh in 2019, but Bash is still there, and on servers, containers and CI systems it is everywhere. Scripts often start with `#!/usr/bin/env bash` so they find it wherever it lives.

### Why it matters

Nearly every useful thing you do on a Linux machine passes through a shell: installing software, reading logs, moving files, deploying a site. Bash lets you glue small tools together instead of waiting for someone to write one big tool. Ten lines of Bash can replace an afternoon of clicking, and the same knowledge works on a Raspberry Pi, a cloud server and the [Windows WSL](windowswsl.md) terminal.

### An everyday analogy: a switchboard operator

Old telephone exchanges had an operator who took your request and plugged cables to connect you. Bash is that operator for programs. You say "take the output of this and send it to that, and write the result to a file", and it plugs the cables: pipes (`|`), redirections (`>`, `<`, `2>`), and background jobs (`&`).

### A worked example: which files are eating my disk?

```bash
#!/usr/bin/env bash
# biggest.sh - list the ten largest files under a directory
set -euo pipefail            # stop on errors and unset variables

dir="${1:-.}"                # first argument, or the current directory

if [[ ! -d "$dir" ]]; then
  echo "Not a directory: $dir" >&2
  exit 1
fi

find "$dir" -type f -printf '%s\t%p\n' 2>/dev/null \
  | sort -rn \
  | head -n 10 \
  | while IFS=$'\t' read -r size path; do
      printf '%8d KB  %s\n' "$((size / 1024))" "$path"
    done
```

Run it with `bash biggest.sh ~/Downloads`, or `chmod +x biggest.sh` then `./biggest.sh ~/Downloads`. What it shows:

- **Variables and defaults**: `${1:-.}` means "argument one, or `.` if none was given". See [Using Variables](bashvariables.md).
- **Tests**: `[[ ! -d "$dir" ]]` checks the path is not a directory. See [if statements](bashif.md).
- **Pipes**: `find` prints size and path, `sort -rn` sorts numerically largest first, `head` keeps ten.
- **Arithmetic**: `$((size / 1024))` does integer maths.
- **Quoting**: every `"$variable"` is quoted so file names with spaces do not break.
- **Safety**: `set -euo pipefail` makes the script stop at the first failure instead of ploughing on.

### Common misconceptions

- **"Bash and the terminal are the same thing."** The terminal is the window; Bash is the program running inside it. You can run zsh or fish in the same window.
- **"`sh` is Bash."** On Debian and Ubuntu, `/bin/sh` is dash, a smaller POSIX shell. Bash-only features such as `[[ ]]` and arrays fail there, so use `#!/usr/bin/env bash` when you rely on them.
- **"Quotes are optional."** Unquoted variables are split on spaces and expanded as wildcards. Quote by default; tools like ShellCheck will tell you where you forgot.
- **"Bash is fine for everything."** Past a hundred lines or so, or when you need real data structures, reach for [Python](python.md) or another language. Bash is the glue, not the whole building.

### How it connects

- [Linux](linux.md): the system Bash drives.
- [Regular Expressions](regularexpressions.md) and awk: the pattern tools you will pipe into constantly.
- [Bash Cookbook](vikidsbashcookbook.md): my own recipes.
- [Files and Directories](filesanddirectories.md): the commands you will run most.

The truth revealed: learning Bash is less about the shell than about learning to think in small tools joined together.

## Sources and Links

- [gnu:bash manual](https://www.gnu.org/software/bash/manual/bash.html)
- [linuxtrainingacademy](http://mirror.linuxtrainingacademy.com)
- [Excellent Free Tutorials to Learn Bash - LinuxLinks](https://www.linuxlinks.com/excellent-free-tutorials-learn-bash/)
- [bash-hackers wiki (archived mirror; the original site went offline in 2023)](https://bash-hackers.gabe565.com/)
- [a course by Ian D. Allen](http://teaching.idallen.com/cst8207/13w/notes/)
- [Bash Reference](https://tiswww.case.edu/php/chet/bash/bashref.html)
- [shell command language](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_10_02)
- [Shell Scripts (LCP) | Linux Training Academy](https://www.linuxtrainingacademy.com/shell-scripts/)
- [Unix Power Tools](https://docstore.mik.ua/orelly/unix/upt/index.htm)

- [ShellCheck - finds bugs in shell scripts](https://www.shellcheck.net/)
