---
title: Deploying a ZNC IRC Bouncing Server
date: '2016-12-12T22:27:04+04:00'
lastmod: '2016-12-12T22:27:04+04:00'
original_id: '{A1040}'
original_name: zncserver
original_blob: blob/B/5/227.txt
revisions: 1
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: zncserver
draft: false
topics:
- networking-web
---

# Deploying a ZNC IRC Bouncing Server

`Date 13 December 2016`

I have recently found myself of IRC more and more often. It is one of the most fun and effective places to be on the
internet if you are doing anything remotely challenging with technology. I've used several clients but found that
ERC in [Emacs](emacs.md) really fits my work flow the best.

The main problem I have found is that I am miss out on a lot of action as I can't keep my client logged in all the time.
I am very mobile and having a fixed machine connected to the IRC servers the whole time is not an option.

The solution seems to an IRC Bouncer. ZNC is the first one I am trying. I will let you know how it goes.

- [ZNC Main Page](http://wiki.znc.in/ZNC)
- [ZNC Installation](http://wiki.znc.in/Installation)
- [Signed SSL Certs](http://wiki.znc.in/Signed_SSL_certificate)

### The plain idea

IRC (Internet Relay Chat) is one of the oldest and still-liveliest text chat systems, but it has one quirk: if your client disconnects, you stop seeing messages, and anything said while you were away is simply gone. A **ZNC bouncer** solves this. It is a small program you run on an always-on server that stays connected to IRC for you around the clock. Your real client connects to ZNC instead of directly to IRC, and ZNC replays everything you missed. This page is my log of setting one up.

### Why it matters

As my note says, if you are mobile, phone, laptop, different machines, you cannot keep a client logged in all the time, so you miss conversations. A bouncer gives you a single, permanent presence on IRC, with full history, no matter which device you pick up. It is the difference between dropping in and out of a conversation and never missing a word.

### An everyday analogy

ZNC is an answering machine for a group phone call that never hangs up. The call (the IRC channel) runs continuously; ZNC sits on the line the whole time, recording everything, and when you rejoin from any phone it plays back what you missed and lets you carry on as if you were there all along.

### A 2026 note

ZNC is still actively maintained and remains the most popular IRC bouncer, though **The Lounge** (a self-hosted web IRC client with a built-in always-on backend) has become a popular modern alternative that needs no separate client. IRC itself is smaller than in its heyday, many communities moved to Slack, Discord or Matrix, but it is far from dead: large free-software projects use **Libera.Chat** (which replaced Freenode in 2021), and **IRCv3** extensions have modernised the protocol. One practical change since 2016: always set up TLS and SASL authentication, which are now standard. ERC in [Emacs](emacs.md) connecting through ZNC is still a lovely setup.

### How it connects

- [Emacs](emacs.md): ERC, the Emacs IRC client I use.
- [Linode](linode.md) and [Online VPS](onlinevps.md): where you run the always-on ZNC server.
- [Encryption](encryption.md): the SSL/TLS certificates the links below cover.

The truth revealed: the fix for missing out on a conversation you cannot always attend is not to try harder to be present, but to leave a faithful proxy connected in your place, which is all a bouncer really is.
