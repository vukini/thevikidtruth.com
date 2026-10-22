---
title: C Syntax
date: '2021-08-27T00:51:47+04:00'
lastmod: '2023-05-19T01:12:26+04:00'
original_id: '{A1466}'
original_name: csytanx
original_blob: blob/B/12/265.txt
revisions: 17
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: csytanx
draft: false
topics:
- c-systems
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) |
  [The Compiler](thecompiler.md) |
  [Identifiers](identifier.md) |
  [Literals](literals.md) |
  [storage_linkage](storagelinkage.md) |

# C Syntax

Here is the truth about C's syntax: **there is very little of it.** A handful of control structures, a few ways to declare things, and that is the whole grammar most programs use. This page is the cheat sheet, but first a few words on why it is shaped the way it is, so it sticks.

### What it is, in plain words

C programs are built from three kinds of pieces:

- **Declarations** say what exists: variables, functions, types (`int n;`, `struct point { int x, y; };`, `typedef unsigned char byte;`).
- **Expressions** compute values: `a + b`, `f(x)`, `p->next`, `n = 0`. Assignment is an expression too, which is why `while ((c = getchar()) != EOF)` works.
- **Statements** control the order things happen: `if`, `switch`, `while`, `do`, `for`, `break`, `continue`, `return`, `goto`, and blocks `{ ... }`.

Any expression followed by `;` is a statement. A block groups statements and starts a new scope for the names declared inside it (see [Identifiers](identifier.md)).

### Why it matters

Almost every language that came after borrowed this syntax: C++, Java, C#, JavaScript, Go, Rust, Zig, Odin, PHP. Learn C's control flow and you can *read* half the code in the world. The quirks matter too: fall-through in `switch`, the dangling `else`, `=` versus `==`. Those quirks were copied as well.

### An everyday analogy: a recipe card

Declarations are the ingredient list. Expressions are the actual actions ("whisk two eggs"). Statements are the instructions about order: "if the batter is lumpy, whisk again", "repeat for each layer", "stop when golden". A recipe with no ingredient list makes no sense, and C agrees: since C99 you must declare a function before you call it.

### A hands-on example: all the structures in one program

```c
#include <stdio.h>
#include <stdbool.h>   /* not needed in C23, where bool is a keyword */

enum colour { RED, GREEN, BLUE };

typedef struct {
    const char *name;
    enum colour c;
} item;

static const char *colour_name(enum colour c) {
    switch (c) {
    case RED:   return "red";
    case GREEN: return "green";
    case BLUE:  return "blue";
    default:    return "?";
    }
}

int main(void) {
    item items[] = { {"apple", RED}, {"leaf", GREEN}, {"sky", BLUE}, {"lime", GREEN} };
    int n = sizeof items / sizeof items[0];
    int greens = 0;

    for (int i = 0; i < n; i++) {
        if (items[i].c != GREEN)
            continue;               /* skip non-green */
        greens++;
        printf("%s is %s\n", items[i].name, colour_name(items[i].c));
    }

    int k = 0;
    do {
        k++;
    } while (k < greens);

    printf("%d greens, loop ran %d times\n", greens, k);
    return 0;
}
```

```bash
gcc -std=c23 -Wall -Wextra syntax.c -o syntax && ./syntax
```

Notice `return` inside `switch` means no `break` is needed. Notice `for (int i = 0; ...)`: declaring the loop variable inside the `for` has been legal since C99 and is normal style today.

### Common misconceptions

- **"`switch` cases stop on their own."** They fall through to the next case unless you `break` or `return`. C23 adds `[[fallthrough]];` to mark it when you mean it, and `-Wimplicit-fallthrough` warns when you do not.
- **"`if (x = 5)` compares."** It assigns 5 and is always true. GCC warns with `-Wall`; some people write `if (5 == x)` to be safe.
- **"`goto` is always evil."** In C it is the standard way to jump to a single clean-up section on error, and the Linux kernel does it everywhere. Jumping *backwards* into loops is what to avoid.
- **"`do ... while` needs no semicolon."** It needs one: `} while (k < greens);`. The cheat sheet below omits it, so watch out.
- **"Braces are optional, so leave them out."** Legal for one statement, but adding a second line later without braces is a classic bug (Apple's 2014 "goto fail" TLS bug was exactly this).

### Connections

- [C Programming](cprogramming.md), [The Compiler](thecompiler.md), [Identifiers](identifier.md), [Objects in C](object.md), [Literals](literals.md).
- [JavaScript Control Flow](jscontrolflow.md) – the same syntax, borrowed.
- [Bash if statements](bashif.md) and [Bash case](bashcase.md) – the shell's very different take.
- [Assembly Language](assemblylanguage.md) – what loops and `if` become underneath: compares and jumps.

### The cheat sheet


 
- IF
- ```
  if (TEST) {
       CODE;
  } else if(TEST) {
       CODE;
  } else {
       CODE;
  }
  ```
- SWITCH
- ```
  switch(OP) {
    case CONST:
      CODE;
      break;
    default:
      CODE;
  }
  ```
- [cppreference:switch](https://en.cppreference.com/w/cpp/language/switch)
- WHILE
- ```
  while(TEST) {
    CODE;
  }
  ```
- ```
  while(TEST){
    if(TEST2){
      continue;
    }
    CODE;
  }
  ```
- ```
  while(TEST){
    if(TEST2){
      break;
    }
    CODE;
  }
  ```
- DO
- ```
  do {
    CODE;
  } while(TEST)
  ```
- FOR
- ```
  for (INIT; TEST; POST) {
    CODE;
  }
  ```
- ENUM
- ```
   enum{CONST1, CONST2} NAME;
  ```
- GOTO
- ```
  if(TEST){
    goto somewhere
  }
  somewhere:
    CODE;
  ```
- FUNCTION
- ```
  TYPE NAME(ARG1, ARG2, ..) {
    CODE;
    return VALUE;
  }
  ```
- TYPEDEF
- ```
  typedef DEF ID;
  ```
- STRUCT
- ```
  struct NAME {
    ELEMS;
  } [VAR_NAME];
  ```
- ```
  typedef struct [STRUC_NAME] {
    ELEMS;
  } ID
  ```
- UNION
- ```
  union NAME {
    ELEMS;
  }[VAR_NAME]
  ```
