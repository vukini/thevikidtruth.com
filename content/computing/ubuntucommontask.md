---
title: Ubuntu CommonTasks
date: '2016-12-10T06:21:07+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1027}'
original_name: ubuntucommontask
original_blob: blob/B/11/405.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: ubuntucommontask
draft: false
---

# Ubuntu CommonTasks

Here is a truth about Ubuntu: **most "how do I…?" questions have one canonical answer, and once you know the pattern you stop searching.** This page is a pocket card of those answers – the tasks people actually do on a fresh Ubuntu box.

### What it is, in plain words

Ubuntu is Debian's friendlier cousin: same `.deb` packages and `apt`, a fixed release cadence (April and October), with **LTS** releases supported for five years (ten with Ubuntu Pro). The current LTS at the time of writing is **24.04 "Noble Numbat"**; non-LTS releases get nine months. Underneath, since 15.04, the init system is **systemd**, so service management is `systemctl` and logs are `journalctl` – the old `service apache2 status` style still works as a thin wrapper, but the native commands are the ones to learn.

I run [Void Linux](bciyh.md) on Vikix day to day, but Ubuntu is what you'll meet on cloud VMs, friends' laptops and most Linux tutorials, so these tasks are worth having in muscle memory.

### Why it matters

The first hour on a new Ubuntu machine is always the same: update, set the hostname, create a user, enable SSH, open a port, install a package, start a service. Doing those cleanly – and knowing how to undo them – is the difference between a tidy box and one you don't trust.

### An everyday analogy: a hotel checkout list

Every hotel stay has the same checklist: key card, Wi-Fi code, checkout time, where the ice machine is. The rooms differ, the checklist doesn't. Ubuntu common tasks are that checklist for a Linux box.

```mermaid
flowchart LR
  A[Fresh Ubuntu] --> B[update & upgrade]
  B --> C[hostname + user + SSH]
  C --> D[install packages]
  D --> E[enable services]
  E --> F[firewall]
```

### A hands-on pocket card

**Update the system**

```bash
sudo apt update
sudo apt full-upgrade          # safer than plain 'upgrade'; handles new deps
sudo apt autoremove --purge    # remove leftover packages
```

**Change the hostname** (replaces the old `hostname` file dance):

```bash
sudo hostnamectl set-hostname vikix-lab
# also put the same name in /etc/hosts next to 127.0.1.1
```

**Create a user and give them sudo**

```bash
sudo adduser vikid
sudo usermod -aG sudo vikid
```

**SSH: install, enable, and use keys**

```bash
sudo apt install openssh-server
sudo systemctl enable --now ssh
# on your laptop:
ssh-copy-id vikid@server
```

Then harden a little: in `/etc/ssh/sshd_config.d/local.conf` set `PasswordAuthentication no` and `PermitRootLogin no`, then `sudo systemctl reload ssh`.

**Packages: find, install, remove**

```bash
apt search nginx
apt show nginx
sudo apt install nginx
sudo apt remove nginx          # leave config
sudo apt purge nginx           # remove config too
apt list --installed | less
```

Prefer `.deb` packages from Ubuntu's repos. Snap is preinstalled; Flatpak is one `apt install flatpak` away. For language toolchains, use the language's own installer (rustup, nvm, uv) rather than outdated distro packages.

**Services with systemd** (Apache is the classic example):

```bash
sudo apt install apache2
sudo systemctl enable --now apache2    # start now and at boot
sudo systemctl status apache2
sudo systemctl reload apache2          # graceful config reload
sudo systemctl stop apache2
journalctl -u apache2 -f               # live logs
```

The old `sudo service apache2 start` still works; it calls systemctl for you.

**Firewall with UFW** (front end to iptables/nftables):

```bash
sudo apt install ufw
sudo ufw allow OpenSSH
sudo ufw allow 'Apache Full'           # or: allow 80,443/tcp
sudo ufw enable
sudo ufw status verbose
```

**Open ports, see who's listening**

```bash
ss -tulpn
sudo ss -tulpn | grep :80
```

**Time, locale, and a static IP tip**

```bash
timedatectl                            # Ubuntu uses systemd-timesyncd by default
sudo timedatectl set-timezone Asia/Dubai
localectl set-locale LANG=en_GB.UTF-8
```

Network on desktop Ubuntu is NetworkManager ([nmtui](nmtui.md) works). On Ubuntu Server it's usually **Netplan** YAML in `/etc/netplan/` – edit, then `sudo netplan apply`.

### Common misconceptions

- **"`apt-get` is the real command; `apt` is fake."** `apt` is the recommended interactive tool since Ubuntu 16.04. Use `apt-get` in scripts for stable output.
- **"`service` is deprecated and broken."** It's a compatibility wrapper. Prefer `systemctl`, but `service` still works.
- **"Snap is mandatory."** Firefox and a few others ship as snaps by default; you can replace them with deb or Flatpak packages if you prefer.
- **"LTS means packages are up to date."** It means *stable*. Language runtimes and desktop apps can lag – use upstream tools or backports when you need newer.
- **"You need reboot after everything."** Only after kernel updates (or use `livepatch` / `kexec`). `systemctl reload` is enough for most services.

### Connections

- [systemd](systemd.md) – what `systemctl` is talking to.
- [nmtui](nmtui.md) – network configuration from a terminal.
- [SSH Login](sshlogin.md) – keys, agents and jump hosts.
- [Firewalls](firewalls.md) – the ideas behind UFW.
- [Linux Tools](linuxtools.md) – the wider toolbox.
- [Arch Linux](archlinux.md) – a different distro's answers to the same questions.

service apache2 status
[start stop apache2](https://www.cyberciti.biz/faq/ubuntu-linux-start-restart-stop-apache-web-server/)
[change the computer hostname](http://askubuntu.com/questions/9540/how-do-i-change-the-computer-name)

## [FunkyTechnology](funkytechnology.md)
