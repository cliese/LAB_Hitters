from sklearn.linear_model import LinearRegression




def get_models(X, model_col ):
    results={}
    remain_col = [col for col in X.columns if not col in model_col]
    # Step 1: get the models M_{p+1}
    for col in remain_col :

        X_model = X[[*model_col, col]]
        reg = LinearRegression().fit(X_model, y)
        RSS = ((reg.predict(X_model)-y)**2).sum()

        results[col]=(reg, RSS)
    return results


def choose_best(results):
    winner = results.keys()[0]
    val = results[winner][0]
    for key, value in results.items():
        if  value[1] <= val:
            winner = key
            val = value[1]
    return winner
# Step 3: update model_col and store model

def update(model_col, models, results):
    winner = choose_best(results)
    model_col = models_col.append(winner)
    models[model_col] = results[winner]

    return model_col, models

def forward_select(X):
    model_col=[]
    models = {}
    while len(models_col) < X.shape[1]:
        results = get_models(X,model_cols)
        update(model_col, models, results)

