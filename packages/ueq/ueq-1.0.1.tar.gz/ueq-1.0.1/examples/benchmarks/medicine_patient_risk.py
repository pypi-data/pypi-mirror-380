import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.calibration import calibration_curve

from ueq import UQ


def main():
    # 1. Load medical dataset (Breast Cancer Wisconsin)
    data = load_breast_cancer()
    X, y = data.data, data.target  # 0 = malignant, 1 = benign

    # Train / Calib / Test split
    X_train_full, X_test, y_train_full, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    X_train, X_calib, y_train, y_calib = train_test_split(
        X_train_full, y_train_full, test_size=0.2, random_state=42, stratify=y_train_full
    )

    # 2. Use Conformal UQ with RandomForest
    uq = UQ(
        model=RandomForestClassifier(n_estimators=100, random_state=42),
        method="conformal",
    )
    uq.fit(X_train, y_train, X_calib, y_calib)

    # 3. Predict with intervals (classification: prediction sets)
    pred_labels, pred_sets = uq.predict(X_test, return_interval=True)

    # Coverage: % of true labels inside prediction sets
    coverage_hits = [y_test[i] in pred_sets[i] for i in range(len(y_test))]
    cov = np.mean(coverage_hits)

    # Sharpness: average size of prediction set
    sharp = np.mean([len(s) for s in pred_sets])

    # Calibration error (ECE for classification)
    base_model = RandomForestClassifier(n_estimators=100, random_state=42)
    base_model.fit(X_train, y_train)
    prob = base_model.predict_proba(X_test)[:, 1]
    frac_pos, mean_pred = calibration_curve(y_test, prob, n_bins=10)

    ece = np.mean(np.abs(frac_pos - mean_pred))

    print("🏥 Medicine Benchmark (Breast Cancer Risk Prediction)")
    print(f"Coverage: {cov:.3f}")
    print(f"Sharpness: {sharp:.3f}")
    print(f"ECE: {ece:.3f}")

    # 4. Visualization: Calibration plot
    plt.figure(figsize=(6, 5))
    plt.plot(mean_pred, frac_pos, "o-", label="Calibration curve")
    plt.plot([0, 1], [0, 1], "k--", label="Perfectly calibrated")
    plt.xlabel("Predicted probability")
    plt.ylabel("True frequency")
    plt.title("Calibration: Breast Cancer Risk Prediction")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
