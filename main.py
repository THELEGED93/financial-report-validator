from src.load_data import load_data
from src.validate_data import validate_data
from src.transform_data import transform_data
from src.generate_report import generate_report

data = load_data("data/raw_financials.csv")

validated_data = validate_data(data)

transformed_data = transform_data(validated_data)

generate_report(transformed_data)

print("Pipeline completed successfully.")