import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

from importlib import reload

from Data_prep import df
import Forward_select as FS

reload(FS)


# Prepare regression  X features and y response
X = df.drop( columns='Salary')
y = df['Salary']

# Implement Forward selection

# Number of features is number of columns of Data Matrix
n = X.shape[1]

models = FS.forward_select(X, y)

print(sorted(models.keys()))
for key, value in models.items():
    print((value[0]))