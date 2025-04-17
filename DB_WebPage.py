import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import calendar
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Robot Analytics", layout="wide")

@st.cache_data
def load_data():
    engine = create_engine("mysql+mysqlconnector://root:admin@localhost/RobotAnalytics")
    facilities = pd.read_sql("SELECT * FROM Facilities", engine)
    robots = pd.read_sql("SELECT * FROM Robots", engine)
    performance = pd.read_sql("SELECT * FROM PerformanceMetrics", engine)
    models = pd.read_sql("SELECT * FROM RobotModels", engine)
    return robots, facilities, performance, models

robots_df, facilities_df, performance_df, models_df = load_data()

# Merge necessary information
robots_full = robots_df.merge(facilities_df, on="facility_id", how="left")
robots_full = robots_full.merge(models_df[['model_id', 'model_type']], on="model_id", how="left")
robots_full = robots_full.rename(columns={"model_type": "category"})

# Sidebar Navigation Menu
with st.sidebar:
    page = option_menu(
        menu_title="Robot Analytics Menu",
        options=["Welcome Page", "Overview", "Facility Overview", "Performance Metrics", "Maintenance & Events"],
        icons=["house", "bar-chart-line", "building", "speedometer", "tools"],
        default_index=0,
        styles={
            "container": {"padding": "10px"},
            "nav-link": {"font-size": "16px", "margin": "2px"},
            "nav-link-selected": {"background-color": "#dbeafe", "font-weight": "bold"},
        }
    )
# ------------------ PAGE: WELCOME ------------------
# ------------------ PAGE: WELCOME ------------------
if page == "Welcome Page":
    st.markdown(
        """
        <div style='text-align: center; margin-top: 80px;'>
            <h1 style='font-size: 50px; font-weight: bold; color: #3b0a55;'>
                ECE 9014 Group Project:<br>DB-Driven Analytic System for Industrial Robots
            </h1>
            <br><br>
            <h4 style='font-size: 22px; color: #3b0a55;'>(Group 3)</h4>
            <h4 style='font-size: 22px;'>Boyang Wang</h4>
            <h4 style='font-size: 22px;'>Haresh Sivakumar</h4>
            <h4 style='font-size: 22px;'>Sannjay Balaji</h4>
        </div>
        """,
        unsafe_allow_html=True
    )


# ------------------ PAGE: OVERVIEW ------------------
elif page == "Overview":
    st.title("Robot Deployment Overview")
    count_df = robots_full["facility_name"].value_counts().reset_index()
    count_df.columns = ["Facility", "Robot Count"]
    fig = px.bar(count_df, x="Facility", y="Robot Count", title="Robots per Facility",
                 color="Facility", color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig, use_container_width=True)

# ------------------ PAGE: FACILITY OVERVIEW ------------------
elif page == "Facility Overview":
    st.title("Facility and Robot Insights")

    col1, col2, col3 = st.columns(3)
    selected_fac = col1.selectbox("Facility", ["All"] + facilities_df["facility_name"].tolist())
    selected_cat = col2.selectbox("Category", ["All"] + robots_full["category"].dropna().unique().tolist())
    selected_stat = col3.selectbox("Status", ["All"] + robots_full["status"].dropna().unique().tolist())

    filtered = robots_full.copy()
    if selected_fac != "All":
        filtered = filtered[filtered["facility_name"] == selected_fac]
    if selected_cat != "All":
        filtered = filtered[filtered["category"] == selected_cat]
    if selected_stat != "All":
        filtered = filtered[filtered["status"] == selected_stat]

    col4, col5 = st.columns(2)
    bar_data = filtered["facility_name"].value_counts().reset_index()
    bar_data.columns = ["Facility", "Count"]
    fig_bar = px.bar(bar_data, x="Facility", y="Count", title="Robots per Facility",
                     color="Facility", color_discrete_sequence=px.colors.qualitative.Dark2)
    pie_fig = px.pie(filtered, names="category", title="Robot Distribution by Category",
                     color_discrete_sequence=px.colors.qualitative.Pastel1)
    col4.plotly_chart(fig_bar, use_container_width=True)
    col5.plotly_chart(pie_fig, use_container_width=True)

    col6, col7 = st.columns(2)
    fig_donut = px.pie(filtered, names="status", hole=0.5, title="Status Distribution",
                       color_discrete_sequence=px.colors.qualitative.Bold)
    filtered["year"] = pd.to_datetime(filtered["installation_date"]).dt.year
    fig_hist = px.histogram(filtered, x="year", nbins=10, title="Installations by Year",
                            color_discrete_sequence=px.colors.qualitative.Set2)
    col6.plotly_chart(fig_donut, use_container_width=True)
    col7.plotly_chart(fig_hist, use_container_width=True)

# ------------------ PAGE: PERFORMANCE METRICS ------------------
elif page == "Performance Metrics":
    st.title("Robot Performance Metrics")

    performance_df['timestamp'] = pd.to_datetime(performance_df['timestamp'])
    performance_df['month'] = performance_df['timestamp'].dt.month
    performance_df['month_name'] = performance_df['month'].apply(lambda x: calendar.month_abbr[x])

    col1, col2 = st.columns(2)
    selected_facility = col1.selectbox("Select Facility", ["All"] + facilities_df["facility_name"].tolist())
    selected_metric = col2.selectbox("Select Metric", ["efficiency", "energy_consumption", "cycle_time"])

    perf_data = performance_df.copy()
    if selected_facility != "All":
        perf_data = perf_data[perf_data["facility_name"] == selected_facility]

    # Monthly Box Plot
    st.subheader(f"Monthly {selected_metric.title()} Distribution (Box Plot)")
    fig_box = px.box(
        perf_data,
        x="month_name",
        y=selected_metric,
        points="all",
        title=f"{selected_metric.title()} Distribution by Month",
        color_discrete_sequence=["#1f77b4"]
    )
    st.plotly_chart(fig_box, use_container_width=True)

    # Scatter Plot
    st.subheader(f"{selected_metric.title()} Over Time (Scatter Plot)")
    fig_scatter = px.scatter(
        perf_data,
        x="timestamp",
        y=selected_metric,
        color="robot_id",
        opacity=0.4,
        title=f"{selected_metric.title()} Density Over Time",
        color_discrete_sequence=px.colors.qualitative.Light24
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Bubble Chart
    perf_data['timestamp'] = pd.to_datetime(perf_data['timestamp'])
    perf_data['month_str'] = perf_data['timestamp'].dt.to_period("M").astype(str)
    bubble_data = perf_data.groupby(["robot_id", "month_str"])[selected_metric].mean().reset_index()

    fig_bubble = px.scatter(
        bubble_data,
        x="month_str",
        y="robot_id",
        size=selected_metric,
        color=selected_metric,
        title=f"Bubble Chart: Robot vs Month Avg {selected_metric.title()}",
        size_max=30,
        color_continuous_scale="Plasma",
        labels={selected_metric: f"Avg {selected_metric.title()}"}
    )
    st.plotly_chart(fig_bubble, use_container_width=True)

# ------------------ PAGE: MAINTENANCE & EVENTS ------------------
elif page == "Maintenance & Events":
    st.title("Maintenance Metrics (Performance-Based)")

    col1, col2 = st.columns(2)
    selected_fac = col1.selectbox("Facility", ["All"] + facilities_df["facility_name"].tolist(), key="fac4")
    energy_threshold = col2.slider("Energy Threshold (Wh)", 1, 30, 10)

    perf_full = performance_df.merge(robots_full[["robot_id", "facility_name"]], on="robot_id", how="left")
    if selected_fac != "All":
        perf_full = perf_full[perf_full["facility_name"] == selected_fac]

    st.subheader("High Energy Cycles")
    high_energy = perf_full[perf_full["energy_consumption"] > energy_threshold]
    count_energy = high_energy["robot_id"].value_counts().reset_index()
    count_energy.columns = ["Robot ID", "High Energy Cycles"]
    fig_energy = px.bar(count_energy, x="Robot ID", y="High Energy Cycles",
                        color_discrete_sequence=px.colors.qualitative.Pastel2)
    st.plotly_chart(fig_energy, use_container_width=True)

    st.subheader("Efficiency Heatmap (Avg. per Robot Daily)")
    perf_full["date"] = pd.to_datetime(perf_full["timestamp"]).dt.date
    heat_data = perf_full.groupby(["robot_id", "date"])["efficiency"].mean().reset_index()
    fig_heat = px.density_heatmap(heat_data, x="date", y="robot_id", z="efficiency",
                                   color_continuous_scale="Hot")
    st.plotly_chart(fig_heat, use_container_width=True)

    st.subheader("Efficiency Levels")
    perf_full["eff_level"] = perf_full["efficiency"].apply(lambda e: "Low" if e < 70 else "Medium" if e < 90 else "High")
    stacked = perf_full.groupby(["robot_id", "eff_level"]).size().reset_index(name="count")
    fig_stack = px.bar(stacked, x="robot_id", y="count", color="eff_level", barmode="stack",
                       color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig_stack, use_container_width=True)

    st.subheader("Low Efficiency Cycles")
    low_eff = perf_full[perf_full["efficiency"] < 70]
    low_eff_count = low_eff.groupby("robot_id").size().reset_index(name="Low Eff. Cycles")
    fig_low = px.bar(low_eff_count, x="robot_id", y="Low Eff. Cycles",
                     color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig_low, use_container_width=True)

    st.subheader("Efficiency Scatter Plot (All Robots)")
    fig_scatter = px.scatter(perf_full, x="timestamp", y="efficiency", color="robot_id",
                             opacity=0.4, title="Efficiency Over Time",
                             color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Monthly Efficiency Box Plot")
    perf_full["month"] = pd.to_datetime(perf_full["timestamp"]).dt.to_period("M").astype(str)
    fig_box = px.box(perf_full, x="month", y="efficiency", points="all", title="Efficiency Distribution by Month",
                     color_discrete_sequence=["#1f77b4"])