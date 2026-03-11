import pandas as pd

# File location
file_path = "data/raw_financials.csv"

# Load the CSV
df = pd.read_csv(file_path)

print("\nFinancial Data Loaded:\n")
print(df)

print("\n--- Running Basic Validation ---\n")

# Check for negative revenue
neg_revenue = df[df["revenue"] < 0]

# Check for expenses greater than revenue
bad_expenses = df[df["expenses"] > df["revenue"]]

if not neg_revenue.empty:
    print("Rows with negative revenue:")
    print(neg_revenue)

if not bad_expenses.empty:
    print("\nRows where expenses exceed revenue:")
    print(bad_expenses)

print("\nValidation complete.")