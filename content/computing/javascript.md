---
title: "JavaScript"
date: '2016-07-25T09:47:24+04:00'
lastmod: '2023-04-11T04:15:01+04:00'
original_id: '{A165}'
original_name: javascript
original_blob: blob/B/12/162.txt
revisions: 47
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: javascript
draft: false
topics:
- javascript
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Javascript

### The plain idea

JavaScript is the programming language of the web. It began in 1995 as a small scripting language to make web pages interactive, and it has grown into one of the most widely used languages in the world: it runs in every browser, on servers (via [Node.js](nodejs.md)), in desktop and mobile apps, and even on tiny devices. The language is formally called **ECMAScript**, and since the big **ES6 (2015)** update it has gained a modern yearly release (we are well past ES2015 now, with ES2024 shipped), adding features like `let`/`const`, arrow functions, classes, modules, promises and `async`/`await`.

### Why it matters

If you want to build anything people use in a browser, you will meet JavaScript; there is effectively no alternative that runs natively everywhere the web does (WebAssembly complements it, it does not replace it). Learning it well, especially its genuinely unusual parts, closures, prototypes, the event loop, "the weird parts" my links below explore, unlocks front-end, back-end and full-stack development with a single language.

### A worked example: the variable keywords in my notes

My notes above contrast `var`, `let` and `const`. The modern rule of thumb is simple: **use `const` by default, `let` when you must reassign, and avoid `var`.** Here is why `var` surprises people:

```js
function demo() {
  if (true) { var x = 1; let y = 2; }
  console.log(x);   // 1  -- var leaked out of the block
  console.log(y);   // ReferenceError -- let stayed in the block
}
```

`var` is function-scoped and "hoisted" (usable before its line, which breeds bugs); `let` and `const` are block-scoped and must be declared before use. That single change, blocks that actually contain their variables, removed a whole category of classic JavaScript mistakes.

### An everyday analogy

Think of a browser page as a stage. HTML is the set, CSS is the lighting and costumes, and JavaScript is the script the actors follow, deciding what happens when the audience (the user) claps, clicks or types. Without it the stage is a static tableau; with it the play comes alive.



[Node JS](nodejs.md)
`"use strict";`
[Data Types](jsdatatypes.md)
[Variables](jsvariable.md)
There are three ways of variable declaration:

1. let - (block-scoped)
1. const
1. var - (function-scoped

“var” has no block scope. Variables, declared with var, are either function-scoped or global-scoped.
“var” tolerates redeclarations
If we declare the same variable with let twice in the same scope, that’s an error.
“var” variables can be declared below their use. Declarations are hoisted, but assignments are not.

```
let message;

let message = 'Hello!';

let user = 'John', age = 25, message = 'Hello';

let user = 'John'
  , age = 25
  , message = 'Hello';

var message = 'Hello';
```

[Control Flow](jscontrolflow.md)
[Scope and Environment](jsscope.md)
[Objects](jsobjects.md)
[Functions](jsfunctions.md)
[Prototypal Inheritance](jsprototypalinheritance.md)
[Events](jsevents.md)
[Three.js](jsthree.md)

#### External Links

- [An Introduction to JavaScript](https://javascript.info/intro)
- [p5js Wiki](https://github.com/processing/p5.js/wiki)
- [You-Dont-Know-JS: A book series on JavaScript](https://github.com/getify/You-Dont-Know-JS)
- [SICP JS](https://sourceacademy.org/sicpjs/index)
- [javascript-the-weird-parts](https://medium.com/@daffl/javascript-the-weird-parts-8ff3da55798e#.4nfqhqbah)
- [Javascript: the weird parts by Charlie Harvey](http://charlieharvey.org.uk/page/javascript_the_weird_parts)
- [Learn JavaScript, Front-End Web Development and Node.js with Frontend Masters Courses](https://frontendmasters.com/courses/)
- [Excellent Free Tutorials to Learn JavaScript - LinuxLinks](https://www.linuxlinks.com/excellent-free-tutorials-learn-javascript/)
- [Excellent Free Tutorials to Learn ECMAScript - LinuxLink](https://www.linuxlinks.com/excellent-free-tutorials-learn-ecmascript/)
- [Draw a Clock with Yurichev](https://yurichev.com/news/20220321_sin_cos_clock/)
- [JSFiddle - Code Playground](https://jsfiddle.net/)
- [3DE Code Editor](https://www.code3dgames.com/3de/)
- [Get Started With Viewing And Changing The DOM | Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/dom)
- [Levelup Tutorials](https://www.leveluptutorials.com)
- [Meteor University | Learn MeteorJS](https://university.meteor.com)

#### Videos

- [bytesize coding](https://bytesizecoding.com)
- [Why I love Meteor - 23 Oct 2020](https://www.youtube.com/watch?v=hTVfpmmGgAk)

#### Other

- [Douglas Crockford's wonderfull site](http://www.crockford.com)
  [Meteor JS](https://www.meteor.com/#!)
