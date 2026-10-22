---
title: Machine Learning
date: '2016-12-01T22:59:57+04:00'
lastmod: '2022-08-03T02:35:08+04:00'
original_id: '{A600}'
original_name: machinelearning
original_blob: blob/B/10/705.txt
revisions: 24
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: machinelearning
draft: false
topics:
- cs-theory
---

[Read This!](caveatemptor.md) |
  [Computing](computing.md) |
  [Picolisp](picolisp.md) | [Picolisp Machine](pilmachine.md) | [Pil Sources](pilsource.md) |
  [Linux](linux.md) | [BASH](bash.md) |
  [C-Programmming](cprogramming.md) | [Javascipt](javascript.md) | [Python](python.md) | [Scheme](scheme.md) |
  [Operating Systems](os.md) | [AssemblyLanguage](assemblylanguage.md) |
  [Computer Security](computersecurity.md) |
  [Firewalls](firewalls.md) |
  [Exploitation](exploitation.md) | [Social Engineering](internetexploitation.md) | [Metasploit](metasploit.md) |
  [Emacs](emacs.md) | [vim](vim.md) |
  [Pharo Smalltalk](pharo.md) |
  [Databases](databases.md) | [Networking](networking.md) | [Machine Learning](machinelearning.md)

# Machine Learning

Here is the truth about machine learning: **it is curve fitting with very good bookkeeping.** You choose a family of functions with adjustable knobs, show it examples, and nudge the knobs until its outputs match the examples. Everything from a spam filter to a large language model is that idea, scaled up.

### What it is, in plain words

Ordinary programming: you write the rules, the computer applies them to data. Machine learning: you give the computer data *and the answers*, and it finds the rules.

The three big families:

1. **Supervised learning** – examples come with labels (this email is spam, this house sold for X). The model learns to predict the label. Regression predicts numbers; classification predicts categories.
2. **Unsupervised learning** – no labels. Find structure: clusters, the main directions of variation (PCA), unusual points.
3. **Reinforcement learning** – an agent acts, gets rewards, and learns a policy that earns more reward.

Since 2017 one architecture, the **transformer**, has taken over language, images, audio and code. Today's large language models are transformers trained first on huge amounts of text to predict the next token (*self-supervised* learning), then tuned with human and AI feedback. But underneath they use exactly the same ingredients as the list below: data as vectors, a model, a loss, and optimisation.

### Why it matters

- It powers search ranking, recommendations, translation, speech recognition, fraud detection, medical imaging and the AI assistants everyone now uses.
- It is **statistics, not magic**. A model only knows the patterns in its training data, including the biases and mistakes. Understanding the basics is how you judge its claims.
- The mathematics is learnable. The outline below (linear algebra, calculus, probability, optimisation) is the whole foundation; nothing else is hidden.

### An everyday analogy: learning to throw darts

Your first throws go everywhere. After each throw you see how far off you were (the **loss**) and adjust your arm a little in the direction that would have helped (the **gradient**). After hundreds of throws you are hitting the board. You never wrote down the physics of darts. Your arm learned a function from "where I aim" to "where it lands". That is gradient descent.

### The core equation

Linear regression is the "hello world" of the field. Given inputs \(x\) and targets \(y\), find weights \(w\) and bias \(b\) so that \(\hat{y} = w x + b\) is close to \(y\). "Close" means minimising the mean squared error:

$$
L(w, b) = \frac{1}{n} \sum_{i=1}^{n} \left( w x_i + b - y_i \right)^2
$$

Gradient descent repeats a small step downhill, with learning rate \(\eta\):

$$
w \leftarrow w - \eta \frac{\partial L}{\partial w}, \qquad b \leftarrow b - \eta \frac{\partial L}{\partial b}
$$

A neural network is the same thing with many layers of weights and a non-linear function between them.

### A hands-on example

Gradient descent from scratch with [NumPy](numpy.md), then the same with scikit-learn:

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.uniform(0, 10, 100)
y = 3 * x + 2 + rng.normal(0, 1, 100)       # true w=3, b=2, plus noise

w, b, eta = 0.0, 0.0, 0.01
for step in range(2000):
    err = w * x + b - y
    w -= eta * 2 * np.mean(err * x)          # dL/dw
    b -= eta * 2 * np.mean(err)              # dL/db
print(f"learned w={w:.2f}, b={b:.2f}")      # close to 3 and 2

from sklearn.linear_model import LinearRegression
m = LinearRegression().fit(x.reshape(-1, 1), y)
print(m.coef_, m.intercept_)
```

Install with `pip install numpy scikit-learn` in a virtual environment (`python -m venv .venv`). For deep learning the standard library in 2026 is **PyTorch**, with JAX as the main alternative. You can follow the same loop by hand even in PicoLisp with fixed-point numbers, which is a good way to prove to yourself there is no magic.

### Common misconceptions

- **"More data always fixes it."** More *bad* or biased data makes a confident wrong model. Quality and coverage matter more than size.
- **"High accuracy means a good model."** If 99% of emails are not spam, a model that always says "not spam" is 99% accurate and useless. Look at precision, recall and the confusion matrix, and always test on data the model has not seen.
- **"The model understands."** It has learned statistical patterns. Sometimes those patterns are deep and useful; it can still be confidently wrong.
- **"ML means neural networks."** For tabular business data, gradient-boosted trees (XGBoost, LightGBM) still often win. Start simple.
- **"You need a GPU to start."** Everything on this page runs on a laptop CPU in seconds.

### Connections

- [Python](python.md), [NumPy](numpy.md), [SciPy](scipy.md), [IPython](ipython.md), [Python spaCy](pythonspacy.md) for language.
- [Linear Algebra](linearalgebra.md), [Vector Spaces](vectorspaces.md), [Linear Operators and Matrices](linearoperators.md), [Inner Product Spaces](innerproductspaces.md), [Tensors](tensors.md).
- [Algorithms](algorithms.md), [Data Structures and Algorithms](datastructuresandalgorithms.md), [Julia](julia.md).

#### Machine learning in a Nutshell:

- **Data**: Raw Environment
- **Model**: Maps input --> Output
- **Learning**: Optimizes Models by finding better parameters to models (patterns).
- **Predictor**: A MLA that is a system that makes predictions
- **We Represent Data as Vectors**
- **Choose a Model**
- **Optimize using numerical methods**

#### The mathematics needed:

- Linear Algebra
- - Systems of Equations
    - Matrices
    - Vector Spaces
    - Linear Mappings
    - Affine Spaces
- Analytic Geometry
- Matrix Decomposition
- Vector Calculus
- Probability Distributions
- Continuous Optimisation
- Models vs Data
- Linear Regression
- Dimensionality
- Principal Component Analysis
- Density Estimation (Gaussian Mixture Models
- Classification with Support Vector Machines

#### Sources, Links and Reading Lists

- [The 100pg ML Book](http://themlbook.com/wiki/doku.php)
- [Python](python.md) --- [SciPy](scipy.md) --- [NumPy](numpy.md)
- [ building-machine-learning-systems-in-python](http://www.twotoreal.com/u/wr/4/building-machine-learning-systems-in-python/
  )
- [Metaoptimize](http://metaoptimize.com)
- [Stack Exchange](http://stats.stackexchange.com)
- [Two To Real](http://www.twotoreal.com)
- [PacktPub](http://PacktPub.com)
- [(Numerical Linear Algebra for Programmers | New Book Chapter Available)](https://aiprobook.com/numerical-linear-algebra-for-programmers/)
- [How Neural Networks Work: 3h50min](https://www.youtube.com/watch?v=dPWYUELwIdM)
- [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA)
- [machine learning and javascript - w3schools](https://www.w3schools.com/ai/ai_javascript.asp)
- [machinelearningjs](http://machinelearningjs.com)
