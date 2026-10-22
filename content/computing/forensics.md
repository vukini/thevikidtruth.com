---
title: Forensics
date: '2016-11-30T06:26:51+04:00'
lastmod: '2016-11-30T06:35:14+04:00'
original_id: '{A534}'
original_name: forensics
original_blob: blob/B/3/221.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: forensics
draft: false
topics:
- security
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Computer Security](computersecurity.md) | [ICSsecurity](icssecurity.md) |
  [Firewalls](firewalls.md) | [Networking](networking.md) | [Security Programs](securityprogram.md) |
 [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) | [wifi-penetration](wifipenetration.md) |
 [Forensics](forensics.md) | [Data Recovery](datarecovery.md)

# Forensics

The Following Steps should be taken to deal with any event that trigger requirement for forensics:

- Acquire Information
- Preserve never alter the state of the machine, if you can
- Never work on **original evidence**
- Maintain the Chain of Custody, Hash Values of Evidence (to prove the integrity of evidence)
- Go for [Data Recovery](datarecovery.md) if possible
- Do Forensic Analysis
- Produce and Present Results

## Tools

These Tools are Accepted

- EnCase, FTK, Magnet AXIOM (commercial suites)
- Autopsy / The Sleuth Kit (open source)
- Volatility (memory forensics)
- Write blockers and forensic imaging hardware

### The plain idea

Digital forensics is the careful recovery, preservation and analysis of digital evidence so that it tells a true story and holds up to scrutiny, in court, in an incident report, or just in your own understanding of what happened. The craft is less about clever tools than about discipline: you work on *copies*, never originals; you prove at every step that the evidence has not changed; and you record who handled it and when. My list above is exactly that discipline, acquire, preserve, never touch the original, keep the chain of custody and hash values, recover, analyse, report.

### Why it matters

After a breach, a fraud, or any dispute, the data is the witness. Handled badly, it is worthless: a defence lawyer need only show you might have altered it, and the whole case collapses. Handled well, it answers the questions that matter, what happened, when, how, and what was taken, and it does so in a way others can verify. The same rigour helps even outside court: good forensics is how you learn the real scope of an incident instead of guessing.

### An everyday analogy: the crime scene photographer

A detective at a crime scene does not rearrange the furniture to get a better look. They photograph everything first, bag each item with a label saying who took it and when, and send copies to the lab while the original stays sealed in evidence. Digital forensics is the same scene, made of bytes: you image the disk before you poke at it, and you keep the sealed original untouched.

### A worked example: imaging a disk and proving it is unchanged

The single most important habit is to capture a bit-for-bit image through a write blocker (hardware or software, so the act of reading cannot alter the source) and then prove the copy matches by hashing both:

```
# make a forensic image
sudo dd if=/dev/sdb of=/evidence/case42.img bs=4M conv=noerror,sync status=progress
# fingerprint source and copy; they must match
sha256sum /dev/sdb /evidence/case42.img
```

Record both hashes in your notes. From now on you analyse `case42.img` (or a copy of it), and anyone can re-hash the image to prove it is the same data you acquired. Note the hash change in my old notes: use **SHA-256**, not MD5 or SHA-1, which are no longer trustworthy against deliberate tampering. On a live machine you also capture volatile evidence first, in order of how quickly it disappears (memory, network connections, running processes) before pulling the disk.

### A note on memory and the cloud

Two things have grown since these notes were written. **Memory forensics** (with tools like Volatility) often matters more than disk forensics now, because malware frequently lives only in RAM. And evidence increasingly sits in the **cloud and on phones**, where you cannot simply pull a drive; you work through provider logs, legal process and mobile-acquisition tools instead. The principles, copy, verify, document, are unchanged.

### Common misconceptions

- **"Deleted means gone."** Deleting usually just unlinks a file; the data often sits on disk until overwritten, which is why recovery works. (Flash storage with TRIM and full-disk encryption complicate this.)
- **"I'll just have a quick look on the original."** Booting or browsing the original changes timestamps and can destroy evidence. Image first, always.
- **"The tool proves it."** The tool helps; your documentation and chain of custody are what make the findings defensible.
- **"Encryption makes forensics pointless."** It raises the bar, but keys, memory, backups and metadata often still tell the story.

### How it connects

- [Data Recovery](datarecovery.md): the techniques for getting data back.
- [Security Programs](securityprogram.md) and [Penetration Testing](penetrationtesting.md): forensics closes the loop after an incident.
- [Encryption](encryption.md): hashing (for integrity) and the obstacle of encrypted evidence.
- [IDS/IPS](idsips.md): the alerts that often begin an investigation.

The truth revealed: forensics is not about being clever with data; it is about being so careful that nobody can doubt what the data says.

## Sources, Reading Lists and Links

- [Linux Security](linuxsecurity.md)
- [Industrial Control Systems Security](icssecurity.md)
- [Penetration Testing](penetrationtesting.md)
- [Firewalls](firewalls.md)
- [Security Programs](securityprogram.md)
