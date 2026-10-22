---
title: Statefull Firewalls
date: '2016-12-01T00:26:47+04:00'
lastmod: '2016-12-01T00:45:23+04:00'
original_id: '{A561}'
original_name: statefullfirewall
original_blob: blob/B/3/437.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: statefullfirewall
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

# Statefull Firewalls

Tracks of Session & updates the Rule Dynamically

```
          Firewall
          Statefull
  Public |         | Private
         |         |
    FB   |         |  MI
 1.1.1.1 |         | x.x.x.x
         |         |
         |         |

 Dicretion  From   To        Action
 ==================================
 Egress     any    any        Allow
 Ingress  1.1.1.1  2.2.2.2    Allow
 Ingress  3.3.3.3  Any        Allow
 Implicit Deny
```

## Types of Firewalls

- [PacketFilteringFireWall](packetfilteringfirewall.md)
- [StatelessFirewall](statelessfirewall.md)
- [StatefullFirewall](statefullfirewall.md)
- [Circuit-Level-Firewall](circuitlevelfirewall.md)
- [Application-Proxy](applicationproxy.md)
- [Next-Generation Firewalls](ngfirewall.md)
