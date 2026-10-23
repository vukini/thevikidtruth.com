---
title: 'Esperanto: PicoLisp Installation'
date: '2021-09-01T01:17:10+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A1612}'
original_name: picolispinstallation
original_blob: blob/B/10/177.txt
revisions: 6
author: admin
last_editor: admin
tags:
- languages
categories:
- languages
wikislug: picolispinstallation
draft: false
topics:
- esperanto
path_step: 26
---

# Esperanto: PicoLisp Installation

I translated PicoLisp's `INSTALL` file into Esperanto as a language exercise. Here it is in both languages, Esperanto first and then the original English, **updated in October 2026 to the current INSTALL (dated 23jan26) that ships with pil21**. Compared with the 2020 version: `binutils` was added to the required packages, macOS users are pointed to `src/Makefile.macos`, there is a new symlink for bash completion, and the documentation section is shorter. At the end I added some notes of my own on installing it today.

```
# 23jan26 Software Lab. Aleksandro Burger

         Instalado de PicoLisp
         =====================

PicoLisp bezonas kongruan sistemon POSIX kaj la LLVM-infrastrukturon. Ĝi
subtenas du instalajn strategiojn: Loka kaj Tutmonda.

Por tutmonda instalado, permesante tutsisteman aliron al la plenumebla kaj
bibliotekaj / dokumentaj dosieroj, vi povas aŭ instali ĝin de preta
distribuo, aŭ agordi iujn simbolajn ligojn al unu el la lokaj instaladaj
dosierujoj kiel priskribite sube.

Notu, ke vi ankoraŭ rajtas havi lokajn instalaĵojn kune kun tutmonda
instalado, kaj alvoki ilin eksplicite laŭplaĉe.
```

```
# 23jan26 Software Lab. Alexander Burger

         PicoLisp Installation
         =====================

PicoLisp needs a POSIX compatible system and the LLVM infrastructure. It
supports two installation strategies: Local and Global.

For a global installation, allowing system-wide access to the executable
and library/documentation files, you can either install it from a
ready-made distribution, or set some symbolic links to one of the local
installation directories as described below.

Note that you are still free to have local installations along with a
global installation, and invoke them explicitly as desired.
```

```
      Loka Instalado
      --------------

La jenaj instrukcioj funkcias ĉe Debian Linukso. Ili devus esti similaj ĉe
aliaj sistemoj (por ekz. MacOS vidu src/Makefile.macos).

1. Instalu bezonatajn pakaĵojn

   $ sudo apt install binutils make clang llvm libreadline-dev libffi-dev libssl-dev pkg-config

2. Malpaku la tarball-on

   $ wget https://software-lab.de/pil21.tgz
   $ tar xfz pil21.tgz

3. Ŝanĝu la dosierujon

   $ cd pil21

4. Kompilu la interpretilon PicoLisp

   $ (cd src; make)
```

```
      Local Installation
      ------------------

The following instructions work on Debian Linux. They should be similar
on other systems (for e.g. MacOS see src/Makefile.macos).

1. Install required packages

   $ sudo apt install binutils make clang llvm libreadline-dev libffi-dev libssl-dev pkg-config

2. Unpack the tarball

   $ wget https://software-lab.de/pil21.tgz
   $ tar xfz pil21.tgz

3. Change the directory

   $ cd pil21

4. Compile the PicoLisp interpreter

   $ (cd src; make)
```

```
      Tutmonda Instalado
      ------------------

La rekomendinda maniero por tutmonda instalado estas uzi picolisp-pakaĵon
de la OS-distribuo.

Se tio ne disponeblas, vi povas (kiel radiko) krei simbolajn ligojn de
/usr/lib kaj /usr/bin al loka instalada dosierujo:

   # ln -s /<pado>/pil21 /usr/lib/picolisp
   # ln -s /usr/lib/picolisp/bin/picolisp /usr/bin
   # ln -s /usr/lib/picolisp/bin/pil /usr/bin

Por aldona aliro al la manlibraj paĝoj, utilaĵoj kaj bash-kompletigo:

   # ln -s /<pado>/pil21/man/man1/picolisp.1 /usr/share/man/man1
   # ln -s /<pado>/pil21/man/man1/pil.1 /usr/share/man/man1
   # ln -s /<pado>/pil21 /usr/share/picolisp
   # ln -s /<pado>/pil21/lib/bash_completion /usr/share/bash-completion/completions/pil
```

```
      Global Installation
      -------------------

The recommended way for a global installation is to use a picolisp
package from the OS distribution.

If that is not available, you can (as root) create symbolic links from
/usr/lib and /usr/bin to a local installation directory:

   # ln -s /<path>/pil21 /usr/lib/picolisp
   # ln -s /usr/lib/picolisp/bin/picolisp /usr/bin
   # ln -s /usr/lib/picolisp/bin/pil /usr/bin

For additional access to the man pages, utilities and bash completion:

   # ln -s /<path>/pil21/man/man1/picolisp.1 /usr/share/man/man1
   # ln -s /<path>/pil21/man/man1/pil.1 /usr/share/man/man1
   # ln -s /<path>/pil21 /usr/share/picolisp
   # ln -s /<path>/pil21/lib/bash_completion /usr/share/bash-completion/completions/pil
```

```
      Alvokado
      --------

En tutmonda instalado oni uzu la komandon 'pil'. Vi povas komenci aŭ en
simpla aŭ en sencimiga reĝimo. La diferenco estas, ke por sencimiga
reĝimo la komandon sekvas unu plus-signo ('+'). La '+' devas esti la
plej lasta argumento en la komandlinio.

   $ pil       # Simpla reĝimo
   :

   $ pil +     # Sencimiga reĝimo
   :

En ambaŭ kazoj la dupunkto ':' estas la invito de PicoLisp. Vi povas
enigi iun Lisp-esprimon,

   : (+ 1 2 3)
   -> 6

Por forlasi la interpretilon, enigu

   : (bye)

aŭ simple tajpu Ctrl-D.

Por loka alvoko, specifu vojnomon, ekz.

   $ ./pil     # Simpla reĝimo
   :

   $ ./pil +   # Sencimiga reĝimo
   :

aŭ

   $ /home/app/pil  # Alvoki lokan instaladon el iu alia dosierujo

Notu, ke 'pil' ankaŭ povas servi kiel ŝablono por viaj propraj memstaraj
skriptoj.
```

```
      Invocation
      ----------

In a global installation, the 'pil' command should be used. You can
either start in plain or in debug mode. The difference is that for debug
mode the command is followed by single plus ('+') sign. The '+' must be
the very last argument on the command line.

   $ pil       # Plain mode
   :

   $ pil +     # Debug mode
   :

In both cases, the colon ':' is PicoLisp's prompt. You may enter some
Lisp expression,

   : (+ 1 2 3)
   -> 6

To exit the interpreter, enter

   : (bye)

or just type Ctrl-D.

For a local invocation, specify a path name, e.g.

   $ ./pil     # Plain mode
   :

   $ ./pil +   # Debug mode
   :

or

   $ /home/app/pil  # Invoking a local installation from some other directory

Note that 'pil' can also serve as a template for your own stand-alone
scripts.
```

```
      Dokumentado
      -----------

Por pliaj informoj, bonvolu rigardi "doc/index.html". Tie vi trovas la
Referencan Manlibron de PicoLisp ("doc/ref.html"), la lernilon de PicoLisp
("doc/tut.html"), kaj la oftajn demandojn ("doc/faq.html").

Kiel ĉiam, la plej ĝusta kaj kompleta dokumentado estas la fontkodo ;-)

Ajna reago estas bonvena!
Mi esperas, ke vi ĝuos :-)

--------------------------------------------------------------------------------

   Aleksandro Burger
   Software Lab. / 7fach GmbH
   Bahnhofstr. 24a, D-86462 Langweid
   abu@software-lab.de, https://www.software-lab.de, +49 8230 5060
```

```
      Documentation
      -------------

For further information, please look at "doc/index.html". There you find
the PicoLisp Reference Manual ("doc/ref.html"), the PicoLisp tutorial
("doc/tut.html"), and the frequently asked questions ("doc/faq.html").

As always, the most accurate and complete documentation is the source
code ;-)

Any feedback is welcome!
Hope you enjoy :-)

--------------------------------------------------------------------------------

   Alexander Burger
   Software Lab. / 7fach GmbH
   Bahnhofstr. 24a, D-86462 Langweid
   abu@software-lab.de, https://www.software-lab.de, +49 8230 5060
```

### My notes on installing it in 2026

- **Build from source if you can.** The `pil21.tgz` tarball is always the latest version (26.9 as I write). It builds in about a minute and needs nothing but the packages above.
- **Distro packages often lag behind** the tarball, so check the version your distribution ships. Void Linux and Homebrew have no package at all, so on those, follow the local installation above.
- **Check what you got** with `pil -version -bye`.
- On a fresh machine, `make` itself may be missing. It is in the package list above for that reason.

See also: [PicoLisp](../computing/picolisp.md), [PicoLisp Tutorials](../computing/piltutorials.md).

#### Multilingual Texts

- [iTalki Community Message](italkicommunity1.md)
- [De Zéro à Un](dezeroaun.md)
- [La Familia de María](lafamiliademaria.md)
- [I like to wake up](wakeupearly.md)
- [Time in a Day](timeinaday.md)
- [Spiritual Wake Up](spiritualwakeup.md)
- [La Ruse du Cerf](laruseducerf.md)
- [Afirmaciones cientificas para la curation](afirmacionescientificasparalacuration.md)
- [Foundations Edge](foundationsedge.md)
- [MEDICAL INFORMATION FORM](medicalinformationform.md)
- [picolisp installation](picolispinstallation.md)
