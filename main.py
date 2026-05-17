from src.load_data import load_data
from src.validate_data import validate_data
from src.transform_data import transform_data
from src.generate_report import generate_report

file_path = "data/raw_financials.csv"

df = load_data(file_path)

validation_results = validate_data(df)

df = transform_data(df)

generate_report(validation_results)

print("Pipeline completed successfully.")