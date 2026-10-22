---
title: Identifiers in C
date: '2016-11-21T05:40:07+04:00'
lastmod: '2023-03-28T07:47:44+04:00'
original_id: '{A311}'
original_name: identifier
original_blob: blob/B/11/630.txt
revisions: 23
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: identifier
draft: false
topics:
- c-systems
---

# Identifiers in C

[Back to Tokens](tokens.md) | [Back to C Programming](cprogramming.md) | [The Compiler](thecompiler.md)

There are 4 types of Identifiers and each type gets its own namespace.

- Label Names, are names that end in a **colon, :**
- Tags for structure, union, and enumeration types
- Names of Structure or Union **members**
- Ordinary Identifiers (all others)

```
struct tag { char tag; ...}
```

Here you can see we have created a structure with the tag **tag**, which also has
a member **tag** of the type char.

```
int count( struct tag *tag)
{
 int len = length( tag->tag)
}
```

Here you can see we defined the function **count** with a parameter named **tag**
which is a pointer to **struct tag**.

In all cases the name **tag** is in different namespaces and do not conflict.

## Identifier Scope

Scopes can confusing, so lets hope we can putthe confusion to rest here.

The scope of an identifier generally begins **after** the declaration except when we
define **structures, union and enumeration types**.

In these cases, the identifier goes into scope **immediately**, within the declaration itself. So you can used the
identifier for **recursive** definitions.

#### File Scope

If you declare the identifier outside of all blocks and parameter lists.
you can use the identifier **anywhere** within the **translation unit / module**.

#### Block Scope

Ignoring **lables**.

An Identifier declared in a block has the scope of the smallest block it is
declared in from its location to the end of the block.

The **parameters** in the function also have block scope.

#### Function Prototype Scope

Identifiers within parameters of the prototype only have scope in the prototype.

#### Function Scope

Labels are special. They take the full scope of the function, no matter if they
are nested within blocks.

i.e. you can use them as **goto** statements.
