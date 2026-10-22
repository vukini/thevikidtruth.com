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
draft: true
review: update
---

[Javascript](javascript.md) | [Javascript kata](jskata.md) |[Node JS](nodejs.md) | [Data Types](jsdatatypes.md) | [Variables](jsvariable.md) | [Control Flow](jscontrolflow.md) |
[Scope and Environment](jsscope.md) | [Objects](jsobjects.md) | [Functions](jsfunctions.md) | [Events](jsevents.md) |
[Prototypal Inheritance](jsprototypalinheritance.md) |

[Three.js](jsthree.md) | [3DE Code Editor](https://www.code3dgames.com/3de/) | [Making Shapes](js3makingshapes.md)

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
