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
draft: true
review: update
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
