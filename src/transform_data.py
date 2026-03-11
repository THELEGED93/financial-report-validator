def transform_data(df):

    df["profit"] = df["revenue"] - df["expenses"]

    df.to_csv("output/clean_financials.csv", index=False)

    return df