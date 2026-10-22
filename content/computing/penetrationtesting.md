---
title: Penetration Testing
date: '2016-11-27T11:05:30+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A415}'
original_name: penetrationtesting
original_blob: blob/B/3/232.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: penetrationtesting
draft: false
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md)
[Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md)

# Penetration Testing

Here is the truth about penetration testing: **it is authorised breaking, done carefully, so the real breakers have a harder time.** Without a clear scope and written permission it is just hacking; with them it is engineering.

### What it is, in plain words

A **penetration test** (pentest) is a structured engagement where an operator attempts to find and exploit vulnerabilities in a system, within agreed rules, and then reports what they found and how to fix it. It answers a sharper question than a vulnerability scan: not "what *might* be wrong?" but "what can an attacker *actually do*?"

Typical phases (the names vary; the ideas don't):

1. **Permission & scoping** – whose systems, which IPs, what's off-limits, when.
2. **Reconnaissance** – public info, DNS, whois, tech fingerprints.
3. **Scanning & enumeration** – open ports, services, users, shares. See [Enumeration](enumeration.md).
4. **Exploitation** – gaining a foothold. See [Exploitation](exploitation.md).
5. **Post-exploitation** – privilege escalation, lateral movement, data access; always within scope.
6. **Reporting & remediation** – clear findings, severity, evidence, fixes. The report is the product.
7. **Retest** – did the fixes work?

### Why it matters

Defenders invent models; attackers invent paths. A pentest is how you borrow an attacker's eyes for a week. Done well, it finds the missing patch, the reused password, the forgotten staging server, the "temporary" firewall hole – before someone uninvited does. Done badly (or without permission), it causes outages and lawsuits.

### An everyday analogy: a red-team fire drill

A fire drill isn't arson. You schedule it, warn the people who need to know, set off the alarm, and watch what fails – which door sticks, who doesn't hear it. Then you write down what to fix. A pentest is a fire drill for security.

```mermaid
flowchart LR
  Auth[Written authorisation] --> Recon
  Recon --> Enum[Enumeration]
  Enum --> Exploit
  Exploit --> Post[Post-exploitation]
  Post --> Report
  Report --> Fix --> Retest
```

### A hands-on example: a home lab, not a stranger's Wi-Fi

Build a disposable lab in [VirtualBox](virtualbox.md) or KVM: an attacker VM (Kali, Parrot or a plain Debian with tools) and a target VM (a deliberately vulnerable image such as OWASP Juice Shop, DVWA, or an old Metasploitable – **isolated on a host-only network**).

```bash
# on the attacker VM, only against lab targets
sudo nmap -sV -sC 192.168.56.10
sudo nmap --script vuln 192.168.56.10

# web app basics
ffuf -u http://192.168.56.10/FUZZ -w /usr/share/wordlists/dirb/common.txt
nikto -h http://192.168.56.10
```

When you find something exploitable, document:

- **What** – e.g. "SQL injection in `/login` parameter `user`"
- **How** – exact request, payload, screenshot/packet capture
- **Impact** – what you could read or do
- **Fix** – parameterised queries, input validation, WAF as defence in depth

Frameworks and toolkits you'll meet: [Metasploit](metasploit.md), Burp Suite, nmap, ffuf/gobuster, sqlmap, BloodHound (AD), [Ettercap](ettercap.md)/Bettercap for LAN MITM. Certifications (OSCP, eJPT, etc.) teach a disciplined version of this loop; they're optional, the discipline isn't.

### Rules that are not optional

- **Written permission** from the owner, with scope and contacts.
- **No testing production** without explicit agreement and a rollback plan.
- **Care with DoS, fuzzing and brute force** – easy to cause outages.
- **Handle findings carefully** – other people's vulnerabilities are sensitive data.
- **Know the law** where you live. Authorisation is the difference between a job and a crime.

### How this differs from related work

| Activity | Goal |
|----------|------|
| Vulnerability scan | Find known issues automatically |
| Penetration test | Exploit and demonstrate impact, within scope |
| Red team | Emulate a real adversary, often with stealth goals |
| Bug bounty | Ongoing invitations for outsiders to report bugs |
| Purple team | Attackers and defenders working together to improve detection |

Most organisations need scanning continuously, a pentest around big changes, and a red-team exercise only once the basics are solid.

### Common misconceptions

- **"A pentest is an automated scan."** A scan lists possible issues. A pentest demonstrates impact and chains findings together.
- **"We got a clean report, so we're secure."** It means that tester, that scope, that week, didn't get in. Re-test after changes.
- **"Pentesting is only for web apps."** Networks, AD, Wi-Fi ([WiFi Penetration](wifipenetration.md)), mobile, cloud, [ICS](icssecurity.md), physical – all fair game when scoped.
- **"The goal is to get root."** The goal is to improve the system's security. Sometimes the most valuable finding is "your logging never noticed me."
- **"Kali makes you a pentester."** Tools don't. Method, notes, communication and ethics do.

### Connections

- [Computer Security](computersecurity.md), [Linux Security](linuxsecurity.md).
- [Exploitation](exploitation.md), [Enumeration](enumeration.md), [Metasploit](metasploit.md).
- [ARP Poisoning](arppoisoning.md), [DNS Poisoning](dnspoisoning.md), [Ettercap](ettercap.md).
- [VirtualBox](virtualbox.md), [Virtualization](virtualization.md) – build labs, don't break the real world.

The are a few things you want to start pentesting:

- [VMware](http://www.vmware.com/products/workstation/)
  [Metasploitable2](http://sourceforge.net/projects/metasploitable/files/Metasploitable2/)
