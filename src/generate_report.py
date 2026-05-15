def generate_report(df):
    negative_revenue = df[df["revenue"] < 0]
    expenses_exceed_revenue = df[df["expenses"] > df["revenue"]]

    report = f"""
Financial Validation Report
---------------------------
Total Rows: {len(df)}
Negative Revenue Rows: {len(negative_revenue)}
Expenses > Revenue Rows: {len(expenses_exceed_revenue)}
"""

    with open("output/validation_report.txt", "w") as f:
        f.write(report)

    print("Report generated in output folder")