---
title: Julia
date: '2021-08-27T10:40:18+04:00'
lastmod: '2021-08-28T22:49:36+04:00'
original_id: '{A1475}'
original_name: julia
original_blob: blob/B/7/632.txt
revisions: 32
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: julia
draft: false
---

[Read This!](caveatemptor.md) | [Algorithms](algorithms.md) | [AssemblyLanguage](assemblylanguage.md) | [BASH](bash.md) |   [C-Programmming](cprogramming.md) |
[Computer Security](computersecurity.md) |  [Databases](databases.md) | [Emacs](emacs.md) |  [Exploitation](exploitation.md) | [Firewalls](firewalls.md) |   [Git](git.md) |
[Javascipt](javascript.md) | [Julia](julia.md) | [Social Engineering](internetexploitation.md) |
[Picolisp](picolisp.md) | [Pharo Smalltalk](pharo.md) |
[Linux](linux.md) |
[Python](python.md) |
[Operating Systems](os.md) |
[Machine Learning](machinelearning.md) | [Metasploit](metasploit.md) |  [Open Data Science](opendatascience.md) |
[Networking](networking.md) | [Machine Learning](machinelearning.md) |[Scheme](scheme.md) |
[Unity](unity.md) | [vim](vim.md) |
[Web Development](webdevelopment.md)

# Julia

This page is derived in large part from the :
[Think Julia Book](https://benlauwens.github.io/ThinkJulia.jl/latest/book.html).
Get new packages at: [Julia Observer](https://juliaobserver.com).

- [Julia Academy](https://juliaacademy.com/courses/)
- [Github: Foundations of Machine Learning](https://github.com/JuliaAcademy/Foundations-of-Machine-Learning)

```
 Keywords
 abstract type  baremodule  begin    break   catch
 const          continue    do       else    elseif
 end            export      finally  for     false
 function       global      if       import  in
 let            local       macro    module  mutable struct
 primitive type quote       return   true    try
 using          struct      where    while
```

- Operators
- - **isa**
    - ` n isa Int64 `
- Values and Types
- - nothing
    - ```
        typeof(nothing) --> Nothing
      ```
- Formal and Natural Languages
- Variables, Expressions and Statements
- - Variable names can be as long as you like.
        They can contain almost all Unicode characters,
         but **they can’t begin with a number.**
    - typing unicode: ` \\:turtle: TAB, \\pi TAB `, if you press tab twice you get suggestions
    - The subscript numbers are available in the Unicode character encoding ` \\_1 TAB, \\_2 TAB, etc.` .
    - Superscript numbers are also available ;{ \^2 TAB

 Assignment Statements 
 Variable Names 
 Expressions and Statements 
An *expression* is a **combination of one or more values, variables and operators**.
A *statement* is a unit of code that has an effect.
 Operator Precedence 
 String Operations 

```
 string1 * string2,  for string concatenation
 string^x concat x repetions of string
```

 Comments

```
 # for comments
```

 Functions 

- Converstion
- ```
  parse(Int64, "10")
  parst(Float64, "2.71")
  trunc(Int64, 3.3333)
  ```
- Math Functions
- ```
  log10()
  sqrt()
  exp(1.0)
  abs()
  ```
- Defining New Functions
- ```
  function myNewFunction(arg)
      x = "hello "
      println(x * arg * " hello")
  end
  ```
- Useful Functions
- ```
  time()
  show()
  ```

 Turtles 
Packages can be installed in the REPL by entering the Pkg REPL-mode using the key **]**.

```
(v1.0) pkg> add https://github.com/BenLauwens/ThinkJulia.jl
```

Before we can use the functions in a module, we have to import it with an using statement:

```
julia> using ThinkJulia
```

 Docstring 

```
"""
polyline(t, n, len, angle)

Draws n line segments with the given length and
angle (in degrees) between them.  t is a turtle.
"""
function myfunc()
end
```

then type ?

```
help?> myfunc
```

 Conditionals and Recursion 

- Floor Division and Modulus
- ` ÷ (\div TAB) `
- Boolean Expressions
- ```
        typeof(true)         # Bool
        x == x               # x is equal to x
        x != y               # x is not equal to y
        x ≠ y                # (\ne TAB)
        x > y                # x is greater than y
        x < y                # x is less than y
        x >= y               # x is greater than or equal to y
        x ≥ y                # (\ge TAB)
        x <= y               # x is less than or equal to y
        x ≤ y                # (\le TAB)
  ```
- Logical Operators
- **&& , || , and ! .**
- Conditional Execution
- ```
  if x < y
      println("x is less than y")
  elseif x > y
      println("x is greater than y")
  else
      println("x and y are equal")
  end
  if 0 < x < 10
      println("x is a positive single-digit number.")
  end
  ```

 Keyboard Input 

```
text = readline()
```

 Fruitful Functions 
 Return Values 
 Incremental Development 
 Composition 
 Boolean Functions 
 More Recursion 
 Leap of Faith 
 One More Example 
 Checking Types 
 Iteration 
 Reassignment 
 Updating Variables 
 The while Statement 
 break 
 continue 
 Square Roots 
 Algorithms 
 Strings 
 Characters 
 A String Is a Sequence 
 length 
 Traversal 
 String Slices 
 Strings Are Immutable 
 String Interpolation 
 Searching 
 Looping and Counting 
 String Library 
 The ∈ Operator 
 String Comparison 
 Case Study: Word Play 
 Reading Word Lists 
 Search 
 Looping with Indices 
 Arrays 
 An Array is a Sequence 
 Arrays Are Mutable 
 Traversing an Array 
 Array Slices 
 Array Library 
 Map, Filter and Reduce 
 Dot Syntax 
 Deleting (Inserting) Elements 
 Arrays and Strings 
 Objects and Values 
 Aliasing 
 Array Arguments 
 Dictionaries 
 A Dictionary Is a Mapping 
 Dictionary as a Collection of Counters 
 Looping and Dictionaries 
 Reverse Lookup 
 Dictionaries and Arrays 
 Memos 
 Global Variables 
 Tuples 
 Tuples Are Immutable 
 Tuple Assignment 
 Tuples as Return Values 
 Variable-length Argument Tuples 
 Arrays and Tuples 
 Dictionaries and Tuples 
 Sequences of Sequences
 Case Study: Data Structure Selection 
 Word Frequency Analysis 
 Random Numbers 
 Word Histogram 
 Most Common Words 
 Optional Parameters 
 Dictionary Subtraction 
 Random Words 
 Markov Analysis 
 Data Structures
 Files 
 Persistence 
 Reading and Writing 
 Formatting 
 Filenames and Paths 
 Catching Exceptions 
 Databases 
 Serialization 
 Command Objects 
 Modules 
 Debugging 
 Structs and Objects 
 Composite Types 
 Structs are Immutable 
 Mutable Structs 
 Rectangles 
 Instances as Arguments
 Instances as Return Values 
 Structs and Functions 
 Time 
 Pure Functions 
 Modifiers 
 Prototyping Versus Planning 
 Multiple Dispatch 
 Type Declarations 
 Methods 
 Additional Examples 
 Constructors 
 show 
 Operator Overloading 
 Multiple Dispatch 
 Generic Programming 
 Interface and Implementation 
 18. Subtyping 
 Cards 
 Global Variables 
 Comparing Cards 
 Unit Testing 
 Decks 
 Add, Remove, Shuffle and Sort 
 Abstract Types and Subtyping 
 Abstract Types and Functions 
 Type Diagrams 
 Debugging 
 Data Encapsulation
 The Goodies: Syntax 
 Named Tuples 
 Functions 
 Blocks 
 Control Flow 
 Types 
 Methods 
 Constructors 
 Conversion and Promotion 
 Metaprogramming 
 Missing Values 
 Calling C and Fortran Code 
 The Goodies: Base and Standard Library 
 Measuring Performance 
 Collections and Data Structures 
 Mathematics 
 Strings 
 Arrays 
 Interfaces 
 Interactive Utilities 
 Debugging 
 
- ` error() `
- Syntax Errors
- Runtime Errors
- Semantic Errors
