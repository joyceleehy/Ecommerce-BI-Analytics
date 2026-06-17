import sqlite3

# -------------------------
# 1. CONNECT TO DATABASE
# -------------------------
conn = sqlite3.connect("../data/olist.db")

# -------------------------
# 2. PULL KEY METRICS
# -------------------------
total_revenue = conn.execute("SELECT SUM(payment_value) FROM payments").fetchone()[0]
total_orders = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
avg_order_value = total_revenue / total_orders

repeat_rate = conn.execute("""
    SELECT ROUND(100.0 * COUNT(CASE WHEN order_count > 1 THEN 1 END) / COUNT(*), 2)
    FROM (
        SELECT customer_unique_id, COUNT(order_id) AS order_count
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY customer_unique_id
    ) sub
""").fetchone()[0]

top_category, top_category_revenue = conn.execute("""
    SELECT ct.product_category_name_english, SUM(oi.price)
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    JOIN category_translation ct ON p.product_category_name = ct.product_category_name
    GROUP BY ct.product_category_name_english
    ORDER BY SUM(oi.price) DESC
    LIMIT 1
""").fetchone()

top_state, top_state_customers = conn.execute("""
    SELECT customer_state, COUNT(DISTINCT customer_id)
    FROM customers
    GROUP BY customer_state
    ORDER BY COUNT(DISTINCT customer_id) DESC
    LIMIT 1
""").fetchone()

total_customers = conn.execute("SELECT COUNT(DISTINCT customer_unique_id) FROM customers").fetchone()[0]

conn.close()

# -------------------------
# 3. RULE-BASED INSIGHT LOGIC
# -------------------------
insights = []

# Retention insight
if repeat_rate < 5:
    insights.append(
        f"Repeat customer rate is critically low at {repeat_rate}%, indicating the business is heavily "
        f"reliant on acquiring new customers rather than retaining existing ones. This represents a major "
        f"opportunity for loyalty programs or post-purchase engagement strategies."
    )
elif repeat_rate < 15:
    insights.append(
        f"Repeat customer rate of {repeat_rate}% is below typical e-commerce benchmarks, suggesting room "
        f"to improve customer retention through targeted re-engagement campaigns."
    )
else:
    insights.append(
        f"Repeat customer rate of {repeat_rate}% reflects healthy customer loyalty for an e-commerce platform."
    )

# AOV insight
if avg_order_value > 150:
    insights.append(
        f"Average order value of R${avg_order_value:,.2f} indicates customers are making relatively "
        f"high-value purchases, supporting a focus on premium product lines."
    )
else:
    insights.append(
        f"Average order value of R${avg_order_value:,.2f} suggests opportunities to increase basket size "
        f"through cross-selling or bundling strategies."
    )

# Category concentration insight
category_share = (top_category_revenue / total_revenue) * 100
insights.append(
    f"{top_category} is the leading revenue category, contributing {category_share:.1f}% of total product "
    f"revenue, highlighting strong customer demand in this segment."
)

# Geographic concentration insight
state_share = (top_state_customers / total_customers) * 100
insights.append(
    f"{top_state} accounts for {state_share:.1f}% of the total customer base, showing significant "
    f"geographic concentration that could inform regional marketing or logistics decisions."
)

# -------------------------
# 4. OUTPUT RESULTS
# -------------------------
print("\n📊 AI-Style Business Insights (Rule-Based):\n")
for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}\n")

# Save to file for easy copy-paste into Power BI
with open("insights_output.txt", "w", encoding="utf-8") as f:
    for insight in insights:
        f.write(f"- {insight}\n")

print("✅ Insights saved to data/exports/insights_output.txt")