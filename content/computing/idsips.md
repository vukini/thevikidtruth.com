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
draft: false
topics:
- security
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
## Updating the notes for 2026

The commands above are from my training-lab days and reflect Snort 2 on an old Ubuntu box with SysV init scripts. Today Snort 3 is the actively developed version (Snort 2 is legacy), its configuration is a Lua file (`snort.lua`) rather than `snort.conf`, and services are managed with `systemctl` rather than `/etc/init.d`. Suricata and Zeek have become the other two big open-source names. The ideas, though, have not changed at all.

### The plain idea

An **intrusion detection system (IDS)** watches traffic or activity and raises an alarm when something looks like an attack. It is a burglar alarm: it notices and tells you (alert, log, email), but it does not stop anything. An **intrusion prevention system (IPS)** does everything an IDS does and can also act, by dropping the offending packets or resetting the connection, because it sits *inline*, in the path of the traffic, rather than off to the side.

There are two places to put one, as in my diagram:

- **NIDS** (network-based) watches a copy of the network traffic, usually fed from a switch's SPAN (mirror) port or a network tap next to the firewall.
- **HIDS** (host-based) runs on a single machine and watches its logs, files and processes. Wazuh and OSSEC are common open-source examples; on desktops this job has largely merged into EDR (endpoint detection and response) products.

Detection works in two broad ways. **Signature** detection matches known patterns ("this byte sequence is the EternalBlue exploit"). **Anomaly** detection learns what normal looks like and flags departures from it ("this server never talks to Russia at 3am, and now it does").

### Why it matters

Firewalls decide what is allowed in. They say nothing about whether allowed traffic is malicious. A web server must accept connections on port 443, and an attacker's exploit arrives on port 443 too. IDS/IPS looks *inside* the allowed traffic. It is also often how you learn you have been breached at all: an alert from a sensor can be the difference between finding an intruder in a day or in a year.

### An everyday analogy: the shop

The [firewall](firewalls.md) is the shop's locked door and opening hours. The IDS is the CCTV camera and the guard watching the monitors: they see the shoplifter and radio for help. The IPS is the guard standing at the door who can physically stop someone walking out with the goods. Stand the guard in the doorway and you also risk them stopping honest customers, which is why IPS rules are tuned more carefully than IDS rules.

### A worked example: a Snort 3 rule

Here is a simple rule that alerts on an ICMP ping sweep reaching the network, the sort of thing my lab exercise triggered with nmap:

```
alert icmp any any -> $HOME_NET any (
    msg:"ICMP ping detected";
    itype:8;
    sid:1000001; rev:1;
)
```

Read it as a sentence: *alert* on *ICMP* traffic from *any* address and port *to* my home network, *any* port, when the ICMP type is 8 (echo request); label it with this message and a unique signature ID (local rules use IDs above 1,000,000).

On a modern system you would run something like:

```
sudo systemctl restart snort3            # service name varies by distro
snort -c /etc/snort/snort.lua -R local.rules -i eth0 -A alert_fast
```

and from another machine, `nmap -sn 192.168.100.0/24` would light up the console. In IPS mode, change `alert` to `drop` and run Snort inline (for example with the `afpacket` DAQ in inline mode) and those packets never arrive.

### Common misconceptions

- **"An IDS will catch everything."** Signatures miss new attacks, and most traffic today is encrypted with TLS, which a network sensor cannot read without decrypting it. Host-based sensors and logs fill the gap.
- **"More alerts means more security."** Untuned sensors bury analysts in false positives until real alerts are ignored. Fewer, well-tuned rules beat thousands of noisy ones.
- **"IPS is just a better IDS."** It trades visibility for risk: a bad rule in an inline IPS can block legitimate business traffic.
- **"A honeypot is an IDS."** Related but different. A [honeypot](honeypots.md) is a decoy; anything that touches it is suspicious by definition.

### How it connects

- [Firewalls](firewalls.md): the first line, which IDS/IPS complements.
- [Honeypots](honeypots.md): the decoy in my diagram on vlan2.
- [Secure Network Architecture](securenetworkarchitecture.md): where sensors go in a well-designed network.
- [Exploitation](exploitation.md) and [Penetration Testing](penetrationtesting.md): the attacks these systems are built to see.

The truth revealed: detection is not about building a wall nobody can climb. It is about making sure that when someone does, you hear them.

## Links

- [Snort 3](https://www.snort.org/snort3)
- [Suricata](https://suricata.io/)
- [Zeek](https://zeek.org/)
- [Wazuh](https://wazuh.com/)
