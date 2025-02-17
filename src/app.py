# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from utils import log_error, log_info
from visualization import (
    create_bar_chart,
    create_line_chart,
    create_pie_chart,
    create_heatmap,
    create_sunburst_chart
)
from data_loader import load_data

st.set_page_config(page_title="Interactive Data Dashboard", layout="wide", page_icon="📊")

data = load_data('data.csv')

data['date'] = pd.to_datetime(data['date'], errors='coerce')

st.sidebar.header("Filters")
selected_category = st.sidebar.selectbox(
    "Select Category:", data['category'].unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range:", []
)

filtered_data = data[data['category'] == selected_category]
if date_range and len(date_range) == 2:
    filtered_data = filtered_data[
        (filtered_data['date'] >= pd.to_datetime(date_range[0])) &
        (filtered_data['date'] <= pd.to_datetime(date_range[1]))
    ]

st.title("Interactive Data Dashboard")
st.write("Explore interactive and visually engaging data insights.")

# Bar Chart
st.subheader("Category Breakdown (Bar Chart)")
bar_chart = px.bar(
    filtered_data,  
    x="subcategory", 
    y="value",
    color="subcategory",  
    color_discrete_sequence=["#0088CC", "#33BBFF", "#99E6FF"],
    title="Category Breakdown"
)
bar_chart.update_layout(
    title_font_size=18,
    font_family="Roboto",
    paper_bgcolor="#F3F6FA",
    plot_bgcolor="#FFFFFF",
    title_font_color="#0088CC",
    font_color="#333333",
    margin=dict(l=20, r=20, t=40, b=20)
)
st.plotly_chart(bar_chart, use_container_width=True)

# Line Chart
st.subheader("Trend Over Time (Line Chart)")
line_fig = create_line_chart(filtered_data)
line_fig.update_layout(
    paper_bgcolor="#F3F6FA",
    plot_bgcolor="#FFFFFF",
    title_font_color="#0088CC",
    font_color="#333333",
    font_family="Roboto"
)
st.plotly_chart(line_fig, use_container_width=True)

# Pie Chart
st.subheader("Proportion Analysis (Pie Chart)")
pie_fig = create_pie_chart(filtered_data)
pie_fig.update_layout(
    paper_bgcolor="#F3F6FA",
    title_font_color="#0088CC",
    font_color="#333333",
    font_family="Roboto"
)
st.plotly_chart(pie_fig, use_container_width=True)

# Heatmap
st.subheader("Value Distribution (Heatmap)")
heatmap_fig = create_heatmap(filtered_data)
heatmap_fig.update_layout(
    paper_bgcolor="#F3F6FA",
    font_color="#333333",
    font_family="Roboto"
)
st.plotly_chart(heatmap_fig, use_container_width=True)

# Sunburst Chart
st.subheader("Hierarchical Breakdown (Sunburst Chart)")
sunburst_fig = create_sunburst_chart(filtered_data)
sunburst_fig.update_layout(
    paper_bgcolor="#F3F6FA",
    font_color="#333333",
    font_family="Roboto"
)
st.plotly_chart(sunburst_fig, use_container_width=True)
