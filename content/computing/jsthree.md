---
title: Three.js
date: '2023-04-02T01:54:13+04:00'
lastmod: '2023-04-11T04:16:59+04:00'
original_id: '{A1751}'
original_name: jsthree
original_blob: blob/B/12/175.txt
revisions: 14
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: jsthree
draft: false
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |

[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) | [Making Shapes](js3makingshapes.md)

# Three.js

[Making Shapes](js3makingshapes.md)

#### Getting Started

[Three.js Official Docs](https://threejs.org/docs/index.html#manual/en/introduction/Creating-a-scene)
 [Installation](https://threejs.org/docs/#manual/en/introduction/Installation)

```
======================================================================================================
Install
======================================================================================================
npm install --save three

npm install --save-dev vite

npx vite

http://localhost:5173
```

[vitejs](https://vitejs.dev/guide/#command-line-interface), [using npm](https://docs.npmjs.com/cli/v9/using-npm/scripts),
[threejs server video](https://threejs-journey.com/lessons/local-server),
[Package management basics](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Package_management)

Files, Code

```
======================================================================================================
index.html
======================================================================================================
<!DOCTYPE html>
<html>
	<head lang="en">
		<meta charset="utf-8">
		<title>My first three.js app</title>
		<style>
			body { margin: 0; }
		</style>
	</head>
	<body>
		<script type="module" src="/main.js"></script>
	</body>
</html>
```

```
======================================================================================================
main.js
======================================================================================================

import * as THREE from 'three';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const geometry = new THREE.BoxGeometry( 1, 1, 1 );
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 5;
function animate() {
	requestAnimationFrame( animate );

	cube.rotation.x += 0.01;
	cube.rotation.y += 0.01;

	renderer.render( scene, camera );
}
animate();
```

to be continued...
