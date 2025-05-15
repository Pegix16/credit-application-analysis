# Credit Application Analysis (SQL + Python)

This project analyzes credit application data using MySQL and Python. The analysis includes data import, basic SQL exploration, and visualization using matplotlib.

## 📂 Files

- `credit_applications.csv` – Sample credit application data
- `create_credit_app_db.sql` – SQL script to create the database and import data
- `analyze_applications.py` – Python script for data analysis and visualization

## 🧰 Tools Used

- MySQL (Workbench)
- Python 3
  - `mysql-connector-python`
  - `pandas`
  - `matplotlib`

## 📊 Analysis Highlights

- Total applications
- Approval rate
- Average income
- Maximum loan request
- Rejected applicants
- Bar chart of loan amounts by applicant

## 📸 Sample Output

![Loan Amount Chart](./loan_amount_chart.png)

## 🚀 How to Run

1. Create database from `create_credit_app_db.sql` in MySQL Workbench
2. Run Python script:
```bash
python3 analyze_applications.py
