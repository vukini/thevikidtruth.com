---
title: Datagram Encapsulation
date: '2016-12-07T12:19:03+04:00'
lastmod: '2016-12-07T12:20:50+04:00'
original_id: '{A754}'
original_name: datagramencapsulation
original_blob: blob/B/4/623.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: datagramencapsulation
draft: false
topics:
- networking-web
---

[Networking](networking.md)

# Datagram Encapsulation

I spent years in the wilderness before understanding this very simple concept.

**Please consider reading the sources at the bottom of the page where I got some
of the diagrams.**

![ipd](/assets/ipd.png)
{.center}

![absd](/assets/absd.png)
{.center}

### The plain idea

Encapsulation is how data travels across a network by being wrapped in layers, like a letter inside an envelope inside a mailbag inside a van. Your actual data (a web request, say) starts at the top of the protocol stack and, as it moves down toward the wire, each layer wraps it in its own header: the application data gets a TCP header (making a *segment*), that gets an IP header (making a *datagram* or *packet*), and that gets a frame header and trailer (making a *frame*) before the bits go out on the wire. At the other end the process runs in reverse: each layer strips off and reads its own header, then hands the contents up to the layer above.

### Why it matters

This one idea is the key that unlocks all of networking. Once you see that each layer only cares about its own envelope and ignores the contents, the whole stack makes sense: why IP does not care whether it is carrying TCP or UDP, why you can run the same web page over Wi-Fi or Ethernet or fibre, why a [firewall](firewalls.md) can filter on IP addresses without understanding the application. As my note says, it is a simple concept that, once grasped, clears years of confusion.

### An everyday analogy: the nested envelopes

You write a letter (the data). You put it in an envelope addressed to a person (that is like TCP, addressing the right *application/port*). You put that in a bigger envelope addressed to a building (IP, addressing the right *machine*). The postal van carries a mailbag between sorting offices (the frame, addressing the next *physical hop*). Each handler reads only the envelope meant for them: the van driver never opens your letter, and your friend never cares which van carried it. Every layer trusts the one below to deliver and the one above to make sense of the contents.

### A worked example: loading a web page

1. **Application (HTTP):** your browser writes `GET /index.html`.
2. **Transport (TCP):** wraps it with source and destination *ports* (e.g. to port 443) and a sequence number -> a **segment**.
3. **Network (IP):** wraps that with source and destination *IP addresses* -> a **datagram/packet** (this is the structure detailed on the [IP Datagrams](ipdatagrams.md) page).
4. **Link (Ethernet/Wi-Fi):** wraps that with source and destination *MAC addresses* and a checksum -> a **frame**.
5. The bits hit the wire. At each router along the way, only the outer frame and IP headers are read and rewritten; the TCP and HTTP contents ride along untouched until they reach the destination machine, which unwraps all the way back up to `GET /index.html`.

Those changing names, segment, datagram, packet, frame, are the "Protocol Data Units" my source links describe: the same data, named differently at each layer by what is currently wrapped around it.

### Common misconceptions

- **"The layers send separate messages."** There is one piece of data; each layer just adds or removes a wrapper around it.
- **"Routers understand my web request."** Routers mostly read the IP envelope (and rewrite the frame) and forward; they do not open the application data.
- **"Encapsulation adds huge overhead."** The headers are small compared to the payload, and the modularity they buy is enormous.

### How it connects

- [IP Datagrams](ipdatagrams.md) and [IPv6](ipv6.md): the detail of the network-layer envelope.
- [Networking](networking.md): the OSI/TCP-IP layer model this expresses.
- [Firewalls](firewalls.md): devices that read specific layers' envelopes.

The truth revealed: a network does not move your data so much as pass around a parcel of nested envelopes, each handler reading only its own label, and that polite mutual ignorance is exactly what lets the whole internet fit together.

## Reading List and Sources


- [tcp/ip guide IP Datagram](http://www.tcpipguide.com/free/t_IPDatagramEncapsulation.htm)
- [tcp/ip guide Encapsulation](http://www.tcpipguide.com/free/t_DataEncapsulationProtocolDataUnitsPDUsandServiceDa.htm)
- [tcp/ip guide Analogies](http://www.tcpipguide.com/free/t_UnderstandingTheOSIReferenceModelAnAnalogy.htm)
