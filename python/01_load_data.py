import pandas as pd

# Load datasets from raw folder
orders = pd.read_csv("../data/raw/olist_orders_dataset.csv")
customers = pd.read_csv("../data/raw/olist_customers_dataset.csv")

# Check basic info
print("✅ Orders shape:", orders.shape)
print("✅ Customers shape:", customers.shape)

print("\n--- ORDERS PREVIEW ---")
print(orders.head())

print("\n--- CUSTOMERS PREVIEW ---")
print(customers.head())