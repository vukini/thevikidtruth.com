---
title: Linearity
date: '2016-12-07T22:06:13+04:00'
lastmod: '2016-12-07T23:00:19+04:00'
original_id: '{A767}'
original_name: linearity
original_blob: blob/B/4/730.txt
revisions: 13
author: admin
last_editor: admin
tags:
- misc
categories:
- misc
wikislug: linearity
draft: false
---

# Linearity

Linear Systems are **systems that can be broken into parts** where each part is **solved independently** and finally
the **solution can be made by the recombination (summation) of these parts**.

By contrast **[Non-Linear](nonlinearity.md "MISSING PAGE")** systems generally **cannot be split up** in this way. The
different components of
the system **depend on each other**. Therefore one cannot **reduce the problem to a simpler statement of the problem** and
usually due to [combinatorial-explosion](combinatorial-explosion.md "MISSING PAGE") the **solution space is massive** and hence difficult to solve.

For example: listening to your two favourite songs **at the same time**
**doubles the noise you hear (Linearity)** but **it doesn't double the pleasure (Non-Linearity)**.

This can be expressed Mathematically as **a linear map or linear function**,

```
f(x) is a function that satisfies the following two properties:

 [1]   Additivity : f(x + y) = f(x) + f(y).
 [2]   Homogeneity: f(αx)    = αf(x)        for all α, (Homogeneity of degree 1)
```

- **Equation [1]** just says that a function of the two variables **x and y** can be split and summed into two functions.
  Just what we said above.
- **Equation [2]** is a bit cooler still. It says that we can really **decompose x itself**. So for example, **50 = 50 x 1,**
  so **f(50) = 50f(1).** Normally calculating any function on 1 is much easier that doing it on some arbitrary number like 50.

Any System that satisfies these two conditions is said to be **Linear**
