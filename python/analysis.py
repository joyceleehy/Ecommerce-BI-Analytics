import sqlite3
import pandas as pd

conn = sqlite3.connect("data/olist.db")


# =========================
# 1. TOTAL ORDERS
# =========================
q1 = "SELECT COUNT(*) AS total_orders FROM orders;"
df1 = pd.read_sql(q1, conn)
df1.to_csv("exports/total_orders.csv", index=False)


# =========================
# 2. TOTAL REVENUE
# =========================
q2 = "SELECT SUM(payment_value) AS total_revenue FROM payments;"
df2 = pd.read_sql(q2, conn)
df2.to_csv("exports/total_revenue.csv", index=False)


# =========================
# 3. MONTHLY TREND
# =========================
q3 = """
SELECT 
    strftime('%Y-%m', o.order_purchase_timestamp) AS month,
    SUM(p.payment_value) AS revenue,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
JOIN payments p ON o.order_id = p.order_id
GROUP BY month
ORDER BY month;
"""
df3 = pd.read_sql(q3, conn)
df3.to_csv("exports/monthly_trend.csv", index=False)


# =========================
# 4. TOP CUSTOMERS
# =========================
q4 = """
SELECT 
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(p.payment_value) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
ORDER BY total_spent DESC
LIMIT 10;
"""
df4 = pd.read_sql(q4, conn)
df4.to_csv("exports/top_customers.csv", index=False)

print("✅ All files exported to /exports folder")