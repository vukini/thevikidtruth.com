---
title: Quantum Mechanics
date: '2016-08-01T23:49:10+04:00'
lastmod: '2016-08-01T23:49:10+04:00'
original_id: '{A244}'
original_name: qm
original_blob: blob/B/1/063.txt
revisions: 1
author: admin
last_editor: admin
tags:
- math
categories:
- math
wikislug: qm
draft: false
topics:
- math-physics
---

# Quantum Mechanics

Here's the truth that the mystique around quantum mechanics hides: **underneath the weirdness, quantum mechanics is linear algebra on complex vectors, plus one strange rule about what happens when you look.**

The core idea, in plain words: the state of a system is a vector. Change over time is a linear operator. Measurement turns amplitudes into probabilities. Almost everything below is one of those three sentences in action, and the pages on [Vector Spaces](vectorspaces.md), [Linear Operators and Matrices](linearoperators.md), [Inner Product Spaces](innerproductspaces.md) and [Tensors](tensors.md) are the toolkit.

The road map, section by section:


#### Superposition Principle

If a system can be in state \(|0\rangle\) and can be in state \(|1\rangle\), it can also be in any combination

$$ |\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1, $$

with complex numbers \(\alpha, \beta\) called **amplitudes**. That's just vector addition. The everyday analogy is a musical chord: a guitar string can vibrate in its fundamental and its overtone at the same time, and the sound is the sum. The misconception to drop at once is "the particle is secretly in one state and we don't know which." A superposition is a genuinely different state, and it can interfere with itself, which a coin we haven't looked at never does.

#### Quantum States as Vectors

States live in a complex [inner product space](innerproductspaces.md) called a Hilbert space. Picture-in-words: imagine an arrow of length 1 that can point in any direction of that space. Multiplying the whole arrow by a phase \(e^{i\theta}\) changes nothing physical, so really a state is a *direction*, not an arrow. A single electron spin needs just two complex dimensions; a particle moving along a line needs infinitely many.

#### Bases and Operations

A measurable quantity (an **observable**) is a self-adjoint [linear operator](linearoperators.md). Its eigenvectors form a perpendicular basis, and its eigenvalues are the only possible measurement results. Each experiment picks a basis to ask questions in. 

**Worked example.** Take \(|\psi\rangle = \tfrac{3}{5}|0\rangle + \tfrac{4}{5}i\,|1\rangle\). Check normalisation: \(\tfrac{9}{25} + \tfrac{16}{25} = 1\). ✔ Measure in the \(\{|0\rangle, |1\rangle\}\) basis and the **Born rule** gives

$$ P(0) = |\langle 0|\psi\rangle|^2 = \tfrac{9}{25} = 0.36, \qquad P(1) = \left|\tfrac{4}{5}i\right|^2 = 0.64. $$

Now measure in the basis \(|\pm\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle \pm |1\rangle)\):

$$ \langle + |\psi\rangle = \tfrac{1}{\sqrt{2}}\left(\tfrac{3}{5} + \tfrac{4}{5}i\right), \qquad P(+) = \tfrac{1}{2}\left(\tfrac{9}{25} + \tfrac{16}{25}\right) = \tfrac{1}{2}. $$

The same state gives completely different odds depending on which question you ask. That's the whole game.

#### Complementary Principle

Bohr's principle: some pairs of properties can't both be sharp at once, because their operators don't share an eigenbasis. If \(A\) and \(B\) **don't commute**, \(AB \neq BA\), then no state is an eigenvector of both. This is the non-commutative [ring](rings.md) of matrices showing up in nature, and it's why quantum mechanics feels so unlike the [commutative](commutativerings.md) world of everyday numbers.

#### Position and Momentum

The most famous non-commuting pair:

$$ \hat{x}\hat{p} - \hat{p}\hat{x} = i\hbar, $$

and from it the uncertainty principle \(\Delta x\,\Delta p \geq \tfrac{\hbar}{2}\). A common misconception is that uncertainty comes from clumsy measurement disturbing the particle. It's deeper: a wave sharply localised in space is necessarily a mixture of many wavelengths, i.e. many momenta. A short click of sound contains every pitch; a pure tone lasts forever.

#### Energy and Quantum Dynamics

Between measurements, states evolve smoothly and *linearly*, driven by the energy operator, the Hamiltonian \(\hat{H}\):

$$ i\hbar\,\frac{d}{dt}|\psi(t)\rangle = \hat{H}\,|\psi(t)\rangle. $$

Energy eigenstates just spin their phase at a rate set by their energy; everything else is a superposition of such spinning pieces, and the beats between them are what we see as motion.

1. [Schrodinger's Equation](schrodingerequation.md "MISSING PAGE")

#### Angular Momentum and Spin

Rotations form a [group](groups.md), and quantum states must carry a representation of it, a [group action](group.md) on the state space. That forces angular momentum to come in whole or half-whole units of \(\hbar\). Spin-\(\tfrac{1}{2}\) particles like electrons have the odd property that a 360° rotation multiplies their state by \(-1\); it takes 720° to get back to start.

#### Measurement Problem

Here's the unsolved part. Evolution is smooth and linear, yet measurement gives one definite outcome with Born-rule probabilities. Where does the linear story stop? Copenhagen, many-worlds, pilot-wave and collapse theories all give different answers with the same predictions. Honest physicists admit nobody knows.

#### Non-Locality and Non-Separability

Two particles together live in the [tensor product](tensors.md) of their spaces. A state like

$$ \tfrac{1}{\sqrt{2}}\left(|0\rangle \otimes |1\rangle - |1\rangle \otimes |0\rangle\right) $$

cannot be written as a single \(u \otimes v\): it's **entangled**. Measure one particle and you know the other, however far away. Bell's theorem shows no local hidden-variable story can reproduce the statistics. Misconception: this lets you signal faster than light. It doesn't; each side alone sees pure randomness.

#### Quantum Information

A **qubit** is a two-dimensional state vector. \(n\) qubits live in a \(2^n\)-dimensional space, which is where quantum computing's potential power, and its difficulty, come from. Picture-in-words: a classical register of 300 bits holds one of \(2^{300}\) numbers; 300 qubits hold an arrow in a space with more dimensions than there are atoms in the observable universe.

```mermaid
graph LR
  S["State vector |ψ⟩"] -->|"linear evolution e^(−iHt/ħ)"| S2["|ψ(t)⟩"]
  S2 -->|"measurement (Born rule)"| O["one outcome, probability |⟨φ|ψ⟩|²"]
```

### How it connects

- **Down** to [Vector Spaces](vectorspaces.md), [Inner Product Spaces](innerproductspaces.md) and [Linear Operators and Matrices](linearoperators.md).
- **Sideways** to [Groups](groups.md) and [Group Actions](group.md) (symmetry and spin), and [Exterior Algebras](exterioralgebras.md) (fermions and Pauli exclusion).
- **Out** to [Relativity](relativity.md), the other great theory of the 20th century, which quantum mechanics still hasn't been fully reconciled with.

The truth revealed: the quantum world isn't irrational. It is linear, complex and perfectly precise, right up to the moment you look.
