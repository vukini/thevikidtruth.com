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

### The plain idea

A circuit-level gateway works at the session layer, between the network-level rules of a [packet filter](packetfilteringfirewall.md) and the content-reading of an [application proxy](applicationproxy.md). Its job is to check that a TCP connection is *legitimate as a connection*: that the three-way handshake (SYN, SYN-ACK, ACK) really happened, between the parties it claims, before any data is allowed to flow. Once the session is approved, the gateway simply relays bytes back and forth without looking at what they say.

In the classic design the gateway terminates the connection itself. Your machine connects to the gateway, the gateway opens a second connection to the destination, and it copies data between the two. The outside world only ever sees the gateway's address. The best-known example is the **SOCKS** proxy protocol (SOCKS5 is still widely used, including by SSH's `-D` dynamic forwarding and the Tor client).

### Why it matters

My note says it was designed to combat "ACK attacks". Old stateless filters let in any packet with the TCP ACK flag set, on the theory that such a packet must belong to an established connection. Attackers simply set the flag on crafted packets to slip past or to map the network (nmap's `-sA` ACK scan still uses the trick to discover filtering rules). A circuit-level gateway is not fooled, because it has seen, or itself performed, the handshake for every session it allows.

It also hides the internal network: because the gateway makes the outbound connection, internal addresses are never exposed.

### An everyday analogy: the switchboard operator

You ring the company switchboard and ask for Accounts. The operator checks who you are and whether Accounts takes calls, then connects you. Once the line is open she does not listen in; she only made sure the call was set up properly. Nobody outside learns the direct extension numbers.

### A worked example: a SOCKS gateway with SSH

```
ssh -D 1080 user@gateway.example.com
```

This opens a SOCKS5 proxy on your machine's port 1080, tunnelled to the gateway. Point a browser at `localhost:1080` as a SOCKS proxy and every new connection is set up by the gateway on your behalf. The destination sees `gateway.example.com`, not you. The gateway decides which destinations are allowed, but it does not inspect the pages themselves.

To see the attack it was built against, compare in a lab: `nmap -sA target` sends bare ACK packets. A stateless filter may answer with RST packets that reveal which ports are unfiltered; a gateway or stateful firewall silently drops them, because they belong to no session it knows.

### Common misconceptions

- **"It protects against malicious content."** No. Once the session is up, anything flows. A virus over an approved connection is still a virus.
- **"It's obsolete."** As a separate box it mostly is: [stateful firewalls](statefullfirewall.md) now do handshake tracking themselves. But the idea survives in SOCKS proxies, in SSH tunnels and in the session-validation features of modern firewalls.
- **"SOCKS encrypts traffic."** SOCKS itself does not. Encryption comes from what carries it (SSH) or what runs inside it (TLS).

### How it connects

Compare [Stateless](statelessfirewall.md) and [Stateful](statefullfirewall.md) firewalls, then [Application Proxies](applicationproxy.md) one layer up. The [OSI layers](networking.md) explain where each sits; [Firewalls](firewalls.md) has the overview.

The truth revealed: a circuit-level gateway checks the handshake, not the conversation.

## Types of Firewalls

- [PacketFilteringFireWall](packetfilteringfirewall.md)
- [StatelessFirewall](statelessfirewall.md)
- [StatefullFirewall](statefullfirewall.md)
- [Circuit-Level-Firewall](circuitlevelfirewall.md)
- [Application-Proxy](applicationproxy.md)
- [Next-Generation Firewalls](ngfirewall.md)

## Tools

The Uncomplicated Firewall (ufw) is a friendly front end for the Linux kernel firewall (netfilter; nftables underneath on current distributions) and is particularly well suited for host-based firewalls.

- [Colasoft Packet Builder](http://www.colasoft.com/packet_builder/)
