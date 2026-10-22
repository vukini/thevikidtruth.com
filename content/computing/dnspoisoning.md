---
title: DNS -Poisoning
date: '2016-11-28T02:45:30+04:00'
lastmod: '2016-11-28T03:37:07+04:00'
original_id: '{A430}'
original_name: dnspoisoning
original_blob: blob/B/2/437.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: dnspoisoning
draft: true
review: update
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md)

# DNS -Poisoning

This is also known as DNS Hijacking or DNS Spoofing.
The Technique is as follows:

- Create and host a fake website use [Social Engineering Toolkit](scocialengineeringtoolkit.md "MISSING PAGE")
- Modify an file called etter.dns
- perform [apr-poisoning](apr-poisoning.md "MISSING PAGE") use [Ettercap](ettercap.md)
- perform [dns-poisoning](dnspoisoning.md) use [Ettercap](ettercap.md)
- Start the Sniffing

## Tools and Reading List

- [Social Engineering Toolkit](scocialengineeringtoolkit.md "MISSING PAGE")
- [Ettercap](ettercap.md)
- [CISCO Layer 2 Mitigation](http://www.cisco.com/c/dam/global/en_ae/assets/exposaudi2009/assets/docs/layer2-attacks-and-mitigation-t.pdf)
- arp
- arp-scan
