---
title: Dropbox Stuff
date: '2016-12-11T21:43:58+04:00'
lastmod: '2016-12-11T21:46:34+04:00'
original_id: '{A1034}'
original_name: dropbox
original_blob: blob/B/5/204.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: dropbox
draft: false
topics:
- networking-web
---

# Dropbox Stuff

I have been using Dropbox for a while - Here are a few links that will help you use this service more effectively.

[ dropbox Selective Sync from the terminal / command line](http://serverfault.com/questions/711101/how-can-i-include-folders-through-dropboxs-selective-sync-feature-in-linux-f
)
[ Install Dropbox in the terminal / command line @ dropbox wiki](http://www.dropboxwiki.com/tips-and-tricks/install-dropbox-in-an-entirely-text-based-linux-environment
)
[dropbox @ buidcontext](http://buildcontext.com/blog/2012/dropbox-linux-ubuntu-ec2-linode-selective-sync)
[ Install two or more Dropboxes Simultaneously on one Linux Box](http://askubuntu.com/questions/475419/how-to-link-and-use-two-or-more-dropbox-accounts-simultaneously
)

### The plain idea

Dropbox is a file-syncing service: a folder on your computer that is automatically mirrored to the cloud and to your other devices. This page collects links for the fiddly bits of running it on **Linux**, especially from the command line (selective sync, headless installs on a server, and running more than one account on one machine).

### Why it matters

Keeping files in sync across machines is one of those quiet conveniences that, once it works, you never think about again, until you need it on a headless Linux server or Linode with no desktop, where the usual point-and-click installer is no help. That is exactly the gap these command-line links fill.

### An everyday analogy

Dropbox is a magic drawer that appears, with the same contents, in every room of your house (every device). Change something in one drawer and it changes in all of them. The Linux command-line tricks here are for the rooms that have no hands to open the drawer, servers you reach only through a terminal.

### A 2026 note

Two things to know today. First, Dropbox has sharply limited its official Linux client over the years (for a time only certain filesystems were supported), so many people on Linux now prefer alternatives: **rclone** (which syncs to Dropbox and dozens of other clouds from the command line), **Nextcloud** (self-hosted, you own the server), or **Syncthing** (peer-to-peer, no cloud at all). Second, if you value the "computing freedom" theme elsewhere on this site, a self-hosted option like Nextcloud or Syncthing keeps your files on hardware you control. The links below still work for classic Dropbox-on-Linux setups.

### How it connects

- [Linux](linux.md) and [Bash](bash.md): where these command-line tips apply.
- [Linode](linode.md) and [seedbox](seedbox.md): the kind of headless servers this is useful on.
- [Computing Freedom](computingfreedom.md): the case for owning your own sync.

The truth revealed: file sync feels like magic until you meet a machine with no screen, and knowing the command-line side, or a self-hosted alternative, is what turns it from a consumer app into a tool you control.
