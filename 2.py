#problem 02

import pandas as pd

df = pd.read_csv("sales_large.csv")

total_sales = df.groupby(["Region", "Product"])["Sales"].sum().reset_index()

top_product = df.groupby("Product")["Sales"].sum().idxmax()

print(total_sales)
print("Top Product:", top_product)
