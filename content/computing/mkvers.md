---
title: mkVers
date: '2017-06-29T02:03:06+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A1165}'
original_name: mkvers
original_blob: blob/B/6/100.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: mkvers
draft: false
topics:
- lisp
---

[Open Data Science](opendatascience.md)

# [mkVers](mkvers.md)

`mkVers` was a tiny PicoLisp script from the 2010s source tree. It stamped the current version into the C header `vers.h`, so that the C interpreter (pil32) reported the same version as the 64-bit one (pil64). I studied it in 2017; this page is updated for 2026.

### What it did

```
#!../bin/picolisp ../lib.l
# 07mar11abu
# (c) Software Lab. Alexander Burger

(load "../src64/version.l")

(out "vers.h"
   (prinl
      "static byte Version[4] = {"
      (glue "," *Version)
      "};" ) )

(bye)

# vi:et:ts=3:sw=3
```

1. **The shebang** runs `../bin/picolisp` with `../lib.l`. Back then the interpreter binary and the base library were given explicitly. Today that is the job of the `pil` wrapper script.
2. **`(load "../src64/version.l")`** read the single source of truth, `*Version`, from the pil64 tree.
3. **`(out "vers.h" ...)`** redirected output into the header file, and `glue` joined the numbers with commas: `(17 6 13)` became `17,6,13`.

It is a neat example of PicoLisp as a build tool: five lines of Lisp generating C.

### What happened to it

**pil21 has no `mkVers`.** There is no C interpreter left to stamp. The version lives directly in `src/vers.l` as `(pico~de *Version 26 9 25)`, which the LLVM build compiles straight into the binary. One file, nothing generated. See [vers.h](versh.md).

The same trick is still useful in your own projects:

```picolisp
(out "version.h"
   (prinl "#define APP_VERSION \"" (glue "." (version T)) "\"") )
```

On 26.9 that writes `#define APP_VERSION "26.9.25"`.

See also: [Makefile](makefile.md), [PicoLisp Sources](pilsource.md).
