---
title: Cool Hardware
date: '2016-11-28T07:03:09+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A435}'
original_name: coolhardware
original_blob: blob/B/2/477.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: coolhardware
draft: false
topics:
- os-hardware
---

[Computing](computing.md) | [Computer Security](computersecurity.md) | [Linux Security](linuxsecurity.md) |
[Industrial Control Systems Security](icssecurity.md) | [Penetration Testing](penetrationtesting.md) |
[Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md)

# Cool Hardware

Here is the truth about cool hardware: **the best gadgets are the ones that make you understand computing better, not the ones that merely look clever on a desk.** A blinking LED you wired yourself beats a sealed plastic brick you can't open.

### What it is, in plain words

This page is a living shelf of hardware worth knowing if you like to tinker: small computers, microcontrollers, unusual keyboards, radios, and tools that sit at the boundary between software and electrons. It is not a buying guide for the latest phone. It is a list of things that teach.

### Why it matters

Software is invisible. Hardware makes it physical – voltages, timing, antennas, motors. Spending time here improves every other layer: suddenly interrupts, buffers, baud rates and power draw stop being abstract. It is also fun, and fun is a legitimate reason to learn.

### An everyday analogy: a kitchen versus meal kits

A meal kit is convenient and closed. A kitchen with knives, a stove and raw ingredients lets you cook anything and understand cooking. Cool hardware is kitchen equipment for computation.

### A hands-on shelf (2026)

**Single-board computers**

- [Raspberry Pi 5](rasberrypi.md) – the default small Linux computer; GPIO, NVMe via hat, great docs.
- **Orange Pi / Rock 5 / Radxa** – often more performance per pound; check Linux support before you buy.
- **Framework Laptop** mainboards – repairable, modular; a statement that hardware can be owned.

**Microcontrollers**

- **Raspberry Pi Pico 2** (RP2350) – dual-core, cheap, MicroPython/C/Rust.
- **ESP32-C6 / C3** – Wi-Fi and Thread/Zigbee on a few dollars; Home Assistant's friend.
- **STM32** "blue/black pills" – denser ARM Cortex-M ecosystem; steeper but deep.

**Keyboards and input**

- Something **QMK/ZMK**-powered (keycaps you flash yourself).
- [Penti](penti.md) hardware or a hand wired chord board.
- A trackball (Kensington / Ploopy) – saves the desk and the shoulder when used with a tiling WM.

**Radio and sensing**

- **RTL-SDR** dongle – turn a laptop into a radio receiver; ADS-B planes, weather satellites, pager noise.
- **Flipper Zero** – controversial toy/tool for proximity protocols; educational if used ethically and legally.
- A basic **logic analyser** (Saleae or a cheap clone) – once you see I²C on a screen, buses make sense.

**Tools that pay for themselves**

- A decent **soldering iron** (Pinecil, TS101) and solder braid.
- Dupont wires, a breadboard, a USB power meter.
- A USB-UART adapter (CP2102 / CH340) – console into routers and headless boards.

### A first afternoon project

Buy a Pico, flash MicroPython, blink an LED, then read a button. When that works, read a BME280 over I²C and print temperature to the serial console. You have just done GPIO, buses and sensors – the same ideas inside every "real" system.

```bash
# on the Pico, with MicroPython REPL via serial
>>> from machine import Pin
>>> led = Pin(25, Pin.OUT)
>>> led.toggle()
```

### Buying without regret

- Prefer vendors who publish schematics or at least pinouts.
- Check the Linux kernel and distro support matrix *before* the board arrives.
- Budget for a good power supply; cheap ones cause "mysterious" SD corruption.
- Start with one ecosystem (Pico **or** ESP32 **or** Pi) and go deep before spreading out.

### The hardware this site runs on: Vikix

My own daily machine, Vikix, is deliberately modest: [Void Linux](archlinux.md) with the StumpWM window manager, chosen so that the whole stack stays understandable. The hardware lessons that matter most there are not exotic:

- **A keyboard remapped in hardware or firmware.** Caps Lock becomes Control, which saves the "Emacs pinky" and works before the OS even boots when done in firmware. See [KMonad](kmonad.md) for the software route and QMK/ZMK for the firmware route.
- **A machine you can open.** RAM you can add, an SSD you can swap, a battery you can replace. Framework and ThinkPad-style repairability is a computing-freedom issue as much as a convenience one.
- **Enough, not maximal.** StumpWM and a Lisp REPL do not need a flagship GPU. Spend the saved money on a good display and a mechanical keyboard you will touch ten thousand times a day.

### RISC-V: hardware you can actually read

The most exciting hardware story of the decade is **RISC-V**, an open instruction-set architecture that anyone may implement without a licence. By 2026 you can buy real boards: the Milk-V and StarFive boards run Linux, and microcontrollers like the ESP32-C series and the Raspberry Pi Pico 2 (whose RP2350 chip has RISC-V cores alongside ARM ones) put it on your desk for a few dollars.

Why it belongs on a "cool hardware" shelf: for the first time the whole stack, from the gate-level CPU design up through the [assembly language](assemblylanguage.md), is open and documented. You can read the ISA manual in an afternoon, write a few instructions, and run them on silicon you did not have to sign an NDA to understand. That is [Build a Computer in Your Head](bciyh.md) made real.

```bash
# Cross-assemble a tiny RISC-V program on Vikix (install the toolchain first)
# xbps-install -S cross-riscv64-linux-gnu qemu-user-static
riscv64-linux-gnu-gcc -static hello.c -o hello-rv
qemu-riscv64-static ./hello-rv      # run it without RISC-V hardware
```

`qemu-user-static` lets you run and debug RISC-V (or ARM) binaries on your x86 laptop, which is the cheapest way to start before a board arrives.

### Radio: computing you can hear

The radio gear at the top of this page is not nostalgia. A cheap **RTL-SDR** dongle turns a laptop into a software-defined radio: the antenna feeds raw samples to your CPU, and *software* does the demodulation that used to need a shelf of analogue circuitry. Decode aircraft transponders (ADS-B), read weather-satellite images, or just watch the spectrum. It is the clearest demonstration there is that "signal processing" is ordinary code running on samples, the same [data structures and algorithms](datastructuresandalgorithms.md) as everything else, just arriving through the air.

### Common misconceptions

- **"More specs = cooler."** Support, documentation and community matter more than GHz.
- **"Hardware is expensive."** A Pico and a bag of LEDs cost less than lunch.
- **"You need an EE degree."** You need curiosity and respect for voltage limits (3.3 V ≠ 5 V).
- **"Wireless is magic."** RF is physics; SDRs and antenna length demystify it.
- **"Modding voids everything that matters."** On open hardware, modding *is* the point. On sealed products, check legality and safety (batteries especially).

### Connections

- [Raspberry Pi](rasberrypi.md), [Penti](penti.md), [Keyboard Config](keyboardconfig.md).
- [Linux](linux.md), [Assembly Language](assemblylanguage.md).
- [ICS Security](icssecurity.md) – when things that move meet networks.

## Radio Stuff

- [MFJ-886B FREQUENCY COUNTER, .3 MHZ TO 2.8 GHZ, 110/220VAC](http://www.mfjenterprises.com/Product.php?productid=MFJ-886B)
- Kaltman Creations HF4060 RF Spectrum Analyzer.
- Alfa AWUS051NH 500mW High Gain 802.11a/b/g/n high power Wireless USB
