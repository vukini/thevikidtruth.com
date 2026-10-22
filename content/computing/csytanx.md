---
title: C Syntax
date: '2021-08-27T00:51:47+04:00'
lastmod: '2023-05-19T01:12:26+04:00'
original_id: '{A1466}'
original_name: csytanx
original_blob: blob/B/12/265.txt
revisions: 17
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: csytanx
draft: false
topics:
- c-systems
---

[computingFreedom](computingfreedom.md) |
  [Build](bciyh.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) |
  [Operating Systems](os.md) |
  [Javascipt](javascript.md) |
  [Emacs](emacs.md)  | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Computer Security](computersecurity.md) |
  [Python](python.md) |
  [The Compiler](thecompiler.md) |
  [Identifiers](identifier.md) |
  [Literals](literals.md) |
  [storage_linkage](storagelinkage.md) |

# C Syntax

 
- IF
- ```
  if (TEST) {
       CODE;
  } else if(TEST) {
       CODE;
  } else {
       CODE;
  }
  ```
- SWITCH
- ```
  switch(OP) {
    case CONST:
      CODE;
      break;
    default:
      CODE;
  }
  ```
- [cppreference:switch](https://en.cppreference.com/w/cpp/language/switch)
- WHILE
- ```
  while(TEST) {
    CODE;
  }
  ```
- ```
  while(TEST){
    if(TEST2){
      continue;
    }
    CODE;
  }
  ```
- ```
  while(TEST){
    if(TEST2){
      break;
    }
    CODE;
  }
  ```
- DO
- ```
  do {
    CODE;
  } while(TEST)
  ```
- FOR
- ```
  for (INIT; TEST; POST) {
    CODE;
  }
  ```
- ENUM
- ```
   enum{CONST1, CONST2} NAME;
  ```
- GOTO
- ```
  if(TEST){
    goto somewhere
  }
  somewhere:
    CODE;
  ```
- FUNCTION
- ```
  TYPE NAME(ARG1, ARG2, ..) {
    CODE;
    return VALUE;
  }
  ```
- TYPEDEF
- ```
  typedef DEF ID;
  ```
- STRUCT
- ```
  struct NAME {
    ELEMS;
  } [VAR_NAME];
  ```
- ```
  typedef struct [STRUC_NAME] {
    ELEMS;
  } ID
  ```
- UNION
- ```
  union NAME {
    ELEMS;
  }[VAR_NAME]
  ```
