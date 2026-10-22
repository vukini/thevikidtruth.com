---
title: ARP -Poisoning
date: '2016-11-28T02:26:41+04:00'
lastmod: '2016-11-28T02:36:15+04:00'
original_id: '{A427}'
original_name: arppoisoning
original_blob: blob/B/2/430.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: arppoisoning
draft: false
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md)

# ARP -Poisoning

The basic method here is called a **Man in the Middle AttacK**

ARP is resolving the IP address to the MAC Address.

So we need to make the other computers think we are the default gateway.
So we broad ARP packets which say, "the mac address of default gateway is the **machine H**"
That is we are going to broadcast ARP packkets with the IP Address of the default gateway.
The other machines on the Network with then update their ARP caches to reflect the MAC address of the **Man in the Middle**.

```
Machine      H       M1          V          M2

IP         . 10     .20         .30        .40
MAC          A       B           C          D
```

### The plain idea

On a local network, machines do not really deliver traffic by IP address; they deliver it by MAC address, the hardware address burned into each network card. ARP (Address Resolution Protocol) is the little announcement system that maps an IP address to a MAC address: "who has 192.168.1.1? Tell me your MAC." The catch, and it is the original sin of ARP, is that any machine can answer, and everyone believes the answer without checking.

ARP poisoning (or ARP spoofing) abuses that trust. The attacker's machine floods the network with ARP replies claiming "the gateway's IP belongs to *my* MAC address." Everyone updates their ARP cache, and from then on they send their internet-bound traffic to the attacker, who quietly forwards it on. The attacker is now in the middle: a **man-in-the-middle (MITM)** attack, as my note says.

### Why it matters

Once you sit in the middle, you can read, record or alter everything that is not end-to-end encrypted, and even tamper with some things that are if the user ignores warnings. It is the foundation of other local attacks: [DNS spoofing](dnspoisoning.md), session hijacking, credential capture. And it works on ordinary switched networks, because switches direct traffic by MAC address, which is exactly what ARP poisoning lies about.

The one piece of good news in 2026 is that end-to-end encryption blunts it. With HTTPS everywhere, HSTS, and encrypted DNS (DoH/DoT), an attacker in the middle mostly sees metadata rather than content. The attack is still very much alive on flat networks, in labs, and against anything still speaking plaintext.

### An everyday analogy: the dishonest mail sorter

Imagine an office where, to send a letter out, you first ask aloud "who takes the outgoing post?" and trust whoever shouts back. A dishonest colleague simply shouts "I do!" every time. Now all your outgoing mail passes through his hands. He reads it, maybe changes a figure, then drops it in the real postbox so nobody notices the delay.

### A worked example: the table above

In my diagram, **H** (10) is the attacker, **V** (30) the victim, and the real gateway is another machine. H sends the victim a forged ARP reply: "gateway IP is at MAC A" (H's own MAC). The victim's ARP cache now points the gateway's IP at H. H also tells the gateway that the victim's IP is at MAC A, so both directions flow through H.

Mechanically, with the classic tool Ettercap (or `arpspoof` from dsniff, or `bettercap` today):

```
# turn on forwarding so the victim still reaches the internet
sudo sysctl -w net.ipv4.ip_forward=1
# poison both the victim and the gateway
sudo bettercap -iface wlan0 -eval "set arp.spoof.targets 192.168.1.30; arp.spoof on; net.sniff on"
```

On the victim you can confirm the attack: `arp -a` shows the gateway's IP mapped to the attacker's MAC. Two different IPs sharing one MAC is the classic tell.

### Common misconceptions

- **"A switch protects me."** Switches route by MAC, which is precisely what the attack forges. Plain switching is no defence.
- **"HTTPS makes me completely safe."** It protects content, but the attacker still sees which sites you visit, can attempt downgrade attacks, and wins if you click through certificate warnings.
- **"It's only inbound."** Poisoning is set up in both directions so neither side notices a break.

### Defences

- **Dynamic ARP Inspection (DAI)** with DHCP snooping on managed switches drops forged ARP replies.
- **Static ARP entries** for critical hosts cannot be overwritten.
- **Port security** limits MAC addresses per switch port.
- **Encryption everywhere**, so that even a successful MITM sees little.
- **Detection** with tools like arpwatch, which alerts when an IP-to-MAC mapping changes.

### How it connects

- [DNS Poisoning](dnspoisoning.md): the usual next step once you are in the middle.
- [Exploitation](exploitation.md) and [Penetration Testing](penetrationtesting.md): where this sits in an attack.
- [Networking](networking.md): ARP lives at the boundary of layers 2 and 3.
- [IDS/IPS](idsips.md): how such attacks are detected.

The truth revealed: ARP was built for a trusting little network of friends, and the internet never stayed that small.

### Tools

- [Ettercap](ettercap.md)
- [bettercap](https://www.bettercap.org/)
- arpspoof (dsniff), arpwatch
