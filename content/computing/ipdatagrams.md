---
title: IP Datagrams
date: '2016-12-05T11:02:14+04:00'
lastmod: '2016-12-05T12:55:01+04:00'
original_id: '{A701}'
original_name: ipdatagrams
original_blob: blob/B/4/334.txt
revisions: 30
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: ipdatagrams
draft: true
review: update
---

[Networking](networking.md) -> [IPv6](ipv6.md)

# IP Datagrams

This is the original 1981 [RFC791](http://www.faqs.org/rfcs/rfc791.html) doc.

I never really understood how IP worked until I read this document. So I highly recommend it.
Following are my notes and interpretations:

- **Data Transmission Order**
  The order of transmission of the header and data described in this
  document is resolved to the octet level.  Whenever a diagram shows a
  group of octets, the order of transmission of those octets is the normal
  order in which they are read in English.  For example, in the following
  diagram the octets are transmitted in the order they are numbered.
  ```
      0                   1                   2                   3
      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |       1       |       2       |       3       |       4       |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |       5       |       6       |       7       |       8       |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |       9       |      10       |      11       |      12       |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  ```
  Whenever an octet represents a numeric quantity the **left most bit** in the
  diagram is the **high order or most significant bit**.  That is, the bit
  labeled 0 is the most significant bit.  For example, the following
  diagram represents the value 170 (decimal).
  ```
                              0 1 2 3 4 5 6 7
                             +-+-+-+-+-+-+-+-+
                             |1 0 1 0 1 0 1 0|
                             +-+-+-+-+-+-+-+-+
  ```
- **The internet protocol** provides for
    transmitting blocks of data called **datagrams** from sources to
    destinations, where sources and destinations are hosts identified by
    fixed length addresses.
- The internet protocol also provides for
    **fragmentation and reassembly** of long datagrams, if necessary, for
    transmission through "small packet" networks.
- The internet protocol is **specifically limited in scope to provide the
    functions necessary to deliver a package of bits (an internet
    datagram) from a source to a destination over an interconnected system
    of networks.**
- This protocol calls on **local network protocols** to carry
    the internet datagram to the next gateway or destination host.
- The internet protocol implements two basic functions:
    **addressing** and
    **fragmentation**.
- The internet protocol treats **each internet datagram** as an **independent
    entity unrelated to any other internet datagram**.
- The internet protocol uses four key mechanisms in providing its
    service:  **Type of Service, Time to Live, Options, and Header Checksum**
- The internet protocol does not provide a reliable communication
    facility.  There are no acknowledgments either end-to-end or
    hop-by-hop.  There is no error control for data, only a header
    checksum.  There are no retransmissions.  There is no flow control.
- The following diagram illustrates the place of the internet protocol
    in the **protocol hierarchy:**
  ```
                   +------+ +-----+ +-----+     +-----+
                   |Telnet| | FTP | | TFTP| ... | ... |
                   +------+ +-----+ +-----+     +-----+
                         |   |         |           |
                        +-----+     +-----+     +-----+
                        | TCP |     | UDP | ... | ... |
                        +-----+     +-----+     +-----+
                           |           |           |
                        +--------------------------+----+
                        |    Internet Protocol & ICMP   |
                        +--------------------------+----+
                                       |
                          +---------------------------+
                          |   Local Network Protocol  |
                          +---------------------------+
                           Protocol Relationships
  ```
- Example of how a packet travels across the network:
  ```
  Application                                           Application
     Program                                                   Program
            \\                                                   /
         Internet Module      Internet Module      Internet Module
               \\                 /       \\                /
               LNI-1          LNI-1      LNI-2         LNI-2
                  \\           /            \\          /
                 Local Network 1           Local Network 2
                              Transmission Path
  ```
- In the routing of messages from one internet module to another,
    datagrams may need to traverse a network whose maximum packet size is
    smaller than the size of the datagram.  To overcome this difficulty, a
    **fragmentation mechanism** is provided in the internet protocol.
- A distinction is made between **names, addresses, and routes**.
     A name indicates what we seek.
     **An address indicates where it is.**
      A route indicates how to get there.
      The internet protocol deals
      primarily with addresses.
- Some hosts will also have several physical
      interfaces (multi-homing).
- There are three formats or classes of internet
      addresses:
    1. in class a, the high order bit is zero, the next 7 bits
          are the network, and the last 24 bits are the local address;
      ```
          Bit                       1                   2                   3
          no.   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
                -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
                0 N N N N N N N L L L L L L L L L L L L L L L L L L L L L L L L
      ```
    1. in
          class b, the high order two bits are one-zero, the next 14 bits are
          the network and the last 16 bits are the local address;
      ```
          Bit                       1                   2                   3
          no.   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
                -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
                1 0 N N N N N N N N N N N N N N L L L L L L L L L L L L L L L L
      ```
    1. in class c,
          the high order three bits are one-one-zero, the next 21 bits are the
          network and the last 8 bits are the local address.
      ```
          Bit                       1                   2                   3
          no.   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
                -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
                1 1 0 N N N N N N N N N N N N N N N N N N N N N L L L L L L L L
      ```
    1. ```
      Address Formats:
            High Order Bits   Format                           Class
            ---------------   -------------------------------  -----
                  0            7 bits of net, 24 bits of host    a
                  10          14 bits of net, 16 bits of host    b
                  110         21 bits of net,  8 bits of host    c
                  111         escape to extended addressing mode
      ```
  Fragmentation of an internet datagram is necessary when it
      originates in a local net that allows a large packet size and must
      traverse a local net that limits packets to a smaller size to reach
      its destination
  The internet fragmentation and reassembly procedure needs to be able
      to break a datagram into an almost arbitrary number of pieces that
      can be later reassembled.
- The internet fragmentation and reassembly procedure needs to be able
      to break a datagram into an almost arbitrary number of pieces that
      can be later reassembled.
- The receiver of the fragments uses the
      identification field to ensure that fragments of different datagrams
      are not mixed.
- The fragment offset field tells the receiver the
      position of a fragment in the original datagram.
- The fragment
      offset and length determine the portion of the original datagram
      covered by this fragment.
- The more-fragments flag indicates (by
      being reset) the last fragment.  These fields provide sufficient
      information to reassemble datagrams.
- The originating protocol module of
      an internet datagram sets the identification field to a value that
      must be unique for that source-destination pair and protocol for the
      time the datagram will be active in the internet system.
- To fragment a long internet datagram, an internet protocol module
      (for example, in a gateway), creates two new internet datagrams and
      copies the contents of the internet header fields from the long
      datagram into both new internet headers.  The data of the long
      datagram is divided into two portions on a 8 octet (64 bit) boundary
      (the second portion might not be an integral multiple of 8 octets,
      but the first must be).  Call the number of 8 octet blocks in the
      first portion NFB (for Number of Fragment Blocks).
- The first
      portion of the data is placed in the first new internet datagram,
      and the total length field is set to the length of the first
  datagram.  The more-fragments flag is set to one.  The second
      portion of the data is placed in the second new internet datagram,
      and the total length field is set to the length of the second
      datagram.  The more-fragments flag carries the same value as the
      long datagram.  The fragment offset field of the second new internet
      datagram is set to the value of that field in the long datagram plus
      NFB.
- This procedure can be generalized for an n-way split, rather than
      the two-way split described.
- **Gateways** implement internet protocol to forward datagrams between
    networks.  Gateways also implement the Gateway to Gateway Protocol
    (GGP) to coordinate routing and other internet control
    information.
- In a gateway the higher level protocols need not be implemented and
    the GGP functions are added to the IP module.
  ```
                     +-------------------------------+
                     | Internet Protocol & ICMP & GGP|
                     +-------------------------------+
                             |                 |
                   +---------------+   +---------------+
                   |   Local Net   |   |   Local Net   |
                   +---------------+   +---------------+
  ```
- IP Header
  ```
      0                   1                   2                   3
      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |Version|  IHL  |Type of Service|          Total Length         |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |         Identification        |Flags|      Fragment Offset    |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |  Time to Live |    Protocol   |         Header Checksum       |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                       Source Address                          |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                    Destination Address                        |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                    Options                    |    Padding    |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                      Example Internet Datagram Header
  ```
- Version:  4 bits
      The Version field indicates the format of the internet header.  This
      document describes version 4.
- IHL:  4 bits
      Internet Header Length is the length of the internet header in 32
      bit words, and thus points to the beginning of the data.  Note that
      the minimum value for a correct header is 5.
- Type of Service:  8 bits
  ```
     0     1     2     3     4     5     6     7
        +-----+-----+-----+-----+-----+-----+-----+-----+
        |                 |     |     |     |     |     |
        |   PRECEDENCE    |  D  |  T  |  R  |  0  |  0  |
        |                 |     |     |     |     |     |
        +-----+-----+-----+-----+-----+-----+-----+-----+
  D = Delay, T=Throughput, R=Reliability
          Precedence
            111 - Network Control
            110 - Internetwork Control
            101 - CRITIC/ECP
            100 - Flash Override
            011 - Flash
            010 - Immediate
            001 - Priority
            000 - Routine
  ```
- Total Length:  16 bits
      Total Length is the length of the datagram, measured in octets,
      including internet header and data.  This field allows the length of
      a datagram to be up to 65,535 octets.
- Identification:  16 bits
      An identifying value assigned by the sender to aid in assembling the
      fragments of a datagram.
- Flags:  3 bits
  ```
      Various Control Flags.
        Bit 0: reserved, must be zero
        Bit 1: (DF) 0 = May Fragment,  1 = Don't Fragment.
        Bit 2: (MF) 0 = Last Fragment, 1 = More Fragments.
            0   1   2
          +---+---+---+
          |   | D | M |
          | 0 | F | F |
          +---+---+---+
    Fragment Offset:  13 bits
  ```
- Time to Live:  8 bits
      This field indicates the maximum time the datagram is allowed to
      remain in the internet system.  If this field contains the value
      zero, then the datagram must be destroyed.
- Protocol:  8 bits
      This field indicates the next level protocol used in the data
      portion of the internet datagram.
- Header Checksum:  16 bits
      A checksum on the header only.
      The checksum algorithm is:
        The checksum field is the 16 bit one's complement of the one's
        complement sum of all 16 bit words in the header.  For purposes of
        computing the checksum, the value of the checksum field is zero.
- There are lots of options: best to see the RFC791 directly
- **Example 1:**
    This is an example of the **minimal data carrying internet datagram:**
  ```
      0                   1                   2                   3
      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |Ver= 4 |IHL= 5 |Type of Service|        Total Length = 21      |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |      Identification = 111     |Flg=0|   Fragment Offset = 0   |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |   Time = 123  |  Protocol = 1 |        header checksum        |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                         source address                        |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                      destination address                      |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |     data      |
     +-+-+-+-+-+-+-+-+
                         Example Internet Datagram
  ```
- **Example 2:**
    In this example, we show first a **moderate size internet datagram** (452
    data octets), then two internet fragments that might result from the
    fragmentation of this datagram if the maximum sized transmission
    allowed were 280 octets.
  ```
      0                   1                   2                   3
      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |Ver= 4 |IHL= 5 |Type of Service|       Total Length = 472      |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |     Identification = 111      |Flg=0|     Fragment Offset = 0 |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |   Time = 123  | Protocol = 6  |        header checksum        |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                         source address                        |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                      destination address                      |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                             data                              |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |                             data                              |
     \                                                               \
     \                                                               \
     |                             data                              |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |             data              |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                         Example Internet Datagram
  ```
