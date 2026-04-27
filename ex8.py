from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# 1. Setup
print("SYSTEM INITIALIZATION...")
n_est = int(input("   > Enter number of estimators: "))
crit = input("   > Enter criterion (gini or entropy): ")

data = load_breast_cancer()
X, y = data.data, (data.target == 0).astype(int)

split_ratios = [0.30, 0.40, 0.25]
split_names = ["70-30", "60-40", "75-25"]
final_results = []

# 2. Detailed Intermediate Steps
for i, ratio in enumerate(split_ratios):
    name = split_names[i]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=ratio, random_state=42)

    rf = RandomForestClassifier(n_estimators=n_est, criterion=crit, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    # Metrics Extraction
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()
    total = tn + fp + fn + tp

    acc = (tp + tn) / total
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0

    # --- INTERMEDIATE STEP: MATRIX + CALCULATIONS ---
    print(f"\nPHASE {i+1}: {name} Configuration")
    print("=" * 60)

    # Visual Confusion Matrix
    print("CONFUSION MATRIX:")
    print(f"{' ':18} | Predicted 0 | Predicted 1 |")
    print("-" * 52)
    print(f"Actual 0 (Neg)    | TN: {tn:<7} | FP: {fp:<7} |")
    print(f"Actual 1 (Pos)    | FN: {fn:<7} | TP: {tp:<7} |")
    print("-" * 52)

    # Calculation Breakdown
    print("\nMETRIC CALCULATIONS:")
    print(f"Accuracy  = (TP + TN) / Total  => ({tp} + {tn}) / {total} = {acc:.4f}")
    print(f"Precision = TP / (TP + FP)     => {tp} / ({tp} + {fp}) = {prec:.4f}")
    print(f"Recall    = TP / (TP + FN)     => {tp} / ({tp} + {fn}) = {rec:.4f}")
    print(f"F1-Score  = 2 * (P * R)/(P + R) => 2 * ({prec:.2f} * {rec:.2f}) / ({prec:.2f} + {rec:.2f}) = {f1:.4f}")
    print("=" * 60)

    final_results.append([name, tp, tn, fp, fn, acc, prec, rec, f1])


print(f"\n{'FINAL OUTPUT':^95}")
print("-" * 95)
header = f"{'Split':<10} | {'TP':<5} | {'TN':<5} | {'FP':<5} | {'FN':<5} | {'Acc':<8} | {'Prec':<8} | {'Rec':<8} | {'F1-Score':<8}"
print(header)
print("-" * 95)

for r in final_results:
    print(f"{r[0]:<10} | {r[1]:<5} | {r[2]:<5} | {r[3]:<5} | {r[4]:<5} | {r[5]:<8.4f} | {r[6]:<8.4f} | {r[7]:<8.4f} | {r[8]:<8.4f}")

print("-" * 95)
