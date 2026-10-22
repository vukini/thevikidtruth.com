---
title: Prototypal Inheritance
date: '2023-04-11T03:13:18+04:00'
lastmod: '2023-04-12T00:35:09+04:00'
original_id: '{A1762}'
original_name: jsprototypalinheritance
original_blob: blob/B/12/200.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: jsprototypalinheritance
draft: false
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Prototypal Inheritance

hidden property [[Prototype]] - null or a reference to other object

```
prototype obj
     ^
     | [[Prototype]]
     |
    obj
```

When we read a property from object, and it’s missing, JavaScript takes it from the prototype
` obj.__proto__ ` can be used to set it

```
let earphones = { speakers: 2 };

let jbl       = { bluetooth: true };

jbl.__proto__ = earphones;  // sets jbl.[[Prototype]] to earphones
```

alternatively:

```
let jbl       = {
  bluetooth: true,
  __proto__: earphones
};
```

## Sources, External Links

[javascript.info/prototype-inheritance](https://javascript.info/prototype-inheritance)
