import pandas as pd
df = pd.read_csv("../data/sales_data.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
print("=== Accuracy Check ===")

negative_prices = (df["price"] < 0).sum()
current_date = pd.Timestamp.now()
future_date_count = (df["date"] > current_date).sum()

print(f"Negative Prices: {negative_prices}")
print(f"Number of Future Dates: {future_date_count}")

print("=== Consistency Check ===")
unique_products = df["product"].unique()
unique_count = df["product"].nunique()

print(f"Unique products: {unique_products}")
print(f"Count of unique products: {unique_count}")

print("=== Completeness Check ===")
missing_values = df.isnull().sum()
completeness_rate = df.notnull().mean().mean() *100

print(f"Missing Values: {missing_values}")
print(f"Overall completeness rate: {completeness_rate:.1f}%")

assert negative_prices ==0, "Negative prices found!"
