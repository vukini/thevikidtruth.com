---
title: Reserve Words
date: '2023-05-22T22:02:13+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1774}'
original_name: bashreservewords
original_blob: blob/B/12/323.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: bashreservewords
draft: false
topics:
- linux
---

[BASH](bash.md)  |   [Bash Cookbook](vikidsbashcookbook.md)  |

# Reserve Words

Here is the truth about Bash reserved words: **they are not commands sitting somewhere in `/bin` – they are part of the language, recognised before anything is looked up.** You cannot name a function `if`, and `type if` will tell you why.

### What it is, in plain words

**Reserved words** (keywords) are tokens Bash treats specially when they appear where a command name would. The POSIX set plus Bash extensions includes:

```
!    case  coproc  do    done
elif else  esac    fi    for
function   if      in    select
then until while   {     }
time [[    ]]
```

They form the control-flow and compound-command syntax: `if … then … fi`, `for … do … done`, `case … esac`, `{ …;}`, `[[ … ]]`.

### Why it matters

Seeing `if` as syntax, not a program, explains a whole class of errors:

- `If` (capital I) is not `if` – the shell looks for a command named `If`.
- `alias if=…` does not do what you want.
- Putting `if` in a variable and expanding it does not recreate an `if` statement.

It also tells you what *not* to name your scripts and functions.

### An everyday analogy: words that hold the sentence together

In English, "the", "if", "and" aren't names of things – they structure the sentence. You can't nickname a friend "If" and expect grammar to ignore it. Reserved words are the grammar of Bash.

### A hands-on example

```bash
type if for [[ time
# if is a shell keyword
# for is a shell keyword
# [[ is a shell keyword
# time is a shell keyword

# These are *not* reserved – they are builtins or commands:
type cd echo test [
# cd is a shell builtin
# test is a shell builtin
# [ is a shell builtin
```

**Keywords vs builtins vs externals:**

| Kind | Found how | Examples |
|------|-----------|----------|
| Reserved word | parsed as syntax | `if`, `for`, `[[` |
| Builtin | implemented inside Bash | `cd`, `echo`, `read`, `test` |
| External | looked up on `PATH` | `/usr/bin/ls`, `git` |

```bash
# Compound commands – notice the keywords
if [[ -f /etc/os-release ]]; then
  while read -r line; do
    case "$line" in
      NAME=*) echo "${line#NAME=}" ;;
    esac
  done < /etc/os-release
fi

# { } groups commands in the current shell; ( ) in a subshell
{ echo a; echo b; } > /tmp/out
( cd /tmp && pwd )   # parent directory unchanged
```

`function` is optional Bash sugar; `name() { …; }` is portable. Prefer the portable form.

`!` as a reserved word negates a pipeline's exit status: `if ! grep -q foo file; then …`. (History expansion also uses `!`, which is a different mechanism – disable with `set +H` in scripts.)

### Word boundaries and when a keyword is a keyword

Reserved words are only special in command position. After an `=` or as an argument they are ordinary text:

```bash
echo if for while          # prints: if for while
alias_name=if              # fine – not command position
# if=foo                   # syntax error: 'if' is reserved here
```

This is why `type` and careful quoting matter when generating scripts, and why syntax highlighters colour these words differently – they really are a different kind of token.

### Common misconceptions

- **"`[` and `[[` are the same."** `[` is a builtin (alias of `test`); `[[` is a keyword with richer parsing and no word-splitting surprises.
- **"`time` is /usr/bin/time."** The keyword `time` times pipelines; the external has different flags. Use `command time` or `\time` to force the external.
- **"You can `export` a keyword."** No. Keywords aren't variables.
- **"`{}` needs no spaces."** `{ echo hi; }` needs a space after `{` and a semicolon (or newline) before `}`.
- **"Reserved words are Bash-only."** Most listed above are POSIX; `[[`, `function`, `coproc`, `select` are Bash/ksh extensions.

### Keywords at work: `time`, `!`, `coproc` and `select`

Four reserved words are rarely explained, and all four are worth knowing.

```bash
# time: a keyword, so it can time a whole pipeline, not just one program
time (find / -name '*.l' 2>/dev/null | wc -l)
TIMEFORMAT='%Rs real, %Us user'; time sleep 0.2

# !: negate the exit status of a pipeline
if ! grep -q vikix /etc/hostname; then echo "not on Vikix"; fi

# coproc: run a program in the background with a two-way pipe to it
coproc BC { bc -l; }
echo '4*a(1)' >&"${BC[1]}"       # send a line to bc
read -r pi <&"${BC[0]}"           # read its answer back
echo "pi is $pi"
kill "$BC_PID"

# select: an instant numbered menu
PS3='Window manager? '
select wm in stumpwm i3 quit; do
  case $wm in
    quit) break ;;
    *)    echo "You chose $wm"; break ;;
  esac
done
```

`coproc` is how you keep a long-running tool such as `bc`, `sqlite3` or even `pil` open and talk to it line by line, instead of starting it again for every question. It is the shell's version of a REPL connection.

### How to check any word

When you meet an unfamiliar word in a script, ask Bash what it is before you search the web:

```bash
type -t if        # keyword
type -t cd        # builtin
type -t ls        # alias (or file)
type -t greet     # function
compgen -k        # list every keyword this Bash knows
help time         # built-in help for keywords and builtins
```

`compgen -k` is the authoritative list for the Bash you are running, which matters as new versions occasionally add words. Bash 5.3 is current in 2026 and the list has been stable for years, but `compgen` never goes out of date.

### Connections

- [BASH](bash.md), [Bash if](bashif.md), [Bash case](bashcase.md), [Bash Variables](bashvariables.md).
- [Bash Cookbook](vikidsbashcookbook.md).

```
if	then	elif	else	fi	time

for	in	until	while	do	done

case	esac	coproc	select	function

{	}	[[	]]	!
```
