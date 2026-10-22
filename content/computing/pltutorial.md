---
title: The Vikid PicoLisp Tutorial
date: '2021-08-26T01:17:21+04:00'
lastmod: '2021-08-28T07:12:43+04:00'
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
---

![picos](/assets/picos.png)
{.right}
 [computingFreedom](computingfreedom.md) |  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C Programmming](cprogramming.md) | [Operating Systems](os.md) | [Javascipt](javascript.md) | [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) | [Computer Security](computersecurity.md) | [Penti](penti.md) | [Picolisp Tutorial](pltutorial.md)

## The Vikid PicoLisp Tutorial

Start picolisp

```
$ pil +
```

Set some values

```
(setq A '(This is the value))  # Set the value of 'A'

(put 'A 'key1 'val1)           # Store property 'key1'

(put 'A 'key2 'val2)           # and 'key2'
```

inspect them with 'show'

```
(show 'A)                      # Now 'show' the symbol 'A'

(put 'B 'a 'A)        # Put 'A' under the 'a'-property of 'B'

(setq Lst '(A B C))   # Create a list with 'B' as second argument

(show Lst 2 'a)       # Show the property 'a of the 2nd element of 'Lst'
```

using vi and v.

```
(vi '(A B))

(v A B)
```

The pretty-print function
pp takes a symbol that has a function defined (or two symbols that specify message and class for a method definition).

```
(pp 'pretty)
```

more is a simple tool that displays the elements of a list one by one.

```
(more (1 2 3 4 5 6))
```

Optionally more takes a function as a second argument and applies that function to each element.

```
(more '(A B) show)
```

The what function returns a list of all internal symbols in the system which match a given pattern (with '@' wildcard characters).

```
(what "prin@")
```

The function who returns "who contains that", i.e. a list of symbols that contain a given argument somewhere in their value or property list.

```
(who 'print)
```

The function can returns a list which indicates which classes can accept a given message.

```
(can 'del>)
```

dep shows the dependencies in a class hierarchy.

```
(dep '+relation)
```

Defining Functions

```
(de hello ()
 (prinl "Hello world") )
```

call it

```
(hello)
```

A function with one argument

```
(de hello (X)
 (prinl "Hello " X) )
```

Call it

```
(hello "world")
```

Preventing arguments evaluation and variable number of arguments.
give the definition a single atomic parameter instead. PicoLisp will then bind all (unevaluated)
arguments as a list to that parameter.

```
(de foo X
 (list (car X) (cadr X)) )
```

Mixing evaluated arguments and variable number of unevaluated arguments

```
(de foo (X Y . Z)     # Evaluate only the first two args
 (list X Y Z) )
```

Variable number of evaluated arguments

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
 (while (args)
    (println (next) (args) (rest)) ) )

(de foo @
 (pass println 9 8 7)       # First print all arguments preceded by 9, 8, 7
 (pass + 9 8 7) )           # Then add all these values
```

There's no distinction between code and data in PicoLisp,
quote will do what you want.

```
((quote (X) (* X X)) 9)

(setq f '((X) (* X X)))  # This is equivalent to (de f (X) (* X X))
```

Debugging: Tracing and single-stepping.

```
$ pil app/file1.l -"trace 'foo" -main -"debug 'bar" app/file2.l +
```

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
```

`(mapc 'fun 'lst ..) -> any`
Applies fun to each element of lst.

```
(mapc untrace '(fact =0 *))
```

Debugging with debug

- inspect the current environment by typing variable names or calling functions
- execute (d) to recursively debug the next expression (looping through subexpressions of this expression)
- execute (e) to evaluate the next expression, to see what will happen without actually advancing on
- type ENTER (that is, enter an empty line) to leave the read-eval loop and continue with the next expression

```
(pp 'stamp)

(de stamp (Dat Tim)
   (and (=T Dat) (setq Dat (date T)))
   (default Dat (date) Tim (time T))
   (pack (dat$ Dat "-") " " (tim$ Tim T)) )

(debug 'stamp)

(unbug 'stamp)
```

Functional I/O

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

NIL: Besides the standard form, NIL is also recognized as (), [] or "".

```
: NIL
-> NIL
: ()
-> NIL
: ""
-> NIL
```

Output will always appear as NIL.
