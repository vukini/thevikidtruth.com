---
title: Enumeration
date: '2016-11-28T00:20:24+04:00'
lastmod: '2016-11-28T00:55:54+04:00'
original_id: '{A424}'
original_name: enumeration
original_blob: blob/B/2/400.txt
revisions: 11
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: enumeration
draft: false
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md)

# Enumeration

## Types

### Black Box

Simulate Outsider: no information is given
    Bug Bounty

#### DNS Enumeration

Most Organisations host multiple DNS servers:

- Root DNS
- Subordinate DNS
- ISP DNS
- Primary & Secondary - Withing the Organisation
    - Broadcast
    - Zone Transfer
- Local Host Files

##### Tools

- dnsenum
- dnsmap
- dnsrecon
- dnswalk
- fierce

So in an attack the intruder is trying to get access and obtain the internal registry entries of the primary DNS Server.

### White Box

Simulate Internal Attacker: provide some information
    for example:
    
- wifi passwords
- login info

#### SNMP Enumeration

[Simple Network Management Protocol](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol) - it allows for centralised monitoring and forwarding of log files.

This protocol normally is installed on Windows Machines.

In ubuntu you can install the software with `sudo apt-get install snmp`

All Machines on the same network have a shared **community name"** often called **public**

##### Tools

- snmp-bridge-mib  snmp-check       snmpgetnext      snmpstatus       snmpusm
  snmpbulkget      snmpconf         snmpinform       snmptable        snmpvacm
  snmpbulkwalk     snmpdelta        snmpkey          snmptest         snmpwalk
  snmpc            snmpdf           snmpnetstat      snmptranslate
  snmpcheck        snmpget          snmpset          snmptrap
- snmpenum

### Grey Box

Split time  60/40 between Black and White Box scenarios

## Sources

[Security Assured Blog](http://securityassured.wordpress.com)

### The plain idea

Enumeration is the reconnaissance phase of an assessment: before anyone attacks a system, they map it. What hosts exist, what services run, what versions, what user names, what shares, what DNS records. My notes above sort this by how much you are told to begin with, black box (nothing, like a real outsider), grey box (a little), and white box (full inside knowledge). Each models a different kind of attacker.

### Why it matters

Attacks almost never start with the exploit; they start with a map. The more an attacker learns in this quiet, often legal-looking phase, the narrower and more effective the real attack becomes. For a defender, understanding enumeration tells you what you are leaking: an overly chatty DNS server, a service banner announcing an old, vulnerable version, a directory listing full of user names. Reducing that footprint is cheap and powerful.

### An everyday analogy: casing the building

A careful burglar does not smash a random window. They watch the building for a week: when lights go on and off, which doors are used, where the cameras point, whose name is on the buzzer. Enumeration is casing the building, in bytes. A penetration test is the same thing done with permission, to find the gaps before a real thief does.

### A worked example: enumerating a host

A typical first pass maps open ports and the services behind them:

```
nmap -sV -sC -p- target.example       # all ports, versions, default scripts
```

That might reveal SSH on 22, a web server on 443 announcing its exact version, and an old SMB service on 445. DNS enumeration (with the tools listed above, `dnsrecon`, `fierce`, `dnsenum`) then tries zone transfers and guesses subdomains to widen the map. The prize my note mentions, a successful **zone transfer**, hands over an organisation's entire internal DNS in one request, a misconfiguration that is rarer now but still found.

### A note for 2026

The ideas are unchanged, but the ground has shifted to the cloud. Much enumeration today targets exposed cloud storage (open S3 buckets), container registries, API endpoints, and the vast amount of information that leaks passively through certificate transparency logs and services like Shodan and Censys, which index the whole internet so an attacker barely has to touch the target at all. The defensive lesson, know and shrink your attack surface, matters more than ever.

### Common misconceptions

- **"Enumeration is harmless noise."** It is often the most valuable phase; everything after it depends on the map.
- **"Only the exploit is illegal."** Aggressive scanning without permission can itself be unlawful, and always noisy. Do it only on systems you are authorised to test.
- **"Hiding versions is pointless security by obscurity."** It does not fix a vulnerability, but it genuinely slows and frustrates automated attackers; defence in depth welcomes it.

### How it connects

- [Exploitation](exploitation.md): what enumeration feeds into.
- [DNS Poisoning](dnspoisoning.md): attacks on the DNS you enumerate here.
- [IDS/IPS](idsips.md): how defenders notice someone mapping them.
- [Security Program](securityprogram.md): building assessment into a wider process.

The truth revealed: the exploit gets the headlines, but the quiet mapping that came first is where the attack was really won.
