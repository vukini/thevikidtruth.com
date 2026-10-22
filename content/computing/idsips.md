---
title: IDS/IPS
date: '2016-11-29T05:45:37+04:00'
lastmod: '2016-11-29T06:34:54+04:00'
original_id: '{A461}'
original_name: idsips
original_blob: blob/B/2/713.txt
revisions: 7
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: idsips
draft: true
review: update
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) | [encryption](encryption.md) |
[IDS/IPS](idsips.md) | [HoneyPots](honeypots.md) | [Securing Web/Apps](securingwebapps.md)

# IDS/IPS

## Intrusion Detection System

- Alert
- Log
- Email

## Intrusion Prevetion System

- IDS - it has all functions of the IDS
- AXN - it can take actions depending on packets
- Drop

```
                 _________
                 |SpanPort|
               x-----------
          |    |	             ________------
          |    |        _______      |vlan1  |HIDS| on host machine
          |    |public  |      |     |       ------
  isp --> | // |--------|Server|-----|
          |    |  ^     |______|     |
          |    |  |                  |       ---------
          |    | NIDS                |_______|Honeypot|
         firewall                     vlan2  ----------

Network Based IDS
Host Based IDS
```

Normally we only use NIDS which sits next to the firewall which is running in spanport mode.
In the IDS software we create rules (signature) and if it matches rule or finds an anomaly
then it will raise a log.

## Tools

Snort

1. Start snort service
1. configure rules
1. restart snort
1. start snort console
1. attack and detect

```
 sudo vi /etc/snort/snort.conf
 /etc/init.d/snort restart
 snort -q -A -i wlan0 -c /etc/snort/snort.conf
 nmap -sU 192.168.100.82
```
