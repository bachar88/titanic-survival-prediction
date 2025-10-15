import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load trained model and feature columns
model = joblib.load("titanic_model.pkl")
columns = joblib.load("titanic_columns.pkl")

def predict_survival(pclass, sex, age, sibsp, parch, fare, embarked):
    sex_val = 1 if sex == "male" else 0
    embarked_val = {"S": 2, "C": 0, "Q": 1}.get(embarked, 2)
    family_size = sibsp + parch + 1

    input_df = pd.DataFrame([[pclass, sex_val, age, sibsp, parch, fare, embarked_val, family_size]], columns=columns)
    prob = model.predict_proba(input_df)[0][1]
    return prob