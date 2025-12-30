import pandas as pd
import datetime
df=pd.read_csv("expenses.csv")
#print(df)
#print(df.info())
#print(df.describe())

df["Date"]=pd.to_datetime(df["Date"])
#Monthly expense analysis
df["Month"]=df["Date"].dt.month
monthly_expenses=df.groupby("Month")["Amount"].sum()
#print(f"Monthly expenses is :{monthly_expenses}")
#category expense analysis
category_expense=df.groupby("Category")["Amount"].sum()
#print(f"Category expenses :{category_expense}")
#Highest Spending Category
highest_category=category_expense.idxmax()
highest_amount=category_expense.max()
print(f"Highest category is: {highest_category} and highest amount is:{highest_amount} ")

