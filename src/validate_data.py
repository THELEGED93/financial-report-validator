def validate_data(df):

    negative_revenue = df[df["revenue"] < 0]
    expenses_exceed_revenue = df[df["expenses"] > df["revenue"]]

    results = {
        "negative_revenue_rows": len(negative_revenue),
        "expenses_exceed_revenue_rows": len(expenses_exceed_revenue)
    }

    return results