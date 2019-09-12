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



def get_new_subset(subsets, columns):
    ''' Inputs: subsets, a list of subsets of the columns of X with cardinality n
     and X, a data matrix
    returns a list of all subsets of the columns of X with cardinality n+1 '''
    new_subsets = []
    for subset in subsets:
        if isinstance(subset, list):
            remain_col = [col for col in columns if col not in subset]
            for col in remain_col:
                temp = subset[:]
                temp.append(col)
                if compare_sets(temp,new_subsets):
                    new_subsets.append(temp)


    return new_subsets

def compare_sets(list_1, list_2):
    unused = True
    for i in range(len(list_2)):
        temp = list_2[i]
        if set(list_1) == set(temp):
            unused = False

    return unused

my_list =[[1],[2],[3],[4]]
my_cols =[1,2,3]



def get_all_subsets(columns):
    all_subsets = []
    all_subsets.append([[col] for col in columns])
    size = 0
    while size + 1 < len(columns):
        all_subsets.append(get_new_subset(all_subsets[size], columns))
        size += 1

    return all_subsets


def check_end(subsets, columns):
    if len(subsets[0]) == len(columns):
        return True




X_test = X.columns[0:5]
print(X_test)
temp=get_all_subsets(X_test)
print(temp[0])
print(temp[1])
print(temp[2])
print(temp[3])
print(temp[4])

