---
title: Javascript Functions
date: '2023-04-02T01:28:00+04:00'
lastmod: '2026-10-22T10:30:00+04:00'
original_id: '{A1747}'
original_name: jsfunctions
original_blob: blob/B/12/172.txt
revisions: 3
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: jsfunctions
draft: false
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Javascript Functions

The truth at the heart of JavaScript: **functions are values.** You can store them in variables, pass them to other functions, return them, and stick them in objects. Everything clever in the language – callbacks, promises, event handlers, array methods – follows from that one fact.

### What it is, in plain words

A function is a reusable piece of code that takes inputs (**parameters**), does something, and optionally gives back an output (the **return value**). In 2026 you'll meet three common shapes:

```js
// 1. Function declaration – hoisted, has its own `this`
function add(a, b) {
  return a + b;
}

// 2. Function expression – a value assigned to a name
const sub = function (a, b) {
  return a - b;
};

// 3. Arrow function – short, no own `this` or `arguments`
const mul = (a, b) => a * b;
```

Plus methods inside objects and classes (`area() { ... }`), and `async` versions of all of the above.

### Why it matters

Functions are how you name an idea and stop repeating yourself. More than that, because they are values, you can build programs by *combining* small functions – the core move of [functional programming](functional.md). JavaScript was designed in 1995 by someone who wanted to put Scheme in the browser; the syntax ended up looking like Java, but the soul is Lisp. Functions are where that soul shows.

### An everyday analogy: a recipe card

A function is a recipe card. The parameters are the ingredient list, the body is the method, and the return value is the dish. Writing the card doesn't cook anything; *calling* the function does. And because it is a card, you can hand it to somebody else – "here, make this when the guests arrive". That hand-off is a **callback**.

### A hands-on example: functions as values

```js
const nums = [3, 1, 4, 1, 5, 9, 2, 6];

// Pass functions to other functions
const evens   = nums.filter(n => n % 2 === 0);      // [4, 2, 6]
const doubled = nums.map(n => n * 2);               // [6, 2, 8, ...]
const total   = nums.reduce((sum, n) => sum + n, 0); // 31

// Return functions from functions
const multiplier = factor => n => n * factor;
const triple = multiplier(3);
console.log(triple(7)); // 21

// Compose
const compose = (...fns) => x => fns.reduceRight((acc, f) => f(acc), x);
const inc = x => x + 1;
const square = x => x * x;
console.log(compose(square, inc)(4)); // 25
```

A function that takes or returns other functions is called **higher-order**. `map`, `filter` and `reduce` are the everyday ones.

### Parameters, modern style

```js
function connect(host, { port = 22, user = "root" } = {}, ...flags) {
  return `${user}@${host}:${port} ${flags.join(" ")}`;
}
console.log(connect("vikix.local", { user: "vikid" }, "-v", "-A"));
// vikid@vikix.local:22 -v -A
```

Default values, destructuring and rest parameters (`...flags`) have replaced the old `arguments` juggling.

### Async functions

Much of JavaScript waits on the network or the disk. An `async` function always returns a **Promise**, and inside it you can `await` other promises as if they were ordinary values:

```js
async function getRepo(name) {
  const res = await fetch(`https://api.github.com/repos/${name}`);
  if (!res.ok) throw new Error(res.status);
  const data = await res.json();
  return data.stargazers_count;
}
getRepo("nodejs/node").then(n => console.log("stars:", n));
```

`fetch` is built into Node.js (since v18) as well as browsers, so this runs in both. In modules you can even use `await` at the top level.

### Arrow functions and `this`

The big difference between arrows and ordinary functions is `this`. An ordinary function gets `this` from *how it is called*; an arrow function borrows `this` from the code around it. That makes arrows perfect for callbacks inside methods, and wrong for methods themselves:

```js
const timer = {
  seconds: 0,
  start() {
    setInterval(() => { this.seconds++; }, 1000); // arrow: `this` is timer
  },
};
```

### Pure functions

A **pure** function's output depends only on its inputs, and it changes nothing outside itself. `x => x * 2` is pure; a function that writes to a global or the DOM is not. Pure functions are easy to test and reason about. You can't build a useful program only from them, but the more of your logic lives in them, the calmer your life gets.

### Common misconceptions

- **"Arrow functions are just shorter syntax."** They also have no own `this`, no `arguments`, and can't be used with `new`.
- **"Functions run when you define them."** They run when *called*. `button.onclick = doThing()` calls it immediately; you meant `doThing`.
- **"`async` makes code run in parallel."** It makes waiting non-blocking. JavaScript still runs one piece of your code at a time on its event loop. For parallel CPU work use Workers.
- **"Callbacks are old-fashioned."** Promises and `async/await` are built on callbacks. `map`, `filter` and event listeners still take them.
- **"Recursion is dangerous in JS."** Deep recursion can overflow the stack (tail-call optimisation is in the spec but only Safari ships it), but for trees and moderate depths it is perfectly fine.

### Connections

- [Scope and Environment](jsscope.md) – each call creates an environment; closures keep it alive.
- [Objects](jsobjects.md) – functions are objects with an extra power: you can call them.
- [Events](jsevents.md) – event listeners are callbacks.
- [Lambda Calculus](lambdacalculus.md) – the mathematics of "functions are values".
- [Functional Programming](functional.md), [Haskell](haskell.md), [PicoLisp](picolisp.md) – languages that take this idea further.
