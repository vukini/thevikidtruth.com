---
title: systemd
date: '2022-08-28T11:55:25+04:00'
lastmod: '2022-08-28T12:00:12+04:00'
original_id: '{A1712}'
original_name: systemd
original_blob: blob/B/11/104.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: systemd
draft: false
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [pil sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) | [SimpleLinuxConfig](simplelinuxconfig.md) |
  [Tools and Software](linuxtoolsandsoftware.md)

# systemd

How to know if you are using systemd?

```
ps --no-headers -o comm 1
```

```
[[ -d /run/systemd/system ]] && echo "using systemd"

[ -d /run/systemd/system ] && echo "using systemd" || echo "NOT using systemd"
```

```
[[ `systemctl` =~ -\.mount ]] || { echo 'Systemd not found'; exit 1; }
```
