import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. SIMPLE CUSTOM DATASET
# [Study_Hours, Marks]
data = [
    [1, 20], [2, 25], [1.5, 22],    # Group 0: Low Effort, Low Marks
    [9, 95], [10, 90], [9.5, 92],   # Group 1: High Effort, High Marks
    [9, 30], [10, 35], [9.5, 32],   # Group 2: High Effort, Low Marks (Inefficient)
    [1, 85], [2, 88], [1.5, 82]     # Group 3: Low Effort, High Marks (Gifted)
]

df = pd.DataFrame(data, columns=['Hours', 'Marks'])

# 2. PREPROCESSING
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# 3. K-MEANS 
km = KMeans(n_clusters=4, random_state=42, n_init=10)
df['KMeans_Labels'] = km.fit_predict(X_scaled)

# 4. EM (Gaussian Mixture)
em = GaussianMixture(n_components=4, random_state=42)
em.fit(X_scaled)
df['EM_Labels'] = em.predict(X_scaled)
probs = em.predict_proba(X_scaled)

# 5. PRINTING LOGICAL OUTPUTS
print("--- CLUSTERING RESULTS ---")
print(df.sort_values(by='KMeans_Labels'))

print("\n--- KEY METRICS ---")
# Inertia: Lower is better (K-Means specific)
print(f"K-Means Inertia: {km.inertia_:.2f}")

# Silhouette Score: Closer to 1 is better (Valid for both)
print(f"K-Means Silhouette Score: {silhouette_score(X_scaled, km.labels_):.2f}")
print(f"EM Silhouette Score: {silhouette_score(X_scaled, df['EM_Labels']):.2f}")

# EM Specific Metric
print(f"EM Convergence Status: {em.converged_}")

print("\n--- EM SOFT PROBABILITIES (Example for first 2 rows) ---")
# This proves EM is 'Soft Clustering'
print(probs[:2].round(3))