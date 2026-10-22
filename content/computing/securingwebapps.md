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
draft: true
review: update
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
