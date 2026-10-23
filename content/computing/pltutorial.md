---
title: 'The Vikid PicoLisp Tutorial'
date: '2021-08-26T01:17:21+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A1445}'
original_name: pltutorial
original_blob: blob/B/7/612.txt
revisions: 18
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pltutorial
draft: false
topics:
- lisp
---

![picos](/assets/picos.png)
{.right}

## The Vikid PicoLisp Tutorial

These are the REPL habits I picked up when I learned PicoLisp. I re-ran every snippet on **PicoLisp 26.9** (pil21) in October 2026 and updated what had changed. The core language has barely moved since I first wrote this. What did change is the tooling around it: the editor, namespaces, and how you install it.

### Start PicoLisp

Build pil21 (see [PicoLisp Installation](../languages/picolispinstallation.md)) and start it in debug mode:

```
$ pil +          # after a global install
$ ./pil +        # or from inside the unpacked pil21 directory
```

The `+` matters: it loads the debug tools (`vi`, `doc`, `trace`, `debug`, `what`, `who`, `can`, `dep`…). Without it you get a plain runtime. Leave with `(bye)` or Ctrl-D.

### Symbols, values and properties

Set some values:

```
(setq A '(This is the value))  # Set the value of 'A'
(put 'A 'key1 'val1)           # Store property 'key1'
(put 'A 'key2 'val2)           # and 'key2'
```

Inspect them with `show`:

```
(show 'A)                      # Now 'show' the symbol 'A'
A (This is the value)
   key2 val2
   key1 val1
(put 'B 'a 'A)        # Put 'A' under the 'a'-property of 'B'
(setq Lst '(A B C))   # Create a list with 'B' as second element
(show Lst 2 'a)       # Show the property 'a of the 2nd element of 'Lst'
```

### Editing: vi and v

```
(vi '(A B))
(v A B)
```

In pil21, `vi` opens **Vip**, PicoLisp's own vi-style editor (written in PicoLisp, in `@lib/vip.l`). It edits the *source* of a function, or the value and properties of a symbol. When you write and quit, the change is read back into the running system. `v` does the same for symbols without quoting. Vip also has some newer extras: `:ai` and `:web` (an LLM client, via `@lib/ai.l`), and `:cal` for a calendar.

### Looking around the system

The pretty-print function `pp` takes a symbol that has a function defined (or two symbols that specify message and class for a method definition):

```
(pp 'pretty)
```

`more` displays the elements of a list one by one. Optionally it takes a function as a second argument and applies it to each element:

```
(more (1 2 3 4 5 6))
(more '(A B) show)
```

`what` returns all internal symbols that match a pattern (with `@` wildcards):

```
(what "prin@")
-> (prin prinl print print> println printsp)
```

`who` returns "who contains that": a list of symbols that contain a given argument somewhere in their value or property list:

```
(who 'print)
```

`can` tells you which classes accept a given message, and `dep` shows the dependencies in a class hierarchy:

```
(can 'del>)
-> ((del> . +Swap) (del> . +List) (del> . +Remote) (del> . +Entity) (del> . +relation))
(dep '+relation)
```

New in pil21: symbols live in **namespaces**. `(symbols)` shows the current search order, and `pico~foo` names a symbol in a specific namespace. Some libraries (for example `@lib/simul.l`, `@lib/ai.l`) define their own namespace, so call `(symbols '(simul pico))` or use the `simul~` prefix.

### Defining functions

```
(de hello ()
   (prinl "Hello world") )
(hello)
```

A function with one argument:

```
(de hello (X)
   (prinl "Hello " X) )
(hello "world")
```

To prevent argument evaluation and take a variable number of arguments, give the definition a single atomic parameter instead. PicoLisp will then bind all the (unevaluated) arguments as a list to that parameter:

```
(de foo X
   (list (car X) (cadr X)) )
```

Mixing evaluated arguments and a variable number of unevaluated arguments:

```
(de foo (X Y . Z)     # Evaluate only the first two args
   (list X Y Z) )
```

A variable number of evaluated arguments:

```
(de foo @
   (list (next) (next)) )

(de foo (X Y . @)
   (list X Y (next) (next)) )

(de foo @
   (while (args)                    # Check if there are some args left
      (let N (next)
         (println N (* N N)) ) ) )

(de foo @
   (pass println 9 8 7)       # First print all arguments preceded by 9, 8, 7
   (pass + 9 8 7) )           # Then add all these values
```

There's no distinction between code and data in PicoLisp, so `quote` will do what you want (see [quote](pilquote.md)):

```
((quote (X) (* X X)) 9)    # -> 81
(setq f '((X) (* X X)))    # This is equivalent to (de f (X) (* X X))
```

### Debugging: tracing and single-stepping

You can trace and debug from the command line:

```
$ pil app/file1.l -"trace 'foo" -main -"debug 'bar" app/file2.l +
```

Or from the REPL:

```
(de fact (N)
   (if (=0 N)
      1
      (* N (fact (dec N))) ) )
(trace 'fact)
(trace '=0)
(trace '*)
(fact 3)
(untrace 'fact)
(mapc untrace '(fact =0 *))   # mapc applies a function to each element
```

Debugging with `debug`:

- Inspect the current environment by typing variable names or calling functions.
- `(d)` recursively debugs the next expression.
- `(e)` evaluates the next expression, so you can see what would happen without advancing.
- An empty line (ENTER) leaves the break and continues with the next expression.

```
(pp 'stamp)
(debug 'stamp)
(stamp)
(unbug 'stamp)
```

When an error happens you land in a break REPL (prompt `!`). There, `(bt)` prints a backtrace, `^` holds the offending expression, and ENTER returns to the top level. `(lint 'foo)` and `(lintAll)` catch unused or undefined variables before you run anything.

### Functional I/O

```
(read)
(in "@lib.l" (read))
(in "@lib.l" (skip "#") (char))
(in "@lib.l" (while (from "nond") (println (read))))
(in "@lib.l" (from "(de ") (till " " T))
(in "f.l" (till NIL T))
(in "@doc/tut.html" (line T))
(in "@doc/tut.html" (line))
```

`@` at the start of a path means "the PicoLisp home directory", wherever it is installed. There is more on this in [Input/Output](plio.md).

### NIL

Besides the standard form, NIL is also recognised as `()` or `""`:

```
: NIL
-> NIL
: ()
-> NIL
: ""
-> NIL
```

Output will always appear as `NIL`. NIL is the empty list, false, and the end of every list all at once (see [Find Boxes in Lists](findboxes.md)).

### Where next

- [PicoLisp Tutorials](piltutorials.md) for a four-week path.
- The official [tutorial](https://software-lab.de/doc/tut.html), which this page follows closely, and the [reference](https://software-lab.de/doc/ref.html).
