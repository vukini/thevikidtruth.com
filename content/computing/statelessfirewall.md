---
title: Stateless Firewalls
date: '2016-12-01T00:22:42+04:00'
lastmod: '2016-12-01T00:45:03+04:00'
original_id: '{A560}'
original_name: statelessfirewall
original_blob: blob/B/3/436.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: statelessfirewall
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

# Stateless Firewalls

```
          Firewall
          Stateless
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

## UFW

The Uncomplicated Firewall (ufw) is a frontend for iptables and is particularly well-suited for host-based firewalls.

- [Ubuntu Article](https://wiki.ubuntu.com/UncomplicatedFirewall)
    [ Dreamhost Article on UFW Firewall](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-14-04
  )
