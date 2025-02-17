# README.md

# Interactive Data Dashboard

## Project Overview

This project is an interactive and visually engaging data dashboard built with Streamlit and Plotly. It allows users to explore data insights using various filters and visualizations such as bar charts, line charts, pie charts, heatmaps, and sunburst charts. The dashboard is modern, user-friendly, and styled with a professional design inspired by Telegram Trends.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <https://github.com/Shreenidhi10/Interactive-Data-Dashboard>
   cd <Interactive-Data-Dashboard>
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your dataset (`data.csv`) in the project root directory.

## Deployment Steps

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t interactive-dashboard .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8501:8501 interactive-dashboard
   ```
3. Access the dashboard at `http://localhost:8501`.

### Manual Deployment

1. Run the Streamlit app:
   ```bash
   streamlit run src/app.py
   ```
2. Open your browser and navigate to the displayed local URL.

## Technology Stack Used

- **Frontend:** Streamlit (Python-based interactive web app framework)
- **Visualization:** Plotly (for creating engaging and interactive charts)
- **Backend:** Python
- **Containerization:** Docker (for easy deployment and scaling)
- **Logging:** Python's logging module

---

Enjoy exploring the data!
