
# Database-Driven Analytics System for Industrial Robots

This repository contains the **Database-Driven Analytics System for Industrial Robots**, a complete solution designed and implemented for the ECE 9014 graduate course project.

## Project Overview

This project features a real-time analytics dashboard built on top of a normalized **MySQL relational database** designed to monitor and evaluate industrial robot performance. The database includes 11 interconnected tables covering:

- Facilities
- Robot Models
- Robots
- Sensors
- Performance Metrics
- Event Logs
- Event Types
- Operators
- Operation Logs
- Alert Configurations (optional)
- Machine Learning Models

All tables follow 3NF normalization, ensuring consistency, minimal redundancy, and easy scalability.

## Dashboard Features (Built with Streamlit + Plotly)

The analytics dashboard is structured into four main pages:

### 1. Overview
- Robot distribution across facilities
- Facility-wise installation metrics

### 2. Facility Overview
- Robot status (Active, Maintenance, Offline)
- Distribution by model categories
- Installation timelines

### 3. Performance Metrics
- Monthly efficiency/cycle time/energy analysis via box plots
- Metric density over time using scatter plots
- Robot vs Month bubble chart
- Top-5 performing robots (line chart)

### 4. Maintenance & Events
- High energy consumption cycles
- Efficiency heatmaps (robot vs date)
- Event count breakdowns by severity
- Efficiency level stack plots

## Machine Learning Integration

The notebook [`DB_RoboticsMLModel.ipynb`](./DB_RoboticsMLModel.ipynb) demonstrates how performance data from the SQL database can be used to build machine learning models. It includes:

- Data extraction using SQLAlchemy
- Feature engineering
- Model training (e.g., Linear Regression)
- Performance metrics (RMSE, MAE)
- Baseline setup for predictive maintenance tasks

## Technologies Used

- **Frontend:** Streamlit, Plotly
- **Backend:** MySQL, SQLAlchemy
- **ML & Data:** Pandas, scikit-learn, NumPy
- **Database Tools:** MySQL Workbench, ERD Modeling

## Repository Structure

```
.
├── streamlit_app.py               # Main Streamlit dashboard
├── DB_RoboticsMLModel.ipynb       # ML model for robot performance
├── RobotAnalytics.sql             # Database schema & sample data
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
```

## 👨‍💻 Contributors

- **Boyang Wang**
- **Haresh Sivakumar**
- **Sannjay Balaji**
