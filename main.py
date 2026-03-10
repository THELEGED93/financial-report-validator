import pandas as pd
import requests
from io import BytesIO

# -----------------------------
# 1. DOWNLOAD ZILLOW DATA
# -----------------------------
url = "https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"

print("Downloading Zillow data...")
response = requests.get(url)
raw = pd.read_csv(BytesIO(response.content))

# -----------------------------
# 2. FILTER FOR FLORIDA METROS
# -----------------------------
fl = raw[raw['State'] == 'FL']

# -----------------------------
# 3. TRANSFORM: MELT TIME-SERIES
# -----------------------------
value_vars = fl.columns[7:]  # dates start at column 8

fl_melted = fl.melt(
    id_vars=['RegionID', 'RegionName', 'City', 'State'],
    value_vars=value_vars,
    var_name='Date',
    value_name='HomeValue'
)

# Convert date column to datetime
fl_melted['Date'] = pd.to_datetime(fl_melted['Date'])

# -----------------------------
# 4. ADD FEATURES
# -----------------------------
# YoY % Change
fl_melted['YoY_Change'] = fl_melted.groupby('RegionID')['HomeValue'].pct_change(12) * 100

# 3-Month Rolling Average
fl_melted['Rolling_3M'] = (
    fl_melted.groupby('RegionID')['HomeValue']
    .rolling(3)
    .mean()
    .reset_index(level=0, drop=True)
)

# -----------------------------
# 5. SAVE CLEANED DATA
# -----------------------------
output_path = "data_clean/florida_cleaned_data.csv"
fl_melted.to_csv(output_path, index=False)

print(f"Cleaned Florida housing data saved to {output_path}")
