---
title: Secure Network Architecture
date: '2016-12-01T00:14:27+04:00'
lastmod: '2016-12-01T02:21:15+04:00'
original_id: '{A556}'
original_name: securenetworkarchitecture
original_blob: blob/B/3/500.txt
revisions: 27
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: securenetworkarchitecture
draft: true
review: update
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
 [Forensics](forensics.md) | [Secure Network Architecture](securenetworkarchitecture.md)

# Secure Network Architecture

## Principles

1. Isolate ICS (Control) Network & Corporate (Production) Network
1. Use minimal connections between Control & Production Networks
1. use [Firewalls](firewalls.md)
1. Filter Packets - ICMP codes, especially Destination Unreachable Network & Host flags
1. Block all Communication by Default
1. Enforce Secure Authentication
1. Enforce Destination Authorisation
1. Record Information
1. Permit the ICS to Implement Operational Policies

## Netwok Architecture

- Dual-Homed Computer/Dual Network Interface Cards (NIC)
  ```
                          Firewall
      ISP -----| |---------|   |-----ProductionNetwork
                             |
                             |
                           ControlNetwork
  ```
- Firewall between Corporate Network & control Network
  ```
                Control Network
                       |
                  |FireWall|
                       |
                       |
                Production Network------|FireWall|---|router|--ISP
  ```
- Firewall & Router between Corporate Network & Control Network
  ```
                Control Network
                       |
                   ---------
                    Router        (Router can filter packets too)
                   ---------
                       |
                  |FireWall|
                       |
                       |
                Production Network------|FireWall|---|router|--ISP
  ```
- Firewall with DMZ between Corporate Network & Control Network
  ```
                         Control Network
                                |
         | DMZ |-----------|FireWall|
                                |
                                |
                         Production Network-------|FireWall|---|router|--ISP
  ```
- Paired Firewalls between Corporate Network and Control Network **Practically Used**
  ```
                Control Network
                       |
                       |
                   |FireWall|       (Router can filter packets too)
                       |
                       |
     | DMZ |-------|FireWall| FS
                       |
                       |                   FO
                Production Network------|FireWall|---|router|--ISP
    Can Use different Firewall Configs Active - Active   |  FAIL - Secure State FO
                                       Active - Passive  |  FAIL - Open State   FS
  ```

## Logically Seperated Control Networks

- ```
    LAN  -----> Virtual LAN -------> Enclave (Grouping of VLANS)
  ```

## Defense in Depth / Onion Security

1. Application & Data
1. Data End Point
1. Patch Management - [Qualys Guard](https://www.qualys.com/suite/vulnerability-management/)
1. Intrusion Prevention
1. Virus Protection
1. Host-Based Firewall
1. Server Hardening
1. Internal Network
1. Perimeter Security
1. Physical Security
1. Policies & Procedures

## Use Secure Protocols

- WEP --> WPA2
- TELNET --> SSH
- FTP --> SFTP
- EMAIL --> PGP ro SMIME
- HTTP --> HTTPS

## Links

- [Linux Security](linuxsecurity.md)
- [Industrial Control Systems Security](icssecurity.md)
- [Penetration Testing](penetrationtesting.md)
- [Firewalls](firewalls.md)
- [Security Programs](securityprogram.md)
