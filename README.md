# **🚢 DMLS MLOps Workshop — Titanic Deliverable**

Welcome to the **MLOps Workshop Deliverable**.  
In this project, you will train and deploy a **baseline classifier** on the Titanic dataset, then expose it through a **FastAPI** service and deploy it to **Render**.

---

## **📂 Project Structure**

```bash
├── deliverable/          # All files you need for the certification deliverable
│ └── api/                # FastAPI app
│   └── app.py            # Main FastAPI application (loads MLflow model artifacts)
│   └── artifacts/        # Exported MLflow model directory (copied in step 6 of train_titanic.ipynb)
│   └── requirements.txt  # Dependencies to serve the API
│   └── test_app.py       # Local test script using FastAPI TestClient
│ └── train_titanic.ipynb # Notebook for training/logging your Titanic model
│
├── notebook/             # penguins workshop notebook
├── render.yaml           # Render Blueprint for deploying the API
├── requirements.txt      # Global dependencies (training the model)
└── README.md
```

---

# **🏅 Certification**

Upon **successful completion**, you will be awarded a **Certificate of Achievement** for this workshop.

## **📤 Submission**

When your model is ready, **deploy it to Render** and obtain a reachable Public API URL. \
Submit your API URL using the following 👉 [Airtable](https://airtable.com/appbzvXorTGCwSsy9/pagYPfSy0uxXrdsUL/form)

## **⏳ Timeline**

You have **1 week** to complete this deliverable. \
Submissions to the `Airtable` will be available until **August 30, 2025 @11:59 PM**

---

# **🚀 Getting Started**

## **1️⃣ Clone or Fork the Repo**

- If you already forked before the `cert/deliverable` branch was created, update your fork:

```bash
git remote add upstream https://github.com/kaippatel/dmls-workshop-mlops.git
git fetch upstream
git checkout -b cert/deliverable upstream/cert/deliverable
git push origin cert/deliverable
```

- If you fork now, you’ll already have the cert/deliverable branch.

> **Work only on cert/deliverable branch for this certificate task.**

## **2️⃣ Setup the Environment**

### **Run this from the root**

```bash
# 1.  Create and activate a virtual-env (Python ≥ 3.11)
python -m venv .venv               # Mac use python3 for all python commands
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -U pip

# 2.  Install core dependencies
python -m pip install -r requirements.txt

# 3.  Register this venv as a Jupyter kernel
python -m pip install ipykernel
python -m ipykernel install --user --name penguins-mlops --display-name "Python (mlops)"
```

## **3️⃣ Pick Your Notebook Frontend (choose one)**

### **Option A — VS Code (Jupyter extension)**

1. Install the Python and Jupyter extensions.
2. Python: Select Interpreter → choose your project’s `.venv`.
3. Open a `.ipynb` notebook → kernel (top-right corner) → select "Python (mlops)".

### **Option B — JupyterLab (browser UI)**

```bash
python -m pip install jupyterlab
jupyter lab
# In the UI: Kernel → Change Kernel → "Python (mlops)"
```

---

## **4️⃣ Open `deliverable/train_titanic.ipynb` to start the deliverable**

This notebook will guide you through all steps of training, testing and deploying.
