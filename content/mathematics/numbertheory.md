---
title: Number Theory
date: '2016-12-07T06:42:39+04:00'
lastmod: '2016-12-08T11:18:32+04:00'
original_id: '{A725}'
original_name: numbertheory
original_blob: blob/B/5/062.txt
revisions: 7
author: admin
last_editor: admin
tags:
- math
categories:
- math
wikislug: numbertheory
draft: false
---

[Math](math.md)

![math-800](/assets/math-800.jpg)
{.center}

# Number Theory

I find Number theory one of the very hardest parts of Mathematics so this is probably the most contrived part of this
wiki. You will find a struggle here but hopefully if you are having a hard time yourself, there maybe some value to you
here below.

My fascination with Mathematics really started with **numbers**. No matter how hard I tried, I couldn't really figure out
what they were ([Ontologically](ontology.md "MISSING PAGE")). Did they have a basis in reality and if not, what basis did they have and
moreover, why did **Reality** and **Math** track so well if they didn't have a basis in reality.

### The plain idea

Number theory is the study of the **whole numbers**, \(1, 2, 3, \dots\), and especially of how they break into pieces by multiplication. Its atoms are the **primes**: numbers greater than 1 whose only divisors are 1 and themselves, \(2, 3, 5, 7, 11, 13, \dots\).

The questions are so simple a child can ask them and so hard that some have stood unanswered for centuries. Is every even number bigger than 2 the sum of two primes? (Goldbach, 1742: still open.) Are there infinitely many pairs of primes two apart, like 11 and 13? (Still open, though since Yitang Zhang's 2013 breakthrough we know there are infinitely many pairs within 246 of each other.) Gauss called number theory "the queen of mathematics", and this mix of innocence and difficulty is why.

### Why it matters

For two thousand years number theory was the purest of pure mathematics, admired precisely because it was useless. Then, in the 1970s, it became the lock on the world's front door. RSA encryption and its descendants rest on one fact: **multiplying two big primes is easy, but splitting the product back into them is (as far as anyone knows) extremely hard.** Every time you see a padlock in your browser, number theory is working.

And it is still moving. Because a large quantum computer could break RSA and elliptic-curve cryptography using Shor's algorithm, NIST published its first post-quantum cryptography standards in 2024 (lattice-based schemes such as ML-KEM). The old question "what are numbers?" turns out to have a very practical edge.

### An everyday analogy: Lego bricks

Every whole number bigger than 1 can be built by multiplying primes, and, crucially, in **only one way** (apart from the order). This is the **Fundamental Theorem of Arithmetic**. Primes are the Lego bricks; every number is a model built from them; and every model has a unique parts list.

$$ 360 = 2^3 \times 3^2 \times 5 $$

No other set of primes multiplies to 360. That uniqueness is what makes primes the right atoms.

### A worked example: why there are infinitely many primes

Euclid's proof, about 300 BC, still the most elegant argument in mathematics:

1. Suppose there were only finitely many primes, \(p_1, p_2, \dots, p_k\).
2. Build \(N = p_1 p_2 \cdots p_k + 1\).
3. Divide \(N\) by any \(p_i\): the remainder is always \(1\). So no prime on the list divides \(N\).
4. But \(N > 1\), so it has *some* prime factor, and that prime is not on the list. Contradiction.

Try it: \(2 \times 3 \times 5 \times 7 + 1 = 211\), which is prime. \(2 \times 3 \times 5 \times 7 \times 11 \times 13 + 1 = 30031 = 59 \times 509\), not prime, but its factors 59 and 509 are new primes. Either way, the list was incomplete.

### Clock arithmetic

Much of modern number theory happens "on a clock": **modular arithmetic**, where we keep only remainders. On a 12-hour clock, \(9 + 5 = 2\). We write \(14 \equiv 2 \pmod{12}\). This is exactly the cyclic [group](groups.md) \(\mathbb{Z}_n\), which is where number theory and abstract algebra shake hands. Fermat's little theorem says that for a prime \(p\) and any \(a\) not divisible by \(p\),

$$ a^{p-1} \equiv 1 \pmod{p} $$

Check: \(3^4 = 81 = 16 \times 5 + 1\), so \(3^4 \equiv 1 \pmod 5\). ✔ This little fact is the engine inside RSA.

### On my question: what *are* numbers?

As for the [ontological](ontology.md) puzzle above, there are three main answers on the table. **Platonists** say numbers exist independently and we discover them. **Formalists** say mathematics is a game with symbols and rules. **Structuralists** say a number is just a position in a pattern: "3" means "the thing after 2 and before 4" and nothing more. In [Set Theory](settheory.md), the von Neumann construction makes this concrete: \(0 = \{\}\), \(1 = \{0\}\), \(2 = \{0, 1\}\), and so on. Why such constructions fit the physical world so well is what Eugene Wigner called "the unreasonable effectiveness of mathematics". Nobody has settled it. You are in good company.

### Common misconceptions

- **"1 is prime."** It isn't, by convention, precisely so that factorisation stays unique.
- **"Primes thin out and eventually stop."** They thin out (near \(n\) about one number in \(\ln n\) is prime, the Prime Number Theorem) but never stop.
- **"Big primes are hard to find."** Testing whether a number is prime is fast; it is *factoring* that is hard.
- **"Number theory is finished."** The Riemann Hypothesis, about the exact distribution of primes, is one of the million-dollar Millennium Prize Problems.

### How it connects

- [Groups](groups.md) and [Rings](rings.md): the integers mod \(n\) are the textbook examples.
- [Fields](fields.md): when \(p\) is prime, arithmetic mod \(p\) is a field, the setting for most cryptography.
- [Abstract Algebra](abstractalgebra.md) and [Set Theory](settheory.md) for the foundations.

The truth revealed: the simplest objects in mathematics are also the most mysterious, and the mystery is guarding your bank account.

### The number systems

- [Natural Numbers](naturalnumbers.md "MISSING PAGE")
  [Rational Numbers](rationalnumbers.md "MISSING PAGE")
  [Real Numbers](realnumbers.md "MISSING PAGE")
  [Complex Numbers](complexnumbers.md "MISSING PAGE")
  [Quarternions](quaternions.md "MISSING PAGE")
  [Constructive Reals](constructivereals.md "MISSING PAGE")
  [Hyper Reals](hyperreals.md "MISSING PAGE")
  [Surreals](surreals.md "MISSING PAGE")
  [Binary Theory](binary.md)
  [Binary Coded Decimal](bcd.md "MISSING PAGE")
  [Signed & Unsigned Representations](signednumbers.md "MISSING PAGE")
  [One's Complement](onescomplement.md "MISSING PAGE")
  [Two's Complement](twoscomplement.md "MISSING PAGE")
  <!-- 
  -{={}}
  -{={}}
  -{={}}
  -{={}}
  -{={}}
  -{={}}
  -{={}}
  -{={}}
  -{={}}
  -{={}}
   -->
