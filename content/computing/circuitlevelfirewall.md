---
title: Circuit-Level-Gateway Firewalls
date: '2016-12-01T00:31:14+04:00'
lastmod: '2016-12-01T00:45:36+04:00'
original_id: '{A562}'
original_name: circuitlevelfirewall
original_blob: blob/B/3/440.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: circuitlevelfirewall
draft: true
review: update
topics:
- security
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

# Circuit-Level-Gateway Firewalls

Is designed to combat AckAttacks.

```
          Firewall
    Circuit-Level-Gateway
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

- [Colasoft Packet Builder](http://www.colasoft.com/packet_builder/)
