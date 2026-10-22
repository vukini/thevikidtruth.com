---
title: Using Linode
date: '2016-12-12T22:15:06+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1037}'
original_name: linode
original_blob: blob/B/5/225.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: linode
draft: false
topics:
- networking-web
---

# Using Linode

Here is the truth about Linode: **it was one of the first hosts to make renting a serious Linux machine feel like a commodity, and after the Akamai acquisition that spirit mostly survived.** A Linode is just a good VPS with a clean API and sane networking defaults.

### What it is, in plain words

**Linode** is a cloud/VPS provider founded in 2003, acquired by Akamai in 2022. You rent virtual machines (**Linodes** / Nanodes / dedicated CPU instances), object storage, Kubernetes (LKE), managed databases and node balancers in a few dozen regions. Images include Ubuntu, Debian, Alpine, Arch and custom uploads; rescue mode and out-of-band console exist when you lock yourself out.

For many of us who grew up with early VPS culture, Linode was where we learned to administer a public box. The [Online VPS](onlinevps.md) page covers the general craft; this page is Linode-specific notes.

### Why it matters

A predictable provider with honest documentation, a usable firewall product, and an API you can script is worth more than a race-to-the-bottom disk slice. Linode/Akamai isn't always the cheapest, but it's a known quantity – and known quantities are how you sleep when running something you care about.

### An everyday analogy: a familiar hardware shop

You could order parts from a random marketplace. Or you could go to the shop whose layout you know, whose return policy you've used, whose staff have seen your face. Linode is that shop for VMs.

### A hands-on example

**Create with the CLI** (`pip install linode-cli` then `linode-cli configure`):

```bash
linode-cli linodes create \
  --type g6-nanode-1 \
  --region gb-lon \
  --image linode/ubuntu24.04 \
  --hostname vikix-lon \
  --authorized_keys "$(cat ~/.ssh/id_ed25519.pub)" \
  --root_pass "$(openssl rand -base64 24)"
linode-cli linodes list
```

Then SSH in as root (or the image's default), create your user, lock down SSH, enable the Linode Cloud Firewall or `nftables` on the box, and proceed with the [first-hour checklist](onlinevps.md).

**Useful bits of the product:**

- **Cloud Firewall** – attach to instances; default-deny inbound is a good start.
- **VLANs / VPCs** – private networks between your Linodes.
- **Images & backups** – automated backups are opt-in; turn them on for anything you would miss.
- **Rescue mode** – boots a recovery environment with your disks mounted; lifesaver after a bad kernel or botched `fstab`.
- **Metadata / StackScripts** – first-boot provisioning.

Akamai's edge and CDN products sit next door if you outgrow a single origin.

### Migrating and leaving

Take regular offline backups (`restic`, `borg`, or even `rsync` to another provider) so leaving is a DNS change, not a hostage situation. Export DNS zones, object storage buckets and secrets the day before you need them. Providers are platforms; your data should not be.

### Running Void Linux on a Linode

The stock images are the mainstream distros, but Vikix is Void, so here is the specific path. Linode lets you boot into **Rescue mode** (a Finnix live environment) and write any system onto the disk, which is how you install a distro they do not list:

```bash
# After booting the Linode into Rescue mode and SSHing in:
# 1. partition the raw disk the dashboard gave you (e.g. /dev/sda)
# 2. mount it, then unpack a Void rootfs tarball from a mirror
mkdir /mnt/void
mount /dev/sda /mnt/void
xzcat void-x86_64-ROOTFS-*.tar.xz | tar -xpf - -C /mnt/void
# 3. chroot in, set a root password, install a kernel and GRUB, enable runit
for d in dev proc sys; do mount --rbind /$d /mnt/void/$d; done
chroot /mnt/void xbps-install -Su base-system grub
chroot /mnt/void grub-install /dev/sda
```

Reboot out of rescue mode and you have a Void VPS. The lesson generalises: with rescue mode and disk access you are never limited to a provider's menu. Alternatively, run Void inside the official image as a container or VM if you only need it for one service.

### Scripting the whole thing

The point of a cloud VPS over a box under your desk is that it is *reproducible*. Treat the server as disposable and keep the recipe in Git. The Linode CLI shown above is the quick way; Terraform (with the `linode` provider) is the durable way:

```hcl
# main.tf  -  terraform init && terraform apply
resource "linode_instance" "vikix" {
  label      = "vikix-lon"
  region     = "gb-lon"
  type       = "g6-nanode-1"
  image      = "linode/ubuntu24.04"
  authorized_keys = [trimspace(file("~/.ssh/id_ed25519.pub"))]
}
```

Now the server is code. You can destroy it, change one line, and recreate it identically. That habit, infrastructure as code, is the single biggest difference between hobby sysadmin and professional operations, and it costs nothing to start.

### When a single Linode is not enough

A Nanode happily runs a personal site, a VPN endpoint or a small [PicoLisp app](appdev.md). You outgrow it when:

- one region is too far from your users (add a **NodeBalancer** and instances in more regions, or put Akamai's CDN in front);
- the database contends with the web server for RAM (move it to a **Managed Database** or a second instance);
- you need to survive a host failure (run two instances behind a balancer, and keep state in object storage or a replicated database).

Resist scaling before you must. A single well-run box with good backups beats a fragile cluster you do not understand, and most projects never outgrow one machine.

### Common misconceptions

- **"Linode disappeared into Akamai."** The Linode control plane and product names largely remain; billing and account live under Akamai Cloud Computing.
- **"Nanode is too small to be useful."** For a static site, WireGuard endpoint or light API, 1 GB RAM is plenty.
- **"The free credit means free production."** Credits expire; set alerts.
- **"Their firewall replaces yours."** Defence in depth – use both cloud rules and on-host rules.
- **"Custom distros aren't allowed."** You can upload images; Void works fine if you bring your own.

### Connections

- [Online VPS](onlinevps.md), [SSH Login](sshlogin.md), [Ubuntu Common Tasks](ubuntucommontask.md).
- [Firewalls](firewalls.md), [TLS](tls.md), [Linux Security](linuxsecurity.md).

`Date: 13 December 2016`

I have been a digital Ocean User for Quite a while now. But I decided to give [linode](https://www.linode.com)
 a chance as I read up some good things about it.

## Links and Sources

- [Linode Manager](https://manager.linode.com/)
- [Your Server](https://www.linode.com/docs/security/securing-your-serverSecuring)
- [using fail2ban](https://www.linode.com/docs/security/using-fail2ban-for-security)
