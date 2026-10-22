---
title: Strings in C Programming
date: '2016-11-22T21:52:26+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A331}'
original_name: cstrings
original_blob: blob/B/1/625.txt
revisions: 9
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: cstrings
draft: false
topics:
- c-systems
---

# Strings in C Programming

Here is the truth about strings in C: **there is no string type – only arrays of `char` that we agree end with a zero byte.** Every convenience and every CVE in C text handling follows from that convention.

### What it is, in plain words

A **C string** is a contiguous sequence of bytes ending in `'\0'`. The type used to point at one is `char *` (or `const char *` when you promise not to modify). The standard library in `<string.h>` and `<stdio.h>` provides the classic tools: `strlen`, `strcpy`, `strncpy`, `strcmp`, `strcat`, `strchr`, `strstr`, `sprintf`, `snprintf`.

```c
char greet[] = "hi";       /* {'h','i','\0'} – array you own */
const char *lit = "hi";    /* pointer to static literal – don't write through it */
```

### Why it matters

Buffer overflows, off-by-ones and forgotten null terminators have been the root of decades of vulnerabilities. Knowing how long a buffer is, always writing with an upper bound (`snprintf`, `memcpy` of a known size), and treating `gets` as radioactive are not style points – they are hygiene.

### An everyday analogy: a row of mailboxes with an empty one at the end

The letters of the string fill mailboxes. The empty mailbox (value 0) says "stop". There is no number on the row telling you how many boxes were allocated – only how many until the empty one. Walk past it and you're reading someone else's mail.

```mermaid
flowchart LR
  H[h] --> E[e] --> L1[l] --> L2[l] --> O[o] --> Z["\\0"]
```

### A hands-on example

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[16];
    const char *src = "Void Linux";

    /* Always bound your writes */
    snprintf(buf, sizeof buf, "%s", src);
    printf("len=%zu buf=%s\n", strlen(buf), buf);

    /* Concatenate safely */
    char path[64] = "/home/";
    snprintf(path + strlen(path), sizeof path - strlen(path), "%s/src", "vikid");
    puts(path);

    /* Compare */
    if (strcmp(buf, "Void Linux") == 0) puts("match");

    /* Tokenise carefully – strtok mutates and is not thread-safe */
    char csv[] = "a,b,c";
    for (char *tok = strtok(csv, ","); tok; tok = strtok(NULL, ","))
        puts(tok);

    return 0;
}
```

```bash
gcc -std=c23 -Wall -Wextra cstrings.c -o cstrings && ./cstrings
```

Prefer `snprintf` over `sprintf`, never use `gets`, and treat `strncpy`'s padding quirks as a reason to use `snprintf` or `memcpy` + explicit `'\0'`. For Unicode, remember `strlen` counts bytes, not characters – see [Unicode in C](unicodeinc.md) and [Characters](cchars.md).

### Common misconceptions

- **"`char *s` allocates a string."** It allocates a pointer. Storage lives elsewhere.
- **"`strncpy` always null-terminates."** It doesn't when the source is longer than `n`.
- **"`strlen` is free."** It walks the bytes every call – cache the length in hot loops.
- **"Literals are mutable."** Writing through them is undefined behaviour.
- **"`sizeof(str)` is the string length."** For an array it includes the terminator; for a pointer it's the pointer size.

### Safer patterns checklist

- Prefer `snprintf(dst, sizeof dst, "%s", src)` to any `strcpy` variant.
- Pass buffer sizes explicitly; never assume "big enough".
- Use `memcpy`/`memmove` when you know lengths; remember `memmove` handles overlap.
- For binary data, don't use string functions – null bytes are legal in binary and terminate C strings early.
- On POSIX, consider `strdup` / `asprintf` (GNU) and free what they allocate.
- Fuzz and test with AddressSanitizer: `gcc -fsanitize=address -g`.

If you need rich Unicode text processing, stop pretending libc strings are enough and use a dedicated library.

### Building strings safely in 2026

Three patterns cover nearly every real need:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    /* 1. Fixed buffer: snprintf truncates and tells you if it did */
    char path[32];
    int n = snprintf(path, sizeof path, "/home/%s/notes/%s", "vikid", "inbox.org");
    if (n < 0 || (size_t)n >= sizeof path)
        fprintf(stderr, "truncated: needed %d bytes\n", n + 1);

    /* 2. Exact size on the heap: ask snprintf for the length first */
    const char *user = "vikid";
    int len = snprintf(NULL, 0, "Hello, %s!", user);
    char *msg = malloc((size_t)len + 1);
    if (msg) {
        snprintf(msg, (size_t)len + 1, "Hello, %s!", user);
        puts(msg);
        free(msg);
    }

    /* 3. Duplicate: strdup is standard since C23 */
    char *copy = strdup("Void Linux");
    if (copy) { copy[0] = 'v'; puts(copy); free(copy); }
}
```

On glibc and musl, `asprintf` does pattern 2 in one call (a GNU/BSD extension, not ISO C). Avoid `strncpy` for general copying: it does not always add the terminating zero and pads with zeros otherwise, which surprises everyone. `strlcpy` and `strlcat`, long available on the BSDs, are now in glibc (2.38+) and musl too, and are fine choices when you need truncating copies.

### Strings and Unicode

A C string is bytes, not characters. With UTF-8, `strlen("café")` is **5**, because `é` takes two bytes. That is usually fine for storing and passing text around, but never cut a UTF-8 string at an arbitrary byte, and do not index it expecting the nth character. Use a library like libunistring or ICU when you need characters, or a language with real Unicode strings. PicoLisp, for example, treats its transient symbols as UTF-8 text and `(length "café")` gives **4**.

### Connections

- [Characters in C](cchars.md), [Literals](literals.md), [C Standard Library](cstandardlibrary.md).
- [C Programming](cprogramming.md), [Exploitation](exploitation.md).
- [Unicode in C](unicodeinc.md).

[Literals](literals.md) | [C Programming](cprogramming.md)
| [Unicode](unicodeinc.md)

The C11 standard provides a new prefix, u8, which allows you to define a UTF-8
string literal

A wide-string literal is defined using the prefix L:
L"This String is Wide."

and of the type **wchar_t**.

Although C does not strictly prohibit modifying string literals, you should not
attempt to do so.
