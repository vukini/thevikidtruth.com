---
title: Find Boxes in Lists
date: '2017-06-21T13:31:50+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1146}'
original_name: findboxes
original_blob: blob/B/5/703.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: findboxes
draft: false
topics:
- lisp
---

# Find Boxes in Lists

Here is the truth about finding boxes on a network: **most "discovery" is just asking politely which doors are open, then writing down who answers.** The skill is doing it thoroughly, quietly enough for the context, and only where you have permission.

### What it is, in plain words

**Finding boxes** means enumerating live hosts and interesting services on a network – the first phase of any lab, inventory or authorised [penetration test](penetrationtesting.md). Tools range from a single `ping` to full-fat scanners like nmap. On a home LAN it is how you remember which Pi has which IP; on an engagement it is how you build the map.

### Why it matters

You cannot secure or attack what you cannot see. Forgotten printers, default-password IoT and that old VM someone left running are how breaches begin. Regular discovery against *your own* networks is hygiene.

### An everyday analogy: knocking on doors with a clipboard

You walk a street with a clipboard. Knock (probe), note who answers and what they say through the door (banner/service). You do not kick doors in. Permission is the warrant that lets you walk that street at all.

### A hands-on example (your lab / home net only)

```bash
# Who answers ICMP on the LAN?
nmap -sn 192.168.1.0/24

# Common TCP ports on one host
nmap -sV -sC -p 22,80,443,8080 192.168.1.50

# Faster discovery of open ports, then detail
nmap -p- --min-rate 1000 -T4 192.168.1.50 -oG - | grep open
```

From Linux you already own: `ip neigh`, `arp -a`, checking the router's DHCP leases, and `avahi-browse -a` for mDNS. Document results – a living inventory beats a one-off scan.

### Common misconceptions

- **"Ping sweep finds everything."** Hosts may ignore ICMP. Try ARP on the LAN and TCP pings.
- **"nmap is only for hackers."** Admins use it constantly.
- **"Scanning is always legal."** On networks you don't own or have written leave for, it may not be. Ask.

### Connections

- [Enumeration](enumeration.md), [Penetration Testing](penetrationtesting.md), [nmap-related notes](linuxtools.md).
- [Networking](networking.md), [Raspberry Pi](rasberrypi.md).

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Picolisp By Example](picolispbyexample.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md) | [Networking](networking.md) | [Machine Learning](machinelearning.md) |
  [Git](git.md) |
  [Machine Learning](machinelearning.md) |
  [Algorithms](algorithms.md) |
  [Open Data Science](opendatascience.md) |

## Picking Boxes

### car, cdr & all that

### heads & tails

### nth
