---
title: Honeypots
date: '2016-11-29T06:05:59+04:00'
lastmod: '2016-11-29T06:10:26+04:00'
original_id: '{A462}'
original_name: honeypots
original_blob: blob/B/2/707.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: honeypots
draft: true
review: update
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) | [encryption](encryption.md) |
[IDS/IPS](idsips.md) | [HoneyPots](honeypots.md)

# Honeypots

```
                 _________
                 |SpanPort|
               x-----------
          |    |	             ________------
          |    |        _______      |vlan1  |HIDS| on host machine
          |    |public  |      |     |       ------
  isp --> | // |--------|Server|-----|
          |    |  ^   | |______|     |
          |    |  |   |              |       ---------
          |    | NIDS |              |_______|Honeypot|
         firewall     |________       vlan2  ----------
                      |Honeypot|
Network Based IDS     ----------
```

We try to create a honey network to correlate data and detect attacks.
