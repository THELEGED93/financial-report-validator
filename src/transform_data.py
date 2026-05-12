def transform_data(df):

    df["profit"] = df["revenue"] - df["expenses"]
    
    return df