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
