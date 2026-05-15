from src.load_data import load_data
from src.validate_data import validate_data
from src.transform_data import transform_data
from src.generate_report import generate_report

<<<<<<< HEAD
data = load_data("data/raw_financials.csv")

validated_data = validate_data(data)

transformed_data = transform_data(validated_data)

generate_report(transformed_data)
=======
file_path = "data/raw_financials.csv"

df = load_data(file_path)

validation_results = validate_data(df)

df = transform_data(df)

generate_report(validation_results)
>>>>>>> 0f58be5838b9413550c1dba6622da7d2c7f383ea

print("Pipeline completed successfully.")