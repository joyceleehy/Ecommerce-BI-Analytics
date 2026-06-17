import pandas as pd
import sqlite3

# Load CLEANED data
orders = pd.read_csv("../data/cleaned/orders_clean.csv")
customers = pd.read_csv("../data/cleaned/customers_clean.csv")
order_items = pd.read_csv("../data/cleaned/order_items_clean.csv")
payments = pd.read_csv("../data/cleaned/payments_clean.csv")
products = pd.read_csv("../data/cleaned/products_clean.csv")
category_translation = pd.read_csv("../data/cleaned/category_translation_clean.csv")

# Create database file inside /data folder
conn = sqlite3.connect("../data/olist.db")

# Save tables into database
orders.to_sql("orders", conn, if_exists="replace", index=False)
customers.to_sql("customers", conn, if_exists="replace", index=False)
order_items.to_sql("order_items", conn, if_exists="replace", index=False)
payments.to_sql("payments", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
category_translation.to_sql("category_translation", conn, if_exists="replace", index=False)

print("✅ Database created successfully with 6 tables!")

# Quick test
result = pd.read_sql("""
    SELECT COUNT(*) AS total_orders,
           (SELECT COUNT(*) FROM order_items) AS total_order_items,
           (SELECT COUNT(*) FROM payments) AS total_payments,
           (SELECT COUNT(*) FROM products) AS total_products
    FROM orders
""", conn)
print(result)

conn.close()