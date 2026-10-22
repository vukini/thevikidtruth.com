---
title: Network Protocols and Technologies
date: '2016-11-30T05:18:36+04:00'
lastmod: '2022-08-04T02:01:03+04:00'
original_id: '{A532}'
original_name: networking
original_blob: blob/B/10/731.txt
revisions: 13
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: networking
draft: false
---

[Quicklinks](quicklinks.md) | [Reading Lists](readinglist.md) | [Computing](computing.md) |
[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) |
  [The Compiler](thecompiler.md) |
  [Identifiers](identifier.md) |
  [Literals](literals.md) |
  [storage_linkage](storagelinkage.md) | [Networking](networking.md)

# Network Protocols and Technologies

It probably hasn't escaped you attention that Computer Networks (Social and Otherwise) are possibly one of the most
important technologies invented in the last century. But how do they work? I mean really work under the hood?

Well you have come to the right place.

## Network Technologies & Relay Systems

- [Ethernet & IEEE 802.3](ethernet.md "MISSING PAGE")
- [Token Ring](tokenring.md "MISSING PAGE")
- [Fiber Distributed Data Interface](fddi.md "MISSING PAGE")
- [Relay Systems](relaysystems.md "MISSING PAGE")
- [WAN](wan.md "MISSING PAGE")

## Addressing

- [Addressing Schemes](addressingschemes.md "MISSING PAGE")
- [Routing](routing.md "MISSING PAGE")
- [Address Resolution Protocol MAC Addresses](arp.md "MISSING PAGE")
- [Reverse Address Resolution Protocol](rarp.md "MISSING PAGE")
- [Subnetting](subnetting.md "MISSING PAGE")

## Main Protocols

- [Multi-Homing](multi-homing.md "MISSING PAGE")
- [IP Datagrams](ipdatagrams.md)
- [IP Version 6](ipv6.md)
- [Internet Control Messaging Protocol (ICMP)](icmp.md "MISSING PAGE")
- [Transmission Control Protocol (TCP)](tcp.md "MISSING PAGE")
- [User Datagram Protocol (UDP)](udp.md "MISSING PAGE")
- [The Routing Information Protocol (RIP)](rip.md "MISSING PAGE")
- [Telnet](telnet.md "MISSING PAGE")
- [Rlogin](rlogin.md "MISSING PAGE")
- [File Transfer Protocol (FTP)](ftp.md "MISSING PAGE")
- [Simple Mail Transfer Protocol (SMTP)](smtp.md "MISSING PAGE")
- [Booting Internet Hosts](bootp.md "MISSING PAGE")
- [TFTP](tftp.md "MISSING PAGE")
- [Simple Network Management Protocol (SNMP)](snmp.md "MISSING PAGE")

## Secondary Protocols

- [Echo Protocol](echoprotocol.md "MISSING PAGE")
- [DiscardProtocol](discardprotocol.md "MISSING PAGE")
- [TimeProtocol](timeprotocol.md "MISSING PAGE")
- [DaytimeProtocol](daytimeprotocol.md "MISSING PAGE")
- [NetworkTimeProtocol](networktimeprotocol.md "MISSING PAGE")
- [LinePrinterDaemonProtocol](lineprinterdaemonprotocol.md "MISSING PAGE")
- [SYSLOG](syslog.md "MISSING PAGE")
- [Finger](finger.md "MISSING PAGE")
- [Whois](whois.md "MISSING PAGE")
- [Character Generation Protocol](charactergenerationprotocol.md "MISSING PAGE")
- [QouteOfTheDay](qouteoftheday.md "MISSING PAGE")
- [UsersProtocol](usersprotocol.md "MISSING PAGE")

## Other Considerations

- [Serial Line IP](slip.md "MISSING PAGE")
- [Filtering Packets on Different Protocols](filtering.md "MISSING PAGE")
- <!-- 
  -{={}}
  -{={}}
  -{={}}
   -->

## Request for Comments

Before you start anywhere you probably want to keep this diagram in your mind. I lifted &
modified from RFC-1180. I spent a lot of time confused about these diagrams and what
they meant. If you are too, then please [read this first](datagramencapsulation.md).

```
                          Module Diagram                      Protocol Layers (OSI &
                                                                             TCP/IP*)
                     ----------------------------             Layer-4*--------------
                     |    network applications  |             |Layer 7.Application |
                     |...   \\ | /  .. \\ | /  ...|             |Layer 6.Presentation|
                     |     -----      -----     |             |Layer 5. Session    |
                     |     |TCP|      |UDP|     |             |Layer 4. Transport  |
                     |     -----      -----     |             ----------------------
                     |         \\      /         |
                     |         --------         | roughly
                     |         |  IP  |         | translating  Layer 3 .Internetwork
                     |  -----  -*------         | to
                     |  |ARP|   |               |
                     |  -----   |               |
                     |      \\   |               |
                     |      ------              |
                     |      |ENET|              |               Layer 2. Link
                     |      ---@--              |
                     ----------|-----------------
                               |
         ----------------------o---------                       Layer 1. Physical
             Ethernet Cable
```

There are more that 2500 of this documents. An impossible task.

Below is a list of the most important ones to read.

- [RFC-1180 A TCP/IP Tutorial](rfc-1180.md "MISSING PAGE")
- [RFC-791 INTERNET PROTOCOL](ipdatagrams.md)
- [RFC-793 Transmission Control Protocol](rfc-793.md "MISSING PAGE")
- [RFC-2460 Internet Protocol, Version 6 (IPv6) Specification](ipv6.md)

## Links, Sources and Reading List

- [Faqs RFC's](http://www.faqs.org/rfcs)
- [http://www.rfc-editor.org](http://www.rfc-editor.org)
- [ TCP/IP STACK](https://en.m.wikibooks.org/wiki/A-level_Computing_2009/AQA/Computer_Components,_The_Stored_Program_Concept_and_the_Internet/Structure_of_the_Internet/TCP_IP_protocol_stack
  )
- [the geek stuff ip protocol](http://www.thegeekstuff.com/2012/03/ip-protocol-header/)
- [MS IP Tech paper](https://technet.microsoft.com/en-us/library/cc786128(v=ws.10).aspx)
- [tcpipguide](http://www.tcpipguide.com/free/t_MessageFormattingHeadersPayloadsandFooters.htm)
   [https://en.m.wikipedia.org/wiki/Transmission_Control_Protocol](https://en.m.wikipedia.org/wiki/Transmission_Control_Protocol)
