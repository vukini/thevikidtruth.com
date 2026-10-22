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
draft: true
review: update
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
