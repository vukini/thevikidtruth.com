---
title: telnetemail
date: '2016-11-28T05:04:44+04:00'
lastmod: '2016-11-28T05:07:00+04:00'
original_id: '{A433}'
original_name: telnetemail
original_blob: blob/B/2/450.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: telnetemail
draft: false
topics:
- networking-web
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Email Exploit](telnetemail.md) | [internet-exploitation](internetexploitation.md)

```
telnet mail.test.server 25
220
HELO CENTAUR
250
MAIL FROM: <>
250
RCPT TO: <>
250
DATA

(press enter twice)

SUBJECT:

(Write body of email)

(hit enter twice)

.
250: email queued
```

### The plain idea

This little transcript shows something that surprises most people: **email is just text sent over a plain conversation**, and you can type that conversation by hand. Using `telnet` to connect to a mail server on port 25 and typing the **SMTP** commands (`HELO`, `MAIL FROM`, `RCPT TO`, `DATA`) yourself, you can hand-deliver an email the same way a mail server does. It is the clearest possible demonstration of how SMTP (the Simple Mail Transfer Protocol) actually works underneath all the apps.

### Why it matters

Doing this once demystifies email forever. You see that `MAIL FROM` and the "From:" header are *different things*, which is exactly why email is so easy to **spoof** (hence this page's place in the security notes: an attacker can put anything in those fields). You also see why spam, phishing and sender-forgery were possible for decades, and why the modern anti-spoofing defences had to be invented.

### An everyday analogy

It is like discovering you can walk up to the post office sorting counter and read out a letter for the clerk to write down and send. Handy to understand, but also alarming: nothing stops you claiming the letter is "from the Queen", which is precisely the problem email spent years fixing.

### A 2026 update

This hand-typed trick is now mostly a teaching exercise, not a practical attack, because the email world locked down:

- **Port 25 is widely blocked** for ordinary users; real sending uses authenticated submission on port 587 or 465 with a login.
- **TLS encryption** is expected, so most servers will not accept a plaintext `telnet` session (you would use `openssl s_client -connect host:587 -starttls smtp` to see the modern equivalent).
- **SPF, DKIM and DMARC** now let receiving servers check that a message really came from where it claims, so naive `MAIL FROM` spoofing lands in the spam folder or is rejected outright.

The protocol underneath is still exactly the SMTP conversation shown here; it just wears authentication and encryption now.

### How it connects

- [Internet Exploitation](internetexploitation.md): email spoofing as a social-engineering tool.
- [Encryption](encryption.md): the TLS and signing that secure mail today.
- [Networking](networking.md): SMTP as an application-layer protocol.

The truth revealed: email is, at bottom, a short polite text conversation between servers, and once you have typed it by hand you understand both how it works and why trusting "who it's from" was never safe.
