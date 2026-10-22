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
topics:
- javascript
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |
[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) |

# Node Js

Here is the truth about Node.js: **it is JavaScript let out of the browser, with one big idea attached: never wait.** Instead of a thread per connection that sits idle while the disk or network responds, Node runs your code on one thread and an *event loop* that picks up each result the moment it is ready.

### What it is, in plain words

Node.js, created by Ryan Dahl in 2009, is a **runtime**: Google's V8 JavaScript engine plus **libuv**, a C library for asynchronous file, network and timer I/O, plus a standard library (`node:fs`, `node:http`, `node:crypto` and so on). It comes with **npm**, the package manager and the largest package registry in the world.

Release rhythm: a new major every April and October; **even-numbered majors become Long Term Support** (LTS). In late 2026 that means Node 24 as the established LTS and Node 26 taking over as the newest LTS line; Node 20 reached end of life in April 2026. Recent Node gives you a lot built in that used to need packages:

- `fetch`, `WebSocket` and Web Streams, the same APIs as the browser;
- a test runner (`node --test`) and watch mode (`node --watch`);
- `node --run script` to run `package.json` scripts quickly;
- running TypeScript files directly by stripping types (`node app.ts` for erasable syntax);
- a permission model (`--permission`) to limit file and network access.

Its competitors **Deno** and **Bun** are worth knowing about too; both run most Node code now.

### Why it matters

- **One language front and back.** The same JavaScript on the server, in the browser and in build tools (Vite, esbuild, Three.js projects).
- **Very good at I/O.** Chat servers, APIs, proxies and anything spending most of its time waiting on networks are Node's sweet spot.
- **The tooling layer of the web.** Even if your site is Hugo, like this one, the search index here is built with an `npx` command.

### An everyday analogy: one waiter, many tables

A traditional server hires one waiter per table, and most of them stand around while the kitchen cooks. Node has one very fast waiter. He takes an order, hands it to the kitchen (libuv), and goes straight to the next table. When a dish is ready, the kitchen rings a bell (an event) and he delivers it. One waiter, hundreds of tables, as long as nobody asks him to cook a ten-hour stew himself (CPU-heavy work, which belongs in `worker_threads` or another process).

### A hands-on example

Install on Vikix with `sudo xbps-install -S nodejs` (it includes npm), or use a version manager like `fnm` or `nvm` if you need several versions. Then a modern server, using ES modules:

```js
// server.mjs  -  run: node --watch server.mjs
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';

const server = createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Hello from Vikix\n');
  } else if (req.url === '/os') {
    const release = await readFile('/proc/sys/kernel/osrelease', 'utf8');
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ kernel: release.trim(), node: process.version }));
  } else {
    res.writeHead(404).end('Not found\n');
  }
});

server.listen(3000, '127.0.0.1', () => console.log('http://127.0.0.1:3000/'));
```

```bash
curl -s localhost:3000/os
# {"kernel":"6.12.10_1","node":"v24.x.x"}
```

Note the server sample further down this page sets `res.status = 200`, which does nothing. The property is `res.statusCode`, or use `res.writeHead(200, headers)` as here.

And a test, with no packages at all:

```js
// sum.test.mjs  -  run: node --test
import { test } from 'node:test';
import assert from 'node:assert/strict';
test('adds', () => assert.equal(1 + 2, 3));
```

### Common misconceptions

- **"Node is single-threaded, so it uses one core."** Your JavaScript runs on one thread, but libuv uses a thread pool for file and crypto work, and `worker_threads` or the `cluster` module use more cores.
- **"`npm install` is safe."** Packages can run install scripts. Check what you add, prefer well-maintained packages, use `npm audit`, and commit your lockfile.
- **"`require` is the way to import."** CommonJS still works, but ES modules (`import`) are the standard in 2026, and Node can now `require()` ES modules too.
- **"You need Express for a web server."** `node:http` is fine for small things; frameworks such as Fastify, Hono or Express help with routing at scale.
- **"Node and the browser are the same JavaScript."** Same language, different globals: no `document` in Node, no `fs` in the browser.

### Connections

- [JavaScript Data Types](jsdatatypes.md), [JavaScript Control Flow](jscontrolflow.md), [JS Functions](jsfunctions.md), [JS Events](jsevents.md).
- [Three.js](jsthree.md), [Web Development](webdevelopment.md), [Application Development](appdev.md).
- [Online VPS](onlinevps.md) and [Using Linode](linode.md) – where Node apps usually end up running.
- [PicoLisp](picolisp.md) – its HTTP server takes the opposite approach, a forked process per session, and is worth comparing.

## Notes


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
