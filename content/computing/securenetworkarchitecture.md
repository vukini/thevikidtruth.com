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

### The plain idea

Secure network architecture is the art of *designing* a network so that a break-in anywhere does the least possible damage. The single biggest idea, running through every principle above, is **segmentation**: split the network into zones, keep the connections between them few and tightly controlled, and deny everything that is not explicitly allowed. My examples focus on the classic and vital case of keeping an [industrial control](icssecurity.md) network separate from the ordinary corporate network.

### Why it matters

A flat network, where everything can talk to everything, is a house with no internal doors: one compromised laptop and the attacker can reach the servers, the backups and the factory floor. Segmentation turns that into a house of locked rooms. It is why the 2016 Ukraine power-grid attack and countless ransomware outbreaks spread so far, and why zoning is the first thing any serious review looks for.

### An everyday analogy: bulkheads in a ship

A ship's hull is divided into watertight compartments. Hole the bow and one compartment floods, but the bulkheads stop the water reaching the rest, and the ship stays afloat. Network segments are bulkheads: a breach in one zone is contained instead of sinking everything.

### A worked example: reading the diagrams

My three sketches are three strengths of the same idea:

1. **Dual-homed host.** One machine with two network cards bridges two zones. Cheap, but that single host is now the only thing between them, a weak bulkhead.
2. **Firewall between zones.** A dedicated [firewall](firewalls.md) enforces the rules, far stronger because its only job is to police what crosses.
3. **Firewall *and* router.** Adds a routed boundary and a second checkpoint. The strongest of the three, and the basis of the modern **DMZ** (demilitarised zone), where internet-facing services sit in a middle zone that can reach neither the internet nor the inside freely.

The "filter ICMP, especially Destination Unreachable" principle is a nice detail: those messages leak network structure to an attacker mapping you (see [enumeration](enumeration.md)), so a careful design quietens them.

### A 2026 update

The frontier today is **zero-trust architecture**: stop trusting anything just because it is "inside" the network, and instead verify every request by identity and device, every time. Combined with **micro-segmentation** (segments as small as a single workload) it is segmentation taken to its logical end. For control systems, the **Purdue model** of layered zones and a **DMZ between IT and OT** remain the reference design.

### Common misconceptions

- **"A firewall at the edge is enough."** Edge defence does nothing once an attacker is inside; internal segmentation is what limits the blast radius.
- **"Air-gapped means safe."** True air gaps are rare and leak via USB sticks and maintenance laptops (Stuxnet crossed one).
- **"Segmentation kills performance."** Done well it barely costs anything and is invisible to users.

### How it connects

- [Firewalls](firewalls.md): the devices that enforce the boundaries.
- [ICS Security](icssecurity.md): the control-network case these principles serve.
- [IDS/IPS](idsips.md) and [Honeypots](honeypots.md): what watches the traffic crossing zones.
- [Security Program](securityprogram.md): where architecture fits a wider plan.

The truth revealed: you cannot stop every break-in, so the real skill is designing the network so that one break-in is never the whole story.
