---
title: Application-Proxy Firewalls
date: '2016-12-01T00:41:58+04:00'
lastmod: '2016-12-01T00:45:48+04:00'
original_id: '{A563}'
original_name: applicationproxy
original_blob: blob/B/3/441.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: applicationproxy
draft: true
review: update
---

[Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) |
  [The Compiler](thecompiler.md) |
  [Identifiers](identifier.md) |
  [Literals](literals.md) |
  [storage_linkage](storagelinkage.md) |
  [Firewalls](firewalls.md)

# Application-Proxy Firewalls

Works a Layer 7 - Application Layer
Initiate a new connection on behalf of user and..
Fitler the packets also on the contents of the payload, unless encrypted

```
          Firewall
      Application-Proxy
  Public |         | Private
         |         |
    FB   |         |  MI
 1.1.1.1 |         | x.x.x.x
         |         |
         |         |
```

## Types of Firewalls

- [PacketFilteringFireWall](packetfilteringfirewall.md)
- [StatelessFirewall](statelessfirewall.md)
- [StatefullFirewall](statefullfirewall.md)
- [Circuit-Level-Firewall](circuitlevelfirewall.md)
- [Application-Proxy](applicationproxy.md)
- [Next-Generation Firewalls](ngfirewall.md)

## Tools

The Uncomplicated Firewall (ufw) is a frontend for iptables and is particularly well-suited for host-based firewalls.

- [Application Firewall @ Wikipedia](https://en.wikipedia.org/wiki/Application_firewall)
