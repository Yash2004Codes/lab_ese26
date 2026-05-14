import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report

# 1. LOAD DATA (Use a simple built-in dataset for speed)
# from sklearn.datasets import load_iris, load_diabetes
# data = load_iris() # Use load_diabetes() for Linear Regression
# X, y = data.data, data.target
# manually data creation
# Define custom data

# use this for classification models
data_dict = {
    'Hours_Studied': [2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Attendance_Pct': [60, 65, 70, 75, 80, 85, 90, 95, 100],
    'Sleep_Hours': [5, 6, 5, 7, 6, 8, 7, 9, 8],
    'Pass_Exam': [0, 0, 0, 0, 1, 1, 1, 0, 0]  # 0 = Fail, 1 = Pass (Target)
}
# use this for linear regression
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Attendance': [40, 45, 50, 60, 70, 75, 80, 85, 90, 95],
    'Marks': [35, 42, 48, 55, 66, 72, 78, 85, 92, 98]  # Continuous Target
}

df = pd.DataFrame(data_dict)

# Separate Features (X) and Target (y)
X = df[['Hours_Studied', 'Attendance_Pct', 'Sleep_Hours']]
y = df['Pass_Exam']

print("Custom Dataset Created:")
print(df.head())

# 2. PREPROCESS
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling is CRITICAL for KNN, SVM, and Logistic Regression
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. THE MODEL (Swap this block based on your exam question)
# ---------------------------------------------------------
#from sklearn.linear_model import LogisticRegression model = LogisticRegression() 


# Swapping options:
# logistic: from sklearn.linear_model import LogisticRegression 
# SVM: from sklearn.svm import SVC; model = SVC()
#from sklearn.neighbors import KNeighborsClassifier; model = KNeighborsClassifier(n_neighbors=5)
# DT:  from sklearn.tree import DecisionTreeClassifier; model = DecisionTreeClassifier()
# RF:  from sklearn.ensemble import RandomForestClassifier; model = RandomForestClassifier()
# XGB: from xgboost import XGBClassifier; model = XGBClassifier()
# ---------------------------------------------------------

# 4. TRAIN
#model.fit(X_train, y_train)

# 5. EVALUATE
#y_pred = model.predict(X_test)

#print(f"Model: {type(model).__name__}")
#print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
#print(classification_report(y_test, y_pred))

# Notes
#Case A: Classification (Logistic, SVM, KNN, RF, XGB, DT)Target ($y$): Discrete categories (0 or 1, "Red" or "Blue").Metric: accuracy_score, classification_report, confusion_matrix.Case B: Regression (Linear Regression)Target ($y$): Continuous numbers (e.g., Student Marks: 75.5, 82.0, 91.0).Metric: mean_squared_error (MSE) or $R^2$ Score.
#print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")

######################### FOR EM USE THIS 
data = [
    # Group 1: Low Effort, Low Marks
    [1, 20], [2, 25], [1.5, 22],
    # Group 2: High Effort, High Marks
    [9, 95], [10, 90], [9.5, 92],
    # Group 3: High Effort, Low Marks (Inefficient)
    [9, 30], [10, 35], [9.5, 32],
    # Group 4: Low Effort, High Marks (Gifted)
    [1, 85], [2, 88], [1.5, 82]
]

df = pd.DataFrame(data, columns=['Study_Hours', 'Marks'])

# --- Standard EM Workflow ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Model
from sklearn.mixture import GaussianMixture 
model = GaussianMixture(n_components=2, random_state=42)
model.fit(X_scaled)

# 4. ASSIGN CLUSTERS
labels = model.predict(X_scaled)

# 5. RESULTS
df['Cluster_Assigned'] = labels
print(df)

# Special EM Output: Probabilities
# Shows how "sure" the model is that a point belongs to a cluster
probs = model.predict_proba(X_scaled)
print("\nProbabilities for each cluster:\n", probs.round(3))

# interpreation 
# [0. , 1.]: The model is saying: "There is a 0% chance this student belongs to Cluster 0, and a 100% chance they belong to Cluster 1."


#####  K MEANS K-Means uses Euclidean Distance.

from sklearn.cluster import KMeans

# 1. Initialize (k=4 clusters)
model = KMeans(n_components=4, random_state=42) # Note: some versions use 'n_clusters'

# 2. Fit and Predict in one go
df['Cluster'] = model.fit_predict(X_scaled)

# 3. Check the "Centers" (The average student in each group)
print(model.cluster_centers_)
