---
title: Packet Filtering Firewalls
date: '2016-12-01T00:18:10+04:00'
lastmod: '2016-12-01T00:44:44+04:00'
original_id: '{A557}'
original_name: packetfilteringfirewall
original_blob: blob/B/3/435.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: packetfilteringfirewall
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

# Packet Filtering Firewalls

Filters Traffic
works on layer 2-3

### The plain idea

A packet-filtering firewall looks at each packet's envelope, not the letter inside. For every packet it reads a few header fields, the source and destination IP address, the protocol (TCP, UDP, ICMP) and the port numbers, and compares them against an ordered list of rules. The first rule that matches decides: allow or drop. If nothing matches, the default policy applies, and on any sensible firewall that default is "deny".

Strictly speaking this works at layer 3 (IP addresses) and layer 4 (ports), with some filters also able to match layer-2 details such as MAC addresses. It is the oldest kind of firewall, dating from the late 1980s, and it is still built into every router, every cloud security group and the Linux kernel itself (netfilter, configured today with `nft`, or through friendlier front ends such as `ufw` and `firewalld`).

### Why it matters

Packet filtering is cheap and fast enough to run on every interface of every device. It cuts away most of the internet's noise before anything else has to think about it: if your server only offers SSH and HTTPS, there is no reason for a packet aimed at port 3389 to reach it at all. Every more sophisticated firewall type described on these pages still starts with this step.

### An everyday analogy: the gated estate

A guard at an estate gate checks the address on each delivery van: "Number 12? You're on the list. Number 40? No such house, turn around." He never opens the parcels. That makes him quick, and it also means a dangerous parcel addressed correctly sails straight through.

### A worked example: a home server with nftables

```
table inet filter {
  chain input {
    type filter hook input priority 0; policy drop;
    iif lo accept                         # local traffic
    ct state established,related accept   # replies to my own connections
    tcp dport { 22, 443 } accept          # SSH and HTTPS
    icmp type echo-request limit rate 5/second accept
  }
}
```

The same policy with ufw is three lines: `ufw default deny incoming`, `ufw allow 22/tcp`, `ufw allow 443/tcp`, then `ufw enable`. Read the rules from top to bottom: a packet to port 443 hits the third rule and is accepted; a packet to port 23 (telnet) matches nothing and falls to `policy drop`. Note the `ct state` line: strictly that is stateful filtering, covered on the [stateful firewall](statefullfirewall.md) page, and in practice every modern packet filter uses it.

### Common misconceptions

- **"Packet filters inspect content."** They do not. Malware delivered over an allowed port looks identical to legitimate traffic.
- **"Blocking by IP stops attackers."** Source addresses can be spoofed for one-way traffic, and attackers rent fresh addresses by the minute.
- **"iptables is how you do it."** iptables still works, but on current distributions it is usually a compatibility layer over nftables. New rules are better written in `nft` or a front end.
- **"Order doesn't matter."** It is first match wins. An early "allow all" makes every later rule pointless.

### How it connects

Packet filtering is the base layer. [Stateless](statelessfirewall.md) and [stateful](statefullfirewall.md) firewalls describe whether it remembers connections; [circuit-level gateways](circuitlevelfirewall.md), [application proxies](applicationproxy.md) and [next-generation firewalls](ngfirewall.md) climb higher up the [network stack](networking.md). See the overview at [Firewalls](firewalls.md).

The truth revealed: a packet filter is a bouncer who checks names on a list. Essential, but never the whole of security.

## Types of Firewalls

- [PacketFilteringFireWall](packetfilteringfirewall.md)
- [StatelessFirewall](statelessfirewall.md)
- [StatefullFirewall](statefullfirewall.md)
- [Circuit-Level-Firewall](circuitlevelfirewall.md)
- [Application-Proxy](applicationproxy.md)
- [Next-Generation Firewalls](ngfirewall.md)

## UFW

The Uncomplicated Firewall (ufw) is a friendly front end for the Linux kernel firewall (netfilter; nftables underneath on current distributions) and is particularly well suited for host-based firewalls.

- [Ubuntu Article](https://wiki.ubuntu.com/UncomplicatedFirewall)
- [DigitalOcean: How to set up a firewall with UFW](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu)
- [nftables wiki](https://wiki.nftables.org/)
