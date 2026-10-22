---
title: Using Variables in Bash
date: '2023-05-22T21:53:51+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1773}'
original_name: bashvariables
original_blob: blob/B/12/317.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: bashvariables
draft: false
---

[BASH](bash.md)  |   [Bash Cookbook](vikidsbashcookbook.md)  |

# Using Variables in Bash

Here is the truth about Bash variables: **they are all strings, and everything interesting is about when those strings get split, expanded or left alone.** Master expansion and the rest of the shell starts to behave.

### What it is, in plain words

A **variable** in Bash is a name bound to a string value (arrays are the structured exception). You assign with `=`, no spaces:

```bash
name=vikix
count=3
os="Void Linux"
```

You read with `$name` or, safer, `${name}`. Environment variables (`PATH`, `HOME`, `EDITOR`) are just variables marked for export to child processes.

```bash
echo "$name"
echo "${name}-box"
export EDITOR=nvim
```

### Why it matters

Almost every Bash bug is an expansion bug: a missing quote that splits a filename with spaces, an unquoted `$@` that mangles arguments, a `$var` that was empty and deleted a flag. Knowing the rules means writing scripts that survive real-world input.

### An everyday analogy: mail merge

A variable is a blank in a form letter. Expansion is printing the letter with the blank filled in. Quoting is putting the filled-in value in an envelope so the post office (the shell) doesn't tear it into separate words at every space.

```mermaid
flowchart LR
  A["\$name"] --> B[expand to value]
  B --> C{quoted?}
  C -- '"..."' --> D[one word]
  C -- unquoted --> E[split on IFS]
```

### A hands-on example

```bash
# Basics
greeting="hello"
echo "$greeting world"

# Default values
echo "${unset_var:-fallback}"      # use fallback if unset/empty
echo "${unset_var:=fallback}"      # also assign it
echo "${greeting:+set}"            # expand if set

# Substrings and lengths
file="archive.tar.gz"
echo "${#file}"                    # length: 14
echo "${file%.gz}"                 # archive.tar
echo "${file%%.*}"                 # archive
echo "${file#*.}"                  # tar.gz
echo "${file##*.}"                 # gz

# Arrays (Bash)
hosts=(vikix pi.local "nas box")
echo "${hosts[0]}"
echo "${hosts[@]}"                 # all elements, correctly quoted
echo "${#hosts[@]}"                # count

# Looping safely
for h in "${hosts[@]}"; do
  echo "host: $h"
done

# Environment vs shell
FOO=bar            # shell only
export FOO         # also children
env | grep '^FOO='
```

**The quoting rules that matter:**

| Form | Meaning |
|------|---------|
| `"$var"` | expand, keep as one word |
| `'$var'` | literal `$var`, no expand |
| `$var` | expand and **split** on IFS (usually space/tab/newline) |
| `"$@"` | all arguments, each separately quoted – **always use this** |
| `"$*"` | all arguments as one word |

```bash
# Dangerous
rm $file                 # if file="a b.txt", removes "a" and "b.txt"
# Safe
rm -- "$file"
```

Special variables: `$0` script name, `$1`…`$9` arguments, `$#` count, `$?` last exit status, `$$` PID, `$!` last background PID, `$_` last argument of previous command.

### Integer and readonly attributes

```bash
declare -i n=5          # integer attribute
n=n+2                   # arithmetic, still stored as string "7"
declare -r pi=3.14159   # readonly
# pi=2                  # error
declare -a nums=(1 2 3) # indexed array
declare -A map=([os]=void [wm]=stump)  # associative (Bash 4+)
echo "${map[os]}"
```

`local` inside a function makes a variable scoped to that call – use it by default so functions don't leak names into the global namespace.

```bash
greet() {
  local name=$1
  echo "hi $name"
}
```

### Export, env and child processes

A child process (another script, `python`, `git`) only sees variables that were exported. A common pattern for one-shot environment:

```bash
EDITOR=nvim crontab -e
env -i HOME="$HOME" PATH="/usr/bin:/bin" bash --noprofile --norc
```

The second starts a clean shell – useful for testing install scripts.

### Common misconceptions

- **"Spaces around `=` are fine."** `name = value` runs a command called `name`. Use `name=value`.
- **"All variables need `export`."** Only those children must see.
- **"`$@` and `$*` are the same."** Only when unquoted. Always `"$@"`.
- **"Arrays are portable."** They're Bash/ksh; POSIX `sh` doesn't have them.
- **"Integers are a type."** `declare -i` helps; arithmetic is still `$(( … ))`. Everything remains a string underneath.

### Connections

- [BASH](bash.md), [Bash if](bashif.md), [Bash case](bashcase.md), [Bash Cookbook](vikidsbashcookbook.md).
- [Bash Reserve Words](bashreservewords.md).
- [Linux Tools](linuxtools.md).

```
#!/bin/bash
echo "hello"
WORD='script'
echo "This is a $WORD"
echo "This ${WORD}ing a $WORD"
ENDING='ed'
echo "${WORD}$ENDING"
ENDING='s'
echo "${WORD}$ENDING"
ENDING='alicious'
echo "${WORD}$ENDING"

# Echo the exit status - notice 0 generally means success
echo ${?}

# User UID
echo ${UID}

# User name - notice the use of $() construct for a command substitution
# you could use `id -un` also

echo $(id -un)
```
