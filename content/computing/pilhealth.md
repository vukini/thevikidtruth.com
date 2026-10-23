---
title: The Health Application
date: '2017-06-24T07:01:50+04:00'
lastmod: '2026-10-23T12:00:00+04:00'
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
draft: false
topics:
- lisp
---

# [The Health Application](pilhealth.md)

Health is a small application that I co-wrote with Alexander Burger to help newcomers understand the nuts and bolts of a very simple PicoLisp application.

It uses the standard libraries, especially [http.l](httpl.md), `@lib/xhtml.l` and `@lib/form.l`. The app consists of two files, `health.l` and `day.l`, whose sources are given below.

## Sources

### health.l

```picolisp
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

### day.l

```picolisp
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

## Walking through Health
The sources above are the whole application. It is worth reading slowly, because almost every line shows off one idea from PicoLisp's application framework. The code was written in 2017, and I re-ran it unchanged on PicoLisp 26.9 (pil21) in October 2026: current PicoLisp kept the same `@lib/http.l`, `xhtml.l`, `form.l` and `adm.l` libraries.
### The plain idea
Health is a tiny weight diary. Each record is a **Day**: a date and a weight in kilograms. You can create days, edit them, search for them, and delete them, all through a web browser, with the data stored in a PicoLisp database file, `health.db`. There is no separate database server, no template language and no JavaScript framework. The data model, the user interface and the web server are all written in the same Lisp, in about fifty lines.
### Why it matters
Most web frameworks spread one small app across a dozen files and three or four languages. Health shows the opposite extreme: a complete database-backed web app you can hold in your head. That makes it an ideal first study for anyone who wants to understand how PicoLisp applications are put together, before tackling the much bigger demo app ([demoApp.tgz](https://software-lab.de/demoApp.tgz), explained in the [application tutorial](https://software-lab.de/doc/app.html)).
### An everyday analogy: a notebook with a librarian
Think of the database as a notebook where each page is a Day. The `+Day` class is the printed form at the top of each page (date, weight). `choDay` is the librarian you ask "show me all the days", and `day.l` is the page you open to read or correct one entry. The server is simply the shop counter where the librarian waits for you.
### A worked example: reading health.l
- `(allowed () "!work" "@lib.css" "day.l")` is a whitelist. Only these URLs may be requested; anything else is refused. Security by default.
- `(load "@lib/http.l" ...)` pulls in the [HTTP server](httpl.md), HTML generation, the form GUI and the admin helpers.
- `(class +Day +Entity)` defines a persistent class. Objects of an `+Entity` class live in the database.
- `(rel dat (+Key +Date))` declares a relation: `dat` is a date, and `+Key` makes it a unique, indexed key, so you can look days up by date and never get two records for the same day.
- `(rel w (+Number) 3)` declares the weight as a number with three decimal places of fixed-point precision (PicoLisp uses scaled integers rather than floating point, so 72.5 kg is stored as 72500).
- `(dm T @ (pass super 'dat (date)))` is the constructor: a new Day gets today's date by default.
- `(dm url> () ...)` tells the framework which page shows this object, so links to a Day open `day.l`.
- `choDay` builds a search dialogue listing Days, formatted as "date: weight".
- `menu` builds the page layout: a left-hand menu with Home and Day, and a main area where the page body runs.
- `work` is the start page, `main` opens the database file, and `go` starts the server on port 8080.
And `day.l`:
- `idForm` builds a complete edit form for one object: a title, a search button wired to `choDay`, an optional Delete button, and the object's date as the heading.
- `<grid> 2` lays out two columns of labels and fields.
- `(gui '(+E/R +DateField) '(dat : home obj) 10)` is the key idea. `+E/R` (entity/relation) binds the field directly to the `dat` relation of the current object. Edit the field and the database changes; no glue code.
- `editButton` gives the classic PicoLisp edit/done toggle, with record locking so two users cannot change the same Day at once.
To run it, save both files in a directory and start:
```
pil health.l -main -go +
```
then open `http://localhost:8080` in a browser. The `+` turns on debug mode so you get a REPL alongside the running server. Use `pil health.l -main -go -wait` for normal running.

`-main` and `-go` are just function calls from the command line: a leading `-` evaluates `(main)` and `(go)`. The database file `health.db` is created on first use.

### Running it for real in 2026

- Put [httpGate](httpgatec.md) (or another reverse proxy) in front for HTTPS, and add `(retire 20)` before `(server ...)` in `go`, so the app sleeps when nobody is using it.
- For more than one class, split the database into several files with `dbs`; see [PicoLisp DB](pildb.md).
- Back up `health.db` like any other file. Run `(dbck)` in the REPL to check its consistency.
### Common misconceptions
- **"This needs an external database."** PicoLisp has its own object database built in; `pool` opens it.
- **"The GUI must be JavaScript."** The forms are generated on the server and work without client-side scripting. A little optional JavaScript only improves the experience.
- **"Fifty lines means a toy."** The same patterns, `+Entity`, `rel`, `idForm`, `+E/R`, scale up to the real business applications Alexander Burger has built for clients for decades.
### How it connects
- [PicoLisp](picolisp.md), [PicoLisp Sources](pilsource.md), [http.l](httpl.md) and [PicoLisp DB](pildb.md): the language and the server underneath.
- [PicoLisp by Example](picolispbyexample.md) and [PicoLisp Tutorials](piltutorials.md): smaller steps before this one.
- [Databases](databases.md): how a built-in object database compares with SQL.
The truth revealed: you do not need a mountain of tools to build a real application, just a language where data, logic and interface speak the same words.
