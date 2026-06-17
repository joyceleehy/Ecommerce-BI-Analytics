# End-to-End E-Commerce Analytics Platform

![Data Pipeline](https://github.com/joyceleehy/ecommerce-analytics-ai-automation/actions/workflows/data_pipeline.yml/badge.svg)

An end-to-end Business Intelligence project built on the Olist Brazilian E-Commerce dataset (99,441 orders, 2016–2018), demonstrating the full analytics lifecycle from raw data processing to business insight delivery using Python, SQL, Power BI, and automated CI/CD.

**Dataset:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle)

---

## Project Overview

This project simulates a real-world BI workflow for an e-commerce business:

- Data cleaning and validation (Python)
- Structured data storage (SQLite)
- Business analysis (SQL)
- KPI dashboards (Power BI)
- Automated insights generation
- CI/CD data pipeline (GitHub Actions)

---

## Business Questions & Insights

**Revenue Trends** — Total revenue reached R$16.01M across 99,441 orders, with monthly fluctuations indicating seasonal demand patterns.

**Product Performance** — Health & Beauty is the top revenue contributor, with revenue concentrated in a small number of categories, indicating dependency on core product lines.

**High-Value Customers** — A small percentage of customers contributes a disproportionate share of revenue, highlighting an opportunity for customer segmentation and targeted retention strategies.

**Customer Retention** — Repeat customer rate sits at just 3.12%, well below typical e-commerce benchmarks, pointing to a critical gap in loyalty and retention strategy.

**Payment Behavior** — Credit cards account for 78.3% of transaction value, with many customers splitting payments across installments — a common practice in the Brazilian market.

**Regional Distribution** — São Paulo accounts for 43% of the total customer base, showing strong geographic concentration and a potential opportunity for regional expansion.

---

## Key Business Takeaways

Revenue is heavily dependent on a small number of product categories. Customer retention is the biggest weakness in the business, with a repeat rate far below industry expectations. Credit card is the dominant payment method, and the customer base is geographically concentrated in São Paulo, creating both an expansion opportunity and a concentration risk.

---

## Power BI Dashboard Preview

### Executive Overview
KPIs including revenue, total orders, and average order value, plus a monthly sales trend.

![Executive Overview](screenshots/page1_executive_overview.png)

### Customer Insights
Customer ranking, retention behavior, and geographic distribution.

![Customer Insights](screenshots/page2_customer_insights.png)

### Product Insights
Category performance and payment behavior analysis.

![Product Insights](screenshots/page3_product_insights.png)

---

## Data Model

The Power BI model is built on tables loaded from the SQLite database: **orders**, **payments**, **customers**, **products**, and **category_translation**, joined on order and product IDs to support revenue, customer, and product-level analysis across all three dashboard pages.

---

## Tech Stack & Skills Demonstrated

**Python** — ETL pipeline, data cleaning, validation, SQLite automation
**SQL** — Joins, CTEs, window functions, conditional aggregation, KPI extraction
**Power BI** — Data modeling, DAX measures, Power Query, interactive dashboards
**GitHub Actions** — Automated CI/CD data pipeline
**Analytics** — Revenue analysis, customer segmentation, retention analysis, product and payment behavior analysis

---

## AI & Automation Layer

`ai/insights_generator.py` extracts live KPI metrics directly from the SQLite database and generates automated business insights. To avoid dependency on paid third-party AI APIs and keep the pipeline fully reproducible, a rule-based insight engine was built using conditional business logic instead of an external LLM call — applying retention, spend, and concentration thresholds to generate consistent, explainable insights.

---

## Automation (CI/CD Pipeline)

`.github/workflows/data_pipeline.yml` automatically re-runs the data cleaning and database creation scripts on a schedule, keeping the pipeline reproducible end-to-end without manual intervention.

---

## Getting Started

```bash
git clone https://github.com/joyceleehy/ecommerce-analytics-ai-automation.git
pip install pandas
cd python
python 02_data_cleaning.py
python 03_create_database.py
cd ../ai
python insights_generator.py
```

---

## Future Improvements

- Customer Lifetime Value (CLV) modeling
- RFM segmentation
- Sales forecasting
- Cloud data warehouse integration

---

## About Me

**Joyce Lee How Yee** — PL-300 Certified Data & BI Analyst with a background in People Analytics. Currently open to Data Analyst, BI Analyst, and Analytics roles.

[LinkedIn](https://www.linkedin.com/in/joyceleehowyee/) · [GitHub](https://github.com/joyceleehy)


