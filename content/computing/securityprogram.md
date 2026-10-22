---
title: Security Programs
date: '2016-11-30T05:26:42+04:00'
lastmod: '2016-11-30T06:05:51+04:00'
original_id: '{A533}'
original_name: securityprogram
original_blob: blob/B/3/201.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: securityprogram
draft: false
topics:
- security
---

# Security Programs

We must make management aware of the

 Tangible &
      loss of life, equipment, etc...
 Intangible Losses
      confidence of partners, employees
      confidence in organisation

We need to define and train cross-functional teams

We should define a Charter Scope
We need to define the asset inventory and assign responsibility matricies.

We need to define ICS Policies and procedures. We should choose a standard.
This standard will give a procedure to implement.

We then should perform risk and vulnerability assessments.

Where Risk = Impact x Probability

```
Probability - Quantitative
Likelyhood - Qualitative
Mitigation - Minimize Risk
Resiliance - How quickly you can run back to normal
```

Threat Modelling

1. Build Asset Inventory
1. Vulnerability Assessment of Asset
1. Identify All Prospective Threat Agents
1. SLE: Single Loss Expectancy (impact)
1. ARO: Annualized Rate of Occurance
1. ALE: Annualized Loss of Expectency
1. Set the Control Accordingly

- RTO - Recovery Time Objective  (How long will you take to recover?)
- RPO - Recovery Point Objective (how often do you backup?)
- MTO - Maximum Tolerable Outage

- Risk Mitigation
- Risk Avoidance
- Risk Transference
- Risk Acceptance
- Risk Ignorance

## Controls

- Physical Controls
- Technical
- Policy
- Directive Control
- Preventitive Control
- Detective Control
- Corrective Control
  ```
    Partial Service Restoration
  ```
- Recovery Control
  ```
   Full Recovery
  ```
- Deterent Control
- Compensatory Control
  ```
   Style of Arrange controls for fall backs
  ```

## Events

- **Event** - Something Happens Once
- **Incident** - Something is Happening Repeatedly
- **Problem** - Incidents are prevailing over long period

You need teams that are continuously preparing, analysing and acting on the above events.

### Analysing Logs

```
  Actual   Log's Claim

    TRUE   POSITIVE
    TRUE   NEGATIVE
    FALSE  POSTIVE
  **FALSE  NEGATIVE**
```

Look at the second term first. This tell you what the log is saying. The first is the truth/falsity in reality. In this case, the last scenario is most dangerous.

## Containment, Eradication & Recovery

## Post-Incident Active

Root Cause Analysis

- Who
- What
- Why
- Recommendations

### The plain idea

A security program is the *management* side of security: not a tool or a trick, but the ongoing process by which an organisation decides what it must protect, how much risk it can accept, and what to do about the rest. My notes above are the skeleton of that process, make leadership aware of the stakes, build teams, inventory your assets, assess risk, and set controls in proportion. The governing equation is simple: **Risk = Impact × Probability.**

### Why it matters

Technology alone never secures anything. Firewalls get misconfigured, patches get skipped, staff click links, because without a program nobody *owns* those tasks. A security program is what turns scattered good intentions into a repeatable system with budgets, responsibilities and review. It is also what regulators, insurers and partners increasingly demand before they trust you.

### An everyday analogy: running a household budget

You cannot protect against every possible expense, so you list what you own, judge what is most likely to go wrong and what it would cost (a boiler breaking versus a meteor), and spend your limited money where risk × cost is highest, insurance here, a smoke alarm there, nothing at all for the meteor. A security program is risk budgeting for an organisation.

### A worked example: the risk maths in my notes

My notes give the quantitative toolkit, and it is worth seeing it work. Suppose a company holds customer records on one server:

- **SLE (Single Loss Expectancy):** what one incident costs. Say a breach of that server costs £200,000.
- **ARO (Annualized Rate of Occurrence):** how often it is expected. Say once every four years, so 0.25 per year.
- **ALE (Annualized Loss Expectancy) = SLE × ARO** = £200,000 × 0.25 = **£50,000 per year.**

Now you can reason about spending: a £10,000-a-year control that cuts the ARO in half saves £25,000 a year, clearly worth it. The same logic sets **RTO** (how fast you must recover) and **RPO** (how much data you can afford to lose, i.e. how often to back up), the two numbers that drive every backup and disaster-recovery plan.

### A 2026 update

The vocabulary has standardised around frameworks. The **NIST Cybersecurity Framework 2.0** (2024) organises everything into six functions, *Govern, Identify, Protect, Detect, Respond, Recover*, and **ISO/IEC 27001** remains the certifiable standard for a security management system. The big shift is "Govern": security is now explicitly a board-level, continuous responsibility, not an IT project, with attention to third-party and supply-chain risk, and to incident response and recovery (ransomware made backups and tested recovery plans non-negotiable).

### Common misconceptions

- **"Buy the right product and you're secure."** Tools without a program are unowned and unmaintained.
- **"Risk can be eliminated."** It can only be reduced, transferred (insurance) or accepted; the goal is informed choice, not zero.
- **"Compliance equals security."** Passing an audit is a floor, not a ceiling; attackers do not read your certificate.
- **"It's the security team's job."** A program works only when responsibility is assigned across the whole organisation.

### How it connects

- [ICS Security](icssecurity.md): the control-system standards a program chooses from.
- [Secure Network Architecture](securenetworkarchitecture.md): a control the program mandates.
- [Forensics](forensics.md) and [IDS/IPS](idsips.md): the detect-and-respond functions.
- [Exploitation](exploitation.md): the threats you are modelling against.

The truth revealed: security is not something you buy or install once; it is a decision you make again every year about what is worth protecting and how much.
