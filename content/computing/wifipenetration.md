---
title: Wifi Penetration
date: '2016-11-30T02:00:02+04:00'
lastmod: '2016-12-13T20:51:13+04:00'
original_id: '{A527}'
original_name: wifipenetration
original_blob: blob/B/5/247.txt
revisions: 12
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: wifipenetration
draft: false
topics:
- security
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) |
  [Picolisp Machine](pilmachine.md) |
  [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) |
  [Operating Systems](os.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) |
  [Social Engineering](internetexploitation.md) |
  [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) | [wifi-penetration](wifipenetration.md)

# Wifi Penetration

The [Wifi-Alliance](http://www.wi-fi.org/) is the worldwide network of companies that brings you Wi-Fi!

## Protocols

- wep - Wired Equivalent Privacy
  ```
      Initialization Vector Packet - are clear text and encrypt the next 3 data packets
         IV ---------> | Access Point | ~~~~~~~~~~~~~~~~~~~~~~~~~~[Victim]
       Packet                            Air Crack
       64-Bit                          50k packets -IV ---> Key
  password  Random                      Cracked in 10-15mins
  ```
- WPA - Wifi Protected Access
- WPA2 -Wifi Protected Access 2
  ```
       Authentication Header - AES Encrypted (symmetric)
            [AH]
          /     \
       [AP]      [V]
           \    /
            [H]
  ```

## Techniques

- Option 1 
  ```
   airmon-ng start wlan0
   airodump-ng mon0
   airodump-ng -c #channelid -w filename --bbsid #(mac address of client) mon0
   aireplay-ng -0 0 -a #BSSID mon0
   aircrack-ng file -w /pentest/passwords/wordlist/darkcode.lst
  ```

### The plain idea

Wi-Fi security is about one hard problem: your data travels through the air, where anyone nearby can listen. So every Wi-Fi standard is an attempt to encrypt that air so only people who know the password can read it. My notes above walk through the generations, WEP, WPA, WPA2, and each one is a patch on the broken promises of the one before. "Wi-Fi penetration" means testing how well that encryption actually holds.

### Why it matters

A wired network has a physical boundary: to tap it you must plug in. Wi-Fi has no such wall; its boundary is wherever the signal reaches, often the street outside. If the encryption is weak, an attacker never has to touch your building. Knowing how each protocol fails is how you choose the right one and spot a network you should not trust.

### An everyday analogy: shouting across a crowded room

Talking over Wi-Fi is like holding a conversation by shouting across a packed café. Everyone can hear the sound; encryption is agreeing a private code beforehand so that, although they hear you, only your friend understands. WEP was a laughably simple code cracked in minutes. WPA2 is a strong one. WPA3 adds the trick that even if someone records the whole conversation and later learns the code, they still cannot decode what was already said.

### A worked example: why WEP fell, and what replaced it

My WEP diagram shows the fatal flaw. WEP sends small "initialisation vectors" (IVs) in clear text, and reuses them often. Capture enough packets, about 50,000 as my note says, and the key falls out by statistics, in ten to fifteen minutes. That is the classic aircrack-ng attack. WEP has been **deprecated since 2004 and must never be used.**

The modern equivalent against WPA/WPA2 is the *handshake capture*, which my "Techniques" commands sketch:

```
sudo airmon-ng start wlan0                         # monitor mode
sudo airodump-ng wlan0mon                          # find the target BSSID/channel
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w cap wlan0mon
sudo aireplay-ng -0 2 -a AA:BB:CC:DD:EE:FF wlan0mon   # deauth to force a reconnect
sudo aircrack-ng cap-01.cap -w wordlist.txt           # crack the captured handshake offline
```

Crucially, WPA2 is **not** cracked live. You capture the four-way handshake when a device joins, then guess the password *offline* against a wordlist. So WPA2's real weakness is a weak, guessable password, not the protocol. A long random passphrase makes this attack hopeless.

### A 2026 update

The big news since these notes: **WPA3** arrived in 2018 and is now standard on current hardware. It replaces the handshake with SAE (Simultaneous Authentication of Equals, the "Dragonfly" exchange), which defeats the offline-guessing attack above and adds forward secrecy. The practical advice today:

- Use **WPA3**, or **WPA2-AES (CCMP)** at minimum; never WEP or WPA1, and avoid TKIP.
- Choose a **long passphrase** (a random phrase of several words), which is the single biggest factor.
- Disable **WPS** (the push-button/PIN setup), which has its own well-known flaws.
- Treat open public Wi-Fi as hostile and rely on HTTPS and a VPN, since the "air" there is unencrypted for everyone.

### Common misconceptions

- **"WPA2 is broken, so it's useless."** The KRACK weakness was patched, and the main risk remains a weak password, not the cipher.
- **"Hiding the network name (SSID) secures it."** It is trivially discovered and only inconveniences you.
- **"MAC address filtering keeps attackers out."** MACs are sent in clear text and easily spoofed; see [internet exploitation](internetexploitation.md).
- **"A longer password slows my connection."** It does not; it only slows attackers.

### How it connects

- [Encryption](encryption.md): the symmetric ciphers (AES) and key exchange underneath.
- [ARP Poisoning](arppoisoning.md): a common next step once an attacker is on the Wi-Fi.
- [Networking](networking.md): where Wi-Fi sits in the stack.
- [Exploitation](exploitation.md): the network vector this belongs to.

The truth revealed: Wi-Fi security is a thirty-year arms race over the one thing you cannot hide, radio in the open air, and today it mostly comes down to a password long enough that no wordlist will ever hold it.

### Tools, Sources and Links

- [aircrack-ng suite](https://www.aircrack-ng.org/)
- [hashcat (offline cracking)](https://hashcat.net/hashcat/)
- [Wi-Fi Alliance on WPA3](https://www.wi-fi.org/discover-wi-fi/security)
