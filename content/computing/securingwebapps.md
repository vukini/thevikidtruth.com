---
title: Securing Web Applications and Softwares
date: '2016-11-29T06:41:07+04:00'
lastmod: '2016-12-01T02:44:39+04:00'
original_id: '{A463}'
original_name: securingwebapps
original_blob: blob/B/3/504.txt
revisions: 20
author: admin
last_editor: admin
reply_to: ({A524})
tags:
- computing
categories:
- computing
wikislug: securingwebapps
draft: false
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) | [encryption](encryption.md) |
[IDS/IPS](idsips.md) | [HoneyPots](honeypots.md) | [Securing Web/Apps](securingwebapps.md)

# Securing Web Applications and Softwares

## Denial of Service

DOS attacks are attacks on the **availability of a service**.
 
### Type of Attacks

- **DHCP** 
   DHCP use DORA (Demand - Offer - Request - Acknowledgement) 
   'D'-Flood: Technique & [DHCP STARV](http://dhcpstarv.sourceforge.net/): Tool
- Network
    - The idea here is to destroy commnication on the network
    - Most networks are switched
    - which have CAM-Table (mapping IP:MAC)
    - if the CAM is filled then the switch degrades to a HUB
    - So the trick here is to fill this table and then BAM!
    - ```
         # = N
         OLD = 8 (normal bandwidth consumption, for example 8)
                  8
         NEW =(N)^
      ```
         Tool:
      ```
         macof -i eth1
      ```
         Mitigation by implementing **port security** on the switch
- Webserver
    - Connection Threshold
    - Bandwidth Congestion
- Individual Machine Attack - Tool: LOIC

#### Connection Threshold

On a TCP/IP connection handshake, attackers can attack on the **Open State (Time between Sync and Ack(**

One mititgation state is to reduce the **Open State** wait time (usually 4s). However the attacker can send Sync packets at a rate greater than the rate the servers drops the packets. We can use hping3

```
 hping3 server.address -S -a spoofed.address --flood

 option -S (enable sync flag) -a to spoof addresss.
```

#### Bandwidth Congestion - DDOS

Distributed Denial of Service - Practically you need a Botnet (such as PRO-RAT)

```
        |||||||||||||||||
        VVVVVVVVVVVVVVVVV
        -----------------
         Buffer Space
        -----------------
              ||
        -----------------
           Webserver
        -----------------
```

# Web-Application Vulnerabilities

**https://www.owasp.org/ OWASP - Open Wen App. Security Project**

### Top Vulnerabilities

- Sequel Injection
- Cross Site Scripting
- Buffer Overflow

## Sequel Injection

Hackers are interested in getting user names and passwords but this is not easy.
Typically they need to find some zero day Vulnerabilities in either the firewall, database or both.

A better way is to inject SQL queries directly into the database:

```
  SELECT * FROM WHERE COL NAME = PASSWORD

  1'or'1'='1

  
```

One good defense to this type of attack is:

- Validate Characters
- Ensure Length of Query is Limited

## Cross Site Scripting Attacks

The Vulnerabilities provides the attacker the ability to induce his source code
into the source code of the web application.

```
<script>alert(xss);</script>
```

If the Vulnerability is found

- Redirect Users
- Cookie Stealing
- Session Hijacking
- Cookie Manager
- Website Defacement

Defense

- Encrypted Session ID

## Buffer Overflows

- [IDA Pro](https://www.hex-rays.com/products/ida/)
- [You need to Understand Stacks](stacks.md)

## Sources and Links

- [infosec institute](http://resources.infosecinstitute.com/dos-attacks-free-dos-attacking-tools/)
- [Cisco Mitigator](http://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)
- [Defeating DDOS Attacks](http://www.cisco.com/c/en/us/products/collateral/security/traffic-anomaly-detector-xt-5600a/prod_white_paper0900aecd8011e927.html)

```

```

### The plain idea

Securing web applications means defending the software people reach over the internet, the part of your system that is, by design, open to everyone, including everyone hostile. My notes above start with **denial-of-service (DoS)**, attacks on *availability*, flooding a service until it falls over, but web security is really about all three parts of the classic triad: keeping data secret (confidentiality), unaltered (integrity) and reachable (availability).

### Why it matters

A web app is your front door to the world, and it is always unlocked for business. Everything behind it, user data, payments, internal systems, is only as safe as that code. Most of the largest breaches in history were web-application flaws: an injection bug, a broken login, a misconfigured server. Understanding the common attack classes is how you stop being the next headline.

### An everyday analogy: a shop open to the public

A web server is a shop with its doors open to any passer-by. Most are customers; a few are shoplifters, and one is parked outside revving an engine to block the entrance so nobody can get in (that is DoS). You cannot lock the doors, that would end the business, so instead you watch behaviour, limit how much any one person can take at once, and design the shop so a troublemaker cannot reach the stockroom.

### A worked example: the DoS attacks in my notes, and defence in depth

My notes name three layers of flooding, and each has a matching defence:

- **Network (MAC flooding).** Fill a switch's CAM table with `macof` and it fails open, broadcasting everything like a dumb hub. *Defence:* port security, limiting MAC addresses per port.
- **Connection (SYN flood).** Open thousands of half-finished TCP handshakes (the "open state between SYN and ACK") so the server runs out of slots. *Defence:* SYN cookies, connection limits.
- **Application (LOIC-style).** Hammer the app with expensive requests. *Defence:* rate limiting, a CDN/WAF, and today's cloud DDoS scrubbing services.

Beyond availability, the modern baseline is the **OWASP Top Ten**: broken access control, injection (SQL, command), cryptographic failures, security misconfiguration and so on. A single well-known example, parameterised queries, kills SQL injection:

```python
# vulnerable: user input becomes part of the query
cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
# safe: input is data, never code
cur.execute("SELECT * FROM users WHERE name = %s", (name,))
```

### A 2026 update

Since these notes, defence has consolidated: HTTPS everywhere (free via Let's Encrypt), a [WAF](applicationproxy.md) in front, content-security-policy headers against cross-site scripting, and framework defaults that are safe out of the box. DDoS has grown to terabit scale, handled by CDNs and scrubbing providers rather than a single server. And the attack surface has shifted to **APIs, dependencies (supply-chain attacks) and cloud misconfiguration**, which is why automated dependency scanning and least-privilege cloud roles now matter as much as the app code itself.

### Common misconceptions

- **"HTTPS means my app is secure."** It only encrypts the connection; it does nothing about injection, broken access control or weak passwords.
- **"Small sites aren't targets."** Most attacks are automated and indiscriminate; bots probe everything.
- **"A firewall protects the app."** A network firewall allows port 443 by definition; attacks ride in on allowed traffic, which is why you need app-level defences.

### How it connects

- [Application Proxy](applicationproxy.md) and [NG Firewalls](ngfirewall.md): WAFs and content inspection.
- [Encryption](encryption.md): HTTPS, password hashing, salting.
- [Exploitation](exploitation.md) and [Enumeration](enumeration.md): how attackers find and hit these flaws.
- [Security Program](securityprogram.md): building testing into the process.

The truth revealed: a web app cannot lock its doors, so security is not about keeping people out, it is about making sure that the ones who mean harm cannot reach anything that matters.
