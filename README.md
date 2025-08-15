
# Task 6 — K-Nearest Neighbors (KNN) Classification (Iris)

A clean, minimal, **ready-to-upload** project that implements KNN on the Iris dataset using scikit-learn.  
Covers: normalization, choosing K, accuracy & confusion matrix, and a 2D decision boundary visualization.

> This matches the internship brief: use KNeighborsClassifier, normalize features, try different K values, evaluate with accuracy & confusion matrix, and visualize decision boundaries (as suggested).

---

## 🔧 Tech Stack
- Python 3.9+
- scikit-learn, numpy, pandas, matplotlib

## 📁 Project Structure
```
knn_iris_task6/
├── src/
│   └── knn_iris.py              # main script: trains, tunes K, saves plots & report
├── results/                     # auto-created: accuracies & plots are saved here
├── requirements.txt
└── README.md
```

## ⚙️ Setup
```bash
# 1) Create & activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt
```

## ▶️ Run
```bash
python src/knn_iris.py
```
This will:
- pick the **best K** based on test accuracy (from 1..20),
- print accuracy + classification report,
- save:
  - `results/accuracy_vs_k.png`
  - `results/confusion_matrix.png`
  - `results/decision_boundary_bestk.png` (2D using petal length & width)
  - `results/report.txt` (compact summary)

## 🔍 What to look at
- **Which K is best?** → open `results/accuracy_vs_k.png`
- **Where are mistakes happening?** → see `results/confusion_matrix.png`
- **How KNN draws regions** → `results/decision_boundary_bestk.png`

## 📌 Notes
- **Normalization is critical** for KNN because it relies on distances. We use `StandardScaler` to scale features to mean 0, std 1.
- Decision boundary is shown in **2D (petal length & width)** to keep it intuitive.
- Reproducibility: we use a fixed `random_state` in `train_test_split`.

## 🧪 Quick sanity check (expected)
- Accuracy should be **> 90%** on Iris with a reasonable K.
- Confusion mostly appears between **versicolor** and **virginica** (classes 1 & 2).

## 🧭 GitHub push guide (works even if remote has commits)
```bash
# initialize (only once)
git init
git add .
git commit -m "KNN Iris: Task 6"

# set main branch
git branch -M main

# add remote (change URL to your repo)
git remote add origin https://github.com/<your-username>/<your-repo>.git

# if remote already has commits (e.g., README), pull + rebase to avoid merge commit
git pull --rebase origin main || echo "Skip if branch doesn't exist yet"

# push
git push -u origin main
```

## 🧠 Interview Quickies
- **How does KNN work?** Stores training data; for a query, finds K nearest points (by distance) and does majority vote.
- **Choosing K?** Try odd K (to avoid ties); tune via validation/curve; too small → overfit, too large → underfit.
- **Why normalize?** Distance gets dominated by large-scale features; scaling makes features comparable.
- **Time Complexity?** Training O(1); prediction O(N·D) per sample (naïve), where N=training size, D=features.
- **Pros/Cons?** ✅ Simple, no training time, multi-class ready. ❌ Slow at inference, sensitive to noise/scale.
