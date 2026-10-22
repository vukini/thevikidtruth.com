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

### The plain idea

A stateless firewall judges every packet on its own, with no memory of what came before. Each packet is compared with the rule table (source, destination, protocol, port) and allowed or dropped. It does not know whether a packet is the start of a new conversation, a reply to something you asked for, or a stray fragment pretending to be either.

My table above shows the consequence. To let a server at 2.2.2.2 receive replies from 1.1.1.1, a stateless firewall needs an explicit *ingress* rule for that traffic, because it cannot work out for itself that the packets are answers to outgoing requests. Everything not listed falls to the implicit deny at the bottom.

### Why it matters

Statelessness is simple and very fast: no connection table to fill, no memory per flow. That is why stateless filtering still appears in the places where speed and scale matter most: router access-control lists, the first line of DDoS scrubbing, and cloud features such as AWS network ACLs (which are stateless, unlike AWS security groups, which are stateful). Understanding the difference saves you hours of puzzling over why replies vanish.

### An everyday analogy: the forgetful doorman

Imagine a doorman with no memory. You step out to fetch something from your car, and when you come back he asks for your ID as if he has never seen you. Worse, if the rules say "nobody enters from the car park", he will not let you back in at all. You have to give him a written rule for every way anyone might legitimately come back.

### A worked example: replies to web browsing

Your laptop at 192.168.1.10 visits a website. The request leaves from a random high port, say 51514, to port 443. The reply comes back *from* port 443 *to* port 51514. With a stateless firewall you must write something like:

```
allow out  tcp 192.168.1.10:any   -> any:443
allow in   tcp any:443            -> 192.168.1.10:1024-65535
```

That second rule is the problem: it lets *anyone* who sends packets from source port 443 reach any of your high ports. Older stateless setups tried to tighten this by matching the TCP ACK flag ("only let in packets that claim to be part of an existing conversation"), which attackers defeated by simply setting the flag on crafted packets: the "ACK attacks" mentioned on the [circuit-level gateway](circuitlevelfirewall.md) page.

### Common misconceptions

- **"Stateless means insecure."** It means limited. As a coarse first filter in front of stateful defences it is perfectly sound.
- **"Home routers are stateless."** Almost every consumer router and operating system firewall is stateful today.
- **"UDP has no state, so it doesn't matter."** Stateful firewalls track UDP "pseudo-connections" by address and port pairs with timeouts; stateless ones cannot.

### How it connects

Read [Packet Filtering](packetfilteringfirewall.md) for the rule mechanics and [Stateful Firewalls](statefullfirewall.md) for the fix to the reply problem. The overview lives at [Firewalls](firewalls.md).

The truth revealed: a firewall that cannot remember has to trust too much.

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
