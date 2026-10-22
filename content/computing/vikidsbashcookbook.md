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
