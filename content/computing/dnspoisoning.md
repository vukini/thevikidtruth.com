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
draft: false
topics:
- security
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

### The plain idea

DNS is the internet's phone book: it turns a name you can remember, like `bank.example`, into the IP address a computer actually connects to. DNS poisoning (also called DNS spoofing or DNS hijacking) is the trick of making that phone book lie, so that a victim typing the right name is sent to the attacker's server instead. The page they see can look identical to the real one, which is why it is a favourite for phishing and credential theft.

There are several places to plant the lie. My lab notes describe the local-network version: get in the middle with [ARP poisoning](arppoisoning.md), then use Ettercap's `etter.dns` file to answer the victim's DNS lookups with your own address. But poisoning can also happen by attacking a DNS *resolver's cache* (the classic 2008 Kaminsky attack), by compromising a home router's DNS settings, or by tampering with records at the registrar.

### Why it matters

If you control name resolution, you control where the victim goes, no matter how carefully they type the address. Combined with a convincing fake site it defeats passwords outright. Historically it also undermined the whole trust model of the web, which is why the big defences, DNSSEC, HTTPS with proper certificates, and encrypted DNS, were built specifically to detect or prevent it.

Those defences change the picture in 2026. A poisoned DNS answer can still send you to the wrong IP, but that server cannot present a valid TLS certificate for `bank.example`, so the browser shows a warning. DNSSEC lets resolvers reject forged records, and DNS over HTTPS/TLS (DoH/DoT) stops an on-path attacker from seeing or editing your lookups in the first place. The attack is far from dead, but it increasingly depends on the victim ignoring a certificate warning.

### An everyday analogy: the tampered phone book

Someone sneaks into your house and changes the number next to "Bank" in your phone book. You dial carefully, reach a polite voice that sounds just like your bank, and read out your account details. You did everything right; the directory was the liar.

### A worked example: the local-network attack in my notes

1. Build a convincing fake page (the Social Engineering Toolkit can clone a login page in seconds).
2. Edit Ettercap's `etter.dns` to point the target domain at your machine:
   ```
   bank.example      A   192.168.1.10
   *.bank.example    A   192.168.1.10
   ```
3. Get in the middle with ARP poisoning, then enable Ettercap's `dns_spoof` plugin.
4. When the victim's browser asks for `bank.example`, Ettercap answers first with your address; the real answer, if it arrives at all, is ignored.

You can see it working from the victim with `nslookup bank.example`: the returned address is yours, not the real one. The modern catch for the attacker is step 5, the TLS certificate, which they cannot forge, so a careful victim gets a browser warning.

### Common misconceptions

- **"HTTPS alone stops it."** HTTPS stops the attacker *impersonating* the site, because they lack a valid certificate, but a poisoned lookup can still redirect or deny service, and users who click through warnings are still caught.
- **"DNSSEC encrypts DNS."** No. DNSSEC *authenticates* records (so forgeries are rejected) but does not hide them. Hiding is what DoH/DoT do.
- **"It only happens on sketchy Wi-Fi."** Router malware, ISP-level hijacking and resolver cache attacks all happen far from the café.

### Defences

- Encrypted DNS (DoH/DoT) and validating resolvers with DNSSEC.
- HTTPS everywhere, HSTS, and never clicking past certificate warnings.
- Hardened routers and resolvers (source-port randomisation defeats the Kaminsky attack).
- On a managed network, the same layer-2 protections that stop [ARP poisoning](arppoisoning.md): DHCP snooping and Dynamic ARP Inspection.

### How it connects

- [ARP Poisoning](arppoisoning.md): the usual way to get into position for the local version.
- [Networking](networking.md) and [IP Datagrams](ipdatagrams.md): how name resolution fits the stack.
- [Exploitation](exploitation.md) and [Social Engineering](internetexploitation.md): the attacks this feeds.

The truth revealed: you can type the address perfectly and still end up in the wrong place, because the name was never the thing you were really trusting.

## Tools and Reading List

## Tools and Reading List

- [Ettercap](ettercap.md)
- [CISCO Layer 2 Attacks and Mitigation (PDF)](http://www.cisco.com/c/dam/global/en_ae/assets/exposaudi2009/assets/docs/layer2-attacks-and-mitigation-t.pdf)
- `arp`, `arp-scan`, `nslookup`, `dig`
- [DNSSEC (Cloudflare explainer)](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)
- [DNS over HTTPS (RFC 8484)](https://www.rfc-editor.org/rfc/rfc8484)
