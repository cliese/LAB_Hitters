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

