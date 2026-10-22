---
title: VikiD Logic
date: '2016-11-30T23:36:06+04:00'
lastmod: '2021-08-24T01:59:48+04:00'
original_id: '{A553}'
original_name: logic
original_blob: blob/B/6/753.txt
revisions: 9
author: admin
last_editor: admin
tags:
- math
categories:
- math
wikislug: logic
draft: false
topics:
- foundations
---

[Everything Else](misc.md) | [Philosophy](philosophy.md) | [Logic](logic.md) | [Economics](economics.md) | [Politics](politics.md)
| [Ethics](ethics.md) | [Aesthetics](aesthetics.md "MISSING PAGE") | [Articles](articles.md)

# VikiD Logic

` Logic is the study of abstract, hypothetical connections, involving necessity.`

These connections are between **'Statements'**, **'Propositions'**, or **'Assertions'**.

Classified into two groups, **valid** vs **invalid**.

[Modus Ponens](modusponens.md) is the very most basic type of connection. It says,

```
if  A => B
    A
   ---
  ∴ B
```

that is, if A implies B, and we "assert" A is "valid", then we can conclude B is also "valid".

This is a pattern of thought that we consider "true" or "valid" axiomatically. We define it as such.
It cannot be derived from logic itself.

### The plain idea

Logic is the study of **what follows from what**. Not whether a statement is true, but whether, *if* certain statements are true, another one *must* be. That "must" is the necessity in the definition above. Logic is the rulebook for that "must".

So an argument has two separate qualities, and confusing them is the root of most bad reasoning:

- **Validity** is about the shape: if the premises were true, could the conclusion still be false? If not, the argument is valid.
- **Soundness** is validity *plus* actually true premises.

"All fish can fly; a salmon is a fish; so a salmon can fly" is perfectly **valid** and completely **unsound**. Logic certifies the pipe, not the water you pour into it.

### Why it matters

Logic is the skeleton of mathematics, the grammar of computer chips and the immune system of a good mind. Every proof is a chain of valid steps. Every `if` statement in a program and every logic gate in a processor is propositional logic made physical. And every time someone tries to sell you a conclusion, logic lets you ask the only question that matters: *does that actually follow?*

### An everyday analogy: a recipe that cannot fail

Think of a valid argument as a recipe guaranteed to work *if* the ingredients are good. Logic checks the recipe. It cannot check whether your eggs are rotten. Garbage in, garbage out; but with a valid recipe, truth in, truth out.

### The building blocks

Propositional logic glues statements together with a handful of connectives:

| Symbol | Read as | True when |
|---|---|---|
| \(\neg A\) | not A | A is false |
| \(A \land B\) | A and B | both are true |
| \(A \lor B\) | A or B | at least one is true |
| \(A \Rightarrow B\) | if A then B | except when A is true and B is false |
| \(A \Leftrightarrow B\) | A if and only if B | both have the same truth value |

The odd one is the conditional. "If it rains, the street is wet" is only *broken* by rain on a dry street. When it isn't raining, the promise hasn't been tested, so logic counts it as kept. This feels strange at first, and it is the source of endless confusion.

### A worked example: checking validity with a truth table

Is this argument valid? *If A then B. B. Therefore A.*

| A | B | \(A \Rightarrow B\) | B | conclusion A |
|---|---|---|---|---|
| T | T | T | T | T |
| T | F | F | F | T |
| F | T | **T** | **T** | **F** |
| F | F | T | F | F |

Look at row three: both premises true, conclusion false. So the argument is **invalid**. It is the famous fallacy of *affirming the consequent*. "If he's a burglar he'd have a crowbar; he has a crowbar; so he's a burglar." Maybe he's a builder.

Do the same for modus ponens (*if A then B; A; therefore B*) and you will find no such row. That is what "valid" means: no possible world where the premises hold and the conclusion fails.

### Beyond the basics

- **Predicate logic** adds quantifiers, "for all" \(\forall\) and "there exists" \(\exists\), so we can say things like \(\forall x\,(x \in A \Rightarrow x \in B)\). This is the language the [ZF Axioms](zf.md) are written in.
- **Gödel's incompleteness theorems** (1931) showed that any consistent formal system strong enough to do basic arithmetic contains true statements it cannot prove. Logic discovered its own limits.
- **Non-classical logics** drop or change rules. Intuitionistic logic rejects "A or not A" as a free gift and demands a construction; it is the logic behind proof assistants like Lean and Coq (now Rocq), which mathematicians increasingly use to check proofs by computer.

### Logic in silicon

In 1937 a 21-year-old Claude Shannon noticed that George Boole's algebra of true and false describes electrical switching circuits exactly. Put two switches in series and current flows only if both are closed: that is \(A \land B\). Put them in parallel and current flows if either is closed: \(A \lor B\). Every processor since is built from this observation, billions of tiny AND, OR and NOT gates evaluating propositions billions of times a second. When people say computers "only understand ones and zeros", what they really mean is that computers only understand logic.

### Common misconceptions

- **"Logical means true."** A valid argument from false premises can reach any conclusion you like.
- **"Correlation implies causation."** Not a logical rule at all, just a tempting shortcut.
- **"If A then B" means "if B then A."** That swap is the converse, and it is exactly the fallacy above.
- **"Logic is cold and opposed to intuition."** Most good proofs start as intuitions; logic is how you find out which ones survive.

### How it connects

- [Modus Ponens](modusponens.md) and [Modus Tollens](modustolens.md): the two most basic valid patterns.
- [Set Theory](settheory.md): "and", "or" and "not" are intersection, union and complement in disguise.
- [Set Relations](setrelations.md) and the [ZF Axioms](zf.md): written entirely in predicate logic.
- [Philosophy](philosophy.md): logic began there, with Aristotle's syllogisms.

The truth revealed: logic doesn't tell you what is true. It tells you what you are committed to once you've said what you believe.

- [Modus Ponens](modusponens.md)
- [Modus Tollens](modustolens.md)

## Further Reading

- [Philosophers to Study](philosophers2study.md)
