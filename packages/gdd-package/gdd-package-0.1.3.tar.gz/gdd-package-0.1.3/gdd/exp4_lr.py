import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
insta = pd.read_csv("insta.csv")

# Features and target
X = insta[['Instagram visit score']]
y = insta['Spending_rank(0 to 100)']

# Train model
model = LinearRegression()
model.fit(X, y)

print(f"Coefficient: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# Visualization
plt.figure(figsize=(10,6))
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Instagram visit score")
plt.ylabel("Spending Rank")
plt.legend()
plt.show()

# Errors
y_pred = model.predict(X)
print("MAE:", mean_absolute_error(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred)))
