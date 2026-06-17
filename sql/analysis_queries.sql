-- ============================================
-- E-COMMERCE ANALYTICS PROJECT — SQL QUERIES
-- Dataset: Olist Brazilian E-Commerce
-- ============================================


-- ============================================
-- PAGE 1: EXECUTIVE OVERVIEW
-- ============================================

-- Q1: Total Revenue, Total Orders, AOV (based on order_items / product price only)
SELECT 
    SUM(price) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(price) / COUNT(DISTINCT order_id) AS avg_order_value
FROM order_items;
-- Result: 13,591,643.70 | 98,666 | 137.75

-- Q2: Total Orders (full orders table)
SELECT COUNT(*) FROM orders;
-- Result: 99,441

-- Q3: Total Revenue (based on payment_value — includes freight/shipping)
SELECT SUM(payment_value) FROM payments;
-- Result: 16,008,872.12 (16.01M)

-- Q4: Average Order Value (based on payment_value)
SELECT 
    SUM(payment_value) / COUNT(DISTINCT order_id) AS avg_order_value
FROM payments;
-- Result: 160.99

-- Q5: Monthly Revenue Trend (used for Page 1 line chart)
SELECT 
    strftime('%Y-%m', o.order_purchase_timestamp) AS month,
    SUM(p.payment_value) AS revenue,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
JOIN payments p ON o.order_id = p.order_id
GROUP BY month
ORDER BY month;


-- ============================================
-- PAGE 2: CUSTOMER INSIGHTS
-- ============================================

-- Q6: Top 10 Customers by Revenue (ranked, anonymized)
SELECT 
    ROW_NUMBER() OVER (ORDER BY SUM(p.payment_value) DESC) AS customer_rank,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(p.payment_value) AS total_spent
FROM orders o
JOIN payments p ON o.order_id = p.order_id
GROUP BY o.customer_id
ORDER BY total_spent DESC
LIMIT 10;

-- Q7: Repeat vs One-time Customers
SELECT 
    CASE 
        WHEN order_count = 1 THEN 'One-time Customer'
        ELSE 'Repeat Customer'
    END AS customer_type,
    COUNT(*) AS total_customers
FROM (
    SELECT 
        customer_unique_id,
        COUNT(order_id) AS order_count
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY customer_unique_id
) sub
GROUP BY customer_type;
-- Result: One-time: 93,099 | Repeat: 2,997

-- Q8: Customer Distribution by State
SELECT 
    customer_state,
    COUNT(DISTINCT customer_id) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC;
-- Top: SP 41,746 | RJ 12,852 | MG 11,635

-- Q9: Total Unique Customers
SELECT COUNT(DISTINCT customer_unique_id) AS total_unique_customers
FROM customers;
-- Result: 96,096

-- Q10: Repeat Customer Rate (%)
SELECT 
    ROUND(100.0 * COUNT(CASE WHEN order_count > 1 THEN 1 END) / COUNT(*), 2) AS repeat_rate_pct
FROM (
    SELECT 
        customer_unique_id,
        COUNT(order_id) AS order_count
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY customer_unique_id
) sub;
-- Result: 3.12%

-- Q11: Average Spend Per Customer
SELECT 
    ROUND(SUM(p.payment_value) / COUNT(DISTINCT c.customer_unique_id), 2) AS avg_spend_per_customer
FROM orders o
JOIN payments p ON o.order_id = p.order_id
JOIN customers c ON o.customer_id = c.customer_id;
-- Result: 166.59


-- ============================================
-- PAGE 3: PRODUCT INSIGHTS
-- ============================================

-- Q12: Top 10 Categories by Revenue
SELECT 
    ct.product_category_name_english AS category,
    ROUND(SUM(oi.price), 2) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN category_translation ct ON p.product_category_name = ct.product_category_name
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 10;
-- Top: Health & Beauty 1,258,681.34 | Watches & Gifts 1,205,005.68

-- Q13: Payment Type Breakdown
SELECT 
    payment_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(payment_value), 2) AS total_revenue
FROM payments
GROUP BY payment_type
ORDER BY total_revenue DESC;
-- credit_card: 76,795 txns | 12,542,084.19
-- boleto: 19,784 txns | 2,869,361.27
-- voucher: 5,775 txns | 379,436.87
-- debit_card: 1,529 txns | 217,989.79
-- not_defined: 3 txns | 0.00

-- Q14: Total Distinct Products
SELECT COUNT(DISTINCT product_id) AS total_products
FROM products;
-- Result: 32,951

-- Q15: Average Price Per Item
SELECT 
    ROUND(AVG(price), 2) AS avg_price_per_item
FROM order_items;
-- Result: 120.65

-- Q16: Average Order Value by Payment Type
SELECT 
    payment_type,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(payment_value) / COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM payments
WHERE payment_type != 'not_defined'
GROUP BY payment_type
ORDER BY avg_order_value DESC;
-- credit_card: 163.94 | boleto: 145.03 | debit_card: 142.66 | voucher: 98.15

-- Q17: Credit Card Installments Distribution
SELECT 
    payment_installments,
    COUNT(*) AS total_transactions,
    ROUND(SUM(payment_value), 2) AS total_revenue
FROM payments
WHERE payment_type = 'credit_card'
AND payment_installments > 0
GROUP BY payment_installments
ORDER BY payment_installments ASC;
-- 1 installment: 25,455 txns (most common)
-- Filtered to 1-10 installments for dashboard visual (11+ negligible)