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

### The plain idea

A stateful firewall remembers conversations. When a connection starts, for example your laptop opening a TCP connection to a web server, the firewall records it in a *state table*: who, to whom, which ports, which protocol, and what stage the conversation has reached. Packets that belong to a known connection are let through automatically; packets that claim to belong to a conversation that never started are dropped. That is what "updates the rule dynamically" means in my note above: you write the policy for who may *start* a conversation, and the firewall handles the replies.

The usual spelling is "stateful". Linux's netfilter does this with its connection tracker (`conntrack`), which labels packets as `new`, `established`, `related` or `invalid`.

### Why it matters

It closes the hole a [stateless firewall](statelessfirewall.md) leaves open. You no longer need broad rules letting in "anything from port 443"; the firewall knows which replies it is expecting. It also understands protocols that open extra connections (FTP's data channel, for instance) and marks them `related`. This is why stateful inspection, invented commercially by Check Point in the early 1990s, became the standard, and why every modern OS firewall, home router and cloud security group is stateful.

### An everyday analogy: the receptionist with a visitor log

A receptionist writes down everyone who leaves for a meeting and who they went to see. When someone comes back saying "I was with Room 4", she checks the log. If the entry is there, in you go. If someone turns up claiming to be returning from a meeting nobody logged, they are stopped.

### A worked example: the rule table above, made stateful

My table allows all *egress* (outbound) traffic and two ingress cases. With state tracking, the replies to any outbound connection need no rule at all. In nftables:

```
table inet filter {
  chain input {
    type filter hook input priority 0; policy drop;   # implicit deny
    ct state invalid drop
    ct state established,related accept               # replies, automatically
    ip saddr 1.1.1.1 ip daddr 2.2.2.2 accept          # ingress rule 1
    ip saddr 3.3.3.3 accept                           # ingress rule 2
  }
  chain output {
    type filter hook output priority 0; policy accept; # egress any -> any
  }
}
```

You can watch the state table live with `sudo conntrack -L`, each line showing a connection's addresses, ports, protocol and state such as `ESTABLISHED` or `TIME_WAIT`.

### Common misconceptions

- **"Stateful means it inspects content."** Stateful tracks connections, not payloads. Content inspection is the job of [application proxies](applicationproxy.md) and [next-generation firewalls](ngfirewall.md).
- **"Allow all egress is harmless."** It is common and convenient, but malware phoning home is egress too. Stricter networks filter outbound traffic as well.
- **"The state table is infinite."** It is not. SYN floods try to fill it; defences include SYN cookies and connection limits.

### How it connects

[Packet Filtering](packetfilteringfirewall.md), [Stateless Firewalls](statelessfirewall.md), [Circuit-Level Gateways](circuitlevelfirewall.md) and the overview at [Firewalls](firewalls.md). See [IDS/IPS](idsips.md) for watching what allowed traffic actually does.

The truth revealed: memory is what turns a filter into a guard.

## Types of Firewalls

- [PacketFilteringFireWall](packetfilteringfirewall.md)
- [StatelessFirewall](statelessfirewall.md)
- [StatefullFirewall](statefullfirewall.md)
- [Circuit-Level-Firewall](circuitlevelfirewall.md)
- [Application-Proxy](applicationproxy.md)
- [Next-Generation Firewalls](ngfirewall.md)
