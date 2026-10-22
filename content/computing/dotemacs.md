---
title: Starting Emacs & the config file
date: '2016-11-22T04:55:06+04:00'
lastmod: '2016-11-22T22:45:27+04:00'
original_id: '{A323}'
original_name: dotemacs
original_blob: blob/B/1/647.txt
revisions: 21
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: dotemacs
draft: true
review: update
---

# Starting Emacs & the config file

[emacs](emacs.md) | [computing](computing.md)

## Launching Emacs

I actually start emacs as a daemon service when entering Linux. This requires a
little setup which is not all that difficult. I don't know which version or
distribution of linux you use. But the line that starts emacs as a daemon is this:

```
$ /usr/bin/emacs24 --daemon
```

You can add this line to "Startup Applications" in Ubuntu. Like so:

![startup-apps](/assets/startup-apps.png)
{.center}

![edit-startup](/assets/edit-startup.png)
{.center}

By doing this emacs is always running in the background.

I then call any emacs session with:

```
$ emacsclient -c
```

Which I setup in the "Main Menu" like this:

![mmenu](/assets/mmenu.png)
{.center}

![props](/assets/props.png)
{.center}

I usually also set to an alias on my system for easy access, like this:

```
alias em='emacsclient -c'
```

The very first lines of my .emacs also contains the line:

```
(server-start)
```

Which ensures that emacs then sets itself as a server that can serve
the **emacsclient** requests.

This way I always have emacs running as a server, **the same instance running
wherever and whenever I need it.**

## Startup Procedure

When emacs starts up, it (usually) reads a configuration file called **.emacs**.

Emacs users use this file to fine tune their emacs configuration and load various
applications, modules, and utility functions.

It has become quite a fashion for people to share these config files on sites like
github and bitbucket. Anyone can the download the **.emacs** files of another user
to incorporate useful code into their own configurations.

I have decided to go another way. What I will attempt to do here is describe my
current strategies.

## Creating your .emacs

I actually keep most of my configuration in an org-mode file called
[init.org](initorg.md) and it
is this file that is loaded at the end of my .emacs.

With the lines:

```
(require 'org)                                ;load org-mode
(require 'ob-tangle)                          ;allow literate programming tangling
(require 'cl)                                 ;allow common-lisp style functions
(org-babel-load-file "~/.emacs.d/init.org")   ;load the init file with source code
```

To continue please visit [init.org](initorg.md).

## Sources

- [orgmode.org babel intro](http://orgmode.org/worg/org-contrib/babel/intro.html)
- [noweb literate programming](http://www.cs.tufts.edu/~nr/noweb/)
