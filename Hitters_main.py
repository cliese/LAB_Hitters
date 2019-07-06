import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


from Data_prep import df

# Prepare regression  X features and y response
X = df.drop( columns='Salary')
y = df['Salary']

# Implement Forward selection

model_col = []

remain_col = [ col for col in X.columns if not col in model_col]
results={}
for col in remain_col :

    X_model = X[[*model_col, col]]
    reg = LinearRegression().fit(X_model, y)
    RSS = ((reg.predict(X_model)-y)**2).sum()
    #print('Residual sum of squares: %.2f')
    results[col]=RSS
print(results)

