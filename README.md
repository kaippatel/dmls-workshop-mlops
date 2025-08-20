# **🐧📦 Dalhousie Machine Learning Society: MLOps Workshop**

Welcome to this **MLOps Workshop** hosted by Kai Patel and Aryan Arya! 🚀

This repository contains materials for learning and experimenting with MLOps.
Throughout the workshop, we'll be walking through important concepts and theory,
up to building a fully version-controlled, experiment-tracked, continuously-integrated ML pipeline.

## **📌 Workshop Overview**

### **Day 1**

- What is MLOps?
- Model Training & EDA
- Versioning with Git & DVC
- Tracking with MLflow
- Branching and PR

### **Day 2**

- Day 1 Recap & Merge PRs
- Containerizing with Docker
- CI with GitHub Actions
- Deployment with Render
- Monitoring & Governance

## **Slides**

https://docs.google.com/presentation/d/1EGb7kbygJQf9-MDvPUXNB1oH7hB9S9iZDhQzms3iTss/edit?usp=sharing

## **📂 Project Structure**

```
dmls-mlops-workshop/
│-- notebook/           # Jupyter notebook for training models and versioning
│-- .gitignore          # Ignore unnecessary or private files
│-- LICENSE.txt         # Open-source MIT license
│-- README.md           # This file (setup instructions)
│-- requirements.txt    # Dependencies for running notebooks (required for local setup)
```

## **🖥️ Prerequisites**

Ensure you have these installed before the workshop:

- **Python ≥ 3.11**  
  Download from [python.org](https://www.python.org/downloads).

- **Git**  
  Download from [git-scm.com](https://git-scm.com/downloads).

- **Docker Desktop**  
  Download from [docker.com](https://docs.docker.com/get-started/get-docker).

After installing, restart your terminal so new commands are available.

## **🛠️ Set‑up**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/kaippatel/dmls-mlops-workshop.git
cd dmls-mlops-workshop
```

### **2️⃣ Setup the Environment**

```bash
# 1.  Create and activate a virtual-env (Python ≥ 3.11)
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -U pip

# 2.  Install core dependencies
python -m pip install -r requirements.txt

# 3.  Register this venv as a Jupyter kernel
python -m pip install ipykernel
python -m ipykernel install --user \
  --name penguins-mlops \
  --display-name "Python (mlops)"
```

### **3️⃣ Pick Your Notebook Frontend (choose one)**

#### **Option A — VS Code (Jupyter extension)**

1. Install the Python and Jupyter extensions.
2. Python: Select Interpreter → choose your project’s `.venv`.
3. Open a `.ipynb` notebook → kernel (top-right corner) → select "Python (mlops)".

#### **Option B — JupyterLab (browser UI)**

```bash
python -m pip install jupyterlab
jupyter lab
# In the UI: Kernel → Change Kernel → "Python (mlops)"
```

### **5️⃣ Open Notebook**

We will begin with `notebook/train_penguins.ipynb`.

---

## **📜 Requirements**

- **Python ≥ 3.11**
- **Git**
- **Docker Desktop**

## **📝 Citations**

1. Batching method for experiment tracking: notebooks/train_penguins.ipynb, cell 22, http://youtube.com/watch?v=6ngxBkx05Fs

## **⚡ Contribution & Feedback**

Pull requests and suggestions are welcome! Feel free to reach out if you encounter any issues.

## **📌 License**

This repository is licensed under the MIT License. Feel free to use and modify as needed.

<p align="start">
  <span style="font-size:2em; font-weight:bold;">Happy shipping! 🚢🐧</span>
</p>
