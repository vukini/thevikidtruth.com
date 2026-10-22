---
title: balance.c
date: '2017-06-19T03:28:40+04:00'
lastmod: '2017-06-29T01:53:58+04:00'
original_id: '{A1133}'
original_name: balancec
original_blob: blob/B/6/051.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: balancec
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

# [balance.c](balancec.md)

> **Reading this in 2026.** This page reproduces `balance.c` from the PicoLisp sources (pil32 tools), as I studied them around 2017. It is a small helper program used when loading sorted data so that index trees come out balanced. PicoLisp is MIT-licensed, © Software Lab, Alexander Burger. Since 2020 the current PicoLisp is **pil21**, which is written in PicoLisp itself and compiled through LLVM, so the line-by-line details here belong to the older 32-bit C implementation; the ideas carry over. Current sources are at [software-lab.de](https://software-lab.de/down.html).


```
/* balance.c
 * 06jul05abu
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <signal.h>
#include <sys/wait.h>

int Len, Siz;
char *Line, **Data;

static void giveup(char *msg) {
   fprintf(stderr, "balance: %s\n", msg);
   exit(1);
}

static char *getLine(FILE *fp) {
	int i, c;
   char *s;

   i = 0;
   while ((c = getc_unlocked(fp)) != '\n') {
      if (c == EOF)
         return NULL;
      Line[i] = c;
      if (++i == Len  &&  !(Line = realloc(Line, Len *= 2)))
         giveup("No memory");
   }
   Line[i] = '\0';
   if (!(s = strdup(Line)))
      giveup("No memory");
   return s;
}

static void balance(char **data, int len) {
   if (len) {
      int n = (len + 1) / 2;
      char **p = data + n - 1;

      printf("%s\n", *p);
      balance(data, n - 1);
      balance(p + 1, len - n);
   }
}

// balance [-<cmd> [<arg> ..]]
// balance [<file>]
int main(int ac, char *av[]) {
   int cnt;
   char *s;
   pid_t pid = 0;
   FILE *fp = stdin;

   if (ac > 1) {
      if (*av[1] == '-') {
         int pfd[2];

         if (pipe(pfd) < 0)
            giveup("Pipe error\n");
         if ((pid = fork()) == 0) {
            close(pfd[0]);
            if (pfd[1] != STDOUT_FILENO)
               dup2(pfd[1], STDOUT_FILENO),  close(pfd[1]);
            execvp(av[1]+1, av+1);
         }
         if (pid < 0)
            giveup("Fork error\n");
         close(pfd[1]);
         if (!(fp = fdopen(pfd[0], "r")))
            giveup("Pipe open error\n");
      }
      else if (!(fp = fopen(av[1], "r")))
         giveup("File open error\n");
   }
   Line = malloc(Len = 4096);
   Data = malloc((Siz = 4096) * sizeof(char*));
   for (cnt = 0;  s = getLine(fp);  ++cnt) {
      if (cnt == Siz  &&  !(Data = realloc(Data, (Siz *= 2) * sizeof(char*))))
         giveup("No memory");
      Data[cnt] = s;
   }
   if (pid) {
      fclose(fp);
      while (waitpid(pid, NULL, 0) < 0)
         if (errno != EINTR)
            giveup("Pipe close error\n");
   }
   balance(Data, cnt);
   return 0;
}
```
