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

### The plain idea

An application-proxy firewall (an *application-level gateway*) works at layer 7, the layer where protocols like HTTP, SMTP and DNS live. It never lets your machine talk directly to the outside. Instead, as my diagram shows, the user's request goes to the proxy, and the proxy opens a brand-new connection to the destination on the user's behalf. Because it fully understands the protocol, it can read and filter the actual content: block certain URLs, strip dangerous attachments, refuse malformed requests, and log exactly who fetched what.

The catch, already in my old note, is encryption. Today well over 90% of web traffic is HTTPS, so a proxy only sees inside if it performs *TLS inspection*: it decrypts, checks and re-encrypts, using a certificate the organisation's computers have been told to trust.

### Why it matters

Lower-level firewalls see addresses and ports. Attackers long ago moved to ports everyone must allow: 80, 443, 25. Only something that understands the application can tell a normal web request from SQL injection in a form field, or a real email from one carrying a malicious macro. Application-layer filtering is the ancestor of today's web application firewalls (WAFs), secure web gateways and the content-inspection features in [next-generation firewalls](ngfirewall.md).

### An everyday analogy: the personal assistant

You don't phone suppliers yourself; you ask your assistant to do it. She places the call, listens to the whole conversation, refuses to pass on anything inappropriate, and relays only what you need. The supplier never learns your direct number. Thorough, but slower than calling yourself, and she has to speak each supplier's language.

### A worked example: a filtering web proxy

A common open-source application proxy is Squid. A minimal rule set:

```
acl office src 10.0.0.0/24
acl blocked dstdomain .example-malware.test .gambling.test
http_access deny blocked
http_access allow office
http_access deny all
```

Office machines are configured (or forced by the network) to use the proxy. A request for `http://news.example/` arrives at Squid, Squid checks the rules, fetches the page itself, and hands it back. A request for `.gambling.test` gets an error page. The access log records the user, the URL and the time. For HTTPS, plain Squid sees only the domain name (from the CONNECT request or the TLS SNI field) unless you configure TLS inspection ("SSL bump").

On the server side, the reverse idea, a WAF such as ModSecurity with the OWASP Core Rule Set in front of a web app, inspects incoming requests and blocks common attacks such as cross-site scripting and SQL injection.

### Common misconceptions

- **"It sees everything."** Not without TLS inspection, which has privacy, legal and certificate-management costs, and breaks apps that use certificate pinning.
- **"One proxy handles all protocols."** Each protocol needs its own proxy logic. Unknown protocols are typically blocked or passed through blind.
- **"It's the fastest option."** Terminating and re-creating every connection costs CPU and latency. That is the trade for depth.

### How it connects

Compare the [circuit-level gateway](circuitlevelfirewall.md), which checks the handshake only, and [next-generation firewalls](ngfirewall.md), which combine all layers. See [Securing Web Apps](securingwebapps.md) for WAFs and [Firewalls](firewalls.md) for the overview.

The truth revealed: the closer a firewall gets to the application, the more it understands, and the more work it has to do.

## Types of Firewalls

- [PacketFilteringFireWall](packetfilteringfirewall.md)
- [StatelessFirewall](statelessfirewall.md)
- [StatefullFirewall](statefullfirewall.md)
- [Circuit-Level-Firewall](circuitlevelfirewall.md)
- [Application-Proxy](applicationproxy.md)
- [Next-Generation Firewalls](ngfirewall.md)

## Tools

The Uncomplicated Firewall (ufw) is a friendly front end for the Linux kernel firewall (netfilter; nftables underneath on current distributions) and is particularly well suited for host-based firewalls.

- [Application Firewall @ Wikipedia](https://en.wikipedia.org/wiki/Application_firewall)
