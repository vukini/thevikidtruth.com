---
title: Securing Industrial Control Systems
date: '2016-11-27T11:03:13+04:00'
lastmod: '2016-12-10T06:16:56+04:00'
original_id: '{A413}'
original_name: icssecurity
original_blob: blob/B/5/131.txt
revisions: 30
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: icssecurity
draft: false
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md)

# Securing Industrial Control Systems

## SCADA

### [The GENERATIONS of Scada](http://electrical-engineering-portal.com/three-generations-of-scada-system-architectures)

Scada has evolved over the years.

- First Generation – **Monolith**
- Second Generation – **Distributed**
- Third Generation – **Networked**
- Fourth Generation – **Internet of Things**

### Primary Scada Services

- **C** - confidentiality - encryption (travelling, stored, action) - stack level encryption
- **I** - integrity - intact - hashing
- **A** - availability - redundancy

#### Secondary Scada Services

- **A** - Authentification - identification (know, are, have)
- **A** - Authorisation - Privaledge - (role, rule, discretionary)
- **A** - Accounting - Logging
- **A** - Accountability - Auditing function
- **A** - Assurance - Testing & Examination

### Achieving Security - Guides and Standards

- [National Institute of Standards and Technology](http://csrc.nist.gov/) 
  [NIST-SP-800-82 (pdf)](/assets/nist-sp-800-82.pdf)
- [Open Source Security Testing Methodology Manual (OSSTMM)](http://www.isecom.org/research/osstmm.html)
- [OWASP](https://www.owasp.org/index.php/Main_Page)
- [PTES](http://www.pentest-standard.org)

#### 5 Phases of Security Testing

1. **Reconaissance, Footing, Information Gathering**
    - Wappalyser
    - web.nvd.nist.gov
    - exploit-db
    - Maltego - paterva.com (get the community version)
    - Shodan
    - Dorks
    - hackersforcharity.org
    - traceroute
    - ping host -l 1000 -f
    - email footprinting
    - [readnotify](http://readnotify.com)
    - [ip2location](http://ip2location.com)
    - email tracking services
1. **Scanning - Port Scanning - Getting the Socket**
    - **Ports can be considered:**
          - Open
          - Closed
          - Filtered (ACL)
    - **nmap, winpcap, zenmap**
    - **Vunerability scanning**
          - [Nessus](http://tenable.com) - checks webapps for malware, missing patches, misconfigs, use of defaults, zero day vulnerabilities, mobile platform weaknesses, PCI DSS Complianse
          - [openVAS the Freesoftware scanner](http://www.openvas.org/)
          - [Acunetix](https://www.acunetix.com/) - Windows & Cloud Only
          - Zed Attack Proxy
          - Websecurify
          - Arachni
          - Nikto
          - Burp Suite
          - Virusdie
          - IronWASP
          - SecApps
          - skipfish
          - wapiti
          - w3af
          - Tamper Data
1. [Enumeration](enumeration.md)
1. [Exploitation](exploitation.md)
1. [Maintaining Access](maintainingaccess.md "MISSING PAGE")
1. [Clearing Your Tracks](cyt.md "MISSING PAGE")

### Geting to Know Types of Threats

- Black Hat Hackers
- State Sponsered Hackers
- Hactivist
- Social Engineers
- Cyber  Terrorist

### Policies & Procedures

- Need dedicated Policies
- Adequate Train (training - how, education - why, awarness - what)
- Security Architecture
- Documented Procedures
- Guidlines - is a modification of a Baseline - diveloped by IGSS (main player) for e.g.
- RACI 
     Responsible - Accountable - Consulted - Informed - Targets
- Regular Audits
- Counter Measures - Honeypots
- Safeguards
- Disaster Recovery Plan - Backups - Business Continuity
- Change Approval Board

### Platform Vunerabilities

- Patches not developed
- Patches not installed
- due care, due diligence
- Depedencies
- Default used
- Backups of Critical info
- Passwords
- Physical Protection
- Dual Network interface card (NIC)
- Daisy Chaining
- Radio & Emp - FBI - Tempest

## SIEM @ SCADA

SIEM - Security Incident and Event Management

Transforms Machine Data into the Operational Intelligence giving Proactive Anticipation of Attacks by Event
Corrolation of **Indicators of Compromise**

### Players in the Market

- HP: [Arcsight](http://www8.hp.com/us/en/software-solutions/siem-security-information-event-management/index.html)
- FREE: [Alien Vault](https://www.alienvault.com/)
- Famous: [SPLUNK](https://www.splunk.com/) - splunkbase

The systems work by installing a forwarder that then forwards machine logs
to an Indexer

```
          Forwarder [collect logs from various machines]
             |
             V
          Indexer [to identify + label fields of the logs]
             |
             V
        Search-Head [event corrolation happens here]
```

### The plain idea

Industrial control systems (ICS), and the SCADA systems that supervise them, are the computers that run physical things: power grids, water treatment, pipelines, factory lines. Securing them means protecting equipment that can *move, heat, and electrify the real world*. My notes above lay out the goals (the CIA triad plus the extra "A" services) and the standards to follow. The crucial twist, and the theme of this whole page, is that in ICS the priorities are **flipped**: in ordinary IT the order is Confidentiality, Integrity, Availability; in ICS it is **Availability and safety first**, because a turbine that stops, or runs wrong, can hurt people.

### Why it matters

An office breach leaks data; an ICS breach can flood a town, black out a city, or injure workers. These systems were designed decades ago for isolated, trusting networks, and then got connected to corporate networks and the internet (my "generations" list, ending in IoT). That collision, old, fragile, safety-critical equipment meeting modern threats, is one of the most serious problems in security today. Stuxnet (2010) destroyed Iranian centrifuges; attackers blacked out parts of Ukraine's grid in 2015 and 2016; the Oldsmar water-plant intrusion (2021) tried to poison a water supply.

### An everyday analogy: a hospital versus a bank

Rob a bank and money is lost, serious, but recoverable. Sabotage a hospital's life-support and the stakes are different in kind. ICS security is hospital security: you cannot simply "turn it off and patch it" when turning it off is itself the danger, and a wrong instruction has physical, sometimes fatal, consequences. That is why ICS cannot just copy IT security wholesale.

### A worked example: why you cannot secure ICS like IT

Imagine the standard IT playbook meeting a power plant:

- **"Just patch it."** The controller runs 20-year-old firmware on hardware that cannot be taken offline without shutting down the plant; a patch may not even exist. *ICS answer:* compensating controls, segment and monitor instead.
- **"Encrypt everything."** Many industrial protocols (Modbus, DNP3) have no security at all and real-time constraints that encryption can break. *ICS answer:* protect them at the network boundary rather than changing the protocol.
- **"Require strong auth everywhere."** An operator must be able to hit an emergency stop *instantly*, so a login prompt in that path could cost lives. *ICS answer:* safety and availability win; secure the surrounding zones instead.

The resulting design is the one on the [secure network architecture](securenetworkarchitecture.md) page: isolate the control (OT) network from the corporate (IT) network, allow only the few necessary, tightly filtered connections through a DMZ, deny by default, and watch everything that crosses.

### A 2026 update

The reference standard is now **IEC 62443**, the dedicated framework for industrial automation security, alongside the **NIST SP 800-82** guide to ICS. The **Purdue model** of layered zones remains the backbone. New pressures: ransomware increasingly hits OT (the 2021 Colonial Pipeline shutdown was triggered by an IT breach spilling toward OT), and the explosion of industrial IoT ("Fourth Generation" in my notes) multiplies the attack surface, making segmentation and monitoring more important than ever.

### Common misconceptions

- **"It's air-gapped, so it's safe."** True isolation is rare and bypassed by USB sticks, vendor laptops and quiet IT-to-OT links.
- **"IT security tools work as-is."** Active scanning or forced patching can crash fragile controllers; ICS needs passive, protocol-aware tooling.
- **"Obscure protocols are protection."** Their details are well documented and, worse, usually unauthenticated.

### How it connects

- [Secure Network Architecture](securenetworkarchitecture.md): the segmentation these systems depend on.
- [Security Program](securityprogram.md): the risk and standards process (IEC 62443, NIST).
- [IDS/IPS](idsips.md) and [Honeypots](honeypots.md): passive monitoring suited to OT.
- [Encryption](encryption.md): the CIA services and their ICS-specific trade-offs.

The truth revealed: ICS security is the one corner of the field where a bug is not measured in lost data but in lost water, power, or lives, which is exactly why its rules run backwards from everything else.
