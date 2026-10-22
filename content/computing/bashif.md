---
title: Bash - if statements
date: '2022-08-29T00:28:43+04:00'
lastmod: '2023-05-22T22:42:14+04:00'
original_id: '{A1715}'
original_name: bashif
original_blob: blob/B/12/325.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: bashif
draft: false
topics:
- linux
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md) | [Networking](networking.md) | [Machine Learning](machinelearning.md) |
  [Git](git.md) |
  [Machine Learning](machinelearning.md) |
  [Algorithms](algorithms.md) |
  [Open Data Science](opendatascience.md) | [Vikid's Bash Cookbook](vikidsbashcookbook.md) |

# Bash - if statements

Here is the truth about `if` in Bash: **it does not test conditions. It runs a command and looks at whether that command succeeded.** `[` is just a command (with a funny name) that succeeds or fails. Once you see that, every strange-looking Bash `if` makes sense.

### What it is, in plain words

The syntax is:

```bash
if COMMANDS; then
  ...
elif COMMANDS; then
  ...
else
  ...
fi
```

Bash runs the `COMMANDS` after `if`. If the last one exits with status **0** (success), the `then` branch runs. Any other status (1 to 255) means failure, and Bash moves on to `elif` or `else`. Note the shell's convention is the reverse of C: **0 is true**.

Three kinds of commands are commonly used as tests:

1. **`[ ... ]`**, also called `test`: the portable POSIX test command. Spaces around the brackets are required because `[` is a command name and `]` is its last argument.
2. **`[[ ... ]]`**: a Bash keyword with safer rules. No word splitting inside, so quoting matters less; supports `&&`, `||`, pattern matching with `==` and regexes with `=~`.
3. **`(( ... ))`**: arithmetic. Succeeds if the expression is non-zero: `(( count > 10 ))`.

And any ordinary command works: `if grep -q root /etc/passwd; then ...`.

### Why it matters

Shell scripts are mostly decisions: does this file exist, did the download work, is this the right user. Getting `if` wrong produces scripts that silently take the wrong branch, which is worse than a crash. And knowing that `if` checks exit status lets you write tests directly against real commands instead of capturing output and comparing strings.

### An everyday analogy: a bouncer with a phone

The bouncer (`if`) does not judge anyone himself. He phones a checker (the command), who answers only "yes" (0) or "no" (anything else). The bouncer lets you in or sends you to the next door (`elif`) based on that one answer. `[` is just the checker who knows how to compare numbers and look at files.

### A hands-on example

```bash
#!/usr/bin/env bash
# backup-check.sh  - decisions four ways
set -u

file=${1:-$HOME/notes.org}

# 1. Test a file with [[ ]]
if [[ ! -f $file ]]; then
  echo "No such file: $file" >&2
  exit 1
fi

# 2. Test a command's success directly
if ping -c1 -W2 backup.local &>/dev/null; then
  echo "Backup host is up"
else
  echo "Backup host unreachable, will retry later"
fi

# 3. Arithmetic with (( ))
size=$(stat -c %s -- "$file")
if (( size > 1024 * 1024 )); then
  echo "$file is over 1 MiB"
fi

# 4. Patterns and regexes with [[ ]]
if [[ $file == *.org ]]; then
  echo "An Org file"
elif [[ $file =~ \.(md|markdown)$ ]]; then
  echo "Markdown: extension ${BASH_REMATCH[1]}"
fi

# Short form for a single action
[[ -w $file ]] || echo "Warning: $file is read-only"
```

Check the exit status of anything yourself with `echo $?` straight after it runs.

### Common misconceptions

- **"`[$# -ne 1]` is fine."** The example lower down this page has exactly this bug. Without spaces, Bash looks for a command literally named `[1` (or similar) and fails. It must be `[ $# -ne 1 ]`.
- **"`=` and `-eq` are the same."** `=` compares *strings*, `-eq` compares *integers*. `[ 010 = 10 ]` is false, `[ 010 -eq 10 ]` is true.
- **"Quoting doesn't matter in `[ ]`."** If `$AGE` is empty, `[ $AGE -lt 13 ]` becomes `[ -lt 13 ]`, a syntax error. Quote (`"$AGE"`) or use `[[ ]]`.
- **"`[[ ]]` works everywhere."** It is Bash (and zsh, ksh). In `#!/bin/sh` scripts, which on Void and Debian run `dash`, use `[ ]`.
- **"`$(whoami) = 'root'` is the way to check for root."** Comparing `$EUID` (or `"$(id -u)"`) with `0` is faster and does not depend on the account's name.

### Connections

- [Bash case statements](bashcase.md), [Using Variables in Bash](bashvariables.md), [Reserved Words](bashreservewords.md), [Vikid's Bash Cookbook](vikidsbashcookbook.md).
- [C Syntax](csytanx.md) and [JavaScript Control Flow](jscontrolflow.md) – where `if` tests values, not commands.
- [Linux Tools](linuxtools.md), [awk](awk.md).

## Examples


```
if [ condition ]; then # you can use [[ ]] also
  your code
fi
```

```
if [[ "${UID}" -eq 0 ]]
then
  echo 'You are root'
else
  echo 'You are not root'
fi
```

```
#!/bin/bash

if [ $(whoami) = 'root' ]; then
	echo "You are root"
fi
```

In one line:

```
if [ $(whoami) = 'root' ]; then echo "root"; else echo "not root"; fi
```

```
#!/bin/bash

if [ $(whoami) = 'root' ]; then
	echo "You are root"
else
	echo "You are not root"
fi
```

```
#!/bin/bash

AGE=$1

if [ $AGE -lt 13 ]; then
	echo "You are a kid."
elif [ $AGE -lt 20 ]; then
	echo "You are a teenager."
elif [ $AGE -lt 65 ]; then
	echo "You are an adult."
else
	echo "You are an elder."
fi
```

```
#!/bin/bash
echo Script name: $0
echo $# arguments
if [$# -ne 1];
    then echo "illegal number of parameters"
fi
```

```
$a -lt $b	        $a < $b
$a -gt $b	        $a > $b
$a -le $b	        $a <= $b
$a -ge $b	        $a >= $b
$a -eq $b	        $a is equal to $b
$a -ne $b	        $a is not equal to $b
-e $FILE	        $FILE exists
-d $FILE	        $FILE exists and is a directory.
-f $FILE	        $FILE exists and is a regular file.
-L $FILE	        $FILE exists and is a soft link.
$STRING1 = $STRING2	$STRING1 is equal to $STRING2
$STRING1 != $STRING2	$STRING1 is not equal to $STRING2
-z $STRING1	        $STRING1 is empty
```
