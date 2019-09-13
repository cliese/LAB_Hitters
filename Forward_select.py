from sklearn.linear_model import LinearRegression


def get_models(X, y, model_col):
    results = {}
    remain_col = [col for col in X.columns if col not in model_col]

    for col in remain_col :

        X_model = X[[*model_col, col]]
        reg = LinearRegression().fit(X_model, y)
        RSS = ((reg.predict(X_model)-y)**2).sum()

        results[col] = (reg, RSS)
    return results


def choose_best(results):
    winner = sorted(results.keys())[0]
    val = results[winner][1]
    for key, value in results.items():
        if value[1] <= val:
            winner = key
            val = value[1]
    return winner


def update(model_col, models, results):
    winner = choose_best(results)
    model_col.append(winner)
    entry = model_col[:]
    models[len(model_col)] = (entry, results[winner])

    return model_col, models


def forward_select(X, y):
    model_col = []
    models = {}
    while len(model_col) < X.shape[1]:
        results = get_models(X, y, model_col)
        model_col, models = update(model_col, models, results)

    return models


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
                if compare_sets(temp, new_subsets):
                    new_subsets.append(temp)

    return new_subsets


def compare_sets(list_1, list_2):
    unused = True
    for i in range(len(list_2)):
        temp = list_2[i]
        if set(list_1) == set(temp):
            unused = False

    return unused



def get_all_subsets(columns):
    all_subsets = []
    all_subsets.append([[col] for col in columns])
    size = 0
    while size < len(columns):
        all_subsets.append(get_new_subset(all_subsets[size], columns))
        size += 1

    return all_subsets

def best_subset_linear(all_subsets):
    winner_list={}
    for size in range(len(all_subsets)):
        results = {}
        for subset in all_subsets[size]:
            X_model = X[subset]
            reg = LinearRegression().fit(X_model, y)
            RSS = ((reg.predict(X_model) - y) ** 2).sum()
            results[subset] = (reg, RSS)
        size_winner = choose_best(results)
        winner_list[size+1]=(size_winner,results[size_winner])






def best_subset_select(Matrix):
    columns = Matrix.columns
    all_subsets = get_all_subsets(columns)

