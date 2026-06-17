# End-to-End E-Commerce Analytics Platform

![Data Pipeline](https://github.com/joyceleehy/ecommerce-analytics-ai-automation/actions/workflows/data_pipeline.yml/badge.svg)

An end-to-end analytics project built using the Olist Brazilian E-Commerce dataset. This project demonstrates the complete analytics workflow, from data cleaning and automation to SQL analysis, Power BI dashboard development, and automated business insights generation.

The solution combines Python automation, SQL analytics, Power BI reporting, and GitHub Actions to create a reproducible analytics pipeline that automatically processes data and supports business decision-making.

**Dataset:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## Project Overview

This project simulates a real-world Business Intelligence solution for an e-commerce company.

The workflow includes:

- Data cleaning and validation using Python
- Data storage in SQLite
- SQL-based business analysis
- Interactive Power BI dashboards
- Automated business insights generation
- CI/CD automation using GitHub Actions

---

## Business Questions

This project was designed to answer the following business questions:

1. What are the overall sales and revenue trends?
2. Which product categories generate the highest revenue?
3. Who are the highest-value customers?
4. What is the customer retention rate?
5. Which payment methods drive the most revenue?
6. Which regions contribute the most customers and sales?
7. How do installment payments impact purchasing behavior?
8. What actionable insights can support business growth?

---

## Tech Stack

- Python (Pandas)
- SQLite
- SQL
- Power BI
- DAX
- Power Query
- Git & GitHub
- GitHub Actions

---

## Data Pipeline

```text
Raw CSV Files
    ↓
Python Data Cleaning & Validation
    ↓
SQLite Database
    ↓
SQL Analysis
    ↓
Power BI Dashboard
    ↓
Automated Insights Generation
```

---

## Repository Structure

```text
.
├── .github/workflows/      # CI/CD automation
├── ai/                     # Automated insights generator
├── data/                   # Raw & cleaned data + SQLite DB
├── powerbi/                # Power BI dashboard files
├── python/                 # ETL and cleaning scripts
├── sql/                    # SQL analysis queries
└── README.md
```

---

## Data Model

A star-schema style data model was created in Power BI to support efficient reporting and KPI analysis.

### Fact Tables
- Orders
- Payments

### Dimension Tables
- Customers
- Products
- Sellers
- Dates

Relationships were optimized for drill-down analysis and dashboard performance.

---

## Skills Demonstrated

### SQL
- Joins
- CTEs
- Window Functions
- Aggregations
- KPI Calculations
- Business Analysis Queries

### Power BI
- Data Modeling
- DAX Measures
- Power Query
- KPI Reporting
- Interactive Dashboards
- Drill-through Analysis

### Python
- Data Cleaning
- Data Validation
- ETL Processing
- SQLite Automation

### Analytics
- Revenue Analysis
- Customer Segmentation
- Retention Analysis
- Product Performance Analysis
- Payment Behavior Analysis

---

## Key Findings

- Total Revenue: **R$16.01M**
- Total Orders: **99,441**
- Repeat Customer Rate: **3.12%**
- Top Revenue Category: **Health & Beauty**
- Credit Card Usage: **78.3% of transactions**
- São Paulo contributes **43% of customers**

---

## Power BI Dashboard Preview

### Executive Overview

High-level business performance including revenue, orders, and AOV trends.

![Executive Overview](screenshots/page1_executive_overview.png)

---

### Customer Insights

Customer segmentation, retention analysis, and geographic distribution.

![Customer Insights](screenshots/page2_customer_insights.png)

---

### Product Insights

Product performance, category revenue, and payment behavior analysis.

![Product Insights](screenshots/page3_product_insights.png)

---

## AI-Assisted Insights Layer

The project includes an automated insights engine located in:

```text
ai/insights_generator.py
```

It generates business insights directly from SQLite KPI outputs.

Due to API limitations (Google Gemini / Anthropic Claude free tiers), a rule-based engine was implemented instead.

This ensures:

- Fully reproducible outputs
- No external API dependency
- Consistent insight generation

---

## Automation

GitHub Actions automates the data pipeline:

```text
.github/workflows/data_pipeline.yml
```

It:

- Runs Python ETL scripts
- Validates datasets
- Updates SQLite database
- Ensures reproducibility

---

## Business Impact

This project enables:

- Monitoring of sales performance
- Identification of high-value customers
- Understanding of retention behavior
- Product category performance tracking
- Payment method analysis
- Data-driven decision making

---

## Future Enhancements

- Customer Lifetime Value (CLV)
- RFM segmentation
- Sales forecasting models
- Real-time dashboard refresh
- Cloud data warehouse integration
- Automated reporting emails

---

## Author

**Joyce Lee How Yee**

PL-300 Certified Data & BI Analyst

### Connect
- LinkedIn: https://linkedin.com/in/joyceleehowyee
- GitHub: https://github.com/joyceleehy

### Skills
Power BI • SQL • Python • Data Analytics • Dashboarding • KPI Reporting • Business Intelligence
