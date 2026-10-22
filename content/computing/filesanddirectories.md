---
title: Going MAD
date: '2016-05-18T11:59:35+04:00'
lastmod: '2016-05-18T15:11:23+04:00'
original_id: '{A31}'
original_name: filesanddirectories
original_blob: blob/B/200.txt
revisions: 3
author: admin
last_editor: admin
last_summary: change title
tags:
- computing
categories:
- computing
wikislug: filesanddirectories
draft: true
review: update
---

### Going MAD

###### Moving Around Directories

Just like when in the shell, once you have started your picolisp process you
may want to
traverse the directories and get other information. 

This is easy enough to accomplish with just a few functions. 

Notice that all the below functions return either a string or a list of strings.
Strings are otherwise know as **Transient Symbols** in picolisp.

```
(pwd)
-> "/home/vid"
```

So simple! and it tells you your **c**urrent **w**orking **d**irectory, **cwd**.
A good Mnemonic to help you remember
this command is **print working directory**, **pwd**.

```
(dir "dirname" flg)
-> ("myDir" "someFile.txt" "myOtherDir")
```

"dirname" defaults to your **cwd** and you can set
flg to **True** to get hidden files too. 

if you supply a filename instead of a directory you get **NIL**.
This is somewhat true
of all picolisp functions. You mostly get **NIL** results for failures.

```
(cd "/some/new/path")
-> "my/current/directory"
```

you can **cd** into any directory just like in the **shell**. 

The return value is your **cwd** and **NIL** if you
gave a non existing directory.

```
(chdir "dir-path" Prgs)

(chdir ".." (cd "..") (dir))
-> ("Public" "Dropbox" "picoLisp" "News" "wiki" "electric.log" "2016-01-07 10.40.55.jpg" "Documents")
```

If you just want to temporarily move directories and get something done and
restore back to the current directory, use **chdir**. 

In the above examples **Prgs** just means 1 or mores lists.

So the second call, 

**(chdir ".." (cd "..") (dir)** just means, **chdir** backwards, **cd** backwards again,
then list directory **(dir)**, and finally restore back to the cwd.

```
(dirname "some/file")
-> "some/"
(basename "some/file")
-> "file"
```

if you finally got the path to your file, you can get the path and filename with dirname and basname.
