---
title: Ettercap
date: '2016-11-28T02:47:13+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A431}'
original_name: ettercap
original_blob: blob/B/2/433.txt
revisions: 1
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: ettercap
draft: false
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md) | [dns-poisoning](dnspoisoning.md)

# Ettercap

Here is an uncomfortable truth about local networks: **most of them still trust whoever is plugged in.** Ettercap is the classic tool that demonstrates what a machine sitting on the same LAN can do to that trust – mostly by quietly inserting itself into other people's conversations.

### What it is, in plain words

**Ettercap** is a free and open-source suite for **man-in-the-middle (MITM)** attacks on a local network. It can:

- discover hosts and the local gateway;
- poison **ARP** tables so traffic between two machines flows through you;
- sniff, log and – with filters – **modify** that traffic on the fly;
- dissect a long list of protocols (HTTP, FTP, SMTP, IMAP, SMB and many more);
- run from a curses text UI, a GTK GUI, or as a pure command-line / daemon tool.

It was first released around 2001, when switched Ethernet was becoming universal and people assumed switches made sniffing impossible. Ettercap showed that ARP poisoning put paid to that assumption. The project is still maintained; the current line is Ettercap 0.8.x.

### Why it matters

Understanding Ettercap is understanding a whole class of LAN attacks: ARP spoofing, DNS spoofing, SSL stripping, credential sniffing. You need that understanding for two reasons:

1. **Offensively**, in authorised penetration tests, to show a client what an attacker on their Wi-Fi or a compromised desktop could do.
2. **Defensively**, so you recognise the symptoms, know which mitigations work (static ARP, Dynamic ARP Inspection, 802.1X, HTTPS everywhere, VPNs), and don't assume "we're on a switch, so we're fine".

Tools like Bettercap have taken over much of Ettercap's day-to-day role in modern red-team work, but Ettercap remains the classic reference and is still useful.

### An everyday analogy: the helpful postman who opens your mail

Imagine a postman who, every morning, tells you "your friend's new address is *my* house" and tells your friend "your address is *my* house". All letters now go through him. He can read them, photocopy them, change a few words and send them on. ARP poisoning is that lie, told to two computers about each other's MAC addresses. Ettercap is the toolkit that postman carries.

```mermaid
flowchart LR
  A[Alice] -- "thinks Eve is Bob" --> E[Eve / Ettercap]
  B[Bob] -- "thinks Eve is Alice" --> E
  E -- "forwards (and maybe alters)" --> A
  E --> B
```

### A hands-on example (lab only)

**Only run this on a network you own or have written permission to test.** ARP poisoning on someone else's LAN is illegal in most places.

Use two VMs and a host-only or internal network in [VirtualBox](virtualbox.md) or KVM – never your real LAN. On the attacker VM (Debian/Ubuntu):

```bash
sudo apt install ettercap-common ettercap-text-only
# or: sudo xbps-install -S ettercap   # Void
```

Enable IP forwarding so traffic actually flows through you:

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

Interactive text UI:

```bash
sudo ettercap -T -Q -i eth0
# inside: press 'h' for help; scan for hosts; select two targets; start ARP poisoning
```

Or one shot from the command line – sniff between a client and the gateway:

```bash
sudo ettercap -T -q -i eth0 -M arp:remote /192.168.56.10// /192.168.56.1//
```

Write a filter that replaces a string in HTTP responses (saved as `funny.filter`):

```
if (ip.proto == TCP && tcp.dst == 80) {
    if (search(DATA.data, "Keep calm")) {
        replace("Keep calm", "Be curious");
        msg("rewrote a page\n");
    }
}
```

```bash
etterfilter funny.filter -o funny.ef
sudo ettercap -T -q -i eth0 -F funny.ef -M arp:remote /192.168.56.10// /192.168.56.1//
```

Watch the victim's browser. Unencrypted HTTP is putty in your hands; HTTPS is not – you'll see the ciphertext and, if you try to intercept TLS without a trusted certificate installed on the victim, they'll get a certificate warning. That warning *is* the defence working.

### Defences that actually work

- **HTTPS everywhere**, with certificate pinning where it matters.
- **Dynamic ARP Inspection (DAI)** and DHCP snooping on managed switches.
- Static ARP entries for critical pairs (gateway ↔ servers) on small networks.
- **802.1X** port authentication so random devices can't join.
- Client tools such as `arpwatch` or `arpon` that alert on ARP changes.
- Don't use open Wi-Fi; prefer WPA3-Enterprise or a VPN.

### Common misconceptions

- **"Switches stop sniffing."** They stop *passive* sniffing. Active MITM via ARP poisoning bypasses that.
- **"HTTPS makes Ettercap useless."** It stops you reading content. You can still deny service, map who talks to whom, or attack protocols that aren't encrypted.
- **"Ettercap is the modern tool."** Bettercap and mitmproxy are more actively developed for many workflows; Ettercap is the classic and still capable.
- **"IP forwarding is on by default."** It isn't – and if you forget to enable it, the victim simply loses connectivity, which is a very obvious attack.
- **"This is theoretical."** Public Wi-Fi and flat office LANs without DAI still fall to these techniques regularly.

### Connections

- [ARP Poisoning](arppoisoning.md) and [DNS Poisoning](dnspoisoning.md) – the techniques in detail.
- [Penetration Testing](penetrationtesting.md) and [Exploitation](exploitation.md).
- [Linux Security](linuxsecurity.md) and [Computer Security](computersecurity.md).
- [Firewalls](firewalls.md) and [Networking](networking.md).
- [VirtualBox](virtualbox.md) – build a lab, don't practise on the real network.
