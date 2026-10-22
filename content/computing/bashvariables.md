---
title: Using Variables in Bash
date: '2023-05-22T21:53:51+04:00'
lastmod: '2023-05-22T21:57:20+04:00'
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
