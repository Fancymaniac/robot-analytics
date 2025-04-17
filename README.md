```markdown
#  DB-Driven Analytic Systems for Industrial Robots

This project presents a comprehensive, database-driven analytics system designed to monitor, analyze, and optimize the performance of industrial robotic arms across multiple facilities.

---

##  Project Structure

```bash
├── DB_WebPage.py                 # Streamlit dashboard for visualizing robot metrics
├── DB_RoboticsMLModel.ipynb      # Jupyter notebook for predictive maintenance using ML
├── Sql_Export/                   # SQL files for setting up the database schema
│   ├── robotanalytics_*.sql      # Individual SQL schema files (alerts, events, robots, etc.)
└── README.md                     # You're here!
```

---

## Features

-  **Normalized SQL schema (3NF)** for efficient data storage and analysis
-  **Streamlit-based web dashboard** to explore robot performance and events
-  **Machine Learning model** (Random Forest) for predicting robot maintenance risk
-  Real-time integration with MySQL backend
-  Modular file structure for deployment and testing

---

##  How to Run

1. **Set up MySQL Database**  
   - Execute all `.sql` files from the `Sql_Export/` folder in your MySQL server.

2. **Run the Web Dashboard**
   ```bash
   streamlit run DB_WebPage.py
   ```

3. **Explore ML Predictions**
   - Open `DB_RoboticsMLModel.ipynb` in Jupyter Notebook or VS Code
   - Follow the notebook to retrain or test the Random Forest model

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Sample Dashboards

The dashboard displays:
- Efficiency, energy, and cycle time analytics
- Facility-wise robot deployment
- Maintenance history and fault trends

---

## Authors

- **Boyang Wang** – Streamlit & visualization
- **Haresh Sivakumar** – SQL schema design & integration
- **Sannjay Balaji** – Machine Learning & predictive modeling

---

## License

This project is for academic use only. Licensing can be added if extended for public or industrial deployment.
```
