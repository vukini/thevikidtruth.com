---
title: The Health Application
date: '2017-06-24T07:01:50+04:00'
lastmod: '2017-06-24T07:12:22+04:00'
original_id: '{A1150}'
original_name: pilhealth
original_blob: blob/B/5/731.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pilhealth
draft: true
review: update
topics:
- lisp
---

[Read This!](caveatemptor.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) | [Pil Tutorials](piltutorials.md) |
  [Picolisp By Example](picolispbyexample.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md) | [Networking](networking.md) | [Machine Learning](machinelearning.md) |
  [Git](git.md) |
  [Machine Learning](machinelearning.md) |
  [Algorithms](algorithms.md) |
  [Open Data Science](opendatascience.md) |

# [The Health Application](pilhealth.md)

Health is a small application that I co-wrote with Alexander Burger to help newcomers understand the nuts and bolts of
a very simplified picolisp application.

It uses the standard libraries. Especially [http.l](httpl.md), [xhtml.l](xhtml-l.md "MISSING PAGE") and [form.l](form-l.md "MISSING PAGE")

The app consists of two files,  [health.l](pilhealth.md) and [day.l](pilhealth.md), who's sources are given below.

## Sources

```
# 09may17abu
# (c) Software Lab. Alexander Burger

(allowed ()
   "!work" "@lib.css" "day.l" )

(load "@lib/http.l" "@lib/xhtml.l" "@lib/form.l" "@lib/adm.l")

(class +Day +Entity)
(rel dat (+Key +Date))                 # Date
(rel w (+Number) 3)                    # Weight [kg]

(dm T @
   (pass super 'dat (date)) )

(dm url> ()
   (list "day.l" '*ID This) )

(de choDay (Dst)
   (choDlg Dst "Days" '(dat +Day)
      NIL
      '(pack (datStr (: dat)) ": " (format (: w) 1)) ) )

(de menu (Ttl . Prg)
   (action
      (html 0 Ttl "@lib.css" NIL
         (<ping> 7)
         (<layout>
            ((180 0 'menu)
               (<div> @
                  (expires)
                  (<menu>
                     (,"Home" "!work")
                     ("Day" "day.l") ) )
               ((NIL NIL 'main)
                  (<div> @ (run Prg 1)) ) ) ) ) ) )

(de work ()
   (app)
   (menu "Health"
      (<h2> NIL "Health") ) )

(de main ()
   (pool "health.db") )

(de go ()
   (server 8080 "!work") )

# vi:et:ts=3:sw=3
```

```
# 09may17abu
# (c) Software Lab. Alexander Burger

(menu "Day"
   (idForm "Day" '(choDay) 'dat '+Day T '(may Delete) '((datStr (: dat)))
      (<grid> 2
         "Date" (gui '(+E/R +DateField) '(dat : home obj) 10)
         "Weight" (gui '(+E/R +FixField) '(w : home obj) 3 7) )
      (<spread> NIL (editButton T)) ) )

# vi:et:ts=3:sw=3
```

```

```
