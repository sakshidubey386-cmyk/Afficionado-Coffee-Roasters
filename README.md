# Afficionado Coffee Roasters
Power BI dashboard for coffee shop sales analysis - Peak hours, weekly trend, Monthly sales 2025


## 📊 Project Overview
Analyzed 1 year of coffee shop sales data to identify key business insights. This dashboard helps track sales performance, peak hours, and product trends.

## 🎯 Key Insights
- **Peak Hours**: Identified busiest hours for staffing optimization
- **Monthly Sales Trend 2025**: Tracked revenue growth month over month  
- **Product Analysis**: Top selling coffee items and categories
- **Weekly Pattern**: Sales trends across weekdays vs weekends

## 🛠️ Tools Used
- **Power BI Desktop** - Data visualization and DAX
- **Excel** - Data cleaning and preprocessing
- **GitHub** - Version control

## 📈 Dashboard Features
- Interactive slicers for date, product, and location
- DAX measures for YOY growth and % contribution
- Drill-down from yearly to daily view

## 📸 Dashboard Screenshots
![Dashboard Overview](dashboard1.png)
![Sales Trend](dashboard2.png)

## 📁 Files
- `coffee project.pbix` - Power BI file. Download and open in Power BI Desktop


# Coffee Shop Sales Analysis – 2025

## Project Overview

This project focuses on analyzing coffee shop sales data for 2025 to identify sales trends, customer demand patterns, peak business hours, slow periods, and differences in sales performance across store locations.

## Analytical Methodology

### 1. Data Ingestion & Validation

- Loaded the transaction dataset into Power BI.
- Checked and converted timestamp values into the correct date and time format.
- Identified and removed duplicate transaction IDs.
- Checked missing values in key fields such as Transaction ID, Date, Quantity, and Price.
- Verified that transaction quantities and unit prices were positive.
- Reviewed invalid or inconsistent records.
- Confirmed that the cleaned dataset was ready for further analysis.

### 2. Feature Engineering (Temporal)

#### Revenue per Transaction

Revenue per Transaction = Transaction Quantity × Unit Price

#### Hour Extraction

- Extracted the hour (0–23) from the transaction timestamp.
- Used the hour for analyzing hourly sales patterns.

#### Day of Week

- Derived the day of the week from the transaction date.
- Compared sales performance across different weekdays.

#### Time Buckets

Transactions were classified into four time buckets:

- **Morning:** 6:00 AM – 11:59 AM
- **Afternoon:** 12:00 PM – 4:59 PM
- **Evening:** 5:00 PM – 9:59 PM
- **Late Hours:** 10:00 PM – 5:59 AM

All engineered features were validated before further analysis.

### 3. Sales Trend Analysis

- Imported the Afficionado Coffee Roasters sales dataset into Power BI.
- Checked missing values and duplicates.
- Converted the date column into the correct date format.
- Verified sales and transaction data.
- Created relationships between tables where required.
- Developed measures such as Total Revenue and Total Transactions.
- Used line charts to analyze daily revenue trends.
- Identified high- and low-performing days.
- Analyzed weekly revenue and transaction performance.
- Examined upward and downward sales trends.
- Compared revenue trends across store locations.
- Identified the best- and lowest-performing stores.
- Summarized findings and provided recommendations.

### 4. Day-of-Week Performance Analysis

- Imported the transaction dataset into Power BI.
- Validated timestamp values.
- Checked for missing and duplicate data.
- Verified transaction quantities and unit prices.
- Reviewed invalid or inconsistent records.
- Confirmed that the cleaned dataset was ready for analysis.

### 5. Time-of-Day Demand Analysis

#### Hourly Transaction Analysis

- Grouped transactions by hour of the day (0–23).
- Analyzed hourly transaction volume.

#### Hourly Revenue Analysis

- Calculated total revenue for each hour.
- Studied the distribution of sales throughout the day.

#### Visualization

- Created line and column charts in Power BI.
- Visualized hourly transaction volume and revenue trends.

#### Peak and Slow Period Identification

- Identified morning rush hours based on transaction volume.
- Detected slower midday periods.
- Identified evening peak hours based on revenue and customer activity.

#### Insights & Recommendations

- Summarized hourly demand patterns.
- Provided recommendations for staff scheduling and operational planning.

### 6. Cross-Location Temporal Comparison

#### Store-wise Data Segmentation

- Segmented the dataset by store location.
- Analyzed sales performance for each store independently.

#### Hourly Heatmap

- Created hourly heatmaps in Power BI.
- Compared transaction volume and revenue across different hours for each store.

#### Peak-Hour Comparison

- Compared peak business hours across store locations.
- Identified similarities and differences in demand patterns.

#### Customer Behaviour Analysis

- Analyzed customer purchasing behaviour at each location.
- Identified location-specific demand patterns and preferences.

#### Insights & Recommendations

- Summarized similarities and differences in temporal sales trends.
- Recommended location-specific staffing, inventory planning, and operational strategies.

- ### 📊 Dataset Description

**Dataset Name:** Aficionado Coffee Roasters - Sales Transaction Data (2025)

**Source:** Kaggle / Company Internal Data
**Total Records:** 149,116 rows
**Total Attributes:** 12 columns

**About the Dataset:**
This dataset contains detailed transaction records of a coffee shop chain across three locations - Astoria, Lower Manhattan, and Hell's Kitchen. It helps in analyzing time-based sales performance.

**Dataset Structure:**

| Column Name | Type | Description |
| :--- | :--- | :--- |
| transaction_id | Integer | Unique identifier for each transaction |
| transaction_date | Date | Date of the transaction |
| transaction_time | Time | Time of the transaction (Used for peak hour analysis) |
| transaction_qty | Integer | Quantity of products sold |
| store_location | String | Location of the store |
| product_category | String | Category like Coffee, Tea, Bakery |
| product_type | String | Sub-type like Latte, Espresso, etc. |
| product_detail | String | Detailed product name |
| unit_price | Float | Price per unit |
| total_sale | Float | Calculated as `transaction_qty * unit_price` - Total revenue |

**Key Columns Used for this Project:**
- `transaction_time` -> To find peak sales hours
- `store_location` -> To compare store performance  
- `product_category` & `product_detail` -> To find best-selling products
- `total_sale` -> To analyze revenue trends






