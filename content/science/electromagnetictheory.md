---
title: viKid Electromagnetics
date: '2022-07-28T05:44:08+04:00'
lastmod: '2022-07-28T05:47:42+04:00'
original_id: '{A1666}'
original_name: electromagnetictheory
original_blob: blob/B/10/541.txt
revisions: 4
author: admin
last_editor: admin
tags:
- science
categories:
- science
wikislug: electromagnetictheory
draft: false
topics:
- physics
---

[Physics](physics.md) | [Biology](biology.md) | [Chemistry](chemistry.md "MISSING PAGE") | [Climate](climate.md) | [Social](social.md "MISSING PAGE") | [Health](health.md) | [Philosophy](philosophy.md) | [Economics](economics.md) | [Politics](politics.md)
| [Ethics](ethics.md) | [Aesthetics](aesthetics.md "MISSING PAGE") | [Networks](networks.md) | [Energy](energy.md) | [Electromagnetic Theory](electromagnetictheory.md)

# viKid Electromagnetics

Electromagentics is the study of the interactions between electric charges at rest and in motion and the application of
electric and magnetic fields.

## The plain idea

Electromagnetism is the force behind almost everything you touch, see and use. Light is electromagnetism. So is the chemistry of your body, the solidity of the chair you sit on (electrons repelling electrons), every motor, every radio and every computer. Gravity holds planets together; electromagnetism holds *everything else* together.

The core picture is simple: **charges make fields, and fields push charges.** A charge at rest surrounds itself with an electric field. A moving charge (a current) also makes a magnetic field. And a changing magnetic field makes an electric field, and vice versa. That last fact is the secret of light.

## Why it matters

In the 1860s James Clerk Maxwell gathered everything known about electricity and magnetism into four equations, added one missing term, and found that they predicted **waves of electric and magnetic field travelling at a speed he could calculate from two laboratory constants**:

$$ c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 3.00 \times 10^{8}\ \text{m/s} $$

That was the measured speed of light. Light, it turned out, *is* an electromagnetic wave. Radio, microwaves, infrared, visible light, ultraviolet, X-rays and gamma rays are all the same thing at different wavelengths. It was one of the greatest unifications in the history of science, and it led directly to radio, television, radar, Wi-Fi and, through puzzles about the speed of light, to Einstein's [relativity](relativity.md).

## Maxwell's equations

In differential form, in a vacuum with charge density \(\rho\) and current density \(\mathbf{J}\):

$$ \nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0} \qquad \nabla \cdot \mathbf{B} = 0 $$

$$ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \qquad \nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} $$

In words:

1. **Gauss's law:** electric field lines start and end on charges.
2. **No magnetic monopoles:** magnetic field lines never start or end; they always loop.
3. **Faraday's law:** a changing magnetic field creates a circulating electric field. This is how generators and transformers work.
4. **Ampère–Maxwell law:** currents *and changing electric fields* create circulating magnetic fields. The second part is Maxwell's addition, and it is what makes self-sustaining waves possible.

## An everyday analogy: the bicycle dynamo

Spin a magnet near a coil of wire (a changing magnetic field) and a current flows: that is Faraday's law lighting your bike lamp. Run a current through the coil instead, and the magnet spins: that is a motor. Same physics, run forwards or backwards. Nearly all the world's electricity comes from this one effect, whether the spinning is driven by steam, water or wind.

## A worked example: the force between two charges

Coulomb's law gives the force between charges \(q_1\) and \(q_2\) a distance \(r\) apart:

$$ F = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r^2} $$

Take two electrons \(1\) nm apart (\(q = 1.602 \times 10^{-19}\) C, \(r = 10^{-9}\) m, \(\tfrac{1}{4\pi\varepsilon_0} \approx 8.988 \times 10^9\ \text{N m}^2/\text{C}^2\)):

$$ F \approx 8.988 \times 10^9 \times \frac{(1.602 \times 10^{-19})^2}{(10^{-9})^2} \approx 2.3 \times 10^{-10}\ \text{N} $$

Tiny, but compare the *gravitational* pull between the same two electrons: about \(5.5 \times 10^{-53}\) N. Electromagnetism beats gravity here by a factor of roughly \(4 \times 10^{42}\). Gravity only wins at large scales because positive and negative charges cancel out, while mass only ever adds up.

## The Fundamental Physical Constants

- Permittivity of Free Space (F/m)
- Permeability of Free Space (H/m)
- Intrinsic Impedance of Free Space
- Speed of Light in a Vacuum (m/s)
- Electron Charge (C)
- Electron Mass (kg)
- Proton Mass (kg)
- Neutron Mass (kg)
- Boltzmann Constant (J/K)
- Avogadro Number (/kg-mole)
- Plank Constant (J.s)
- Acceleration due to Gravity (m/s)
- Universal Gravitation Constant
- Newtons, N, (m/kg)^2
- Electron-volt (J)

### The values

Since the 2019 redefinition of the SI units, several of these constants are **exact by definition**; the rest are measured (CODATA 2022 recommended values, rounded):

| Constant | Symbol | Value |
|---|---|---|
| Speed of light in vacuum | \(c\) | 299 792 458 m/s (exact) |
| Elementary (electron) charge | \(e\) | \(1.602\,176\,634 \times 10^{-19}\) C (exact) |
| Planck constant | \(h\) | \(6.626\,070\,15 \times 10^{-34}\) J s (exact) |
| Boltzmann constant | \(k_B\) | \(1.380\,649 \times 10^{-23}\) J/K (exact) |
| Avogadro constant | \(N_A\) | \(6.022\,140\,76 \times 10^{23}\) /mol (exact) |
| Permittivity of free space | \(\varepsilon_0\) | \(8.854\,187\,8 \times 10^{-12}\) F/m |
| Permeability of free space | \(\mu_0\) | \(1.256\,637\,06 \times 10^{-6}\) H/m (≈ \(4\pi \times 10^{-7}\)) |
| Impedance of free space | \(Z_0 = \sqrt{\mu_0/\varepsilon_0}\) | ≈ 376.73 Ω |
| Electron mass | \(m_e\) | \(9.109\,383\,7 \times 10^{-31}\) kg |
| Proton mass | \(m_p\) | \(1.672\,621\,9 \times 10^{-27}\) kg |
| Neutron mass | \(m_n\) | \(1.674\,927\,5 \times 10^{-27}\) kg |
| Gravitational constant | \(G\) | \(6.674\,3 \times 10^{-11}\) N m²/kg² |
| Standard gravity | \(g_n\) | 9.806 65 m/s² (exact, by convention) |
| Electron-volt | eV | \(1.602\,176\,634 \times 10^{-19}\) J (exact) |

Two corrections to my list above: acceleration due to gravity is measured in m/s² (not m/s), and the unit of \(G\) is N m²/kg². Also note that since 2019 \(\mu_0\) is no longer exactly \(4\pi \times 10^{-7}\); it is measured, and agrees with that value to about one part in ten billion.

## Common misconceptions

- **"Electricity flows at the speed of light."** The *signal* (the field) travels at a large fraction of \(c\) along a wire; the electrons themselves drift at roughly millimetres per second.
- **"Magnetism and electricity are different forces."** They are two faces of one field. Relativity shows that what one observer sees as a pure electric field another sees as partly magnetic.
- **"Light needs a medium (the ether)."** Electromagnetic waves travel through empty space. The Michelson–Morley experiment (1887) found no ether.
- **"Static electricity is a different kind."** Same charges, just not moving much.

## How it connects

- [Physics](physics.md), [Relativity](relativity.md) and [Quantum Mechanics](qm.md): quantum electrodynamics (QED) is the quantum version, and the most precisely tested theory in science.
- [The Standard Model](standardmodel.md): the photon is the carrier of the electromagnetic force.
- [Energy](energy.md): generators, motors and the grid.
- [Div, Grad, Curl](divgradcurl.md) for the vector calculus behind Maxwell's equations.

The truth revealed: the light you are reading this by is a ripple in the same field that holds your atoms together.
