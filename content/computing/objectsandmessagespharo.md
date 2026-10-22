---
title: Objects and Messages
date: '2016-12-04T02:27:20+04:00'
lastmod: '2016-12-04T02:29:59+04:00'
original_id: '{A635}'
original_name: objectsandmessagespharo
original_blob: blob/B/4/044.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: objectsandmessagespharo
draft: false
topics:
- other-languages
---

[Computing](computing.md) |
 [BCIYH](bciyh.md) |
 [Pharo Smalltalk](pharo.md) | [Learning Online](learningonline.md) |
 [Learn Pharo with Vikid](learnpharo.md) |

# Objects and Messages

I am a beginner at programming SmallTalk & Pharo in particular. The notes/lesson here are my attempt at learning the
language and taking notes on what I have learnt in as clear a way that I can. Hopefully as a beginner you can benefit from
this approach yourself.

- [Object and Messages](objectsandmessagespharo.md)

### The plain idea

The single most important thing to understand about [Pharo](pharo.md) and Smalltalk is this: **everything is an object, and you make things happen by sending messages to objects.** There are no operators, no built-in control keywords, no special syntax hiding in the corners. `3 + 4` is the object `3` receiving the message `+` with the argument `4`. A loop, a conditional, printing to the screen, all of it is just objects being sent messages. Learn that one idea deeply and the whole language opens up.

### Why it matters

Most languages bolt objects onto an older, procedural core, so you get objects *plus* a pile of exceptions (operators, keywords, primitive types that are not really objects). Smalltalk has no exceptions: the uniformity is the point. Once "send a message to an object" is the *only* rule, the language becomes astonishingly small and consistent, and the skill transfers everywhere, because this is the model most modern OOP languages imitate.

### The three kinds of message

Smalltalk has exactly three message forms, and knowing them is most of the syntax:

```smalltalk
5 factorial.          "unary: just a name, sent to one object -> 120"
3 + 4.                "binary: a symbol with one argument -> 7"
2 raisedTo: 10.       "keyword: named argument(s) -> 1024"
array at: 1 put: 99.  "keyword with two arguments"
```

- **Unary** messages (like `factorial`) take no argument and bind tightest.
- **Binary** messages (like `+`) take one argument and come next.
- **Keyword** messages (like `at:put:`) have named parts ending in colons and bind loosest.

So `2 raisedTo: 3 + 1` means "3 + 1 first (binary beats keyword), then raisedTo:", giving `2 raisedTo: 4` = 16. That precedence, unary, then binary, then keyword, is the one rule you must memorise.

### An everyday analogy

Think of objects as people and messages as polite requests. You do not reach into someone's head and change it; you *ask* them something, and they decide how to answer. `account deposit: 50` is not "set the balance"; it is "please deposit 50", and the account object itself decides what that means. That politeness, objects in charge of their own behaviour, is the heart of good object design.

### Common misconceptions

- **"`+` is an operator."** In Smalltalk it is a binary *message*; numbers decide what `+` does, which is why you can define `+` on your own classes.
- **"There must be `if`/`while` keywords somewhere."** No: `condition ifTrue: [...]` and `[...] whileTrue: [...]` are ordinary messages sent to booleans and blocks.

### How it connects

- [Pharo](pharo.md): the live environment where you send these messages.
- [Learn Pharo with Vikid](learnpharo.md): the rest of my beginner notes.

The truth revealed: once you see that there are no operators and no keywords, only objects answering messages, Smalltalk stops looking strange and starts looking like the simplest idea in programming, taken all the way to its conclusion.
