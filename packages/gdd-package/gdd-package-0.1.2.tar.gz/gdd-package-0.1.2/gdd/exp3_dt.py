import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load dataset
drug = pd.read_csv("drug200.csv")

# Features and target
X = drug.drop('Drug', axis=1)
y = drug['Drug']

# One-hot encoding for categorical variables
X = pd.get_dummies(X, columns=['Sex', 'BP', 'Cholesterol'], drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=42)

# Train model
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, y_train)

# Predict and evaluate
y_pred = dt_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Plot tree
plt.figure(figsize=(20, 10))
plot_tree(dt_classifier, filled=True, feature_names=X_train.columns)
plt.show()
