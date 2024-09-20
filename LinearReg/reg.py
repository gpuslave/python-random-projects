import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv(
    Path("../datasets/cars.csv").resolve(),
    header=0,
)
print(df.columns)
# df.drop(labels=["year", "car_name"], axis=1, inplace=True)
df["This_Year"] = 2024
df["Number_Of_Years"] = df["This_Year"] - df["year"]
df = df.drop("year", axis=1)
df = df.drop("This_Year", axis=1)
df = df.drop("name", axis=1)

# df = pd.get_dummies(data=df, drop_first=True)
print(df)

# cat_col = df.select_dtypes(include=["object"]).columns
# encoder = OrdinalEncoder()
# df[cat_col] = encoder.fit_transform(df[cat_col])

X = df.drop("selling_price", axis=1)
y = df["selling_price"]

print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.1,
    random_state=42,
)

reg = LinearRegression().fit(X_train, y_train)
print(r2_score(y_test, reg.predict(X_test)))
