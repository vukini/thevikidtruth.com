---
title: Honeypots
date: '2016-11-29T06:05:59+04:00'
lastmod: '2016-11-29T06:10:26+04:00'
original_id: '{A462}'
original_name: honeypots
original_blob: blob/B/2/707.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: honeypots
draft: false
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) | [encryption](encryption.md) |
[IDS/IPS](idsips.md) | [HoneyPots](honeypots.md)

# Honeypots

```
                 _________
                 |SpanPort|
               x-----------
          |    |	             ________------
          |    |        _______      |vlan1  |HIDS| on host machine
          |    |public  |      |     |       ------
  isp --> | // |--------|Server|-----|
          |    |  ^   | |______|     |
          |    |  |   |              |       ---------
          |    | NIDS |              |_______|Honeypot|
         firewall     |________       vlan2  ----------
                      |Honeypot|
Network Based IDS     ----------
```

We try to create a honey network to correlate data and detect attacks.
### The plain idea

A honeypot is a decoy. It is a system (or service, or file, or account) that has no legitimate reason to be touched, deliberately placed so that attackers find it. Because nobody should ever interact with it, *any* interaction is suspicious by definition. That is its great virtue: a honeypot has almost no false positives. A hit is a signal, not noise.

Honeypots come in two strengths. **Low-interaction** honeypots merely imitate a service, enough to log the first probe. **High-interaction** honeypots are real, fully functioning systems, which reveal far more about an attacker's methods but are riskier, because a real system can be taken over and turned against you. A collection of honeypots wired together, as in my diagram, is a **honeynet**: you place decoys on their own VLAN and correlate what hits them to understand an attack campaign.

### Why it matters

Most detection drowns analysts in alerts. A honeypot flips the problem: instead of sifting mountains of normal traffic for the one bad packet, you set a trap that only the bad packet springs. It gives you early warning (someone is already inside, probing), threat intelligence (which tools and exploits they use), and delay (time spent on the decoy is time not spent on your real assets). The same idea scaled up gives us internet-wide honeypots and *honeytokens*: fake credentials or documents that scream when used.

### An everyday analogy: the marked decoy banknote

Shops sometimes keep a bundle of marked "bait money" in the till. It is never given to real customers, so if those exact notes turn up anywhere, the shop knows there was a robbery and can trace them. The bait is useless for business and valuable precisely because it should never move.

### A worked example: a honeytoken

You do not need a whole fake network to use the idea. Create a database row for a user who does not exist, say `admin_backup@yourcompany`, and set an alert for any login attempt or any query that reads it. No employee or application ever references that row, so the day it is touched, you know someone is poking through your database who should not be. The same trick works with a tempting-looking file (`passwords.xlsx`) wired to alert when opened, or a fake AWS key planted in a repo (the canarytokens.org service does exactly this for free).

For a networked example matching my diagram, a low-interaction tool such as **Cowrie** pretends to be an SSH server. Attackers "log in", and Cowrie records every command they type into a fake shell, capturing their scripts and downloaded malware without ever giving them a real machine.

### Common misconceptions

- **"A honeypot protects a system."** It does not defend anything directly; it detects and informs. It complements firewalls and [IDS/IPS](idsips.md), it does not replace them.
- **"Attracting attackers is dangerous and illegal."** Watching people attack a decoy you own is legal in most places. The real risk is a high-interaction honeypot being used as a springboard, which is why decoys are isolated on their own segment.
- **"Entrapment."** Honeypots do not induce anyone to commit a crime; they sit still and wait. They record what attackers choose to do.
- **"They catch everything."** A careful attacker who recognises a decoy will avoid it. Honeypots catch the opportunistic and the automated especially well.

### How it connects

- [IDS/IPS](idsips.md): the honeypot sits alongside detection sensors, as in the shared diagram.
- [Secure Network Architecture](securenetworkarchitecture.md): where to place a honeynet so it is reachable but isolated.
- [Exploitation](exploitation.md) and [Forensics](forensics.md): honeypots feed both the study of attacks and the evidence afterwards.

The truth revealed: the cleverest alarm is not a stronger lock, but a door nobody honest will ever open.

### Tools and reading

- [Cowrie SSH/Telnet honeypot](https://github.com/cowrie/cowrie)
- [T-Pot multi-honeypot platform](https://github.com/telekom-security/tpotce)
- [Canarytokens](https://canarytokens.org/)
- [The Honeynet Project](https://www.honeynet.org/)
