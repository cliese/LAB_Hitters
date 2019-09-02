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

# print(sorted(models.keys()))
# for key, value in models.items():
#     print((value[0]))

#We no choose the best model in models

# for i in range(len(X.columns)):
#     name = 'Card' +str(i)
# print (X.columns)

# calculate all subsets

def get_new_subset(subsets, X):

    new_subsets = []
    for subset in subsets:

        remain_col = [col for col in X.columns if col not in subset]
        for col in remain_col:
            temp = subset[:]
            temp.append(col)


            new_subsets.append(temp)

    return new_subsets




def get_all_subsets(X):
    all_subsets = []
    all_subsets.append([[col] for col in X.columns])
    all_subsets.append(get_new_subset(all_subsets[0], X))
    return all_subsets

all_subsets = get_all_subsets(X)
print(all_subsets)
