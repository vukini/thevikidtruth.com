---
title: Crytography
date: '2016-11-29T05:18:10+04:00'
lastmod: '2016-12-01T02:40:48+04:00'
original_id: '{A460}'
original_name: encryption
original_blob: blob/B/3/503.txt
revisions: 7
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: encryption
draft: true
review: update
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) | [encryption](encryption.md) |
[IDS/IPS](idsips.md)

# Crytography

```
                           Cryto
			   /   \\
                      visible invisible
                       /   \\        \\
	       encryption  hashing   stagenography
	       /       \\
	asymmetric   symmetric
	/       \\          \\
    publicKey   privateKey   uniqueKey
```

### Symmetric Key

- DES
- 3DES
- AES*

There is a problem in symmetric encryption because of the number of keys required for N number of
people in a network. Which is:

```
    Number of keys required is:   N(N-1)
                              -----
			        2
```

For each person in the network I need to have a unique key (N), the next person in the Network needs to keep (N-1) keys, etc.. etc... so the number of keys becomes N + (N-1).

## Asymmetric Encryption

1. Generate Key Pair
1. Share Public Key
1. Import the Public Key of the Receiver
1. Encrypt - Public - Receiver
1. Decrypt - Private - Receiver

- DEFFIE-HELLMAN
- RSA*
- PGP -
     [MIT PGP Server](http://pgp.mit.edu)

### Tools

- Mailvelope - Chrome Extension for PGP

```
    Number of keys required is:   2N
```

## Hashing

- MD5
- SHA1
- SHA256*

## Stegnography

ADS (alternate data stream) -  Vulnerability - DLP (Data Leak/Lock Prevention) tools

- image hiding

### Tools, Links and Reading Lists

- [OpenStego](http://www.openstego.com/)
- <u>[Brutus](http://www.darknet.org.uk/2006/09/brutus-password-cracker-download-brutus-aet2zip-aet2/)</u>

}
