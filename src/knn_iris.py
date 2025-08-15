
# KNN on Iris — trains, tunes K, saves plots & report
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -------- Settings --------
TEST_SIZE = 0.2
RANDOM_STATE = 42
K_RANGE = range(1, 21)
FEATURES_FOR_2D = [2, 3]  # petal length, petal width

# -------- Load data --------
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# -------- Scale features --------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------- Train/test split --------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)

# -------- Tune K --------
accuracies = []
for k in K_RANGE:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

best_k = int(K_RANGE[np.argmax(accuracies)])

# -------- Train final model with best K --------
final_clf = KNeighborsClassifier(n_neighbors=best_k)
final_clf.fit(X_train, y_train)
y_pred_final = final_clf.predict(X_test)
final_acc = accuracy_score(y_test, y_pred_final)
cm = confusion_matrix(y_test, y_pred_final)

# -------- Save accuracy vs K plot --------
plt.figure(figsize=(6, 4))
plt.plot(list(K_RANGE), accuracies, marker='o')
plt.title('Accuracy vs K (Iris)')
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('../results/accuracy_vs_k.png', dpi=150)
plt.close()

# -------- Save confusion matrix plot --------
fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(cm, interpolation='nearest')
ax.figure.colorbar(im, ax=ax)
ax.set(xticks=np.arange(cm.shape[1]), yticks=np.arange(cm.shape[0]))
ax.set_xticklabels(target_names)
ax.set_yticklabels(target_names)
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
ax.set_title('Confusion Matrix (KNN, best K={})'.format(best_k))

# annotate cells
thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, format(cm[i, j], 'd'),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "black")
fig.tight_layout()
fig.savefig('../results/confusion_matrix.png', dpi=150)
plt.close(fig)

# -------- Decision boundary (2D) --------
def plot_decision_boundary_2d(X_scaled_all, y_all, k, feature_idx=(2, 3), path='../results/decision_boundary_bestk.png'):
    # Use only two features
    X2d = X_scaled_all[:, list(feature_idx)]
    # Split similarly (stratify for consistent distribution)
    X_train2d, X_test2d, y_train2d, y_test2d = train_test_split(
        X2d, y_all, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y_all
    )
    # Train KNN on 2D features
    clf2d = KNeighborsClassifier(n_neighbors=k)
    clf2d.fit(X_train2d, y_train2d)

    # Create mesh
    x_min, x_max = X2d[:, 0].min() - 0.5, X2d[:, 0].max() + 0.5
    y_min, y_max = X2d[:, 1].min() - 0.5, X2d[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                         np.linspace(y_min, y_max, 300))
    grid = np.c_[xx.ravel(), yy.ravel()]
    Z = clf2d.predict(grid).reshape(xx.shape)

    # Plot
    plt.figure(figsize=(6, 5))
    plt.contourf(xx, yy, Z, alpha=0.3)
    # Plot train and test points
    plt.scatter(X_train2d[:, 0], X_train2d[:, 1], s=20, label='train', alpha=0.8)
    plt.scatter(X_test2d[:, 0], X_test2d[:, 1], s=30, marker='^', label='test', alpha=0.9)
    plt.title('Decision Boundary (features: petal length & width), K={}'.format(k))
    plt.xlabel('Feature {} (scaled)'.format(feature_idx[0]))
    plt.ylabel('Feature {} (scaled)'.format(feature_idx[1]))
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()

plot_decision_boundary_2d(X_scaled, y, best_k)

# -------- Save text report --------
report_lines = []
report_lines.append("Best K: {}".format(best_k))
report_lines.append("Test Accuracy (best K): {:.4f}".format(final_acc))
report_lines.append("Confusion Matrix (rows=actual, cols=pred):")
report_lines.append(np.array2string(cm))
report_lines.append("Classification Report:")
report_lines.append(classification_report(y_test, y_pred_final, target_names=target_names))

with open('../results/report.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(report_lines))

print("\\n".join(report_lines))
print("\\nSaved figures to ../results and report to ../results/report.txt")
# -------- End of script --------