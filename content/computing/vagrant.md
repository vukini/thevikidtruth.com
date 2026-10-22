---
title: Vagrant
date: '2023-05-21T00:39:21+04:00'
lastmod: '2023-05-22T21:43:06+04:00'
original_id: '{A1772}'
original_name: vagrant
original_blob: blob/B/12/313.txt
revisions: 7
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: vagrant
draft: true
review: update
---

[Algorithms](algorithms.md) | [Apple](apple.md) | [AssemblyLanguage](assemblylanguage.md) |
[BASH](bash.md)  |   [Bash Cookbook](vikidsbashcookbook.md)  |
[C-Programmming](cprogramming.md) | [CommonLisp](commonlisp.md) | [Computer Security](computersecurity.md) | [CuisSmalltalk](cuissmalltalk.md) |
[Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) | [Firewalls](firewalls.md) |
[Forth](forth.md) | [Fortran](fortran.md) | [Functional Programming](functional.md) |
[Git](git.md) | [GNUSmalltalk](gnusmalltalk.md) | [Haskell](haskell.md) |  [Javascript](javascript.md) |  [Julia](julia.md) |
[Linux](linux.md) | [Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |[Machine Learning](machinelearning.md) |
[Networking](networking.md) | [Operating Systems](os.md) | [Open Data Science](opendatascience.md) | [Odin](odin.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) | [Purescript](purescript.md) | [Python](python.md) |
[Racket](racket.md) | [Rust](rust.md)| [Scheme](scheme.md)  | [Social Engineering](internetexploitation.md)  |
[Unity](unity.md) | [vagrant](vagrant.md) | [vim](vim.md) | [virtualbox](virtualbox.md) | [V](vlang.md) |
[Web Development](webdevelopment.md) | [Windows](windows.md) |[Zig](ziglang.md)

# Vagrant

- [archlinux: Vagrant Installation](https://wiki.archlinux.org/title/Vagrant)
- ```
  TERM=xterm-256color ssh
  ```
- `vagrant init jasonc/centos7`
  this will create a Vagrant File
- Configure said file:
  ```
  Vagrant.configure("2") do |config|
    # https://docs.vagrantup.com &  https://vagrantcloud.com/search.
    config.vm.box = "jasonc/centos7"
    config.vm.provider "virtualbox" do |vb|
      vb.customize ['modifyvm', :id, '--cableconnected1', 'on']
    end
    config.vm.define "server1" do |server1|
      server1.vm.hostname = "server1"
      server1.vm.network "private_network", ip: "192.168.56.10"
    end
    config.vm.define "server2" do |server2|
      server2.vm.hostname = "server2"
      server2.vm.network "private_network", ip: "192.168.56.11"
    end
  ```
- `vagrant up`
- `vagrant ssh`
- `vagrant destroy`
- <!-- 
  -{}
   -->
