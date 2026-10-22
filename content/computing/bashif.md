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
