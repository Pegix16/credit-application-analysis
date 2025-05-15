import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",  # Replace with your actual password
    database="credit_app_db"
)

# Query to fetch data
query = "SELECT applicant_name, loan_amount FROM credit_applications WHERE applicant_name IS NOT NULL"
df = pd.read_sql(query, conn)

# Print DataFrame to verify it's not empty
print("DataFrame:\n", df)

# Check if DataFrame is empty
if df.empty:
    print("⚠️ The DataFrame is empty. Check your database table.")
else:
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(df['applicant_name'], df['loan_amount'], color='skyblue')
    plt.xlabel('Applicant Name')
    plt.ylabel('Loan Amount')
    plt.title('Loan Amount Requested by Each Applicant')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Close the connection
conn.close()
