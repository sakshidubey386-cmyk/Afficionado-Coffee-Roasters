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



## 🔍 Methodology

**1. Data Collection & Cleaning**
- Raw sales data ko Excel me import kiya
- Duplicate values, nulls aur wrong date formats remove kiye
- New columns banaye: `Hour`, `DayName`, `Month` for better analysis

**2. Data Modeling in Power BI**
- Date table banayi aur Sales table se relationship join ki
- Primary Key: `TransactionID` | Secondary Key: `ProductID`, `Date`
- DAX measures banaye: `Total Sales`, `YOY Growth %`, `Avg Transaction Value`

**3. Dashboard Development**
- 3 interactive pages banaye: Overview, Sales Trend, Product Analysis
- Slicers add kiye: Date, Product Category, Location
- Conditional formatting use ki for peak hours highlight

**4. Insights & Recommendations**
- Peak hours identify kiye for staff scheduling
- Monthly trend se low sales months nikale
- Top 5 products ka analysis karke inventory suggestion diya
