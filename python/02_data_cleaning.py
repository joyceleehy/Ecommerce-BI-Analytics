import pandas as pd

# -------------------------
# LOAD DATA
# -------------------------
orders = pd.read_csv("../data/raw/olist_orders_dataset.csv")
customers = pd.read_csv("../data/raw/olist_customers_dataset.csv")
order_items = pd.read_csv("../data/raw/olist_order_items_dataset.csv")
payments = pd.read_csv("../data/raw/olist_order_payments_dataset.csv")
products = pd.read_csv("../data/raw/olist_products_dataset.csv")
category_translation = pd.read_csv("../data/raw/product_category_name_translation.csv")

# -------------------------
# 1. CHECK MISSING VALUES
# -------------------------
print("Missing values in orders:")
print(orders.isnull().sum())

print("\nMissing values in customers:")
print(customers.isnull().sum())

print("\nMissing values in order_items:")
print(order_items.isnull().sum())

print("\nMissing values in payments:")
print(payments.isnull().sum())

print("\nMissing values in products:")
print(products.isnull().sum())

print("\nMissing values in category_translation:")
print(category_translation.isnull().sum())

# -------------------------
# 2. REMOVE DUPLICATES
# -------------------------
orders = orders.drop_duplicates()
customers = customers.drop_duplicates()
order_items = order_items.drop_duplicates()
payments = payments.drop_duplicates()
products = products.drop_duplicates()
category_translation = category_translation.drop_duplicates()

# -------------------------
# 3. FIX DATE FORMAT
# -------------------------
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# -------------------------
# 4. HANDLE PRODUCT NULLS
# -------------------------
# Some products have missing category names - fill with "unknown"
products["product_category_name"] = products["product_category_name"].fillna("unknown")

# -------------------------
# 5. CHECK SHAPES AFTER CLEANING
# -------------------------
print("\nAfter cleaning:")
print("Orders shape:", orders.shape)
print("Customers shape:", customers.shape)
print("Order items shape:", order_items.shape)
print("Payments shape:", payments.shape)
print("Products shape:", products.shape)
print("Category translation shape:", category_translation.shape)

# -------------------------
# 6. SAVE CLEAN FILES
# -------------------------
orders.to_csv("../data/cleaned/orders_clean.csv", index=False)
customers.to_csv("../data/cleaned/customers_clean.csv", index=False)
order_items.to_csv("../data/cleaned/order_items_clean.csv", index=False)
payments.to_csv("../data/cleaned/payments_clean.csv", index=False)
products.to_csv("../data/cleaned/products_clean.csv", index=False)
category_translation.to_csv("../data/cleaned/category_translation_clean.csv", index=False)

print("\n✅ Cleaned files saved successfully!")
