---
title: Knowledge Representation
date: '2016-12-05T22:37:42+04:00'
lastmod: '2016-12-05T22:43:39+04:00'
original_id: '{A711}'
original_name: krep
original_blob: blob/B/4/410.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: krep
draft: false
topics:
- cs-theory
---

# Knowledge Representation

It is a really important question that at first doesnt look like it even needs questioning,

**How do we record, store & retrieve our thoughts & memories?**

## Source & Links

- Learn more about [knowledge representation click on this link](http://www.lisperati.com/tellstuff/) by Conrad Barski

### The plain idea

Knowledge representation (KR) is the study of how to put what we *know* into a form a computer (or a mind) can store, connect and reason over. It is not about storing raw data, a pile of facts, but about capturing *meaning*: that a dog is a kind of animal, that Paris is the capital of France, that "if it rains the match is cancelled". The hard part, as my opening question says, is that it seems obvious until you try to make it precise.

### Why it matters

Everything that "understands" rather than merely stores depends on KR: search engines that answer questions, the knowledge graphs behind digital assistants, medical expert systems, and the structured memory that even modern AI reaches for when it must be accurate. Choose the wrong representation and simple questions become impossible; choose a good one and reasoning almost falls out for free. It is also, quietly, a theory of how *we* organise thought.

### An everyday analogy: a library versus a pile of books

A heap of books contains all the knowledge but answers no questions. A library *represents* that same knowledge, by subject, author, cross-reference, so you can find "everything on Roman history" in minutes. KR is designing that cataloguing scheme for a computer: the shelves, labels and links that turn facts into something you can navigate and reason about.

### A worked example: ways to say the same thing

Suppose we know "Socrates is a man, and all men are mortal." Different representations capture it differently:

- **Logic:** `Man(Socrates)` and `∀x (Man(x) → Mortal(x))`, from which a reasoner *derives* `Mortal(Socrates)`.
- **Semantic network / graph:** nodes `Socrates` -> `is-a` -> `Man` -> `is-a` -> `Mortal`, following the links to the same conclusion.
- **Frames / objects:** a `Man` frame with a slot `mortal: true`, inherited by the `Socrates` instance.
- **Triples (RDF):** `(Socrates, type, Man)`, the form behind the Semantic Web and today's knowledge graphs.

The facts are identical; what differs is what each form makes *easy*, and that choice is the whole craft.

### A 2026 update

KR has had a renaissance. The web runs on triples and ontologies (RDF, OWL, schema.org); Google, Wikidata and most big AI systems maintain vast **knowledge graphs**. And large language models have revived the old debate: they hold knowledge implicitly in billions of weights, which is powerful but hard to inspect or guarantee, so systems increasingly *combine* them with explicit, checkable knowledge bases (retrieval-augmented generation). The century-old questions, how to represent meaning, handle exceptions, and reason reliably, are suddenly current again.

### Common misconceptions

- **"A database is knowledge representation."** A database stores facts; KR adds the structure and rules that let you *infer* new facts.
- **"More detail is always better."** Over-specified representations become brittle and slow; good KR captures just what reasoning needs.
- **"LLMs made KR obsolete."** They made it more relevant: their weakness is exactly the reliable, explainable knowledge that explicit representations provide.

### How it connects

- [Machine Learning](machinelearning.md): the statistical counterpart to symbolic KR.
- [Databases](databases.md): where facts are stored before they are structured.
- [Lisp](commonlisp.md): the traditional language of symbolic AI (the linked tutorial is in Lisp).
- [Algorithms](algorithms.md): the reasoning procedures that run over representations.

The truth revealed: the deepest trick in making a machine seem to think is not the thinking at all, it is finding the right way to write down what it knows.
