---
title: Enumeration
date: '2016-11-28T00:20:24+04:00'
lastmod: '2016-11-28T00:55:54+04:00'
original_id: '{A424}'
original_name: enumeration
original_blob: blob/B/2/400.txt
revisions: 11
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: enumeration
draft: true
review: update
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md)

# Enumeration

## Types

### Black Box

Simulate Outsider: no information is given
    Bug Bounty

#### DNS Enumeration

Most Organisations host multiple DNS servers:

- Root DNS
- Subordinate DNS
- ISP DNS
- Primary & Secondary - Withing the Organisation
    - Broadcast
    - Zone Transfer
- Local Host Files

##### Tools

- dnsenum
- dnsmap
- dnsrecon
- dnswalk
- fierce

So in an attack the intruder is trying to get access and obtain the internal registry entries of the primary DNS Server.

### White Box

Simulate Internal Attacker: provide some information
    for example:
    
- wifi passwords
- login info

#### SNMP Enumeration

[Simple Network Management Protocol](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol) - it allows for centralised monitoring and forwarding of log files.

This protocol normally is installed on Windows Machines.

In ubuntu you can install the software with `sudo apt-get install snmp`

All Machines on the same network have a shared **community name"** often called **public**

##### Tools

- snmp-bridge-mib  snmp-check       snmpgetnext      snmpstatus       snmpusm
  snmpbulkget      snmpconf         snmpinform       snmptable        snmpvacm
  snmpbulkwalk     snmpdelta        snmpkey          snmptest         snmpwalk
  snmpc            snmpdf           snmpnetstat      snmptranslate
  snmpcheck        snmpget          snmpset          snmptrap
- snmpenum

### Grey Box

Split time  60/40 between Black and White Box scenarios

## Sources

[Security Assured Blog](http://securityassured.wordpress.com)
