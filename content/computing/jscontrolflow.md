---
title: Javascript Control Flow
date: '2022-08-24T01:03:54+04:00'
lastmod: '2023-04-11T04:15:55+04:00'
original_id: '{A1706}'
original_name: jscontrolflow
original_blob: blob/B/12/167.txt
revisions: 11
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: jscontrolflow
draft: false
topics:
- javascript
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Javascript Control Flow

Here is the truth about control flow in JavaScript: **the keywords are borrowed from C, but the decisions are made by JavaScript's own rules about truth and equality.** `if`, `for` and `switch` will look familiar. What they *consider true* will not, until you learn the short list below.

### What it is, in plain words

Control flow is how a program decides what to run next. JavaScript gives you:

- **Branches**: `if / else if / else`, `switch`, the ternary `cond ? a : b`, and the short-circuit operators `&&`, `||` and `??`.
- **Loops**: `for`, `for...of` (values of an iterable), `for...in` (keys of an object), `while`, `do...while`, plus array methods like `forEach`, `map` and `filter`.
- **Jumps**: `break`, `continue`, `return`, `throw` with `try / catch / finally`.
- **Asynchronous flow**: `async` / `await` and Promises, which decide *when* code runs as well as whether.

Every branch and loop condition is converted to a boolean using **truthiness**. Exactly eight values are *falsy*: `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` and `NaN`. Everything else, including `[]`, `{}`, `"0"`, `"false"` and `Infinity`, is truthy.

### Why it matters

Most JavaScript bugs in conditions come from two places: loose equality (`==`) doing surprising type conversions, and truthiness treating `0` or `""` as "missing". Knowing the rules lets you write conditions that mean what you think, and read other people's code without second-guessing.

### An everyday analogy: a lenient doorman and a strict one

`==` is a lenient doorman. Show him the number 5 or the text "5" and he lets you both in, because he converts you to the same thing first. Sometimes he converts in very odd ways (`0 == ""` is true). `===` is the strict doorman: same type *and* same value, or you are not coming in. Use the strict one unless you have a reason.

### A hands-on example

Run this with `node flow.js` (or paste into the browser console):

```js
// flow.js
const items = [
  { name: "pil",   stars: 5 },
  { name: "emacs", stars: 0 },
  { name: "vim" },               // stars missing
];

for (const { name, stars } of items) {
  // ?? only falls back for null/undefined, so 0 stays 0
  const s = stars ?? "unrated";
  // || would wrongly turn 0 into "unrated"
  console.log(name.padEnd(6), s, stars || "unrated");
}

// switch uses === to compare
function kind(x) {
  switch (typeof x) {
    case "number": return Number.isNaN(x) ? "NaN" : "number";
    case "string": return "string";
    case "object": return x === null ? "null" : Array.isArray(x) ? "array" : "object";
    default:       return typeof x;
  }
}
console.log([1, "a", null, [], {}, NaN, 10n].map(kind));

// Loop control and labels
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 1) continue;
    if (i === 2) break outer;
    console.log(i, j);
  }
}

// Asynchronous control flow
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
async function main() {
  try {
    await wait(100);
    throw new Error("demo");
  } catch (e) {
    console.log("caught", e.message);
  } finally {
    console.log("always runs");
  }
}
main();
```

Notice `stars ?? "unrated"` versus `stars || "unrated"` for emacs: the first keeps `0`, the second throws it away. The nullish coalescing operator `??` (ES2020) fixed a whole category of bugs.

### Common misconceptions

- **"`Infinity` is falsy."** The table further down this page says so, and it is wrong: `Boolean(Infinity)` is `true`. Only the eight values listed above are falsy. (The `()` line there is not valid JavaScript at all.)
- **"There are seven falsy values."** The list lower down has seven because it leaves out `-0`, which is falsy too. MDN lists eight (and `document.all`, a browser oddity).
- **"`[] == false` so `[]` is falsy."** `[] == false` is `true` because of type conversion, yet `if ([])` runs. Equality and truthiness are different rules, which is the best argument for `===`.
- **"`for...in` loops over an array's values."** It loops over *keys* (as strings), including inherited ones. Use `for...of` for values.
- **"`switch` uses `==`."** It uses strict equality, so `case "5":` never matches the number 5.
- **"`await` blocks the program."** It pauses only that `async` function; the event loop keeps running everything else.

### Connections

- [JavaScript Data Types](jsdatatypes.md), [JS Variables](jsvariable.md), [JS Scope](jsscope.md), [JS Functions](jsfunctions.md), [JS Events](jsevents.md).
- [C Syntax](csytanx.md) – where these keywords came from; [Bash if statements](bashif.md) – a very different idea of "true".
- [Node Js](nodejs.md), [Three.js](jsthree.md), [Web Development](webdevelopment.md).

## Equality

- **Triple Equals**
- ```
    1 === 1;
  ```
- **type**
- **value**
- **Double Equals**
- ```
    1 == 1;
  ```
- **Weird Examples**
- ```
    0 == "0"         // true
    0 == ""          // true
    0 == []          // true
  ```
- ```
    0 == null        // false
    0 == undefined   // false
  ```
- ```
    "true"  == true  // false
    "false" == false // false
  ```
- ```
    5 == "5";
  ```
- ```
    5 === Number("5");
  ```
- **Truthy or Falsy?**
- ```
    ""       // falsy
    []       // truthy
    ()       // truthy
    NaN      // falsy
    Infinity // falsy
    0        // falsy
  ```
- ```
           "" == false      // true
            0 == false      // true
           0n == false      // true
          Nan == false      // false
         null == false      // false
    undefined == false      // false
  ```
- ### memorize the 7 falsy values
- - ""
    - 0
    - 0n
    - NaN
    - undefined
    - null
    - false
- ```
  null == null              // true
  null == false             // false
  null == true              // false
  ```

**Objects**
  
```
  Obj1 === obj2   // always false
  
```

unless they are literally the same object.
}

## If Statements

```
  let condition  = true;
  let condition2 = false;
  if (condition) {
  console.log("Do action");
  } else if (condition2) {
  console.log("take alternative actions");
  } else {
  console.log("take default action");
  }
```

```

```
