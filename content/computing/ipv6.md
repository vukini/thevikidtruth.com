---
title: IP Version 6
date: '2016-12-05T12:55:59+04:00'
lastmod: '2016-12-05T13:17:48+04:00'
original_id: '{A702}'
original_name: ipv6
original_blob: blob/B/4/354.txt
revisions: 16
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: ipv6
draft: true
review: update
---

[Networking](networking.md) | [IPDatagrams <--](ipdatagrams.md) [IPv6](ipv6.md)

# IP Version 6

The orginal [RFC2460](http://www.faqs.org/rfcs/rfc2460.html) can be found here.

The following are my notes and interpretations of the document.

- **IPv6** increases the IP address size from 32 bits to **128 bits**
- IP headers are simplified compared to [IPv4](ipdatagrams.md)
- **Flow Labeling Capability**
- **New Authentication and Privacy Capabilities**
- **node**        - a device that implements IPv6.
- **router**      - a node that forwards IPv6 packets not explicitly
                   addressed to itself.
- **host**        - any node that is not a router.
- **upper layer**
  a protocol layer immediately above IPv6.  Examples are
                   transport protocols such as TCP and UDP, control
                   protocols such as ICMP, routing protocols such as OSPF,
                   and internet or lower-layer protocols being "tunneled"
                   over (i.e., encapsulated in) IPv6 such as IPX,
                   AppleTalk, or IPv6 itself.
- **link**
  a communication facility or medium over which nodes can
                   communicate at the link layer, i.e., the layer
                   immediately below IPv6.  Examples are Ethernets (simple
                   or bridged); PPP links; X.25, Frame Relay, or ATM
                   networks; and internet (or higher) layer "tunnels",
                   such as tunnels over IPv4 or IPv6 itself.
- **neighbors**   - nodes attached to the same link.
- **interface**  - a node's attachment to a link.
- **address**    - an IPv6-layer identifier for an interface or a set of
                   interfaces.
- **packet**     - an IPv6 header plus payload.
- **link MTU**    - the maximum transmission unit, i.e., maximum packet
                   size in octets, that can be conveyed over a link.
- **path MTU**    - the minimum link MTU of all the links in a path between
                   a source node and a destination node.

## IPv6 Header Format

- Much Simplified Format:
  ```
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |Version| Traffic Class |           Flow Label                  |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |         Payload Length        |  Next Header  |   Hop Limit   |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                                                               |
     +                                                               +
     |                                                               |
     +                         Source Address                        +
     |                                                               |
     +                                                               +
     |                                                               |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                                                               |
     +                                                               +
     |                                                               |
     +                      Destination Address                      +
     |                                                               |
     +                                                               +
     |                                                               |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  ```
- **Version**            4-bit Internet Protocol version number = 6.
- **Traffic Class**        8-bit traffic class field.
- **Flow Label**       20-bit flow label.
- **Payload Length**      16-bit unsigned integer.  Length of the IPv6
                          payload, i.e., the rest of the packet following
                          this IPv6 header, in octets.  (Note that any
                          extension headers present are
                          considered part of the payload, i.e., included
                          in the length count.)
- **Next Header**        8-bit selector.  Identifies the type of header
                          immediately following the IPv6 header.  Uses the
                          same values as the IPv4 Protocol field [RFC-1700
                          et seq.].
- **Hop Limit**        8-bit unsigned integer.  Decremented by 1 by
                          each node that forwards the packet. The packet
                          is discarded if Hop Limit is decremented to
                          zero.
- **Source Address**       128-bit address of the originator of the packet.
- **Destination Address**  128-bit address of the intended recipient of the
                          packet (possibly not the ultimate recipient, if
                          a Routing header is present).
