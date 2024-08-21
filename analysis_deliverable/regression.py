import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('../final_final_csv.csv')

df.dropna(subset=['Average Value', 'Violent Total Rate'], inplace=True)
X = df[['Average Value']].values
y = df['Violent Total Rate'].values

model = LinearRegression().fit(X, y)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R^2 Score:", model.score(X, y))

plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red', linewidth=3)
plt.xlabel('Average Value')
plt.ylabel('Violent Total Rate')
plt.title('Linear Regression: Average Value vs. Violent Total Rate')
plt.show()