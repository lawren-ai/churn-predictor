import pandas as pd

# load dataset
df = pd.read_csv("data/telco-churn.csv")

# preview structure
print("Shape: ", df.shape)
print("Columns : \n", df.dtypes)
print("Sample rows: \n", df.head(3))

# check for missing values
print("\n Missing values: \n", df.isnull().sum())

# class balance
print("\n Churn Distribution: \n", df["Churn"].value_counts(normalize=True))

# Summary stats
print("Numeric Summary: \n", df.describe())