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
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Javascript Data Types

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
