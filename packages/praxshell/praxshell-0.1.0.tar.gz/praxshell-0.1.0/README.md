# Praxshell
![PyPI](https://img.shields.io/pypi/v/praxshell)
![Python](https://img.shields.io/pypi/pyversions/praxshell)
![License](https://img.shields.io/github/license/diputs-sudo/praxshell)

Praxshell is a lightweight Python-powered CLI for learning machine learning concepts.  
It provides explanations, searchable notes, study roadmaps, and interactive notebooks in a shell-like interface.

---

## What is Praxshell?

Praxshell is designed as a **learning shell**.  
It works by combining:

- A **vault** of notes, study roadmaps, and linked notebooks.  
- A set of **commands** for explanations, search, and roadmap navigation.  
- A simple **compiler** that renders Markdown notes into styled HTML with code and plots.

The shell is dependency-free and runs with the Python standard library.  
Rendering notebooks requires only two assets:
- A **vault** (knowledge base), available here: [PraxsVault](https://github.com/diputs-sudo/praxvault)  
- A local copy of `plotly.min.js` for plots  

Both of these are handled automatically by Praxshell on first run.  
No additional dependencies need to be installed.

---

# Installation

Praxshell is published as a Python package. Install it directly:

```bash
pip install praxshell
```
After installation, launch it with:
```bash
praxshell
```

Or clone the repository:

```bash
git clone https://github.com/yourname/praxshell.git
cd praxshell
```
Run the shell:
```bash
python -m praxshell.cli.cli 
```

---

# Commands

## General

- `help` – List commands or get help on a specific one  
- `history` – Show past commands, or clear them  
- `exit` / `quit` – Leave Praxshell  
- `version` – Show the current version  

## Study

- `explain <concept>` – Explain an AI concept (from vault notes)  
- `notebook <concept>` – Open a linked notebook in the browser  
- `search <keywords>` – Search notes by keyword or sentence  
- `roadmap [list|show|next]` – View or step through study roadmaps  

## Vault Management

- `update vault` – Replace your local vault with the latest  
- `update vault merge` – Merge new content without overwriting existing files  

---

# Showcase

Here’s what working with Praxshell looks like:

```bash
$ praxshell
    ____                       __         ____
   / __ \_________ __  _______/ /_  ___  / / /
  / /_/ / ___/ __ `/ |/_/ ___/ __ \/ _ \/ / /
 / ____/ /  / /_/ />  <(__  ) / / /  __/ / /
/_/   /_/   \__,_/_/|_/____/_/ /_/\___/_/_/

+=== Welcome to Praxshell v0.1.0 ===+
Type 'help' to see available commands.

prax > help Transformer
[*] Transformer (concept)
    Category: models
    Description: Transformers are neural architectures based on self-attention, widely used in NLP and beyond.

prax > explain adam 
[*] Explanation for Adam
------------------------
Category: optimizer
Description: Adam (Adaptive Moment Estimation) combines momentum and RMSProp, adjusting learning rates adaptively for each parameter.

Related Concepts
----------------
  - SGD
  - Momentum
Notebook: vault/notes/optimizer/Adam.md

prax > roadmap list
[*] Available Roadmaps:
- ML_Starter → A path through the most essential machine learning fundamentals.
- Optimization_and_Training → Understand how models are trained efficiently.
- Classification → Learn the core models and losses for classification tasks.

prax > roadmap show ML_Starter
[*] Roadmap: ML Starter
Description: A path through the most essential machine learning fundamentals.


Steps
-----
  - LinearAlgebra → Start with the math foundations for machine learning.
  - Calculus → Understand derivatives and gradients, key for optimization.
  - Probability → Learn probability basics for uncertainty in ML.
  - GradientDescent → Study how parameters are optimized using gradients.
  - LinearRegression → Train your first regression model.
  - MSE → Understand Mean Squared Error for regression evaluation.

prax > roadmap next 
[*] Next Step in ML_Starter:
- LinearAlgebra → Start with the math foundations for machine learning.

[*] Explanation for LinearAlgebra
---------------------------------
Category: theory
Description: Linear Algebra provides the building blocks of ML, with vectors, matrices, and operations like dot products and matrix multiplication.

Related Concepts
----------------
  - Calculus
  - GradientDescent
Notebook: vault/notes/theory/LinearAlgebra.md

prax > notebook LinearAlgebra 
[*] Opening notebook for LinearAlgebra...

prax > history all
[*] Command History:
1. help Transformer
2. explain Adam
3. roadmap list
4. roadmap show ML_Starter
5. roadmap next 
6. notebook LinearAlgebra

prax > help explain
[*] explain - Explain an AI concept. Usage: explain <concept>

prax > help Transformer
[*] Transformer (concept)
    Category: models
    Description: Transformers are neural architectures based on self-attention, widely used in NLP and beyond.

prax > search why does gradient descent sometimes get stuck in local minima
[*] Search results for 'why does gradient descent sometimes get stuck in local minima':
- GradientDescent → Gradient Descent is a fundamental optimization algorithm that updates parameters by moving in the direction of the negative gradient of the loss.
- SGD → Stochastic Gradient Descent (SGD) updates parameters using small random batches of data, making it scalable for large datasets.
- Calculus → Calculus underlies optimization with derivatives, gradients, and the chain rule for backpropagation.
- MSE → Mean Squared Error is a loss function used in regression tasks, measuring the squared difference between predictions and targets.
- Momentum → Momentum is an extension of SGD that accumulates past gradients to speed up convergence and smooth oscillations.

...and many more commands available.
```

---

# Requirements

Praxshell is designed to be dependency-free. It only requires:

- **Python 3.9+** 
- **PraxVault** – contains all study notes, roadmaps, and examples  
  - Repository: [https://github.com/diputs-sudo/praxvault](https://github.com/diputs-sudo/praxvault)  
  - Praxshell will download and set this up automatically on first run  
- **plotly.min.js** – used for rendering interactive charts in notebooks  
  - This is also automatically downloaded into the `html/` folder  

No additional Python dependencies are required.  

---

## Contributing
Contributions are welcome! Please open an issue or pull request on GitHub.

---

## License

Praxshell is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

SPDX-License-Identifier: Apache-2.0
