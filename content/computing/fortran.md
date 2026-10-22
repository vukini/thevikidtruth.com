---
title: Computing
date: '2022-09-15T05:29:55+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1731}'
original_name: fortran
original_blob: blob/B/11/342.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: fortran
draft: false
---

[Readinglist](readinglist.md)  | [Quick Links](quicklinks.md) | [Algorithms](algorithms.md) | [Apple](apple.md) | [AssemblyLanguage](assemblylanguage.md) |
[BASH](bash.md) |   [C-Programmming](cprogramming.md) | [CommonLisp](commonlisp.md) | [Computer Security](computersecurity.md) | [CuisSmalltalk](cuissmalltalk.md) |
[Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) |
[Fortran](fortran.md) | [Functional Programming](functional.md) |
[Firewalls](firewalls.md) |   [Git](git.md) | [GNUSmalltalk](gnusmalltalk.md) | [Haskell](haskell.md) | [Javascript](javascript.md) |  [Julia](julia.md) |
[Linux](linux.md) | [Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |[Machine Learning](machinelearning.md) |
[Networking](networking.md) | [Operating Systems](os.md) |[Open Data Science](opendatascience.md) | [Odin](odin.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) | [Purescript](purescript.md) |
[Python](python.md) |
[Racket](racket.md) | [Scheme](scheme.md) | [Social Engineering](internetexploitation.md) |
[Unity](unity.md) | [vim](vim.md) | [V](vlang.md) |
[Web Development](webdevelopment.md) | [Windows WSL](windowswsl.md) | [Zig](ziglang.md)

# Computing

## Fortran

Here's a truth that surprises most programmers: **the oldest high-level language still in heavy use isn't a relic – it's quietly running the world's weather forecasts, climate models and supercomputers.** Fortran is old; modern Fortran is not.

### What it is, in plain words

**Fortran** ("FORmula TRANslation") was created at IBM by John Backus's team and released in 1957 – the first widely used compiled high-level language. It was designed for one thing: turning mathematical formulas into fast machine code.

The language has been revised many times. Forget the punched-card FORTRAN 77 with its fixed columns and `GOTO`s. Modern Fortran means **Fortran 90 and later** – the current standard is **Fortran 2023** – with:

- free-form source (`.f90` files), modules, and `implicit none`;
- **whole-array operations** and array slicing built into the language;
- dynamic allocation, derived types, object-oriented features;
- **coarrays** for parallel programming built into the language itself, plus `do concurrent`;
- standard interoperability with C (`iso_c_binding`).

### Why it matters

When the job is "crunch huge arrays of floating-point numbers as fast as the hardware allows", Fortran remains a top choice. The language forbids certain kinds of pointer aliasing that C allows, so compilers can optimise array loops aggressively. Much of the world's scientific code – weather (ECMWF, WRF), climate (CESM), computational chemistry, physics, and the reference BLAS and LAPACK libraries that sit underneath [NumPy](numpy.md) and [SciPy](scipy.md) – is Fortran. Every time you call `numpy.linalg.solve`, there's a decent chance Fortran-descended code does the work.

### An everyday analogy: a specialist's tool

A Swiss Army knife can do many things. A surgeon's scalpel does one thing superbly. Fortran is the scalpel for numerical computing. You wouldn't write a web server in it (you could, but why?), but for slicing through a matrix, very little is cleaner or faster.

```mermaid
flowchart LR
  A["Fortran (LAPACK, BLAS, solvers)"] --> B["C / C++ wrappers"]
  B --> C["NumPy / SciPy / Julia / R"]
  C --> D["Your Python notebook"]
```

### A hands-on example

Install a compiler and the Fortran Package Manager:

```bash
sudo xbps-install -S gcc-fortran   # Void (provides gfortran)
sudo pacman -S gcc-fortran         # Arch
sudo apt install gfortran          # Debian/Ubuntu
# fpm: from conda-forge, pip (pip install fpm) or a release binary
```

`heat.f90` – a 1D heat-diffusion simulation in modern style:

```fortran
program heat
  implicit none
  integer, parameter :: dp = kind(1.0d0)
  integer, parameter :: n = 50, steps = 500
  real(dp), parameter :: alpha = 0.25_dp
  real(dp) :: u(n), unew(n)
  integer :: t

  u = 0.0_dp
  u(n/2) = 100.0_dp                      ! a hot spot in the middle

  do t = 1, steps
     ! whole-array slice arithmetic – no explicit inner loop
     unew(2:n-1) = u(2:n-1) + alpha * (u(1:n-2) - 2*u(2:n-1) + u(3:n))
     unew(1) = 0; unew(n) = 0            ! cold ends
     u = unew
  end do

  print '(a, f8.4)', 'peak temperature: ', maxval(u)
  print '(a, f8.4)', 'total heat:       ', sum(u)
end program heat
```

```bash
gfortran -O2 -Wall -std=f2018 heat.f90 -o heat && ./heat
```

The line inside the loop is the update rule

$$ u_i^{t+1} = u_i^{t} + \alpha\,(u_{i-1}^{t} - 2u_i^{t} + u_{i+1}^{t}) $$

written almost exactly as the maths reads. That's the original promise of FORmula TRANslation, still kept.

With **fpm** a project is as easy as Rust's Cargo:

```bash
fpm new myproj && cd myproj
fpm run
fpm test
```

### Compilers in 2026

- **gfortran** (GCC) – free, everywhere, solid Fortran 2008/2018 support.
- **LLVM Flang** – the LLVM project's Fortran compiler (the binary is now simply `flang`), maturing quickly and backed by national labs and vendors.
- **Intel ifx** – free oneAPI compiler, strong optimisation and coarrays.
- **LFortran** – a new interactive compiler that can run Fortran in a Jupyter notebook; still in beta.
- **NVIDIA nvfortran** – for offloading to GPUs with `do concurrent` and OpenACC.

The **fortran-lang.org** community also maintains `stdlib`, a growing standard library, and the Discourse forum is very welcoming.

### Common misconceptions

- **"Fortran is FORTRAN 77."** That's like judging today's C by K&R first edition. Modern Fortran has modules, allocatable arrays, OOP and built-in parallelism.
- **"Nobody uses it."** It consistently appears among the main languages on the world's largest supercomputers.
- **"C is always faster."** For dense array maths, Fortran's aliasing rules often give the optimiser *more* freedom than C.
- **"Arrays start at 0."** Default is 1, but you can declare any lower bound: `real :: a(0:9)` or `a(-5:5)`.
- **"It's case sensitive / needs capitals."** Fortran is case-insensitive; modern style is lowercase.

### Connections

- [NumPy](numpy.md) and [SciPy](scipy.md) – Python that leans on Fortran underneath.
- [Julia](julia.md) – a newer language aiming at the same scientific crowd.
- [C Programming](cprogramming.md) – the other classic systems language; interoperate with `bind(c)`.
- [Algorithms](algorithms.md) – numerical methods are where Fortran shines.
- [Computer Languages](computerlanguages.md) – the family tree Fortran started.

#### Links

- [Exploring Modern Fortran Basics](https://youtube.com/watch?v=-u7qa2SzlFU&feature=share)
- [Fortran Tutorial](https://youtube.com/watch?v=__2UgFNYgf8&feature=share)
