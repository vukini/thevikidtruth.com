---
title: Next-Generation Firewalls
date: '2016-12-01T00:47:46+04:00'
lastmod: '2016-12-01T00:47:46+04:00'
original_id: '{A564}'
original_name: ngfirewall
original_blob: blob/B/3/442.txt
revisions: 1
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: ngfirewall
draft: false
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

# Next-Generation Firewalls

Works a Layer 2 to 7 - Datalink to Application Layer

```
          Firewall
      Ng-Firewall
  Public |         | Private
         |         |
    FB   |         |  MI
 1.1.1.1 |         | x.x.x.x
         |         |
         |         |
```

### The plain idea

A next-generation firewall (NGFW) is all the earlier firewall types in one box, plus a few new tricks. It does [packet filtering](packetfilteringfirewall.md) and [stateful](statefullfirewall.md) tracking, but it also identifies *applications* rather than ports ("this is Zoom", "this is BitTorrent", even when both use port 443), ties traffic to *users* via the company directory, and runs an [intrusion prevention system](idsips.md) inline. Most add TLS inspection, URL filtering by category, malware sandboxing and threat-intelligence feeds that block known-bad addresses. The term was popularised around 2009, with Palo Alto Networks as the pioneer; Fortinet, Check Point, Cisco and others followed.

My note says layers 2 to 7, and that is the point: one policy engine looking at every layer at once.

### Why it matters

Port-based rules stopped meaning much once everything moved to HTTPS on port 443. An NGFW lets you write rules that match how people actually think about networks: "Marketing may use Salesforce and Slack; nobody may use personal file-sharing; engineers may SSH to production only from managed laptops." That is far closer to a real security policy than "allow TCP 443".

In 2026 the same functions increasingly live in the cloud as well as in boxes: *firewall as a service* and SASE/SSE platforms apply NGFW policy to remote workers wherever they are, part of the wider shift to zero-trust networking.

### An everyday analogy: airport security

An old firewall checks your boarding pass at the door. An NGFW is the whole airport security system: it checks your pass (addresses and ports), confirms you are who you say (user identity), scans your bag (content inspection), compares you against watch lists (threat intelligence), and knows the difference between a laptop and something that only looks like one (application identification).

### A worked example: one policy, many layers

A typical NGFW rule reads like a sentence rather than a list of numbers:

```
Rule: Allow-Sales-CRM
  Source zone:   Office      User group: Sales
  Destination:   Internet
  Application:   salesforce-base, salesforce-uploading
  Service:       application-default
  Security:      IPS profile "strict", anti-malware, URL filtering
  Action:        allow, log
Rule: Block-Unsanctioned-Sharing
  Application:   category file-sharing (except corporate-drive)
  Action:        deny, log
```

If someone in Sales opens Salesforce, the first rule matches and the traffic is scanned for exploits and malware on the way through. If they try to upload a file to a personal sharing service over the same port 443, application identification spots it and the second rule blocks it.

### Common misconceptions

- **"An NGFW makes other defences unnecessary."** It sees network traffic only. Endpoint protection, patching and backups still matter, and encrypted traffic you choose not to inspect stays opaque.
- **"Turning on every feature is free."** Each feature (TLS decryption, IPS, sandboxing) costs throughput. Vendors quote headline speeds with features off.
- **"Application ID is perfect."** It relies on signatures and behaviour, and new or evasive apps can be misidentified.
- **"NGFW and WAF are the same."** A WAF specialises in protecting your own web apps from incoming attacks; an NGFW governs general traffic.

### How it connects

It builds on every other firewall type on these pages; see [Application Proxies](applicationproxy.md), [IDS/IPS](idsips.md), [Secure Network Architecture](securenetworkarchitecture.md) and the overview at [Firewalls](firewalls.md).

The truth revealed: "next generation" is mostly about knowing *who* and *what*, not just *where*.

## Types of Firewalls

- [PacketFilteringFireWall](packetfilteringfirewall.md)
- [StatelessFirewall](statelessfirewall.md)
- [StatefullFirewall](statefullfirewall.md)
- [Circuit-Level-Firewall](circuitlevelfirewall.md)
- [Application-Proxy](applicationproxy.md)
- [Next-Generation Firewalls](ngfirewall.md)

## Tools

The Uncomplicated Firewall (ufw) is a friendly front end for the Linux kernel firewall (netfilter; nftables underneath on current distributions) and is particularly well suited for host-based firewalls.

- [NG-Firewalls @ Wikipedia](https://en.wikipedia.org/wiki/Next-Generation_Firewall)
