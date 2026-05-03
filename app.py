import streamlit as st
import pandas as pd

st.title("📊 APL Logistics Profitability Dashboard")

# df = pd.read_csv("APL_small.csv", encoding='latin1')Load dataset

# KPIs
total_revenue = df['Sales'].sum()
total_profit = df['Order Profit Per Order'].sum()
profit_margin = (total_profit / total_revenue) * 100

st.metric("Total Revenue", round(total_revenue,2))
st.metric("Total Profit", round(total_profit,2))
st.metric("Profit Margin (%)", round(profit_margin,2))

# Category analysis
category = df.groupby('Category Name').agg({
    'Sales': 'sum',
    'Order Profit Per Order': 'sum'
}).reset_index()

category['Margin %'] = (category['Order Profit Per Order'] / category['Sales']) * 100

st.subheader("Category Profitability")
st.bar_chart(category.set_index('Category Name')['Margin %'])

# Top customers
customers = df.groupby('Customer Id').agg({
    'Sales': 'sum',
    'Order Profit Per Order': 'sum'
}).reset_index()

top_customers = customers.sort_values(by='Order Profit Per Order', ascending=False).head(10)

st.subheader("Top Customers")
st.dataframe(top_customers)
