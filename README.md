# AI-Powered E-Commerce Analytics & Automation Platform

![Data Pipeline](https://github.com/joyceleehy/ecommerce-analytics-ai-automation/actions/workflows/data_pipeline.yml/badge.svg)

An end-to-end analytics project on the Olist Brazilian E-Commerce dataset, combining Python automation, SQL analysis, Power BI dashboarding, and an AI-driven insights layer — with a fully automated CI/CD data pipeline via GitHub Actions.

**Dataset:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle)

## Tech Stack
Python (pandas) · SQLite · SQL · Power BI (DAX, Power Query) · GitHub Actions

## Pipeline
Raw CSVs → Python cleaning & validation → SQLite database → SQL analysis → Power BI dashboard → Automated insights generator. GitHub Actions re-runs the cleaning and database steps on a schedule.

## Repository Structure
├── .github/workflows/   # CI/CD automation

├── ai/                  # Business insights generator

├── data/                # Raw, cleaned data & SQLite database

├── powerbi/             # Power BI dashboard file

├── python/              # Cleaning & database scripts

├── sql/                 # Analysis queries

## Key Findings
- Total revenue: R$16.01M across 99,441 orders
- Repeat customer rate: only 3.12% — a critical retention insight
- Health & Beauty is the top revenue category
- Credit card dominates payments at 78.3% of transaction value
- São Paulo accounts for 43% of the total customer base

## Power BI Dashboard
**Executive Overview** — Revenue, orders, AOV KPIs, and monthly sales trend.

**Customer Insights** — Top 10 customers, repeat vs. one-time breakdown, distribution by state.

**Product Insights** — Top categories, payment type breakdown, AOV by payment method, installment analysis.

## AI-Assisted Insights Layer
`ai/insights_generator.py` pulls live metrics from the database to generate business insights. Google Gemini and Anthropic Claude APIs were both evaluated for AI-generated text, but free-tier billing restrictions on both led to building a **rule-based insight engine** instead — applying conditional business logic to produce the same style of actionable insights without external API dependency.

## Automation
A GitHub Actions workflow (`.github/workflows/data_pipeline.yml`) automatically re-runs the cleaning and database scripts on a schedule, demonstrating a reproducible, automated pipeline.

## Author
**Joyce Lee How Yee** — PL-300 Certified Data & BI Analyst | Power BI · SQL · Python
[LinkedIn](https://linkedin.com/in/joyceleehowyee) · [GitHub](https://github.com/joyceleehy)
