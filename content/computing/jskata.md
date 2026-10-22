---
title: Javascript Kata
date: '2023-04-05T22:08:12+04:00'
lastmod: '2023-04-11T04:15:14+04:00'
original_id: '{A1753}'
original_name: jskata
original_blob: blob/B/12/163.txt
revisions: 12
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: jskata
draft: true
review: update
topics:
- javascript
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Javascript Kata

Memorize each code block cold.

```
let a = "a";
var n = 1;
let m = n + 1;
var l;
var code = "code";
var test = 1 === 1; // !==, >, >=, <, < =
var ans = m <= 2 && n === 1 || code === "code"
var abcd = [a, "b", "c", "d"];
```

```
abstract, alert, as

boolean, break, byte
```

```
case, catch, char, class, continue, const

debugger, default, delete, do, double
```

```
else, enum, export, extends

false, finally, float, for, function

goto
```

```
if, implements, import, in, instanceof, int, interface, is

long

namespace, native, new, null
```

```
package, private, protected, public

return

short, static, super, switch, synchronized
```

```
this, throws, transient, true, try, typeof
```

```
use

var, void, volatile

while, with
```

```
m = n+n;
var l = n++         //use then increment

    l = ++n         //increment then use
```

```
"l = " + l +"."
```

```
var question = "What is your name?"
var defaultAnswer = "Vikid"
var name = prompt(question, defaultAnswer)
```

```
var test = 1 === 1; // !==, >, >=, <, < =

if (!test) {
  code+" if";
}
else if(!test) {
  code+" if else";
}
else{
 code+" else";
}
```

```
abcd[0] = "A";
abcd.pop();
abcd.push("e", "f");
abcd.shift();
abcd.unshift("yy" "zz");
abcd.splice(1,0, "__");
abcd.splice(0,2)
```

```
let o  = new Object();
let oo = {}

let key = "height"
let user = {name: "vikid", age: "44", "my nickname": "vkt", [key + " (inches)"]: 171};

user.isCool = true;
delete user.isCool;

function Person(name, age) {
  return {name, age};
};
```

```
"name" in user;
for (key in user) {
  console.log(key);
}
```
