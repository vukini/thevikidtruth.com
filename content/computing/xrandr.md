---
title: xrandr
date: '2022-09-06T12:14:39+04:00'
lastmod: '2023-05-22T21:26:00+04:00'
original_id: '{A1723}'
original_name: xrandr
original_blob: blob/B/12/304.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: xrandr
draft: false
---

# xrandr

# Find Connected Screen

```
xrandr -q | grep ' connected' | head -n 1 | cut -d ' ' -f1
```

## Changing Screen Brightness

```
xrandr --output SCREEN --brightness 0.6
```

for 60% brightness
[using xrandr and creating a small script](https://bbs.archlinux.org/viewtopic.php?id=134972)
[archwiki:Backlight](https://wiki.archlinux.org/title/Backlight)
