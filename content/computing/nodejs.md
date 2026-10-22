---
title: Node Js
date: '2016-12-11T00:02:18+04:00'
lastmod: '2023-04-11T04:15:24+04:00'
original_id: '{A1033}'
original_name: nodejs
original_blob: blob/B/12/164.txt
revisions: 15
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: nodejs
draft: false
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Node Js

[Official Node Documentation](https://nodejs.dev/en/learn/)
**On older Ubuntu releases the command was `nodejs`, not `node`:**

```
ln -s /usr/bin/nodejs /usr/bin/node
```

[Mixu's Node Book](http://book.mixu.net/node/single.html)

## Install NVM Manjaro Linux

Use Node Version Manager, NVM.

```
sudo pacman -S nvm

nvm install --lts
npm install "package name"
nvm uninstall --lts
```

## Getting Started npm

```
npm install <package-name>
```

flags:

```
 --save-dev        saves to devDependencies
 --no-save         saves to Dependencies
 --save-optional   saves to optionalDependencies
 --no-optional

 -S --save
 -D --save-ve
 -O --save-optional
```

```
npm update
```

```
npm update <package-name>
```

```
npm install <package-name>@<version>
```

## Running Tasks

```
npm run <task-name>

{
    "scripts":{
        "start-dev": "node lib/server-development"
        "start": "node lib/server-production"
    }
}
npm run start-dev
```

How do I find which version of V8 ships with a particular version of Node.js?

```
node -p process.versions.v8
```

## http Server Sample

```
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.status = 200;
  res.setHeader('Content-Type','text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

## Development, Production Environment

```
{
    "scripts":{
        "start-dev": "node lib/server-development"
        "start": "node lib/server-production"
    }
}
```

```
in bash:

export NODE_ENV=production
NODE_ENV=production node app.js

if (process.env.NODE_ENV === 'development'){
  app.use(express.errorHandler({ dumpExecptions: true, showStack: true }));
}

if (process.env.NODE_ENV === 'production'){
  app.use(express.errorHandler());
}

if (['production', 'staging'].includes(process.env.NODE_ENV)){
  //
}
```
