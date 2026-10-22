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
