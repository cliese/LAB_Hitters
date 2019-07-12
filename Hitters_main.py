import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


from Data_prep import df

# Prepare regression  X features and y response
X = df.drop( columns='Salary')
y = df['Salary']

# Implement Forward selection

# Number of features is number of columns of Data Matrix
n = X.shape[1]
print(n)

# Initialize forward selection
model_col = []
p=0


remain_col = [ col for col in X.columns if not col in model_col]
results={}

# Step 1: get the models M_{p+1}
for col in remain_col :

    X_model = X[[*model_col, col]]
    reg = LinearRegression().fit(X_model, y)
    RSS = ((reg.predict(X_model)-y)**2).sum()
    #print('Residual sum of squares: %.2f')
    results[col]=(reg, RSS)
print(results)
# Step 2: choose best model
winner = remain_col[0]
val = results[remain_col[0]][1]
for key, value in results.items():
    if  value[1] <= val:
        winner = key
        val = value[1]
# Step 3: update model_col and store model



