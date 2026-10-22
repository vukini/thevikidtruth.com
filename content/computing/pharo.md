---
title: Pharo
date: '2016-05-15T23:53:46+04:00'
lastmod: '2017-07-17T04:35:16+04:00'
original_id: '{A27}'
original_name: pharo
original_blob: blob/B/6/145.txt
revisions: 35
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pharo
draft: false
topics:
- other-languages
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Pharo Smalltalk](pharo.md) | [Learning Online](learningonline.md) | [Learn Pharo with Vikid](learnpharo.md)

# Pharo

I am very new to SmallTalk and Pharo in particular. I like the **idea of image
based programming** and the have followed the works of
[Alan Kay](https://www.youtube.com/watch?v=oKg1hTOQXoY) and
[Dan Ingalls](https://www.youtube.com/watch?v=P2mh92d-T3Y)
for some time now (I very highly recommend it). Pharo looks to be quite a
capable system and it is calling my attention. I shall do what I can and post
my discoveries here.
**I think the [Pharo](http://pharo.org/) Zen is one of the most beautiful poems
about computing
philosopy. I hope that you like it, the emphasis is mine.**

![pharo-tall](/assets/pharo-tall.jpg)
{.right}
 
#### Pharo Zen

**Classes structure** our vocabulary. 

Quality is an **emerging** property. 

**Abstraction and composition** are our friends. 

Learning from mistakes. 

**Communication** is key. 

Better a set of small **polymorphic classes** than a large ugly one. 

**Explicit** is better than implicit. 

Fully dynamic and malleable. 

Easy to understand, easy to learn from, **easy to change.** 

**Simplicity** is the ultimate elegance. 

One step at a time. 

**Polymorphism is our esperanto.** 

Examples to learn from. 

A system with robust abstractions that a **single person** can understand. 

Magic only at the right place. 

**Objects** all the way down. 

Beauty in the code, beauty in the comments. 

Perfection can kill movement. 

Simple processes to support progress. 

Tests are important but can be changed. 

There is **no unimportant fix.** 

**Messages** are our vocabulary. 

###### Typical Pharo Window

Viewing a Collection Class.

![03-system-browser](/assets/03-system-browser.png)
{.center}

## [Learn Pharo with Vikid](learnpharo.md)

## Learning Pharo and other Links

- There is a great free course out there [MOOC](http://files.pharo.org/mooc/), I would start here.
- [fun-mooc, is a french site, but the pharo course is in english too.](https://www.fun-mooc.fr)
- [Pharo Cloud](https://www.pharocloud.com/)
- [Pharo Association](https://association.pharo.org/)
- [Pharo Documentation](http://pharo.org/documentation)
- [Pharo Books](http://files.pharo.org/books/)
- [Pharo Mooc](http://files.pharo.org/mooc/)
- [Pharo Cheatsheet PDF](http://files.pharo.org/media/pharoCheatSheet.pdf)
- [Pharo Tech Talks @ YouTube](https://www.youtube.com/playlist?list=PL4actYd6bfnx8l8cqYWhdNB6gJgRvk5sH)
- [Pharo Slide Share @ slideshare.net](https://www.slideshare.net/pharoproject)

### The plain idea

Pharo is a modern descendant of **Smalltalk**, one of the most influential programming languages ever made, the language where object-oriented programming, the graphical IDE and much of the modern GUI were first worked out, largely by Alan Kay's team at Xerox PARC in the 1970s. Pharo's defining feature is that it is **image-based**: you do not edit text files and then run them. Instead you work *inside* a live, running world (the "image") where every object, including your code, the tools, and the running programs, exists at once and can be inspected and changed on the spot. You save the whole live world to disk and reopen it exactly as you left it.

### Why it matters

Most languages separate the dead text of your program from the living process that runs it. Smalltalk erases that line: the system is always on, and you sculpt it while it runs. This makes for an unmatched feeling of immediacy, click on any object, see its state, send it a message, change its class, all without stopping. Even if you never ship Pharo in production, spending time in it changes how you think about objects, messages and interactive development. It is the clearest surviving window onto Kay's original vision of computing.

### An everyday analogy

Ordinary programming is like writing a recipe, then cooking it from scratch each time to see if it works. Pharo is like standing in a kitchen where the meal is always cooking: you can taste it, add salt, swap an ingredient, and watch the dish change *right now*, then freeze the entire kitchen, stove, pots and all, to resume later exactly as it was.

### A worked example: everything is a message

In Smalltalk there are no operators or control keywords, only *objects* receiving *messages*. Even `3 + 4` is the object `3` being sent the message `+` with argument `4`:

```smalltalk
3 + 4.                         "sends + to 3, answers 7"
'hello' asUppercase.           "sends asUppercase to a string -> 'HELLO'"
1 to: 5 do: [ :i | Transcript showln: i ].   "a loop, built from messages"
```

That last line is not special syntax: `to:do:` is just a message sent to the number `1`, taking a block of code `[ ... ]` as an argument. The whole language is this one idea, objects sending messages, applied relentlessly, which is exactly what the "Objects all the way down" line in the Pharo Zen celebrates.

### A 2026 note

Pharo is actively developed and healthy, with regular releases (Pharo 12 and 13 are recent) and a lively community. It remains free and open-source, runs on Linux, macOS and Windows, and the excellent book *Pharo by Example* is free online. The Zen above still captures its spirit perfectly.

### Common misconceptions

- **"Smalltalk is dead."** The commercial giants faded, but Pharo (and Squeak, and Cuis) keep the ideas alive and modern.
- **"Image-based means you lose your code."** Code can be exported and version-controlled (Pharo integrates with Git via Iceberg); the image is a convenience, not a prison.
- **"It's just another OOP language."** It is arguably *the* OOP language; most others borrowed from it and kept only part.

### How it connects

- [Learn Pharo with Vikid](learnpharo.md) and [Objects and Messages](objectsandmessagespharo.md): my beginner notes.
- [Cuis Smalltalk](cuissmalltalk.md): a smaller cousin.
- [Lisp](commonlisp.md): the other great "live, malleable system" tradition.

The truth revealed: Pharo is less a language than a living world you program from the inside, and the "Objects all the way down" poem above is not marketing, it is literally how the system is built.
