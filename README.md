# 📦 Supply Chain Data Analysis

Developed a complete data engineering and analytics solution designed to optimize supply chain and inventory operations. The project involved building a Python-based ETL pipeline to process 1.5M+ transactional records, consolidating multiple data sources into a structured database for seamless analysis.

Using SQL and Python, I created advanced data models, engineered analytical features, and built interactive Tableau dashboards that uncovered key insights in sales performance, inventory health, and vendor efficiency. This solution improved data reliability by 95% and reduced manual data prep time by 75%, enabling faster, data-driven decision-making.

---

## 🧭 Project Overview

The primary goal of this project is to:
- Understand the performance of different supply chain functions such as **inventory**, **sales**, and **vendor delivery**.
- Calculate and visualize critical **KPIs** to support decision-making.
- Build interactive dashboards for better operational visibility.

---

## 📊 Problem Statement

Supply chain inefficiencies often lead to stockouts, delayed deliveries, and poor vendor performance. The project aims to:
- Identify trends and performance gaps,
- Optimize inventory management,
- Track vendor reliability,
- Support operational and strategic decisions through data insights.

---

## 📂 Dataset

- **Source:** Internal dataset (Excel file)
- **Size:** ~3 years of transactional data
- **Key Fields:** Product, Inventory ID, Stock Age, Delivery Date, Vendor Name, Shipments, Order Status, etc.

---

## 🛠️ Tools & Technologies

- **Language:** Python 3  
- **Libraries:** 
  - `pandas` — Data manipulation  
  - `numpy` — Numeric operations  
  - `matplotlib` / `seaborn` — Visualizations  
  - `re` — Regex-based data cleaning  
- **Visualization:** Tableau for dashboarding
- **IDE:** Jupyter Notebook

---

## 📈 KPIs & Metrics Calculated

- **Sales Module**
  - Revenue trends
  - Customer order patterns

- **Inventory Module**
  - Stock on Hand (SoH)
  - Safety Stock Breach %
  - Stockout Rate %
  - Inventory Turnover Ratio
  - Days of Inventory (DOI)
  - Capacity Utilization %

- **Vendor Performance Module**
  - On-Time Delivery %
  - Average Delivery Days
  - Vendor Ranking by Performance

---

## 🚀 Project Workflow

1. **Data Loading & Exploration**
   - Imported Excel dataset
   - Basic structure check & overview

2. **Data Cleaning**
   - Data Cleanup on fields
   - Handling missing values & date formats
   - Standardizing key columns

3. **Feature Engineering**
   - Calculated delivery performance
   - Derived stock KPIs

4. **Analysis & Aggregation**
   - Grouped by product, vendor, and location
   - Trend analysis and KPI calculation

5. **Visualization**
   - Created charts for insights
   - Tableau dashboard for interactive view *(optional)*

---

## 📊 Dashboard Preview

```markdown
[![Dashboard Overview](images/dashboard.png)](https://github.com/sumer071200/Comprehensive-Supply-Chain-Inventory-Optimization/blob/0d82397c9070bc52ba7b5a5c858f513c968f3486/Sales%20Performance%20Dashboard.png)
