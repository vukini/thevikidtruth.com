---
title: utf2.c
date: '2017-06-29T02:06:24+04:00'
lastmod: '2017-06-29T02:12:41+04:00'
original_id: '{A1174}'
original_name: utf2c
original_blob: blob/B/6/110.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: utf2c
draft: false
topics:
- lisp
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
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

# [utf2.c](utf2c.md)

> **Reading this in 2026.** This page reproduces `utf2.c` from the PicoLisp sources (pil32 tools), as I studied them around 2017. It is a small character-set conversion utility (ISO-8859-15 to UTF-8). PicoLisp is MIT-licensed, © Software Lab, Alexander Burger. Since 2020 the current PicoLisp is **pil21**, which is written in PicoLisp itself and compiled through LLVM, so the line-by-line details here belong to the older 32-bit C implementation; the ideas carry over. Current sources are at [software-lab.de](https://software-lab.de/down.html).


```
/* utf2.c
 * 31mar05abu
 * Convert process or file (ISO-8859-15) to stdout (UTF-8, 2-Byte)
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <signal.h>
#include <sys/wait.h>

// utf2 [-<cmd> [<arg> ..]]
// utf2 [<Infile/ISO-8859-15>]
int main(int ac, char *av[]) {
	int c;
   pid_t pid = 0;
   FILE *fp = stdin;

   if (ac > 1) {
      if (*av[1] == '-') {
         int pfd[2];

         if (pipe(pfd) < 0) {
            fprintf(stderr, "utf2: Pipe error\n");
            return 1;
         }
         if ((pid = fork()) == 0) {
            close(pfd[0]);
            if (pfd[1] != STDOUT_FILENO)
               dup2(pfd[1], STDOUT_FILENO),  close(pfd[1]);
            execvp(av[1]+1, av+1);
         }
         if (pid < 0) {
            fprintf(stderr, "utf2: Fork error\n");
            return 1;
         }
         close(pfd[1]);
         if (!(fp = fdopen(pfd[0], "r"))) {
            fprintf(stderr, "utf2: Pipe open error\n");
            return 1;
         }
      }
      else if (!(fp = fopen(av[1], "r"))) {
         fprintf(stderr, "utf2: '%s' open error\n", av[1]);
         return 1;
      }
   }
	while ((c = getc_unlocked(fp)) != EOF) {
      if (c == 0xA4)
         putchar_unlocked(0xE2), putchar_unlocked(0x82), putchar_unlocked(0xAC);
      else if (c >= 0x80) {
         putchar_unlocked(0xC0 | c>>6 & 0x1F);
         putchar_unlocked(0x80 | c & 0x3F);
      }
      else
         putchar_unlocked(c);
	}
   if (pid) {
      fclose(fp);
      while (waitpid(pid, NULL, 0) < 0)
         if (errno != EINTR) {
            fprintf(stderr, "utf2: Pipe close error\n");
            return 1;
         }
   }
   return 0;
}
```
