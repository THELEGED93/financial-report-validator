# Financial Report Validator

<<<<<<< HEAD
A Python project that reads financial CSV data, checks for issues like negative revenue and expenses greater than revenue, and helps validate reporting data.

## Features
=======
A Python project that reads financial CSV data and checks for issues such as negative revenue and expenses greater than revenue.

## Features

>>>>>>> 0f58be5838b9413550c1dba6622da7d2c7f383ea
- Loads CSV financial data with pandas
- Detects negative revenue
- Detects rows where expenses exceed revenue
- Simple project structure for validation workflows

## Tech Used
<<<<<<< HEAD
=======

>>>>>>> 0f58be5838b9413550c1dba6622da7d2c7f383ea
- Python
- pandas
- CSV

## Project Structure
<<<<<<< HEAD
```text
data/
output/
src/
main.py
=======

```
financial_validator
│
├── data/
│   └── raw_financials.csv
│
├── output/
│   ├── clean_financials.csv
│   └── validation_report.txt
│
├── src/
│   ├── load_data.py
│   ├── validate_data.py
│   ├── transform_data.py
│   └── generate_report.py
│
├── main.py
└── requirements.txt
```

## How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Run the program:

```
python main.py
```
>>>>>>> 0f58be5838b9413550c1dba6622da7d2c7f383ea
