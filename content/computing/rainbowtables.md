---
title: Rabinbow Tables
date: '2016-11-28T01:54:08+04:00'
lastmod: '2016-11-28T02:02:46+04:00'
original_id: '{A426}'
original_name: rainbowtables
original_blob: blob/B/2/420.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: rainbowtables
draft: false
topics:
- security
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md)

# Rainbow Tables

[Wikipedia Article on Rainbow Tables](https://en.wikipedia.org/wiki/Rainbow_table) 

L0PHTCRACK (LC6) - PASSWORD - AUDITOR

Perpetrators can use huge tables (terabytes in size) to lookup passwords to known hashes.

This is a brute force method but effective for small passwords.

**The only and best way to protect against this sort of attack is to use passwords greater than 15 characters**

### The plain idea

A rainbow table is a huge pre-computed dictionary that maps password *hashes* back to the passwords that made them. Systems never store your password; they store its hash (a one-way fingerprint, see [encryption](encryption.md)). If an attacker steals that list of hashes, they cannot reverse a hash directly, so instead they hash millions of candidate passwords in advance and look yours up. A rainbow table is a clever, space-saving version of that idea: it stores "chains" of hashes rather than every entry, trading a little extra computation for a massive saving in storage.

### Why it matters

It turns a stolen hash database into stolen passwords, in seconds, for any password short or common enough to be in the table. It is the attack that explains two of the most important rules in all of security: **salt your hashes**, and **use a slow hashing algorithm**.

### An everyday analogy: the answer key

Imagine a teacher who locks the answers in a safe but publishes, for every possible exam paper, the exact pattern of correct ticks and crosses. Steal the mark sheet and you can match the pattern straight to the answers, without opening the safe. A *salt* is the teacher secretly adding a different random question to each student's paper, so one universal answer key no longer fits anybody.

### A worked example: why a salt destroys the table

Two users both pick the password `summer2026`. Without a salt, both rows store the identical hash, and one rainbow-table lookup cracks both. Now add a unique random salt to each:

```
hash1 = SHA256("a9f3..." + "summer2026")
hash2 = SHA256("7c1e..." + "summer2026")
```

The stored hashes are now completely different, and no pre-computed table helps, because the attacker would need a separate table for every possible salt. That is the whole defence: rainbow tables rely on the same password always producing the same hash, and salting breaks that.

### Updating my old note for 2026

My original advice, "use passwords longer than 15 characters", is good for you as a *user*, and length genuinely does push a password out of reach of these tables. But the real fix lives on the *defender's* side:

- **Salt every password** with a unique random value.
- **Use a slow, memory-hard algorithm** designed for passwords, bcrypt, scrypt or Argon2, not a fast general hash like MD5, SHA-1 (both broken) or even plain SHA-256. These are deliberately expensive, so billions of guesses per second become thousands.
- Tools like L0phtCrack (mentioned above) and today's hashcat and John the Ripper are how auditors (and attackers) test this.

With a proper salted, slow hash, classic rainbow tables are essentially obsolete; attackers fall back to slow brute force and dictionary attacks, which strong, unique passwords and a password manager defeat.

### Common misconceptions

- **"Hashing a password is enough."** Not if it is fast and unsalted.
- **"A longer table cracks anything."** Salting makes a universal table useless no matter how big.
- **"Rainbow tables encrypt."** They do the opposite: they undo hashing by lookup, not by decryption.

### How it connects

- [Encryption](encryption.md): hashing, salting and why password hashing differs from encryption.
- [Exploitation](exploitation.md): where stolen hash databases come from.
- [Wifi Penetration](wifipenetration.md): the same lookup idea attacks captured Wi-Fi handshakes.

The truth revealed: a rainbow table does not break hashing; it beats *lazy* hashing. A pinch of salt ruins the whole recipe.
