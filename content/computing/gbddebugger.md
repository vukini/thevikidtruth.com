---
title: Using the C Debugger
date: '2021-08-27T01:41:01+04:00'
lastmod: '2022-09-15T05:28:31+04:00'
original_id: '{A1467}'
original_name: gbddebugger
original_blob: blob/B/11/337.txt
revisions: 14
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: gbddebugger
draft: false
topics:
- c-systems
---

[Readinglist](readinglist.md)  | [Quick Links](quicklinks.md) | [Algorithms](algorithms.md) | [Apple](apple.md) | [AssemblyLanguage](assemblylanguage.md) |
[BASH](bash.md) |   [C-Programmming](cprogramming.md) | [CommonLisp](commonlisp.md) | [Computer Security](computersecurity.md) | [CuisSmalltalk](cuissmalltalk.md) |
[Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) |
[Functional Programming](functional.md) |
[Firewalls](firewalls.md) |   [Git](git.md) | [GNUSmalltalk](gnusmalltalk.md) | [Haskell](haskell.md) | [Javascript](javascript.md) |  [Julia](julia.md) |
[Linux](linux.md) | [Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |[Machine Learning](machinelearning.md) |
[Networking](networking.md) | [Operating Systems](os.md) |[Open Data Science](opendatascience.md) | [Odin](odin.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) | [Purescript](purescript.md) |
[Python](python.md) |
[Racket](racket.md) | [Scheme](scheme.md) | [Social Engineering](internetexploitation.md) |
[Unity](unity.md) | [vim](vim.md) | [V](vlang.md) |
[Web Development](webdevelopment.md) | [Windows WSL](windowswsl.md) | [Zig](ziglang.md)

# Using the C Debugger

[The GBD Tutorial](http://www.gdbtutorial.com), [Online Docs](https://sourceware.org/gdb/current/onlinedocs/gdb/index.html#SEC_Contents)


Here is the truth about debuggers: **a debugger is a time machine with a pause button.** Instead of guessing what your program did and sprinkling `printf` everywhere, you stop it at the moment that matters and look at everything: every variable, the whole call stack, even the CPU registers. GDB, the GNU Debugger, is that time machine for C (and C++, Rust, Zig, Go, Fortran and assembly).

### What it is, in plain words

GDB was written by Richard Stallman in 1986 and is still actively developed (the 16.x series is current in 2026). It runs your program under its control using the kernel's `ptrace` interface, and uses the **debug information** that `gcc -g` puts into the binary (in DWARF format) to map machine addresses back to your source lines and variable names.

The core loop is always the same:

1. **Stop** – with a *breakpoint* (stop at this line or function), a *watchpoint* (stop when this variable changes) or a *catchpoint* (stop on a signal, exception or system call). Or the program stops itself by crashing.
2. **Look** – `print` variables, `backtrace` the stack, `info locals`, `x` to examine raw memory.
3. **Move** – `next` (step over calls), `step` (step into calls), `finish` (run until this function returns), `continue`.
4. **Change** – `set var x = 5` and carry on to test a theory without recompiling.

### Why it matters

- **Crashes become answers.** A segmentation fault tells you nothing. GDB on the same crash tells you the exact line, the bad pointer and how you got there.
- **You learn how C really works.** Watching the stack grow, pointers change and arrays decay is the best possible teacher for [Objects in C](object.md) and [Strings in C](cstrings.md).
- **It works on things you did not write.** Core dumps from production, running processes (`gdb -p PID`), and programs with no source (in assembly view).

### An everyday analogy: a video replay referee

In a football match you see a blur and argue about whether it was a foul. The video referee pauses the replay, steps forward frame by frame, zooms in on the boot and checks the angle from another camera. GDB is the replay booth for your program. You do not argue about what happened; you look.

### A hands-on example: find the bug in 60 seconds

```c
/* buggy.c */
#include <stdio.h>
#include <string.h>

int count_vowels(const char *s) {
    int n = 0;
    for (size_t i = 0; i <= strlen(s); i++)      /* bug: <= */
        if (strchr("aeiou", s[i])) n++;
    return n;
}

int main(void) {
    printf("%d\n", count_vowels("vikix"));      /* expect 2 */
}
```

It prints `3`. Why?

```bash
gcc -g -O0 buggy.c -o buggy
gdb -q ./buggy
(gdb) break count_vowels
(gdb) run
(gdb) display i
(gdb) display s[i]
(gdb) next            # press Enter to repeat; watch i and s[i]
...
1: i = 5
2: s[i] = 0 '\000'
(gdb) print strchr("aeiou", 0)
```

At `i = 5`, `s[i]` is the terminating zero byte, and `strchr` counts the string's *own* terminator as a match. The loop should be `i < strlen(s)`. Found by looking, not guessing.

Habits that pay off:

```bash
gdb -tui ./buggy                  # split screen: source above, commands below
ulimit -c unlimited               # allow core dumps, then after a crash:
gdb ./buggy core                  # post-mortem: 'bt' shows where it died
gdb -batch -ex run -ex bt ./buggy # run and print a backtrace, non-interactive
```

Put settings in `~/.gdbinit`, for example `set history save on` and `set print pretty on`. Inside Emacs, `M-x gdb` gives a multi-window IDE-style debugger; see [Emacs Notes](emacsnotes.md).

### Common misconceptions

- **"Debuggers are for beginners; experts use printf."** Experts use both. Printing is good for a history of events; a debugger is better for a single moment examined in depth.
- **"`-O2` code debugs fine."** The optimiser reorders and removes variables, so you see `<optimized out>`. Debug with `-O0 -g` (or `-Og`), then test optimised builds separately.
- **"GDB only works for C."** It debugs any language whose compiler emits DWARF, and has Python scripting for custom views.
- **"Sanitizers replace the debugger."** They find *that* something is wrong (`-fsanitize=address` reports the bad access); GDB shows you *why*. Use them together.
- **"`step` and `next` are the same."** `step` goes into function calls; `next` runs them in one go. Use `finish` to climb back out.

### Connections

- [C Programming](cprogramming.md), [The Compiler](thecompiler.md), [Objects in C](object.md), [Strings in C](cstrings.md), [C Standard Library](cstandardlibrary.md).
- [Assembly Language](assemblylanguage.md), [objdump](objdump.md), [pmap](pmap.md), [Linux Processes and Memory](linuxprocessesandmemory.md), [Linux Introspection](linuxinstrospection.md).
- [Emacs Notes](emacsnotes.md), [Penetration Testing](penetrationtesting.md) (debuggers are the core tool of exploit development).

## GDB command reference


- Compile your program with '-g'
- ```
  gcc -g main.c
  ```
- run gbd
- ```
  gdb a.out
  ```
- exit gbd
- ```
  (gdb) quit
  ```

Common Commands

- **help**	List gdb command categories
- **help** *category*	List gdb commands of category
- **help** *command*	Displays description of command
- -------------------------------------------------------
- **apropos** *search-word*	Display commands list containing search-word in their help description
- **info** *args*
- **i** *args*	Displays arguments of current function
- **info** *breakpoints*
- **info** *break*
- **info** *b*
- **i** *b*	Displays list of breakpoints
- **info** *break* breakpoint-number
- **i** *b* breakpoint-number	Displays description of breakpoint having breakpoint-number
- **info** *watchpoints*
- **i** *watchpoints*	Displays list of watchpoints
- **info** *registers*
- **i** *r*	Display processor's register contents
- **info** *threads*
- **i** *threads*	Display information about current thread
- **info** *set*
- **i** *set*	List set-able options
- -------------------------------------------------------
- **r**	Start running program until a breakpoint or end of program
- -------------------------------------------------------
- **break** *funname*
- **break** *line-no*
- **break** *ClassName::funcName*	Set a breakpoint at specified function or line number.
- **break** *+line-offset*
- **break** *-line-offset*	Set a breakpoint at specified number of lines forward or backward from current line of execution.
- **break** *filename:funcname*	Set a breapoint at specified funcname of given filename.
- **break** *filename:line-no*	Set a breakpoint at given line-no of specified filename.
- **break** **address*	Set a breakpoint at specified instrunction address.
- **break** *line-no if condition*	Set a conditional breakpoint at line-no of current file. Program will suspend only when condition is true.
- **break** *line thread thread-no*	Set a breakpoint at line in thread with thread-no.
- -------------------------------------------------------
- **tbreak**	tbreak is similar to break but it will temporary breakpoint. i.e. Breakpoint will be deleted once it is hit.
- -------------------------------------------------------
- **watch** *condition*	Set a watchpoint for given condition. Program will suspend when condition is true.
- -------------------------------------------------------
- **clear**
- **clear** *function*
- **clear** *line-number*	Delete breakpoints as identified by command option.
- **Delete**  all breakpoints in function
- -------------------------------------------------------
- **Delete** *breakpoints* at given line
- **delete**	Delete all breakpoints, watchpoints, or catchpoints.
- **delete** *breakpoint-number*
- **delete** *range*	Delete the breakpoints, watchpoints, or catchpoints specified by number or ranges.
- -------------------------------------------------------
- **disable** *breakpoint-number*
- **disable** *range*
- -------------------------------------------------------
- **enable** *breakpoint-number*
- **enable** *range*	Enable/Disable breakpoints, watchpoints or catchpoints specified by number or ranges.
- **enable** *breakpoint-number* once	Enables given breakpoint once. And disables it after it is hit.
- -------------------------------------------------------
- **continue**
- **c**	Continues/Resumes running the program until the next breakpoint or end of program
- **continue** *number*	Continue but ignore current breakpoint  number times.
- -------------------------------------------------------
- **finish**	Continue until the current function is finished
- -------------------------------------------------------
- **step**	Runs the next line of the program
- **step** *N*	Runs the next N lines of program
- -------------------------------------------------------
- **next**   Like s, but it does not step into functions
- **print** *var*	Prints the current value of the variable "var"
- **set** *var=val*	Assign "val" value to the variable "var"
- **backtrace**	Prints a stack trace
- **q**	Quit from gdb

#### External Links

- [Debugging with GDB, Edition.pdf - Free download books](https://www.dbooks.org/debugging-with-gdb-0983159238/)
