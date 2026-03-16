#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Bank Customer Churn Analytics",
    layout="wide"
)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_data_European_Bank.csv")
    return df

df = load_data()

st.title("European Bank Customer Churn Analytics")

st.markdown("Interactive analytics dashboard for customer segmentation and churn risk.")

# ---------------------------
# SIDEBAR FILTERS
# ---------------------------

st.sidebar.header("Customer Filters")

geo = st.sidebar.multiselect(
    "Geography",
    options=df["Geography"].unique(),
    default=df["Geography"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

products = st.sidebar.multiselect(
    "Number of Products",
    options=df["NumOfProducts"].unique(),
    default=df["NumOfProducts"].unique()
)

filtered_df = df[
    (df["Geography"].isin(geo)) &
    (df["Gender"].isin(gender)) &
    (df["NumOfProducts"].isin(products))
]

# ---------------------------
# KPI SECTION
# ---------------------------

total_customers = len(filtered_df)

churn_rate = filtered_df["Exited"].mean() * 100

high_value = filtered_df[filtered_df["Balance"] > 100000]

high_value_churn = high_value["Exited"].mean() * 100

inactive = filtered_df[filtered_df["IsActiveMember"] == 0]

inactive_churn = inactive["Exited"].mean() * 100

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Customers", total_customers)

col2.metric("Overall Churn Rate", f"{churn_rate:.2f}%")

col3.metric("High Value Churn", f"{high_value_churn:.2f}%")

col4.metric("Inactive Customer Churn", f"{inactive_churn:.2f}%")

st.divider()

# ---------------------------
# GEOGRAPHY CHURN ANALYSIS
# ---------------------------

st.subheader("Geography Risk Index")

geo_churn = filtered_df.groupby("Geography")["Exited"].mean().reset_index()

fig_geo = px.bar(
    geo_churn,
    x="Geography",
    y="Exited",
    color="Geography",
    title="Churn Rate by Geography"
)

st.plotly_chart(fig_geo, use_container_width=True)

# ---------------------------
# AGE VS TENURE CHURN
# ---------------------------

st.subheader("Age vs Tenure Churn Analysis")

age_churn = filtered_df.groupby("AgeGroup")["Exited"].mean().reset_index()

fig_age = px.bar(
    age_churn,
    x="AgeGroup",
    y="Exited",
    color="AgeGroup",
    title="Churn Rate by Age Group"
)

st.plotly_chart(fig_age, use_container_width=True)

tenure_churn = filtered_df.groupby("TenureGroup")["Exited"].mean().reset_index()

fig_tenure = px.bar(
    tenure_churn,
    x="TenureGroup",
    y="Exited",
    color="TenureGroup",
    title="Churn Rate by Tenure Group"
)

st.plotly_chart(fig_tenure, use_container_width=True)

# ---------------------------
# HIGH VALUE CUSTOMER EXPLORER
# ---------------------------

st.subheader("High Value Customer Churn Explorer")

fig_scatter = px.scatter(
    filtered_df,
    x="EstimatedSalary",
    y="Balance",
    color="Exited",
    title="Balance vs Salary"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# ---------------------------
# SEGMENT CHURN
# ---------------------------

st.subheader("Customer Segment Churn")

segment = filtered_df.groupby("BalanceSegment")["Exited"].mean().reset_index()

fig_segment = px.bar(
    segment,
    x="BalanceSegment",
    y="Exited",
    color="BalanceSegment",
    title="Churn by Balance Segment"
)

st.plotly_chart(fig_segment, use_container_width=True)


# In[ ]:




