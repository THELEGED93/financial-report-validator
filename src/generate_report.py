def generate_report(results):

    report = f"""
Validation Report
------------------
Negative Revenue Rows: {results["negative_revenue_rows"]}
Expenses > Revenue Rows: {results["expenses_exceed_revenue_rows"]}
"""

    with open("output/validation_report.txt", "w") as f:
        f.write(report)

    print("Report generated in output folder")