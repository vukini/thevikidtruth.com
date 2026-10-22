---
title: ext.c
date: '2017-06-19T03:29:43+04:00'
lastmod: '2017-06-29T01:55:17+04:00'
original_id: '{A1135}'
original_name: extc
original_blob: blob/B/6/053.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: extc
draft: false
topics:
- lisp
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md) | [Networking](networking.md) | [Machine Learning](machinelearning.md) |
  [Git](git.md) |
  [Machine Learning](machinelearning.md) |
  [Algorithms](algorithms.md) |
  [Open Data Science](opendatascience.md)

# [ext.c](extc.md)

> **Reading this in 2026.** This page reproduces `ext.c` from the PicoLisp sources (pil32), as I studied them around 2017. It is the optional extension module with helpers such as `ext:Snx` (a soundex-like key) and Base64 encoding. PicoLisp is MIT-licensed, © Software Lab, Alexander Burger. Since 2020 the current PicoLisp is **pil21**, which is written in PicoLisp itself and compiled through LLVM, so the line-by-line details here belong to the older 32-bit C implementation; the ideas carry over. Current sources are at [software-lab.de](https://software-lab.de/down.html).


```
/* 01apr16abu
 * (c) Software Lab. Alexander Burger
 */

#include "pico.h"

/*** Soundex Algorithm ***/
static int SnxTab[] = {
   '0', '1', '2', '3', '4', '5', '6', '7',  // 48
   '8', '9',   0,   0,   0,   0,   0,   0,
     0,   0, 'F', 'S', 'T',   0, 'F', 'S',  // 64
     0,   0, 'S', 'S', 'L', 'N', 'N',   0,
   'F', 'S', 'R', 'S', 'T',   0, 'F', 'F',
   'S',   0, 'S',   0,   0,   0,   0,   0,
     0,   0, 'F', 'S', 'T',   0, 'F', 'S',  // 96
     0,   0, 'S', 'S', 'L', 'N', 'N',   0,
   'F', 'S', 'R', 'S', 'T',   0, 'F', 'F',
   'S',   0, 'S',   0,   0,   0,   0,   0,
     0,   0,   0,   0,   0,   0,   0,   0,  // 128
     0,   0,   0,   0,   0,   0,   0,   0,
     0,   0,   0,   0,   0,   0,   0,   0,
     0,   0,   0,   0,   0,   0,   0,   0,
     0,   0,   0,   0,   0,   0,   0,   0,  // 160
     0,   0,   0,   0,   0,   0,   0,   0,
     0,   0,   0,   0,   0,   0,   0,   0,
     0,   0,   0,   0,   0,   0,   0,   0,
     0,   0,   0,   0,   0,   0,   0, 'S',  // 192
     0,   0,   0,   0,   0,   0,   0,   0,
   'T', 'N',   0,   0,   0,   0,   0, 'S',
     0,   0,   0,   0,   0,   0,   0, 'S',
     0,   0,   0,   0,   0,   0,   0, 'S',  // 224
     0,   0,   0,   0,   0,   0,   0,   0,
     0, 'N'
   // ...
};

#define SNXBASE   48
#define SNXSIZE   ((int)(sizeof(SnxTab) / sizeof(int)))

// (ext:Snx 'any ['cnt]) -> sym
any Snx(any ex) {
   int n, c, i, last;
   any x, nm;
   cell c1, c2;

   x = cdr(ex);
   if (!isSym(x = EVAL(car(x))) || !(c = symChar(name(x))))
      return Nil;
   while (c < SNXBASE)
      if (!(c = symChar(NULL)))
         return Nil;
   Push(c1, x);
   n = isCell(x = cddr(ex))? evCnt(ex,x) : 24;
   if (c >= 'a' && c <= 'z' || c == 128 || c >= 224 && c < 255)
      c &= ~0x20;
   Push(c2, boxChar(last = c, &i, &nm));
   while (c = symChar(NULL))
      if (c > ' ') {
         if ((c -= SNXBASE) < 0 || c >= SNXSIZE || !(c = SnxTab[c]))
            last = 0;
         else if (c != last) {
            if (!--n)
               break;
            charSym(last = c, &i, &nm);
         }
      }
   drop(c1);
   return consStr(data(c2));
}

/*** Math ***/
// (ext:Pow 'x 'y 'scale) -> num
any Pow(any ex) {
   double x, y, n;

   x = evDouble(ex, cdr(ex));
   y = evDouble(ex, cddr(ex));
   n = evDouble(ex, cdddr(ex));
   return doubleToNum(n * pow(x / n, y / n));
}

// (ext:Exp 'x 'scale) -> num
any Exp(any ex) {
   double x, n;

   x = evDouble(ex, cdr(ex));
   n = evDouble(ex, cddr(ex));
   return doubleToNum(n * exp(x / n));
}

// (ext:Log 'x 'scale) -> num
any Log(any ex) {
   double x, n;

   x = evDouble(ex, cdr(ex));
   n = evDouble(ex, cddr(ex));
   return doubleToNum(n * log(x / n));
}

// (ext:Sin 'angle 'scale) -> num
any Sin(any ex) {
   double a, n;

   a = evDouble(ex, cdr(ex));
   n = evDouble(ex, cddr(ex));
   return doubleToNum(n * sin(a / n));
}

// (ext:Cos 'angle 'scale) -> num
any Cos(any ex) {
   double a, n;

   a = evDouble(ex, cdr(ex));
   n = evDouble(ex, cddr(ex));
   return doubleToNum(n * cos(a / n));
}

// (ext:Tan 'angle 'scale) -> num
any Tan(any ex) {
   double a, n;

   a = evDouble(ex, cdr(ex));
   n = evDouble(ex, cddr(ex));
   return doubleToNum(n * tan(a / n));
}

// (ext:Asin 'angle 'scale) -> num
any Asin(any ex) {
   double a, n;

   a = evDouble(ex, cdr(ex));
   n = evDouble(ex, cddr(ex));
   return doubleToNum(n * asin(a / n));
}

// (ext:Acos 'angle 'scale) -> num
any Acos(any ex) {
   double a, n;

   a = evDouble(ex, cdr(ex));
   n = evDouble(ex, cddr(ex));
   return doubleToNum(n * acos(a / n));
}

// (ext:Atan 'angle 'scale) -> num
any Atan(any ex) {
   double a, n;

   a = evDouble(ex, cdr(ex));
   n = evDouble(ex, cddr(ex));
   return doubleToNum(n * atan(a / n));
}

// (ext:Atan2 'x 'y 'scale) -> num
any Atan2(any ex) {
   double x, y, n;

   x = evDouble(ex, cdr(ex));
   y = evDouble(ex, cddr(ex));
   n = evDouble(ex, cdddr(ex));
   return doubleToNum(n * atan2(x / n, y / n));
}

/*** U-Law Encoding ***/
#define BIAS   132
#define CLIP   (32767-BIAS)

// (ext:Ulaw 'cnt) -> cnt  # SEEEMMMM
any Ulaw(any ex) {
   int val, sign, tmp, exp;

   val = (int)evCnt(ex,cdr(ex));
   sign = 0;
   if (val < 0)
      val = -val,  sign = 0x80;
   if (val > CLIP)
      val = CLIP;
   tmp = (val += BIAS) << 1;
   for (exp = 7;  exp > 0  &&  !(tmp & 0x8000);  --exp, tmp <<= 1);
   return boxCnt(~(sign  |  exp<<4  |  val >> exp+3 & 0x000F) & 0xFF);
}

/*** Base64 Encoding ***/
static char Chr64[] =
   "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

// (ext:Base64) -> num|NIL
// (ext:Base64 'num1|NIL ['num2|NIL ['num3|NIL]]) -> flg
any Base64(any x) {
   any y;
   int c, d;
   char *p;
   static int i, n;

   if (!isCell(x = cdr(x))) {
      if (!Chr)
         Env.get();
      while (Chr >= 0  &&  Chr <= ' ')
         Env.get();
      if (!(p = strchr(Chr64, Chr))) {
         if (Chr == '=') {
            Env.get();
            if (i == 1)
               Env.get();
         }
         i = 0;
         return Nil;
      }
      c = p - Chr64;
      Env.get();
      switch (i) {
      case 0:
         if (!(p = strchr(Chr64, Chr))) {
            i = 0;
            return Nil;
         }
         n = p - Chr64;
         Env.get();
         ++i;
         return boxCnt(c << 2 | n >> 4);
      case 1:
         d = (n & 15) << 4 | c >> 2;
         n = c;
         ++i;
         return boxCnt(d);
      }
      i = 0;
      return boxCnt((n & 3) << 6 | c);
   }
   if (isNil(y = EVAL(car(x))))
      return Nil;
   c = unDig(y) / 2;
   Env.put(Chr64[c >> 2]);
   x = cdr(x);
   if (isNil(y = EVAL(car(x)))) {
      Env.put(Chr64[(c & 3) << 4]),  Env.put('='),  Env.put('=');
      return Nil;
   }
   d = unDig(y) / 2;
   Env.put(Chr64[(c & 3) << 4 | d >> 4]);
   x = cdr(x);
   if (isNil(y = EVAL(car(x)))) {
      Env.put(Chr64[(d & 15) << 2]),  Env.put('=');
      return Nil;
   }
   c = unDig(y) / 2;
   Env.put(Chr64[(d & 15) << 2 | c >> 6]),  Env.put(Chr64[c & 63]);
   return T;
}

/*** Password hashing ***/
// (ext:Crypt 'key 'salt) -> str
any Crypt(any x) {
   any y;

   y = evSym(x = cdr(x));
   {
      char key[bufSize(y)];

      bufString(y, key);
      y = evSym(cdr(x));
      {
         char salt[bufSize(y)];

         bufString(y, salt);
         return mkStr(crypt(key, salt));
      }
   }
}
```
