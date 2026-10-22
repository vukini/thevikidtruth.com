---
title: Picolisp Chat Program
date: '2017-06-14T02:03:19+04:00'
lastmod: '2017-06-18T11:31:56+04:00'
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
draft: true
review: update
---

# Picolisp Chat Program

[Computing](computing.md) | [Picolisp](picolisp.md) | [ASM](pilasm.md) | [pil sources](pilsource.md)

# A Study

Once you have downloaded the picolisp sources you will find a folder called `  misc  ` inside the main `  picoLisp  ` folder.
This has various example programs that are great to study.

In this article we are going to study the code inside the **chat** program.

The whole source for this is at the bottom of the article for reference.

## Running Chat

Firstly make sure the permissions are set correctly. In bash type:

```
 $ chmod 755 chat
```

The program works as a chat server. We will first edit the server file to point to the correct binaries and libraries.
Then we will open two additional terminals within which we will simulate a chat between two parties.

The file comes with a 'shebang' on line 1, this line points the file to the correct pil binaries & sources
when running the program as a script.

We will will edit it to point to the right place in your system.

```
#!bin/picolisp lib.l
```

change it to:

```
#!/home/emperor/picoLisp/bin/picolisp /home/emperor/picoLisp/lib.l
```

Now, I am assuming that you installed picolisp in your home folder. Mine is called ` /home/emperor `.
Do whats right in your particular circumstance.

Now the server is ready to run. Inside the folder misc/chat in the terminal run:

```
$ ./chat
```

The server is now running and ready to accept connections.

![chat](/assets/chat.png)
{.center}

Now open two separate terminals. We are going to use [telnet](telnet.md "MISSING PAGE") to connect to the server.

**telnet** uses the following command signature:

```
$ telnet host port
```

in this particular case our host is **localhost** and our port is `4004` as set on line 12 of the source. So type:

```
$ telnet localhost 4004
```

you should see the following output:

![telnet-1](/assets/telnet-1.png)
{.center}

Type in a name and do the same again in the second terminal and you will now is the out put in the first terminal.

![telnet-2](/assets/telnet-2.png)
{.center}

You are ready to chat. So play around.

(Learn about telnet and client-server programming [here](https://www.youtube.com/watch?v=eA9mnY1Z2so))

Now you may find it hard to exit from telnet when pressing ctrl-C. Fear not. Telnet captures this sequence as an input
and the input is not caught by the terminal it self.

This is the explanation I found on Stackoverflow:

```
The reason Ctrl+C doesn't interrupt or suspend the connection is that an interrupt signal or a Ctrl+C
often needs to be passed through to the remote end (so you can break programs there, if you're working
on a remote shell), which wouldn't be possible if the telnet client intercepted it for its own purposes.
– blubberdiblub
```

So if your on Ubuntu or some flavour of linux this should work:

```
ctrl-]
```

then

```
> quit
```

Now that we have understood how the chat works and played around with it, lets try to understand the code. **Its amazing
what you can achieve with just 32 lines of code!**

## Examining the Source

All picolisp programs kind of start the same way.

```
  1 #!/home/emperor/picoLisp/bin/picolisp /home/emperor/picoLisp/lib.l
  2 # 14jun17abu
  3
  4 # *Port *Sock *Name
```

**Line 1** is a Unix convention to tell the terminal which interpreter to use. In this case **picolisp**
with the library lib.l

**Line 2** is a comment telling you when the file was last modified any by who, **abu** (short for Alexander Burger, creator
of picolisp)
in this case.

**Line 4** tells you which Globals are in use (***Variable**, is a picolisp convention).

**Line 6 - 9**. Here, we define the chat function. Lets ignore it for now as how it is used becomes apparent later.

**Line 12** - Working with TCP Sockets.

```
(setq *Port (port 4004))
```

we call `(port 4004)` and set it to the global ![*Port} for easy reference.

This what a call to
[port](https://picolisp.com/wiki/@doc/refP.html#port) does:

```
Opens a TCP-Port and returns a socket descriptor which we can use to connect to the port.
```

We do this later with **listen**.

So we know to look out for either a [listen](https://picolisp.com/wiki/@doc/refL.html#listen) or `accept`
later in the code.

**lines 14-17**: This use of **loop** is an idiomatic picolisp style for writing **client-server code**.

Let's examine it in detail.

```
 14 (loop
 15    (setq *Sock (listen *Port))
 16    (NIL (fork) (close *Port))
 17    (close *Sock) )
```

**Line 14** Starts a loop. This is good point to look at the
[Picolisp Reference](https://picolisp.com/wiki/@doc/refL.html#loop) for how a loop works.

Essentially, **we are entering
an infinite loop with conditional exits.**

Here there is only one conditional exit, on line 16.

When we load the chat program, the code will run (from line 1 to 13) until **Line 14** when the process enters a
'potentially' infinite loop doomed to repeat lines 15 - 17 again and again.

Let's examine what happens now.

**Line 15** We start listening to the ***Port** we just established on line 12 with the TCP Protocol.

When executing
[listen](https://picolisp.com/wiki/@doc/refL.html#listen), your program will
just wait there 'indefinitely' until a connection is made.

That's why we used `telnet localhost 4004` earlier, precisely to connect with this port. Assuming this is done,
**listen** will return with a file descriptor, which we then set to *Sock.

**Line 16** This is the core of our client-server pattern. We have a conditional exit point in the loop. We will spawn
a **new process** here with a call to [fork](https://picolisp.com/wiki/@doc/refF.html#fork).

So lets name these processes incrementally (so we don't get confused).

Our current process is **process 0** also called **the server.** It will fork new **child processes** in sequential order
named **Process 1, 2, ...**.

So here in **Line 15**, two things happen,

1. In **process 0** i.e. the Server, fork will return some number, which is never NIL. The Exit condition of the loop
  is NOT met, so we move on to line 17. Line 16 has no other effect.
  **Line 17** we close the connection to *Sock. And restart the loop. Process 0 will go back to line 15 and wait another
  connection. The server (process 0) closes it's connection with the telnet process. No data from telnet will reach
  the server anymore. Which is fine and what we want. That is left to the child.
1. Fork creates a new process, which is essentially a copy of process 0. It has the same state, it is in the same place,
  it was just at the place (fork) was called
  EXCEPT fork returns **NIL**. This time the loop exit condition is met.
  ```
  (close *Port)
  ```
   is executed. The child process will not be in a position to listen for anymore connections. Neither should
  it. It is already connected to the telnet session we used to connect to it.

**So to summarize**

- Before we entered the loop we have a single process, **process 0**, with an open TCP port.
- **Process 0** then enters the
  loop and starts **listening** for connections, and waits there.
- Once a connection is made we enter a **loop condition.**
- Now we have 2 process, the parent (process 0) and a child process (process 1).
- **Process 0**, the parent, closes ***Sock** connecting to the telnet process and goes back into loop (line 14),
  ready to spawn new client processes as connections come in.
- **Process 1**, the client, closes ***Port** as it used by the Server and which needs it to make new connections.
- It has a **direct TCP
  connection** to the outside process such as telnet through ***Sock.**
- **Process 1** will now continue executing the rest of the code in the file, **process 0** will not. It is stuck in the loop on
  line 14.

**line 19 - 21** in **process 1** we send data via [out](https://picolisp.com/wiki/@doc/refO.html#out) to our telnet process.

**Line 20** we print **"Please enter your name: "** so this line appears in our telnet process.

**Line 21** we [flush](https://picolisp.com/wiki/@doc/refF.html#flush) all buffered data to our output. In Unix, a
newline automatically flushes stdout, but here we don't have a newline here.

**Line 22** We presume that a person on the telnet process types a name and presses ENTER. So we use
[in](https://picolisp.com/wiki/@doc/refI.html#in). `(line T)` takes the input typed and converts it to a string.
See [line](https://picolisp.com/wiki/@doc/refL.html#line).

We then set that to the global ***Nam**e so that we have a reference to it.

**line 24** Use of **Family Inter Process Communication** using [tell](https://picolisp.com/wiki/@doc/refT.html#tell).

**tell** is interesting. It takes its arguments and converts it into a list. This list is then executed in all processes
 that are either **children of the process or siblings of the process.** That is all process 1, 2 onwards.

So take the line

```
(tell 'chat "+++ " *Name " arrived +++")
```

this is effectively converted to:

```
(chat "+++ " *Name " arrived +++")
```

and executed in every client process created by the server. So effectively, When we open telnet for the second chat
window there by creating process 2, it's sibling Process 1, will execute this code.
Printing:

```
+++ Vikid arrived +++
```

in the first terminal of the telnet process.

This code, **line 6-9**, should now be familiar:

```
  6 (de chat Lst
  7    (out *Sock
  8       (mapc prin Lst)
  9       (prinl) ) )
```

Each process has it's own handle ***Sock**, the TCP connection.

It prints the arguments given to `chat`, namely,
"+++ " *Name " arrived +++", then prints a newline with `prinl`

**We are now approaching the end of the code.**

**Line 26 - 31**

We have done a lot of work, and we haven't even started chatting! So these next few lines will finally take care of
that :-)

Of course once you finish chatting. You would like your code, to close all revelant connections and processes like a good citizen,
and perhaps even notify other people that you have left, so they don't keep chatting to you.

So let's see how it is done.

Read up on [task](https://picolisp.com/wiki/@doc/refT.html#task),
[*Run](https://picolisp.com/wiki/@doc/refR.html#*Run) and
[wait](https://picolisp.com/wiki/@doc/refW.html#wait) first.

```
 26 (task *Sock
 27    (in @
 28       (ifn (eof)
 29          (tell 'chat *Name "> " (line T))
 30          (tell 'chat "--- " *Name " left ---")
 31          (bye) ) ) )
 32 (wait)
```

**Line 26** This can be simplified conceptually to

```
  (task *Sock (some code to run))
```

That is **setup a task to run some code when data arrives at *Sock**.

**Line 32** We then make a call to `(wait)`.

That is our processes (1, 2, etc...) will sit and wait for some data to come in.

When the data arrives, the task we set up, which is now sitting in the *Run global, fires of the code in
**lines 27 - 31**.

**Lines 27 - 31**

**Line 27** Here the **@** is set to ***Sock**, as ***Run tasks** act like [flow functions](https://software-lab.de/doc/ref.html).

**Line 28** So we take 1 of 2 options.

1. If we do not encounter a End-of-File, [eof](https://picolisp.com/wiki/@doc/refE.html#eof), then,
  use **tell** to broadcast the contents received from `(line T)` to all client processes (1, 2, ...).
  **This is the heart of the Chat!**
1. **line 30** Else, if you do encounter a **eof**, then broadcast "--- " *Name "left ---" and,
  **line 31** Exit the process with `(bye)`, this will automatically close all open file descriptors and the process
  will free all memory back to your OS.

**Line 32** wait for data to come in on *Sock, and then fire the appropriate **task** attached to it in *Run.

**We're done.**

## Conclusion

**So that brings us to an end of the source, hopefully every line of this code is now understood. The next task for me, is
to extend this little program.

For example, how about adding a private chat feature between any two parties or getting a list of current users.
Perhaps sending files to each other?

Who knows, the options are endless.

If you liked this 'study'. The please find me on the #picolisp channel on IRC under the name **vikid**.

I would love to hear from you.

Adios,**

![Sig](/assets/sig.jpg)
{.center}

#### Source of misc/chat:

```
#!/home/emperor/picoLisp/bin/picolisp /home/emperor/picoLisp/lib.l
# 13jun17abu

# *Port *Sock *Name

(de chat Lst
   (out *Sock
      (mapc prin Lst)
      (prinl) ) )

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
