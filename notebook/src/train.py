
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

DATA_PATH = "data/penguins.csv"
MODEL_OUT = "models/baseline_model.pkl"

def main():
    df = pd.read_csv(DATA_PATH).dropna(subset=["species"])
    y = df["species"]
    X = df.drop(columns=["species"])

    num_cols = ["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]
    pre = ColumnTransformer([("num", SimpleImputer(strategy="median"), num_cols)], remainder="drop")

    pipe = Pipeline([("pre", pre), ("clf", RandomForestClassifier(n_estimators=200, random_state=42))])

    idx = np.arange(len(df))
    rng = np.random.default_rng(42); rng.shuffle(idx)
    cut = int(0.8 * len(df)); tr, va = idx[:cut], idx[cut:]

    pipe.fit(X.iloc[tr], y.iloc[tr])
    acc = accuracy_score(y.iloc[va], pipe.predict(X.iloc[va]))

    Path("models").mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": pipe, "val_accuracy": float(acc)}, MODEL_OUT)
    print(f"Saved {MODEL_OUT} | val_accuracy={acc:.4f}")

if __name__ == "__main__":
    main()
