---
title: Javascript Data Types
date: '2022-08-24T00:05:54+04:00'
lastmod: '2023-04-11T04:15:36+04:00'
original_id: '{A1705}'
original_name: jsdatatypes
original_blob: blob/B/12/165.txt
revisions: 18
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: jsdatatypes
draft: false
topics:
- javascript
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Javascript Data Types

Here is the truth about JavaScript types: **variables have no types; values do, and there are only eight kinds of value.** Seven are simple, unchangeable *primitives*. The eighth, *object*, covers everything else, including arrays and functions. Most "JavaScript is weird" moments are about where that line between primitive and object falls.

### What it is, in plain words

The ECMAScript standard (ES2026 in 2026, a new edition every June) defines these types:

| Type | Example | `typeof` says |
|---|---|---|
| Undefined | `undefined` | `"undefined"` |
| Null | `null` | `"object"` (a famous historical bug) |
| Boolean | `true`, `false` | `"boolean"` |
| Number | `42`, `3.14`, `NaN`, `Infinity` | `"number"` |
| BigInt | `10n` | `"bigint"` |
| String | `"pil"`, `'vim'`, `` `hi ${name}` `` | `"string"` |
| Symbol | `Symbol("id")` | `"symbol"` |
| Object | `{}`, `[]`, `new Date()`, functions | `"object"` or `"function"` |

So the list at the top of the notes below is close but not quite right: **functions are objects** (callable ones, which is why `typeof` gives them their own answer), and **null** is a type of its own that belongs in the list.

**Primitives** are immutable and compared by value: `"abc" === "abc"` is true. **Objects** are mutable and compared by *reference*: two separate `{}` are never equal, which is exactly what the `person` / `newPerson` example below shows. Copying a variable that holds an object copies the reference, not the object.

### Why it matters

- **Numbers are all 64-bit floats.** `0.1 + 0.2 === 0.30000000000000004`. Integers are exact only up to `Number.MAX_SAFE_INTEGER` (2^53 − 1). For money, IDs or big counts use `BigInt` or integers of cents.
- **Shared references cause spooky changes.** Change an object in one function and every variable that holds it sees the change.
- **Types drive conversions.** `"5" * 2` is `10` but `"5" + 2` is `"52"`. Knowing which operator converts which way avoids silent bugs.

### An everyday analogy: photocopies and house keys

A primitive is a photocopy. Give a friend a copy of your shopping list and they can scribble on it all they like; your list does not change. An object is your house key. Give a friend a copy of the key and you both open the *same* house. If they rearrange the furniture, you see it when you get home.

### A hands-on example

```js
// types.js  -  run with: node types.js
const values = [undefined, null, true, 42, 10n, "pil", Symbol("id"), {}, [], () => 1];
for (const v of values) console.log(String(v).padEnd(14), typeof v);

// Numbers: floats, safe integers, BigInt
console.log(0.1 + 0.2);                          // 0.30000000000000004
console.log(Number.MAX_SAFE_INTEGER + 2);        // 9007199254740992 (wrong!)
console.log(2n ** 64n);                          // 18446744073709551616n

// Value versus reference
const a = { lang: "PicoLisp" };
const b = a;              // same object
const c = { ...a };       // shallow copy
const d = structuredClone(a);  // deep copy (built in since 2022)
b.lang = "Scheme";
console.log(a.lang, c.lang, d.lang);             // Scheme PicoLisp PicoLisp

// Telling things apart properly
console.log(Array.isArray([]), Number.isNaN(NaN), Object.is(-0, 0));  // true true false

// Immutable updates (ES2023): return new arrays, leave the original alone
const nums = [3, 1, 2];
console.log(nums.toSorted(), nums);              // [1,2,3] [3,1,2]
```

Compare PicoLisp, which has just three types (numbers, symbols, lists) and arbitrary-precision integers by default, so `(** 2 64)` simply returns `18446744073709551616` with no special syntax.

### Common misconceptions

- **"`typeof null === "object"` means null is an object."** It is a bug from 1995 kept for compatibility. Test with `x === null`.
- **"Arrays are a separate type."** They are objects with numeric keys and a `length`. Use `Array.isArray`.
- **"`const` makes an object immutable."** It only stops the *variable* being reassigned. Use `Object.freeze` for a shallow freeze.
- **"`NaN === NaN`."** It is false. Use `Number.isNaN(x)` or `Object.is(x, NaN)`.
- **"Strings are arrays of characters."** They are immutable sequences of UTF-16 code units, so an emoji can have `length` 2. Use `[...str]` to iterate by character.

### Connections

- [JavaScript Control Flow](jscontrolflow.md), [JS Variables](jsvariable.md), [JS Objects](jsobjects.md), [Prototypal Inheritance](jsprototypalinheritance.md), [JS Functions](jsfunctions.md).
- [C Integers](cints.md) and [C Floats](cfloats.md) – the same float behaviour, because JavaScript numbers are C doubles.
- [Node Js](nodejs.md), [Three.js](jsthree.md), [PicoLisp](picolisp.md).

## My original notes

There are 8 fundamental data types:

- Numbers, Strings, Booleans, Objects, Functions, Undefined, Bigints, Symbols

Variables don't have types. The values have types. remember to use ` typeof ` operator.

1. ## Numbers
1. ```
  5
  0b101
  0o5
  0x5
  5e7
  ```
1. ```
  10 * "string" => NaN
  10/0 => Infinity
  -10/0 => -Infinity
  ```
1. Strings
1. `"" '' ```
1. ```
  let s = "Jane is good"
  s.length //12
  s.toLowerCase()
  s.toUpperCase()
  ```
1. ## Booleans
1. ```
  true
  false
  ```
1. ```
  ""
  0
  NaN
  0n  // Bigint value
  null
  undefined
  false
  ```
1. ## Objects
1. ```
  let person ={
   name: "Jane",  // don't forget the commas!
   age: 5
  }
  person.name;
  person["name"];
  person.age = 6;
  let newPerson = person;
  ```
1. ```
  newPerson.age = 7;
  person.age;        // 7
  ```
1. `newPerson`
1. `person`
1. ```
  let name = "Jane";
  let age = 8;
  let oldPerson = {
    name,
    age,
   }
  ```
1. ```
  let somePerson = null;
  typeof somePerson; // 'object'
  ```
1. ### Arrays
1. ```
  let a = [0, 1];  // undefined
  a.length;
  a[0] = 2;
  a.push(3);
  a.pop();
  a.unshift(4)
  a.shift().
  a.indexOf(1);
  ```
1. ```
  map filter sort
  ```
1. ## Functions
1. ```
   function add(x, y){
      return x+y;
   }
  ```
1. ```
  let add1 = function(x, y){
      return x+y;
   }
  ```
1. ```
  let add2 = (x, y) => {
      return x+y;
   }
  ```
1. ## Undefined
1. ```
  typeof blah; //undefined
  let x; //undefined
  blah.x //undefined
  blah[0] //undefined
  typeof undefined; // undefined
  typeof null; // object
  ```
1. ## Bigints
1. ` 10n `
1. ```
    10n + BigInt(2) // 12n
  ```
1. ## Symbols
1. ```
    let mySym = Symbol("aGoodSymbol");
    mySym;                             // Symbol(aGoodSymbol)
    let mySym1 = Symbol.for("aVeryGoodSymbol");
  ```
