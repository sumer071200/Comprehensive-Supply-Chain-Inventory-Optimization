# 📦 Supply Chain Data Analysis

This project analyzes supply chain data to identify key performance trends, optimize inventory, monitor vendor performance, and support data-driven decision-making. It demonstrates real-world data cleaning, transformation, and visualization workflows commonly used in business analytics.

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

If published on Tableau Public:  
👉 [View Interactive Dashboard](#) *(Replace with your Tableau Public link)*

Or add screenshots like:

```markdown
![Dashboard Overview](images/dashboard.png)
