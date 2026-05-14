import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# 1. CUSTOM DATASET
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.5, 8.5, 4.5, 2.5],
    'Attendance': [40, 45, 50, 55, 75, 80, 85, 90, 95, 100, 35, 88, 60, 48],
    'Passed': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
}
df = pd.DataFrame(data)
X, y = df[['Hours', 'Attendance']], df['Passed']

# 2. PREPROCESS
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------------------------------------------------
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()

# from sklearn.svm import SVC
# model = SVC(kernel='linear')

# from sklearn.neighbors import KNeighborsClassifier
# model = KNeighborsClassifier(n_neighbors=3)

# from sklearn.tree import DecisionTreeClassifier
# model = DecisionTreeClassifier(max_depth=3)

# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=100)

#from xgboost import XGBClassifier
#model = XGBClassifier()

# from sklearn.ensemble import AdaBoostClassifier
# model = AdaBoostClassifier(n_estimators=50, learning_rate=1.0)

# from catboost import CatBoostClassifier
# model = CatBoostClassifier(iterations=100, learning_rate=0.1, verbose=0)

# -------------------------------------------------------------------

# 4. TRAIN AND EVALUATE
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Model Used: {type(model).__name__}")
print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.2f}")
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred))