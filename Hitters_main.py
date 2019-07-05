import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


df_hitters = pd.read_csv('/Users/Caddi/Data/Hitters/Hitters.csv')

# drop the rows with missing value in Salary

df_hitters=df_hitters.dropna(subset=['Salary'])
 # drop names

df_hitters = df_hitters.drop(columns=df_hitters.columns[0])


# Check which clolumns contain missing values
thresh=0
droplist = []
for col in df_hitters.columns:
    if df_hitters[col].isna().mean() > thresh :
        droplist.append(col)
print(droplist)

# Prepare regression  X features and y response
X = df_hitters.drop( columns='Salary')
y = df_hitters['Salary']

# Implement Forward selection

model_col = ['Hits']

remain_col = [ col for col in X.columns if not col in model_col]
results={}
for col in remain_col :

    X_model = X[[*model_col, col]]
    reg = LinearRegression().fit(X_model, y)
    RSS = ((reg.predict(X_model)-y)**2).sum()
    #print('Residual sum of squares: %.2f')
    results[col]=RSS
print(results)