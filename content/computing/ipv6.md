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
draft: false
topics:
- networking-web
---

[Networking](networking.md) | [IPDatagrams <--](ipdatagrams.md) [IPv6](ipv6.md)

# IP Version 6

The orginal [RFC 2460](https://www.rfc-editor.org/rfc/rfc2460) (now superseded by [RFC 8200](https://www.rfc-editor.org/rfc/rfc8200)) can be found here.

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

### The plain idea

IPv6 is the current version of the Internet Protocol, the system that gives every device an address and routes packets between them. Its headline change is the address size: IPv4 used 32-bit addresses (about 4.3 billion of them), and IPv6 uses **128-bit** addresses, an almost unimaginable number, roughly 340 undecillion (3.4 × 10³⁸). It also tidies up the header, builds in features that were bolt-ons in IPv4, and does away with some old complications.

### Why it matters

The world ran out of IPv4 addresses. Every phone, laptop, server, camera and smart bulb needs an address, and 4.3 billion was never going to be enough. The stopgap was NAT (many devices hiding behind one public address), which works but breaks the internet's original promise that any device can talk directly to any other. IPv6 restores that end-to-end model with addresses to spare, which is why, by 2026, a large share of global internet traffic, well over 40% to Google, and the majority in some countries, already runs over IPv6.

### An everyday analogy: running out of phone numbers

Imagine a country whose phone numbers filled up, so everyone had to share a single office switchboard (NAT) and dial extensions to reach each other. It works, but you can no longer be called directly from outside. IPv6 is like moving to much longer numbers, so long that every grain of sand could have its own, and handing a unique, directly-dialable number back to every device.

### A worked example: reading an IPv6 address

IPv6 addresses are written as eight groups of four hex digits:

```
2001:0db8:0000:0000:0000:ff00:0042:8329
```

Two shorthand rules make them bearable: drop leading zeros in each group, and replace one run of all-zero groups with `::`. So the address above becomes:

```
2001:db8::ff00:42:8329
```

You will also meet `::1` (localhost, the IPv6 equivalent of 127.0.0.1) and addresses starting `fe80::` (link-local, auto-configured on every interface). The header fields in my RFC notes above reflect the simplification: a fixed-size header, the old fragmentation and checksum fields removed (handled elsewhere), a **Flow Label** for prioritising streams, and **Hop Limit** replacing IPv4's "Time To Live". A nice touch is **SLAAC** (stateless address autoconfiguration): a device can often generate its own valid address from the router's advertised prefix, no DHCP server required.

### A 2026 update

My notes cite RFC 2460; that was obsoleted by **RFC 8200** in 2017, which is the current IPv6 specification. Adoption, slow for years, is now substantial and steady. In practice most networks run **dual stack** (IPv4 and IPv6 together) during the long transition, and mobile networks in particular lean heavily on IPv6. The old IPsec "built-in security" selling point turned out to be optional in practice; real-world security still comes from TLS and configured IPsec, not from IPv6 itself.

### Common misconceptions

- **"IPv6 is just IPv4 with longer addresses."** The header, autoconfiguration, neighbour discovery (replacing ARP) and the end of NAT-by-necessity are real changes.
- **"IPv6 is automatically more secure."** The privacy and authentication hooks exist but are not magic; misconfiguration and unencrypted traffic are still unsafe.
- **"We don't need it yet."** IPv4 exhaustion is real; new networks increasingly must use IPv6, and ignoring it leaves half the internet's addressing unlearned.
- **"NAT is a firewall."** NAT hid devices as a side effect; it is not a security control, and IPv6's return to end-to-end addressing makes a real [firewall](firewalls.md) more important, not less.

### How it connects

- [IP Datagrams](ipdatagrams.md): the IPv4 header this simplifies.
- [Datagram Encapsulation](datagramencapsulation.md): where IP sits in the stack.
- [Networking](networking.md): the broader protocol picture.
- [Firewalls](firewalls.md): why end-to-end addressing needs real filtering.

The truth revealed: IPv6 is less a new internet than the old internet given enough room to be itself again, every device with its own address, able to speak directly to any other, the way it was meant to work before we ran out of numbers.
