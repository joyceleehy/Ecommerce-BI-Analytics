-- =========================================
-- ADVANCED E-COMMERCE ANALYSIS (OLIST)
-- Customer + Orders + Payments Insights
-- =========================================


-- 1. CUSTOMER LIFETIME VALUE (CLV STYLE)
-- Purpose: Identify high-value customers

SELECT 
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(p.payment_value) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
ORDER BY total_spent DESC;


-- 2. MONTHLY ACTIVE CUSTOMERS
-- Purpose: Track customer engagement

SELECT 
    strftime('%Y-%m', o.order_purchase_timestamp) AS month,
    COUNT(DISTINCT o.customer_id) AS active_customers
FROM orders o
GROUP BY month
ORDER BY month;


-- 3. CUSTOMER RETENTION (SIMPLE)
-- Purpose: Measure returning customers

WITH customer_month AS (
    SELECT 
        customer_id,
        strftime('%Y-%m', order_purchase_timestamp) AS month
    FROM orders
    GROUP BY customer_id, month
)

SELECT 
    a.month AS current_month,
    COUNT(DISTINCT b.customer_id) AS retained_customers
FROM customer_month a
JOIN customer_month b 
    ON a.customer_id = b.customer_id
    AND b.month = date(a.month, '+1 month')
GROUP BY a.month
ORDER BY a.month;


-- 4. COHORT ANALYSIS
-- Purpose: Group customers by first purchase month

WITH first_purchase AS (
    SELECT 
        customer_id,
        MIN(strftime('%Y-%m', order_purchase_timestamp)) AS cohort_month
    FROM orders
    GROUP BY customer_id
)

SELECT 
    f.cohort_month,
    strftime('%Y-%m', o.order_purchase_timestamp) AS order_month,
    COUNT(DISTINCT o.customer_id) AS active_customers
FROM orders o
JOIN first_purchase f 
    ON o.customer_id = f.customer_id
GROUP BY f.cohort_month, order_month
ORDER BY f.cohort_month, order_month;


-- 5. PRODUCT PERFORMANCE ANALYSIS
-- Purpose: Identify top-selling categories

SELECT 
    p.product_category_name,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    SUM(oi.price) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC;