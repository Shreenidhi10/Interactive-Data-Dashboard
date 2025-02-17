import plotly.express as px

def create_bar_chart(data):
    return px.bar(
        data,
        x="subcategory",
        y="value",
        color="subcategory",
        title="Bar Chart",
    )

def create_line_chart(data):
    return px.line(
        data,
        x="date",
        y="value",
        color="subcategory",
        title="Line Chart",
    )

def create_pie_chart(data):
    return px.pie(
        data,
        names="subcategory",
        values="value",
        title="Pie Chart",
    )

def create_heatmap(data):
    return px.density_heatmap(
        data,
        x="subcategory",
        y="date",
        z="value",
        color_continuous_scale="Viridis",
        title="Heatmap",
    )

def create_sunburst_chart(data):
    return px.sunburst(
        data,
        path=["category", "subcategory"],
        values="value",
        title="Sunburst Chart",
    )
