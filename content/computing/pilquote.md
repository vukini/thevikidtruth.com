---
title: quote
date: '2017-06-24T08:08:02+04:00'
lastmod: '2017-06-25T03:55:35+04:00'
original_id: '{A1152}'
original_name: pilquote
original_blob: blob/B/6/033.txt
revisions: 53
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pilquote
draft: false
topics:
- lisp
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
  [Picolisp By Example](picolispbyexample.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md) | [Networking](networking.md) | [Machine Learning](machinelearning.md) |
  [Git](git.md) |
  [Machine Learning](machinelearning.md) |
  [Algorithms](algorithms.md) |
  [Open Data Science](opendatascience.md) |

# [quote](pilquote.md)

> **Reading this in 2026.** These are my study notes from around 2017, when the 32-bit C (pil32) and 64-bit assembly (pil64) implementations were current. Since 2020 PicoLisp is **pil21**, written in PicoLisp itself and compiled through LLVM; the language, libraries and examples are largely the same, so the ideas here still apply, but file names and internals differ. See [Pil Sources](pilsource.md) and [software-lab.de](https://software-lab.de/down.html).

This article is under construction. There will be plenty of errors so please keep it in mind.

![quote](/assets/quote.png)
{.left}

Quote is probably the most used character/function/macro in lisp. It is central to getting almost anything done.
A good place to start is
[https://picolisp.com/wiki/?ArticleQuote](https://picolisp.com/wiki/?ArticleQuote). This article does a pretty good job of explaining things and part of the
official picolisp pages. If you want my take on things (it's literally a tour of lisp itself) please read on!

**Picolisp defines `quote` to return all arguments, without evaluating them.**

The question is why you would want to do that and what purpose it serves.

Before we get into `quote` I really feel it is good to recap on the **programming model** used in most lisps. What exactly
is going on and why does it work the way it does?

Quote just happens to be so fundamental we might as well start at the beginning.

## In the beginning...

 
![army](/assets/army.jpg)
{.right}

Humans got inundated with information and the need to transform the information into more and more useful abstractions.

**Ancients Kings and Priests need to ask questions like:**

- How much land does that peasant have and how much tax does he owe me?
- How many warriors do I have and of which kind?
- How much grain do we have in storage?
- How many subjects do we have to rule over?
- What does the holy book say about dealing with crime?
- etc.. etc...

**As we got more and more advanced our questions and abstraction got more and more complicated, yet, in some fundamental way
remained the same. Question like:**

- How much fuel do I need to fly to Vancouver with half passengers on board?
- What is the value of my stocks?
- How much do I need to budget for National Child Care Benefits
- How do I draw a polygon on to the screen of my computer
- What are the names of all the employees in the company
- etc.. etc..

**What essentially remained the same is this:**

1. We have some physical or conceptual system
1. We want to measure & record it in some unified / standard way.
1. Those collected measurements are called **data**
1. We need to need to **transform the data** into something useful
1. while we are at it, we might as well give the data and transformations easy to remember names, so that we can easily
  **refer** to them.

**Lisp** is just one of methodologies that allows us to do this is a very simple and uniform manner and it goes like this:

- All **data** is kept as lists (except for a few primitive types)
- All **transformations** are kept as lists (except a few primitives), transformations are also called **code**
- **References are names** (also called **symbols**) to either lists or primitive types

## Primitives

Lets deal with the **primitives first**. We need them to be the **'bottom'** of the system. Somewhat like Lego blocks. You
use Lego blocks to build what you want, however, you don't build the blocks themselves. No these usually come from the
factory.

 
![lego](/assets/lego.jpg)
{.center}

A curious thing about Lego blocks are that they are so simple that even a little child can conceive of their
purpose, their structure and use, yet it would be very difficult to make them. You need a state of the art factory, distribution
systems, staff, labour, etc... to make these blocks successfully.

The picolisp environment is something like this factory. Out of the box, comes some pretty sophisticated primitives, easy to
understand and use, but not so easy to code from scratch. Neither should you want to for general use.

So we have primitives like, **small numbers, big numbers, symbols, cons pairs, lists, functions, etc...**
that act as a sort of **'bottom'**
to the system.

And using them is as simple as typing them out. Please try this for best pedagogic effect.

```
: 1
```

is simaccording to these three rulesply the number 1 (you should see -> 1) **this means the system got and return a 1**,

```
: "Hello Dear Friend"
```

is just a symbol *(that behaves like a string)*. Your should get it back.

```
: Hello
```

ah, something new happens, you get **NIL**. So now try this,

```
: 'Hello
```

and you should get a **Hello** back. Why? we shall explore a little later I promise.

## (Lists Data Code)

Like Lego, a single block, while being something of interest to look and perhaps study is not very useful by itself. The
magic only happens when we start connecting them up to build something of value.

In **picolisp we do this with lists**.

A list is simply something like a string of beads. Where each bead is a primitive.

![beads](/assets/beads.jpg)
{.center}
 

Which doesn't sound so much more useful a single block until your think of **DNA**, which is also not so dissimilar to
a string of beads. **And look at what has been created with DNA!**

![dna](/assets/dna.jpg)
{.center}
 

In picolisp we simply write out lists between **Brackets with a space between each item in the list**. Such as:

- `(a 1 b 2 c 3 d 4)`
- `("john" "fred" "simon")`
- `(+ 4 4)`
- `( (a 1) (b 2) (c 3) )`

However if you type this into your picolisp REPL, you probably won't get the results you are expecting. For that you
need to **quote**. Just why, will be explained later in the article.

**But what is data and what is code?**

**The most important insight is the fact that what is data and what is code is mostly a matter of perspective.**

Take for example a recipe to bake a cake.

```

```

**Vanilla Cake** 
![cake](/assets/cake-2.jpg)
{.right}

**INGREDIENTS**

175g margarine,
175g sugar,
3 eggs,
175g self-raising flour, sifted
1tsp baking powder
1tsp vanilla extract
pinch of salt

**METHOD**

Heat the oven to 180°C. Lightly grease an 18cm round cake tin with a margarine and cut a piece of greaseproof paper or non-stick baking parchment to fit the base of the tin.
Put all the ingredients in a large mixing bowl and beat with a wooden spoon or a hand-held mixer for 1 minute, or until just combined. It's important not to beat the batter too much - just long enough to make it smooth.
Pour or spoon the mixture into the tin, smooth the top and bake on the middle shelf of the oven for about 45-50 minutes. The cake is cooked when it looks well risen and golden; the top should spring back when lightly touched with a fingertip. Another test is to insert a skewer into the centre of the cake - it should come out clean.
Let the cake sit in the tin for 5 minutes, then gently run a knife around the edge and turn the cake out onto a wire rack to cool. Serve dusted with icing sugar.

```

```

**Is it code or is it data?**

Mostly it is matter of perspective, it is clearly data, your reading it. Currently saved on a file, served to you
over the internet.
Yet, if you were in your kitchen with the
ingredients, ready to bake a cake, it would be code (that is the **instructions to transform ingredients into a cake**).

It is the same in picolisp. At times we might want to process a list as code. At other times we might just want
read it or store it as data, to be used somewhere else at a later time.

That's what `quote` does. It lets you choose what is data and what is code.

## Read, Evaluate, Print, Loop

1. Just like your brain right now which is this sentence. Picolisp must read each statement that you load/type into
  it. This is called **'Reading'**
1. and once it has done reading, just like you, it must **'Evaluate'** what it has read. What is vikid saying, what does he mean
1. And to be any use to you, it must report back its finding. This is called **'Print'ing**.
  As it usually prints it back to the screen. You do this automatically,
  usually by talking to your self in your head.
  then finally, why stop there? Just like you, it will read the next sentence, and the next, till it is told to exit.
  That is called **'Loop'ing**

**This is what Wikipedia says about it:**

```

```

In a REPL, the user enters one or more expressions (rather than an entire compilation unit) and the REPL evaluates them and displays the results. The name read–eval–print loop comes from the names of the Lisp primitive functions which implement this functionality:

- The read function accepts an expression from the user, and parses it into a data structure in memory. For instance, the user may enter the s-expression (+ 1 2 3), which is parsed into a linked list containing four data elements.
- The eval function takes this internal data structure and evaluates it. In Lisp, evaluating an s-expression beginning with the name of a function means calling that function on the arguments that make up the rest of the expression. So the function + is called on the arguments 1 2 3, yielding the result 6.
- The print function takes the result yielded by eval, and prints it out to the user. If it is a complex expression, it may be pretty-printed to make it easier to understand. In this example, though, the number 6 does not need much formatting to print.

```

```

However there is a problem here in that **everything 'read' is 'evaluated'** and very often,
you just don't want to do that. We wouldn't want to bake a cake every time we read the recipe would we? :-)

Sometimes you want to read a recipe so that you can decide what you need to buy at the shops in preparation.
Sometimes you want to ready a recipe in order to get ideas to write new recipes, for example to make chocolate cake.

### Evaluation

PicoLisp tries to evaluate everything entered into the REPL
Basically, it does so by applying the following three rules:

1. A number evaluates to itself.
1. A symbol evaluates to its value
1. A list is evaluated as a function call
    - the first element of the list is considered as the function
    - the rest of the elements are considered data to the function
    - This data is in turn evaluated using the same 3 rules
1. [reference](https://software-lab.de/doc/ref.html)
