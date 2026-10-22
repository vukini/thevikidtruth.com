---
title: Python spaCy NLP Library
date: '2023-03-31T14:47:25+04:00'
lastmod: '2023-03-31T15:01:30+04:00'
original_id: '{A1743}'
original_name: pythonspacy
original_blob: blob/B/11/665.txt
revisions: 4
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: pythonspacy
draft: false
---

[Python Libraries, tools and Links](pythonlibrariestoolsandlinks.md) | [Official Python Docs](https://docs.python.org/3/)
| [Intro to Pygame](intropygame.md) | [spaCy](pythonspacy.md)

# Python spaCy NLP Library

[Official spaCy page](https://spacy.io/)

```
  pip install spacy
```

```
  python -m spacy info
```

```
  pip install -U spacy
```

```
  python -m spacy download en
```

```
  python -m spacy download en_core_web_md
```

```
import spacy
nlp = spacy.load('en_core_web_md')
doc = nlp(u'I am learning to program NLP in Spacy. It\'s so amazing.')
print([w.text for w in doc])

for token in doc:
  print(token.text, token.lemma_)
```
