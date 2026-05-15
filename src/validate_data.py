import pandas as pd


def validate_data(df):

    negative_revenue = df[df["revenue"] < 0]
    expenses_exceed_revenue = df[df["expenses"] > df["revenue"]]
    required_columns = ["revenue", "expenses"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")
    if df.empty:
        raise ValueError("The uploaded file is empty")

    if df[required_columns].isnull().any().any():
        raise ValueError("Missing values found in revenue and expenses columns")
    
    if not pd.api.types.is_numeric_dtype(df["revenue"]):
        raise ValueError("Revenue column must be numeric")
    
    if not pd.api.types.is_numeric_dtype(df["expenses"]):
        raise ValueError("Expenses column must be numeric")
    
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if df["date"].isnull().any():
        raise ValueError("Invalid date format found in date column")
    
    negative_revenue = df[df["revenue"] < 0]
    expenses_exceed_revenue = df[df["expenses"] > df["revenue"]]
    results = {
        "negative_revenue_rows": len(negative_revenue),
        "expenses_exceed_revenue_rows": len(expenses_exceed_revenue)
    }
    
    print(results)

    return df