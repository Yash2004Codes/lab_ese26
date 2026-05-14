import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# 1. CUSTOM DATASET (4 Features)
# Features: [Hours_Studied, Attendance, Internal_Marks, Mock_Test_Score]
data = {
    'Hours': [1, 2, 3, 8, 9, 10, 5, 6, 2, 9],
    'Attendance': [40, 45, 38, 90, 95, 92, 60, 70, 42, 88],
    'Internals': [10, 12, 11, 28, 30, 29, 20, 22, 15, 27],
    'Mock_Score': [30, 35, 32, 85, 90, 88, 55, 60, 40, 82],
    'Passed': [0, 0, 0, 1, 1, 1, 0, 1, 0, 1] # Labels (needed for LDA)
}
df = pd.DataFrame(data)
X = df.drop('Passed', axis=1)
y = df['Passed']

# 2. STANDARDIZATION (CRITICAL for PCA/LDA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- A. PCA (Unsupervised) ---
# Reduces 4 features to 2 Principal Components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("--- PCA RESULTS ---")
print(f"Original Shape: {X_scaled.shape}")
print(f"Reduced Shape: {X_pca.shape}")
print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}") 
# Sum of ratios tells you how much info you kept (e.g., 0.95 = 95%)

# --- B. LDA (Supervised) ---
# Maximizes class separation. Components = (classes - 1), so for 2 classes, n=1
lda = LDA(n_components=1)
X_lda = lda.fit_transform(X_scaled, y)

print("\n--- LDA RESULTS ---")
print(f"Reduced Shape: {X_lda.shape}")
print(f"Explained Variance Ratio: {lda.explained_variance_ratio_}")

# --- C. SVD (Matrix Factorization) ---
# Often used for sparse data or image compression
svd = TruncatedSVD(n_components=2)
X_svd = svd.fit_transform(X_scaled)

print("\n--- SVD RESULTS ---")
print(f"SVD Components (Singular Values):\n{svd.singular_values_}")

# 3. LOGICAL DATA CHECK
print("\nFirst 2 rows of PCA-reduced data:")
print(X_pca[:2])