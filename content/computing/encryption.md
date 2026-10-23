---
title: "Cryptography"
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
draft: false
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

### The plain idea

Cryptography is the science of keeping information safe by transforming it. My little tree above sorts the field: you either try to keep data *invisible* (steganography, hiding the very existence of a message) or you keep it *visible but unreadable*. The second path splits again into **encryption** (reversible: scramble now, unscramble later with a key) and **hashing** (one-way: turn data into a fixed fingerprint you cannot reverse).

Encryption itself comes in two kinds. **Symmetric** uses one shared secret key for both locking and unlocking, fast but you must somehow share the key. **Asymmetric** (public-key) uses a pair: a public key anyone may have, and a matching private key you keep. What one locks, only the other unlocks. That solves the key-sharing problem and is the backbone of HTTPS, signed software and secure messaging.

### Why it matters

Almost everything private online rests on these ideas: the padlock in your browser, your messages, your passwords, your bank transfers, cryptocurrency, software updates you can trust. Get the concepts straight and most of security stops being mysterious. Get them muddled, "I'll just hash it to encrypt it", and you build something that looks safe and is not.

A 2026 update to my old notes: the recommended tools have moved on. **AES** is still the symmetric standard, now often as AES-GCM or ChaCha20-Poly1305 (which authenticate as well as encrypt). **DES and 3DES are retired.** For hashing, **MD5 and SHA-1 are broken** and must not be used for security; use **SHA-256** or SHA-3. For protecting passwords specifically, use a slow, salted algorithm such as **bcrypt, scrypt or Argon2**, never a plain fast hash. And a new frontier has opened: **post-quantum cryptography**. In 2024 NIST standardised the first quantum-resistant algorithms (ML-KEM/Kyber for key exchange, ML-DSA/Dilithium for signatures), and browsers and servers began deploying hybrid key exchange to guard against future quantum computers.

### An everyday analogy: padlocks and fingerprints

Symmetric encryption is a padlock where the same key locks and opens it, fine if you can hand the key to your friend safely. Asymmetric is cleverer: imagine a padlock anyone can *snap shut* (the public key) but only you hold the key to *open* (the private key). You post open padlocks to the world; anyone can lock a box and send it, and only you can open it. Hashing is different again: it is a fingerprint. From a person you can take a fingerprint, but from a fingerprint you cannot rebuild the person.

### A worked example: why symmetric keys do not scale, and how asymmetric fixes it

My note gives the formula for symmetric keys among N people: every pair needs its own shared key, so the number of keys is

$$\frac{N(N-1)}{2}.$$

For 10 people that is 45 keys; for 1,000 people it is 499,500. Nobody can manage that. Asymmetric cryptography replaces it: each person has just *one* key pair, so N people need only 2N keys total. To message anyone, you look up their public key and lock the message with it.

In practice the two are combined. TLS (the "s" in HTTPS) uses slow asymmetric cryptography once, at the start, only to agree on a fresh random symmetric key, then uses fast symmetric encryption (AES-GCM) for the actual data. You get the key-sharing of public-key and the speed of symmetric:

```
openssl rand -hex 32                 # a 256-bit symmetric key
echo "secret" | openssl enc -aes-256-gcm -pbkdf2 -k "passphrase"
printf 'hello' | sha256sum           # a one-way fingerprint
```

### Common misconceptions

- **"Hashing is a kind of encryption."** No. Encryption is reversible with a key; hashing is deliberately one-way. You verify a password by hashing the attempt and comparing fingerprints, never by "decrypting" the stored hash.
- **"Encoding is encryption."** Base64 and URL-encoding are not secret at all; anyone can reverse them. They hide nothing.
- **"Longer passwords beat a bad hash."** If a site stores passwords as unsalted MD5, length helps little once the database leaks. Salting and a slow algorithm (Argon2) are what matter.
- **"I should invent my own cipher."** Almost always a mistake. Use vetted, standard implementations; home-made crypto fails in ways you will not see.
- **"Quantum computers already broke encryption."** Not yet. The migration to post-quantum algorithms is precautionary, guarding against "harvest now, decrypt later".

### How it connects

- [Securing Web Apps](securingwebapps.md) and [IDS/IPS](idsips.md): where encryption sits in defence.
- [Rainbow Tables](rainbowtables.md): the attack that salting defeats.
- [SSL (ssl.c)](sslc.md): a small real TLS client.
- [Networking](networking.md): TLS as a layer of the stack.

The truth revealed: encryption hides the message, hashing proves it, and the hard part was never the maths, it was sharing the key, which public-key cryptography finally solved.

### Tools, Links and Reading Lists

### Tools, Links and Reading Lists

- [OpenStego](https://www.openstego.com/)
- [age - modern file encryption](https://age-encryption.org/)
- [GnuPG](https://gnupg.org/) and [Mailvelope](https://www.mailvelope.com/) for PGP
- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [Crypto 101 (free book)](https://www.crypto101.io/)
