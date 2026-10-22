---
title: 'Three.js: making Shapes'
date: '2023-04-02T02:01:56+04:00'
lastmod: '2023-04-11T04:17:34+04:00'
original_id: '{A1752}'
original_name: js3makingshapes
original_blob: blob/B/12/176.txt
revisions: 20
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: js3makingshapes
draft: false
topics:
- javascript
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |

[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) | [Making Shapes](js3makingshapes.md)


### The plain idea

[Three.js](jsthree.md) is a [JavaScript](javascript.md) library that makes 3D graphics in the browser approachable. Raw WebGL (the browser's 3D interface) is powerful but punishingly low-level; Three.js wraps it in friendly objects, a *scene* to hold things, *meshes* (a shape plus a surface) to put in it, *lights* to see them by, and a *camera* to view from, then a *renderer* draws the result onto the page. This page is a hands-on kata: copy the code, run it, and build the muscle memory for the four pieces every 3D program needs.

### The four ingredients

Every Three.js sketch, including the one below, is built from the same cast:

1. **Scene** – the stage that holds everything.
2. **Camera** – the eye; where you look from and how wide your view is.
3. **Geometry + Material = Mesh** – the shape (a sphere, a box) wrapped in a surface (its colour and how it responds to light).
4. **Renderer** – the artist that draws the scene from the camera's viewpoint onto a canvas.

### An everyday analogy

It is exactly like setting up a photograph of toy models. You arrange objects on a table (the scene), you make each model by taking a shape and painting it (geometry + material = mesh), you switch on a lamp (light), and you decide where to stand and how much to frame (camera). Press the shutter and you get a picture (render).

### A 2026 note on the code

The snippets below still teach the right ideas, but Three.js has moved on since they were written, so two things to know when you run them today:

- Load the library as a **module** from a current source, e.g. `import * as THREE from 'three';` via an import-map or a CDN like `https://unpkg.com/three`, rather than a local `/three.js` file.
- **`MeshBasicMaterial` ignores light** (it always shows its flat colour), so the `AmbientLight` here has no visible effect on it. To actually see lighting, use `MeshStandardMaterial` or `MeshPhongMaterial`. The modern geometry classes (`SphereGeometry`, `BoxGeometry`) still work; the old generic `THREE.Geometry` was removed in favour of `BufferGeometry`, which these now use under the hood.

With those tweaks the kata is as useful as ever: repetition until the four ingredients come without thinking.


# Three.js: making Shapes

Use [code3games](https://www.code3dgames.com/3de/) for a quick online editor. Copy the text into your editor as many times
as you need till it comes to you as second nature.

```
<body></body>
<script src="/three.js"></script>
<script>
  //
  var scene = new THREE.Scene();
  var flat = {flatShading: true};
  var light = new THREE.AmbientLight('white', 0.8);
  scene.add(light);

  //
  var aspectRatio = window.innerWidth / window.innerHeight;
  var camera = new THREE.PerspectiveCamera(75, aspectRatio, 1, 10000);
  camera.position.z = 500;
  scene.add(camera);

  //
  var renderer = new THREE.WebGLRenderer({antialias: true});
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  var geometry = new THREE.SphereGeometry(100, 30 , 30);
  var material = new THREE.MeshBasicMaterial(flat);
  var ball = new THREE.Mesh(geometry, material);
  scene.add(ball);

  var geometry = new THREE.BoxGeometry(200, 300 , 30)
  var material = new THREE.MeshBasicMaterial(flat);
  var cube = new THREE.Mesh(geometry, material);
  cube.rotation.set(3.14/4,3.14/4,3.14/4);
  cube.position.set(50,0,0);
  scene.add(cube);

  renderer.render(scene, camera);

</script>
```

```
  // The "camera" is what sees the stuff:
  var aspectRatio = window.innerWidth / window.innerHeight;
  var camera = new THREE.PerspectiveCamera(75, aspectRatio, 1, 10000);
  camera.position.z = 500;
  scene.add(camera);

  // The "renderer" draws what the camera sees onto the screen:
  var renderer = new THREE.WebGLRenderer({antialias: true});
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  // ******** START CODING ON THE NEXT LINE ********

var body = new THREE.SphereGeometry(100);
var cover = new THREE.MeshNormalMaterial();
var avatar = new THREE.Mesh(body, cover)
scene.add(avatar);

var hand = new THREE.SphereGeometry(50);

var rightHand = new THREE.Mesh(hand, cover);
rightHand.position.set(-130,0,0);
avatar.add(rightHand);

var leftHand = new THREE.Mesh(hand, cover);
leftHand.position.set(+130,0,0);
avatar.add(leftHand);

var foot = new THREE.SphereGeometry(50);

var leftFoot = new THREE.Mesh(foot, cover);
leftFoot.position.set(-75,-125,0);
avatar.add(leftFoot);

var rightFoot = new THREE.Mesh(foot, cover);
rightFoot.position.set(+75,-125,0);
avatar.add(rightFoot);

var isCartwheeling = true;
var rotx = 0
var roty = 0
var rotz = 0
function animate(){
  requestAnimationFrame(animate)
  if (isCartwheeling) {
    rotx += 0.00
    roty += 0.01
    rotz += 0.00
    avatar.rotation.set(rotx,roty,rotz);
  }
  renderer.render(scene, camera)
}
animate()
  // Now, show what the camera sees on the screen:
  renderer.render(scene, camera);
</script>
```

## Constructors

```
SphereGeometry(radius, widthSegments, heightSegments,
               phiStart, phiLength,
               thetaStart, thetaLength)

radius: Float —  Default is 1.

widthSegments : Integer —  Minimum 3, default 32.
heightSegments : Integer —  Minimum 2, default 16.

phiStart : Float —  horizontal starting angle. Default is 0.
phiLength : Float — horizontal sweep angle size. Default is Math.PI * 2.

thetaStart : Float — specify vertical starting angle. Default is 0.
thetaLength : Float — specify vertical sweep angle size. Default is Math.PI.
```

```
BoxGeometry(width, height, depth, widthSegments, heightSegments, depthSegments)

width : Float
height : Float
depth : Float

widthSegments : Integer
heightSegments : Integer
depthSegments : Integer
```

```
MeshNormalMaterial( parameters : Object )

Parameters Properties

.bumpMap :           Texture

.bumpScale :         Float

.displacementMap :   Texture

.displacementScale : Float

.displacementBias :  Float

.flatShading :       Boolean - Default is false.

.fog :               Boolean - Default is false.

.normalMap :         Texture

.normalMapType :     Integer: The type of normal map.

                     Options are THREE.TangentSpaceNormalMap (default)
                                 THREE.ObjectSpaceNormalMap.

.normalScale :       Vector2
                     How much the normal map affects the material. Typical ranges are 0-1.
                     Default is a Vector2 set to (1,1).

.wireframe :         Boolean Default is false

.wireframeLinewidth : Float Default is 1.
```
