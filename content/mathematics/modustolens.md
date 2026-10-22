---
title: Modus Tollens
date: '2016-11-30T23:43:22+04:00'
lastmod: '2021-08-24T01:37:03+04:00'
original_id: '{A555}'
original_name: modustolens
original_blob: blob/B/6/751.txt
revisions: 2
author: admin
last_editor: admin
tags:
- math
categories:
- math
wikislug: modustolens
draft: false
topics:
- foundations
---

# Logic - Modus Tollens

[Everything Else](misc.md) | [Logic](logic.md) | [Philosophy](philosophy.md) | [Logic](logic.md) | [Economics](economics.md) | [Politics](politics.md)
| [Ethics](ethics.md) | [Aesthetics](aesthetics.md "MISSING PAGE") | [Articles](articles.md)

- [Modus Ponens](modusponens.md)
- [Modus Tollens](modustolens.md)

Modus tollens is modus ponens's sharper sibling, and the logic behind every good experiment. The truth: **if a prediction fails, the idea that made it is in trouble.**

### The core idea, in plain words

If you know "if \(p\) then \(q\)" and you know \(q\) is false, you may conclude \(p\) is false.

$$ \frac{p \to q \qquad \neg q}{\therefore\ \neg p} $$

The Latin is *modus tollendo tollens*, "the mode that denies by denying". It is valid because \(p \to q\) is logically equivalent to its **contrapositive** \(\neg q \to \neg p\), and modus tollens is just [modus ponens](modusponens.md) applied to the contrapositive.

| \(p\) | \(q\) | \(p \to q\) | \(\neg q\) |
|---|---|---|---|
| T | T | T | F |
| T | F | F | T |
| F | T | T | F |
| F | F | T | T ← both premises true, \(p\) false |

### An everyday analogy

"If the dog had barked, the neighbour would have woken. The neighbour slept through. So the dog didn't bark." (Sherlock Holmes's "dog that did nothing in the night-time" is this very argument.)

### A small worked example

1. If \(n\) is divisible by 4, then \(n\) is even.
2. \(30\) is not divisible by 4… careful, that's the *antecedent*. Let's use \(n = 31\): \(31\) is **not even**.
3. ∴ \(31\) is not divisible by 4. ✔

Notice the trap I nearly walked into in step 2: knowing 30 isn't divisible by 4 tells you *nothing* about whether 30 is even. That's the next fallacy.

### The impostor: denying the antecedent

$$ \frac{p \to q \qquad \neg p}{\therefore\ \neg q} \quad \text{(INVALID)} $$

"If it's raining, the pavement is wet. It's not raining. So the pavement is dry." The car-washer strikes again. Numerically: "if divisible by 4 then even; 30 is not divisible by 4; so 30 is not even." False conclusion from true premises, so the form is invalid (row 3 of the table).

**The four forms at a glance**

| Form | Premises | Conclusion | Valid? |
|---|---|---|---|
| Modus ponens | \(p \to q\), \(p\) | \(q\) | ✔ |
| Modus tollens | \(p \to q\), \(\neg q\) | \(\neg p\) | ✔ |
| Affirming the consequent | \(p \to q\), \(q\) | \(p\) | ✘ |
| Denying the antecedent | \(p \to q\), \(\neg p\) | \(\neg q\) | ✘ |

### A picture in words

Draw \(p\) as a small circle inside a bigger circle \(q\) (everything that is \(p\) is \(q\)). If you are **outside** \(q\), you are certainly outside \(p\): modus tollens. If you're outside \(p\), you could still be in the ring of \(q\): that's why denying the antecedent fails.

```mermaid
graph LR
  NQ["not q"] -- "contrapositive: ¬q → ¬p" --> NP["so not p"]
```

### Common misconceptions

- **"The contrapositive and the converse are the same."** The contrapositive \(\neg q \to \neg p\) is equivalent to \(p \to q\). The converse \(q \to p\) and the inverse \(\neg p \to \neg q\) are not (they are equivalent to each other).
- **"A failed prediction disproves my *particular* hypothesis."** In practice \(p\) is a bundle of assumptions (theory + instruments + conditions). Modus tollens tells you *at least one* of them is false, not which one (the Duhem–Quine problem).
- **"Tollens is a proof by contradiction."** Close cousins, not identical, but every tollens step can be rewritten as one.

### How it connects

- [Modus Ponens](modusponens.md) is its twin; together they're the two valid ways to use a conditional.
- Karl Popper's falsificationism is modus tollens as a philosophy of science: theories can be refuted by failed predictions but never proven by successful ones (that would be affirming the consequent). See [Philosophy](philosophy.md) and [Logic](logic.md).

The truth revealed: you can't prove an idea by its successes, but a single honest failure can bring it down.

## Further Reading

- [Philosophers to Study](philosophers2study.md)
