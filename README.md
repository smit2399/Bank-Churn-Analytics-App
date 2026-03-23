# 🏦 European Bank Customer Churn Analytics

### Customer Segmentation & Churn Pattern Analytics Web Application

An interactive **Streamlit web application** designed to analyze customer churn behavior in a European banking dataset.
The application enables users to explore **churn patterns, customer segmentation, and high-value customer risk** through dynamic visualizations and KPI metrics.

This project demonstrates a complete **end-to-end data analytics workflow**, including:

* Data cleaning and feature engineering
* Exploratory Data Analysis (EDA)
* Customer segmentation analytics
* Interactive dashboard development with Streamlit

---

# 📊 Project Overview

Customer churn represents a significant challenge in retail banking. Losing existing customers results in:

* Reduced customer lifetime value
* Increased acquisition costs
* Revenue instability

This project addresses these challenges by building an **interactive analytics platform** that allows business users to explore churn behavior across multiple customer segments.

---

# 🚀 Live Web Application

After deployment, the application can be accessed here:

```
https://bank-churn-analytics-app.streamlit.app/
```

---

# 📈 Key Performance Indicators (KPIs)

The dashboard monitors several key business metrics:

| KPI                         | Description                                 |
| --------------------------- | ------------------------------------------- |
| **Total Customers**         | Total customers in selected filters         |
| **Overall Churn Rate**      | Percentage of customers who exited          |
| **High Value Churn**        | Churn rate among premium customers          |
| **Inactive Customer Churn** | Churn rate among inactive members           |
| **Segment Churn Rate**      | Churn distribution across customer segments |
| **Geographic Risk Index**   | Regional churn exposure                     |

---

# 🖥️ Final Web App Layout

```
------------------------------------------------
European Bank Customer Churn Analytics
------------------------------------------------

KPIs
Total Customers | Churn Rate | High Value | Inactive

------------------------------------------------
Geography Risk Index

Churn by Country
------------------------------------------------

Age vs Tenure Churn

Age Group Chart
Tenure Chart
------------------------------------------------

High Value Customer Explorer

Balance vs Salary Scatter
------------------------------------------------

Customer Segmentation

Churn by Balance Segment
------------------------------------------------
```

---

# 📊 Dashboard Features

### 1️⃣ Overall Churn Summary

Provides a quick overview of key churn metrics:

* Total customers
* Overall churn rate
* High-value customer churn
* Inactive customer churn

---

### 2️⃣ Geography Risk Analysis

Visualizes regional churn patterns to identify high-risk markets.

Example insight:

* Germany typically shows higher churn rates compared to France and Spain.

---

### 3️⃣ Age & Tenure Churn Comparison

Analyzes how churn behavior varies across:

* Age groups
* Customer tenure segments

This helps identify **loyal vs at-risk customer cohorts**.

---

### 4️⃣ High Value Customer Explorer

Investigates churn behavior among high-balance customers.

Visualization:

* **Balance vs Salary Scatter Plot**

This helps identify **high-value customers at risk of leaving**.

---

### 5️⃣ Customer Segmentation Analysis

Explores churn patterns across customer segments such as:

* Balance segments
* Product ownership
* Engagement levels

---

# 🎛️ Interactive User Capabilities

The application supports interactive exploration through:

✔ Geography filters
✔ Gender filters
✔ Product filters
✔ Dynamic KPI updates
✔ Drill-down visualizations

These capabilities allow business users to **analyze churn patterns from multiple perspectives**.

---

# 📂 Project Structure

```
bank-churn-streamlit-app
│
├── app.py
├── data
│   └── cleaned_data_European_Bank.csv
│
├── requirements.txt
└── README.md
```

---

# 🛠️ Technology Stack

| Tool             | Purpose                    |
| ---------------- | -------------------------- |
| **Python**       | Data processing            |
| **Pandas**       | Data analysis              |
| **Plotly**       | Interactive visualizations |
| **Streamlit**    | Web application framework  |
| **Scikit-Learn** | Machine learning utilities |

---

# ⚙️ Installation & Setup

### Clone the repository

```bash
git clone https://github.com/yourusername/bank-churn-streamlit-app.git
```

### Navigate to project folder

```bash
cd bank-churn-streamlit-app
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit app

```bash
streamlit run app.py
```

The application will launch at:

```
http://localhost:8501
```

---

# 📊 Dataset Description

The dataset contains customer information from a European bank.

| Feature         | Description                |
| --------------- | -------------------------- |
| CustomerId      | Unique customer identifier |
| Geography       | Customer country           |
| Gender          | Male / Female              |
| Age             | Customer age               |
| Tenure          | Years with the bank        |
| Balance         | Account balance            |
| NumOfProducts   | Number of bank products    |
| HasCrCard       | Credit card ownership      |
| IsActiveMember  | Customer activity status   |
| EstimatedSalary | Estimated annual salary    |
| Exited          | Churn indicator            |

---

# 📌 Example Business Insights

Key insights discovered during analysis include:

• Germany has the **highest churn rate among regions**
• Customers with **only one product churn significantly more**
• **Inactive customers are nearly twice as likely to churn**
• **High balance customers represent major revenue risk when they churn**

---

# 📈 Future Enhancements

Planned improvements include:

* Churn prediction model (XGBoost)
* Customer segmentation using K-Means clustering
* SHAP explainable AI analysis
* Customer lifetime value (CLV) modeling
* Power BI executive dashboard

---

# 👨‍💻 Author

**Smit Prajapati**

Data Analyst / Data Science Enthusiast
Passionate about building **data-driven solutions and analytics applications**.

---

# ⭐ If You Found This Project Useful

Please consider giving the repository a **⭐ star** on GitHub!
