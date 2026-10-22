---
title: Haskell Kata
date: '2023-04-06T04:16:37+04:00'
lastmod: '2023-04-06T04:16:57+04:00'
original_id: '{A1755}'
original_name: haskellkata
original_blob: blob/B/12/044.txt
revisions: 2
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: haskellkata
draft: false
---

[Haskell](haskell.md) | [Haskell Kata](haskellkata.md) |

# Haskell Kata

## Getting Started

min 1 2
max 1 2
}

```
dbl x = x + x
dbls x y = dbl x + dbl y

dsn x = if x > 100
  then x
  else x*2
dsn' x = (if x > 100 then x else x*3) + 1
```

```
nL = [0,1,2,3,4,5,6,7,8,9]
nL ++ [10,11,12]
0:nL
nL!!3
nLL= [nL,nL,nL]
nLL ++ [[0,2]]
[10,11,12]:nLL
```

```
length nL
null nL
take 5 nL
drop 5 nL
head [ ]
head nL
tail nL
last nL
init nL
reverse nL
maximum nL
minimum nL
sum nL
product nL
5 `elem` nL
elem 5 nL
```

```
[1..10]
['a'..'l']
[3, 4..12]
take 5 [40, 45..]
take 20 (cycle nL)
take 10 (repeat 5)
replicate 4 10
```

```
[ dsn x | x <- nL, x > 5 ]
beepBop xs = [ if x < 5 then "beep" else "bop" | x <- xs, odd x]
[ x*y | x <- [2,5,10], y <- [8,10,11]]
```
