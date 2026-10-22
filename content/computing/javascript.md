---
title: Javascript
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
draft: true
review: update
topics:
- javascript
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Javascript

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
