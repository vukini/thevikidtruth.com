---
title: Computer Security
date: '2016-11-27T11:01:30+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A412}'
original_name: computersecurity
original_blob: blob/B/6/524.txt
revisions: 28
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: computersecurity
draft: false
topics:
- security
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Computer Security](computersecurity.md) | [ICSsecurity](icssecurity.md) |
  [Firewalls](firewalls.md) | [Networking](networking.md) | [Security Programs](securityprogram.md) |
 [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) | [wifi-penetration](wifipenetration.md) |
 [Forensics](forensics.md) | [SecureNetworkArchitecture](securenetworkarchitecture.md)

# Computer Security

Here is the truth about computer security: **it is not a product you buy or a department you hire – it is the practice of making systems fail safely when people, software and physics all misbehave.** Everything else is technique.

### What it is, in plain words

**Computer security** is the set of ideas and practices that protect the **confidentiality**, **integrity** and **availability** of information and systems (the classic CIA triad). Around those three sit authentication ("who are you?"), authorisation ("what are you allowed to do?"), accountability (logging and audit), and non-repudiation.

Attacks exploit gaps between what a system *should* do and what it *actually* does: a buffer that can overflow, a password that can be guessed, a user who can be phished, a backup that doesn't restore. Defence is layered because any single layer fails.

```mermaid
flowchart TB
  subgraph defence in depth
    P[Physical] --> N[Network]
    N --> H[Host]
    H --> A[Application]
    A --> D[Data]
  end
  People[People & process] -.-> defence in depth
```

### Why it matters

Software now runs hospitals, banks, voting machines, cars and the communication we trust with our lives. The same laptop that holds your family photos is one reused password away from becoming a foothold into somewhere else. Curiosity about how systems break – the same curiosity that makes someone love Linux and Lisp – is the foundation of defending them.

### An everyday analogy: a city, not a vault

A vault has one thick door. A city stays safe with locks, street lights, police, fire codes, identity papers, and citizens who notice when something is wrong. Compromise one street and the city still functions. Computer security done well looks like a city: many boring, overlapping protections, plus the ability to detect and recover.

### A hands-on example: thinking like an attacker, fixing like an engineer

Take a small web app that stores sessions in a cookie.

```bash
# 1. What's exposed?
nmap -sV -p 1-1000 target.example          # only with permission
curl -I https://target.example
```

Questions a security-minded engineer asks:

- Is TLS configured sanely? (See [TLS](tls.md).)
- Is the cookie `Secure`, `HttpOnly`, `SameSite`?
- Is input validated, or can `' OR 1=1--` change a query?
- Are dependencies updated? (`npm audit`, `pip audit`, `xbps`/`apt` updates)
- If the server is compromised, how far can an attacker go – is there credential reuse, a wide-open internal network, a missing [firewall](firewalls.md)?

A tiny, concrete fix – hashing passwords properly (Node.js example):

```js
import { scrypt, randomBytes, timingSafeEqual } from "node:crypto";
import { promisify } from "node:util";
const scryptAsync = promisify(scrypt);

async function hashPassword(password) {
  const salt = randomBytes(16);
  const derived = await scryptAsync(password, salt, 64);
  return `${salt.toString("hex")}:${derived.toString("hex")}`;
}

async function verify(password, stored) {
  const [saltHex, hashHex] = stored.split(":");
  const derived = await scryptAsync(password, Buffer.from(saltHex, "hex"), 64);
  return timingSafeEqual(derived, Buffer.from(hashHex, "hex"));
}
```

Never store plaintext or simple hashes (`md5(password)`). Prefer scrypt, Argon2id or bcrypt, with a per-password salt.

### The major landscapes

- **Host & OS** – [Linux Security](linuxsecurity.md), patching, least privilege, [SSH](sshlogin.md).
- **Network** – [Firewalls](firewalls.md), segmentation, VPN, [IDS/IPS](idsips.md).
- **Application** – OWASP Top 10, secure coding, dependency hygiene; [Securing Web Apps](securingwebapps.md).
- **Cryptography** – [Encryption](encryption.md), [TLS](tls.md) – use well-reviewed libraries, don't invent your own.
- **Identity** – passwords, keys, MFA, passkeys; the human is part of the system.
- **Offensive / verification** – [Penetration Testing](penetrationtesting.md), [Exploitation](exploitation.md), red teams, bug bounties.
- **Response** – [Forensics](forensics.md), backups, incident plans. Assume breach; practise recovery.

### Threat models before tools

Before picking a tool, write one sentence: "I am protecting ___ from ___ who can ___." A laptop at a café, a family file server, a public web API and a hospital network have different enemies and different budgets. A threat model keeps you from buying a vault for a bicycle – or a bicycle lock for a vault.

### Common misconceptions

- **"I'm too small to be targeted."** Opportunistic bots don't care who you are. They care that your port 22 accepts passwords.
- **"Encryption means I'm secure."** Encryption protects data in transit or at rest. It doesn't fix bad auth, bugs or phishing.
- **"Antivirus = security."** On servers it's nearly irrelevant next to patching and access control. On desktops it's one layer.
- **"Open source is automatically secure."** Many eyes *can* help; they don't automatically look. Heartbleed was open source.
- **"Security loves complexity."** Complexity is the enemy. Small systems with clear trust boundaries win.

### Connections

- [Linux Security](linuxsecurity.md), [Firewalls](firewalls.md), [Encryption](encryption.md), [TLS](tls.md).
- [Penetration Testing](penetrationtesting.md), [Exploitation](exploitation.md), [Metasploit](metasploit.md).
- [Honeypots](honeypots.md), [Forensics](forensics.md), [ICS Security](icssecurity.md).
- [Computing Freedom](computingfreedom.md) – why control over your own machine matters.

Security can mean a lot of things within and without computer systems but generally revolves around a few core concepts,
including, **Integrity, Availability, Authenticity, Encryption  & Authority of Data and Processes**.

- [Linux Security](linuxsecurity.md)
- [Industrial Control Systems Security](icssecurity.md)
- [Penetration Testing](penetrationtesting.md)
- [Firewalls](firewalls.md)
- [Security Programs](securityprogram.md)
- [Secure Network Architecture](securenetworkarchitecture.md)
- [Malware Types](malwaretypes.md)
- [TLS](tls.md)
- [SSH Login](sshlogin.md)

## Tools, Links and Sources

- [eforensicsmag](https://eforensicsmag.com/)
- [OpenVPN Presentation - User Space](https://openvpn.net/papers/BLUG-talk/index.html)
- [OpenVPN Home](https://openvpn.net/)
- [Fluxion](https://github.com/deltaxflux/fluxion)
- [Securitytube](http://www.securitytube.net/)
- [Pico CFT Security Training](https://www.picoctf.org)
