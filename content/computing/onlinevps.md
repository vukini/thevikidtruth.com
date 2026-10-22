---
title: Online VPS, SaaS, PaaS, IaaS
date: '2016-12-12T22:38:11+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1042}'
original_name: onlinevps
original_blob: blob/B/5/235.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: onlinevps
draft: false
topics:
- networking-web
---

# Online VPS, SaaS, PaaS, IaaS

Here is the truth about a VPS: **you are renting a virtual machine that thinks it is a computer, and you are its sysadmin.** The freedom is real; so is the responsibility when the cron job fills the disk at 3 a.m.

### What it is, in plain words

A **VPS** (Virtual Private Server) is a virtual machine sold by a host – [Linode](linode.md)/Akamai, DigitalOcean, Hetzner, OVH, Vultr, Oracle Cloud's free tier, and many smaller providers. You get a public IP, a chosen Linux image (or your own), CPU/RAM/disk quotas, and root access. Underneath, it's a KVM (usually) guest on hardware you don't own.

Related products:

- **Shared hosting** – someone else runs the web server; you get a panel. Less power, less rope.
- **Dedicated** – whole machine. More money.
- **PaaS** – Fly.io, Render, Railway – deploy apps, less SSH.
- **Home lab** – a Pi or old PC on your fibre; cheap, you handle power and uplink.

### Why it matters

A VPS is how this site, a personal Git host, a VPN endpoint or a PicoLisp app leaves your laptop and meets the world. Learning to harden, update and back up one VPS is the most practical sysadmin education available for a few dollars a month.

### An everyday analogy: renting a workshop

A PaaS is a shared makerspace with rules. A VPS is a locked workshop on an industrial estate: bring your own tools, change the locks, leave at midnight. The landlord (the host) keeps the building standing; everything inside is yours to break.

```mermaid
flowchart LR
  U[You / SSH] --> V[VPS guest]
  V --> H[Hypervisor + host hardware]
  V --> I[Public IP]
  I --> N[Internet]
```

### A hands-on first-hour checklist

1. **Create the VM** with your SSH public key baked in (never password-only on a public IP).
2. **Log in, update, reboot if kernel changed.**
3. **Create a sudo user**, disable root password login, lock SSH to keys – see [SSH Login](sshlogin.md).
4. **Firewall** – allow 22/80/443 only. [Firewalls](firewalls.md), `ufw` or `nftables`.
5. **Point DNS** at the IP; issue TLS with Caddy or certbot – [TLS](tls.md).
6. **Automatic updates** for security patches, plus a backup plan ([Data Recovery](datarecovery.md) mindset).
7. **Monitoring** – even a cron that curls your site and mails on failure.

```bash
ssh root@YOUR.IP
adduser vikid && usermod -aG sudo vikid   # or wheel
# install key for vikid, then:
sudo apt update && sudo apt full-upgrade
sudo apt install fail2ban ufw
sudo ufw allow OpenSSH && sudo ufw allow http && sudo ufw allow https
sudo ufw enable
```

Pick a nearby region for latency; pick a provider whose network and support you've read about when things break. Price is not the only axis – egress bandwidth, IPv6, snapshots and honest status pages matter.

### Cost control

Set a billing alert the day you open the account. Snapshot calendars, unused load balancers and egress to the public internet are how "\$5/month" becomes a surprise. Prefer providers that charge egress honestly and let you cap it. Tear down experiments when you're done – a forgotten VM is a forgotten attack surface.

### Common misconceptions

- **"A VPS is anonymous."** Payment, abuse complaints and WHOIS tell stories. Don't be evil.
- **"More CPU means better."** Burstable credits, noisy neighbours and disk IOPS often matter more.
- **"Snapshots are backups."** Snapshots live with the host. Copy critical data elsewhere.
- **"Managed means secure."** Managed database ≠ patched app. You still own your code.
- **"Free tiers are free forever."** Read the terms; set billing alerts.

### Connections

- [Linode](linode.md), [SSH Login](sshlogin.md), [Ubuntu Common Tasks](ubuntucommontask.md).
- [Firewalls](firewalls.md), [TLS](tls.md), [Linux Security](linuxsecurity.md).
- [Seedbox](seedbox.md), [Virtualization](virtualization.md).

## Sources and Links

- [DigitalOcean vs AWS @ upguard](https://www.upguard.com/articles/digitalocean-vs-aws)
- [DigitalOcean vs Linode @ upguard](https://www.upguard.com/articles/digitalocean-vs-linode)
- [DigitalOcean vs Upcloud @ upguard](https://www.upcloud.com/vs/digitalocean/)
