import pandas as pd


df_hitters = pd.read_csv('Hitters.csv')

# drop the rows with missing value in Salary

df_hitters=df_hitters.dropna(subset=['Salary'])
 # drop names

df_hitters = df_hitters.drop(columns=df_hitters.columns[0])

# encode categorical features


df = pd.get_dummies(df_hitters)

