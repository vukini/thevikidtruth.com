---
title: Help
date: '2016-05-09T01:21:24+04:00'
lastmod: '2016-12-07T15:09:54+04:00'
original_id: '{5}'
original_name: help
original_blob: blob/B/4/643.txt
revisions: 27
author: admin
last_editor: admin
tags:
- help
categories:
- help
wikislug: help
draft: false
---

[Please Read This Disclaimer, it is Important!](caveatemptor.md) | [bookstemplate](bookstemplate.md "MISSING PAGE")

## Help

Your best friend on this site is the **search bar** above.

The site is fully indexed, which means that it will find any word (over 3 letters long) which is
relevant to you. Once your on a page, use your browsers 'find in page' function to locate the
item.

**So good luck!**

This Wiki has a very simple syntax. It always starts with a single
character (that specifies the type of markup) followed by an opening brace, and
extends till the matching closing brace.

Currently, the following markup types are supported:

```
   3{Heading}                 Heading (level 3)
                              Levels 1 .. 6 are allowed

   &{3}                       Insert 3 line breaks
   &{-3}                      Insert 3 line breaks, clear float style

   /{italic}                  Italic font
   !{bold}                    Bold font
   _{underline}               Underlined font

   *{                         Unordered list
      -{List item 1}             List items
      -{List item 2}
   }

   +{                         Ordered list
      -{List item 1}             List items
      -{List item 2}
   }

   <{content}                 Left-floating content (e.g. image, video)
   @{content}                 Non-floating content (e.g. image, video)
   >{content}                 Right-floating content (e.g. image, video)

   ={Doc Page}                Internal link to the document "Doc"
                                 The optional label text is "Page"

   ^{http://ext.org Text}     External link to "http://ext.org"
                                 The optional label text is "Text"

   :{code}                    'code' style

   :{                         Pre-formatted text
      formatted
   }

   \{                         Escaped brace

   #{comment}                 Comment
```

[http://thevikidtruth.com/wiki/wiki/public_html/math.html](http://thevikidtruth.com/wiki/wiki/public_html/math.html)
