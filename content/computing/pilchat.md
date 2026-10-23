---
title: 'PicoLisp Chat Program'
date: '2017-06-14T02:03:19+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
original_id: '{A1062}'
original_name: pilchat
original_blob: blob/B/5/623.txt
revisions: 24
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pilchat
draft: false
topics:
- lisp
---

# PicoLisp Chat Program

# A Study

This is one of my favourite little PicoLisp programs: **a multi-user chat server in about 25 lines.** It used to ship in the PicoLisp sources as `misc/chat`. Current PicoLisp (pil21) no longer includes it, so below is the full source, re-tested on **PicoLisp 26.9** in October 2026, with my walk-through.

![chat](/assets/chat.png)
{.center}

## The source

Save this as `chat`:

```picolisp
#!/usr/bin/pil
# chat: a tiny multi-user chat server on port 4004
# *Port *Sock *Name

(de chat Lst
   (out *Sock
      (mapc prin Lst)
      (prinl)
      (flush) ) )

(setq *Port (port 4004))

(loop
   (setq *Sock (listen *Port))
   (NIL (fork) (close *Port))
   (close *Sock) )

(out *Sock
   (prin "Please enter your name: ")
   (flush) )
(in *Sock (setq *Name (line T)))

(tell 'chat "+++ " *Name " arrived +++")

(task *Sock
   (in @
      (ifn (eof)
         (tell 'chat *Name "> " (line T))
         (tell 'chat "--- " *Name " left ---")
         (bye) ) ) )
(wait)
```

## Running chat

Make it executable:

```
$ chmod 755 chat
```

**Line 1, the shebang**, tells the shell which interpreter runs the script. In 2017 I had to edit it to something like `#!/home/emperor/picoLisp/bin/picolisp /home/emperor/picoLisp/lib.l`. With pil21 it is simpler. After a global install (see [PicoLisp Installation](../languages/picolispinstallation.md)) `/usr/bin/pil` exists and the line above just works. If you only built pil21 in your home folder, point it at the `pil` script there instead, for example `#!/home/emperor/pil21/pil`.

Start the server:

```
$ ./chat
```

Now open two more terminals and connect to port 4004 in each, with `telnet` or, if telnet isn't installed (common on modern distros), `nc`:

```
$ telnet localhost 4004
$ nc localhost 4004
```

![telnet-1](/assets/telnet-1.png)
{.center}

Type a name in each terminal, and you will see the arrivals announced in the other one. Then chat.

![telnet-2](/assets/telnet-2.png)
{.center}

When I tested it on 26.9, "ali" and "bob" connected; bob saw `ali> hello bob` and then `--- ali left ---`, and ali saw `+++ bob arrived +++`. Note that you never see your own messages echoed back.

Exiting telnet can be confusing, because Ctrl-C is passed through to the remote end instead of stopping telnet. Press `Ctrl-]` and then type `quit`. With `nc`, Ctrl-C works normally.

## Examining the source

**The comment `# *Port *Sock *Name`** lists the globals in use. A leading `*` on global variables is a PicoLisp convention.

**`(de chat Lst ...)`** defines `chat` with a single atomic parameter, so it receives *all* its arguments as a list (see [The Vikid PicoLisp Tutorial](pltutorial.md)). It prints them to this process's socket. How it gets called becomes clear below.

**`(setq *Port (port 4004))`** opens a TCP port and returns a socket descriptor for it. So we look out for a [listen](https://software-lab.de/doc/refL.html#listen) or `accept` later in the code.

**The `loop`** is the idiomatic PicoLisp shape for a forking server. It is an infinite loop with conditional exits ([loop in the reference](https://software-lab.de/doc/refL.html#loop)):

```
(loop
   (setq *Sock (listen *Port))
   (NIL (fork) (close *Port))
   (close *Sock) )
```

- `listen` waits, indefinitely, until a client connects, and returns the new connection's descriptor in `*Sock`.
- `(fork)` creates a child process, an exact copy of the server, at exactly this point. Let's call the server **process 0** and the children **process 1, 2, …**
- In **process 0**, `fork` returns the child's PID, which is never NIL, so the exit clause `(NIL ...)` does not fire. The server closes its copy of `*Sock` (the child owns that conversation now) and loops back to `listen` for the next client.
- In the **child**, `fork` returns `NIL`, so the exit clause fires. The child closes `*Port` (only the server should accept connections) and leaves the loop. Everything after the loop runs only in children, one per connected user.

**Asking for a name.** `out` and `in` temporarily redirect output and input to the socket. `(line T)` reads one line as a string.

**`tell`** is the magic. It sends an expression to *all other* PicoLisp processes in the same family (the server's children), and each of them evaluates it. So `(tell 'chat "+++ " *Name " arrived +++")` makes every *other* child run `chat`, which prints to *its own* user's socket. That is the broadcast, with no shared memory and no message queue to write.

**`task`** installs a background handler on `*Sock`. Whenever input arrives, the body runs with `@` bound to the descriptor. If it isn't end-of-file, the line is broadcast with the sender's name. On EOF (the user disconnected) we announce the departure and `bye` ends this child.

**`(wait)`** waits forever, letting the `task` handlers and incoming `tell` messages do the work.

**It's amazing what you can achieve with so few lines of code!** The same pattern of fork per connection, `tell` between processes and `task` for events sits underneath PicoLisp's web application server. See [Application Development](appdev.md) and [http.l](httpl.md).

## Things to try

- Add a `/who` command that lists everyone online (hint: `tell` everyone to reply).
- Timestamp messages with `(tim$ (time))`.

![Sig](/assets/sig.jpg)
