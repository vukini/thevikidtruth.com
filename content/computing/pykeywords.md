---
title: Python Keywords
date: '2021-09-05T05:50:54+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1627}'
original_name: pykeywords
original_blob: blob/B/10/313.txt
revisions: 1
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pykeywords
draft: false
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [pil sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) |
  [RasberryPi](rasberrypi.md) |

# Python Keywords

Here is the truth about Python keywords: **there are only a few dozen of them, they are the grammar of the language, and you cannot use them as names.** Everything else is a builtin or an ordinary identifier.

### What it is, in plain words

A **keyword** (reserved word) is a token the Python parser treats specially. As of Python 3.12/3.13 the set includes:

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

Soft keywords (context-dependent) include `match`, `case`, `type` (3.12+) and `_` in some positions. Builtins like `print`, `len`, `list` are *not* keywords – you *can* shadow them (please don't).

### Why it matters

Knowing the keyword list means you recognise structure when you read code, you avoid silly `SyntaxError`s when naming variables, and you know which constructs (`async`/`await`, `with`, `yield`) open whole styles of programming. It is also a short enough list to learn properly.

### An everyday analogy: rivets in a bridge

Most of a bridge is steel you could swap for another alloy. Rivets and joints are specific shapes that hold the structure together. Keywords are the joints. Rename a beam if you want; don't melt the joints.

### A hands-on example

```python
import keyword
print(keyword.kwlist)
print(keyword.iskeyword("yield"))   # True
print(keyword.iskeyword("print"))   # False – builtin, not keyword
print(keyword.issoftkeyword("match"))
```

A tour of the ones that structure programs:

```python
# Binding and control
x = None
if x is None and not False:
    pass
elif x in {1, 2}:
    pass
else:
    raise ValueError("nope")

for i in range(3):
    if i == 1:
        continue
    break
else:
    # for-else: runs if loop did *not* break
    print("exhausted")

# Functions, classes, scope
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

class Box:
    def __init__(self, n): self.n = n

# Exceptions and context managers
try:
    with open("/etc/os-release", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError as e:
    print(e)
finally:
    pass

# Iteration tools
def countdown(n):
    while n:
        yield n
        n -= 1

# Async
async def fetch():
    await some_io()
```

`lambda` makes tiny anonymous functions (`lambda x: x*x`) – useful in `map`/`sort` keys, easy to overuse. `assert` documents assumptions and can be stripped with `-O`. `del` unbinds a name (or deletes a slice); it does not "free memory now".

### Keywords versus builtins versus standard library

Three shelves:

1. **Keywords** – grammar (`if`, `def`, `yield`). Cannot assign.
2. **Builtins** – always available names (`len`, `range`, `str`), living in `builtins`. Can assign (but shouldn't).
3. **Standard library** – imported modules (`os`, `sys`, `json`, `pathlib`).

When something feels "part of the language", check which shelf it sits on. `print` moved from keyword-ish statement to builtin between Python 2 and 3; that one change explains a generation of tutorial confusion.

### Common misconceptions

- **"`print` is a keyword."** Not since Python 3. It's a builtin function.
- **"`_`, `match`, `case` are always keywords."** Soft keywords – only special in certain grammatical positions.
- **"You can `from keyword import …` to get them."** The `keyword` module only *lists* them.
- **"`is` and `==` are interchangeable."** `is` tests identity; `==` tests equality. Use `is` for `None`.
- **"Keywords never change."** Rarely they grow (`async`/`await`, soft `match`). Read What's New when you upgrade.

### Connections

- [Python](python.md), [Python Libraries](pythonlibrariestoolsandlinks.md).
- [BASH reserved words](bashreservewords.md) – the same idea in the shell.
- [Functional Programming](functional.md) – where `lambda` and `yield` lead.

  
```
False      await      else       import     pass

None       break      except     in         raise

True       class      finally    is         return

and        continue   for        lambda     try

as         def        from       nonlocal   while

assert     del        global     not        with

async      elif       if         or         yield
   
```
