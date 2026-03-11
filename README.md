# Financial Report Validator

A Python project that reads financial CSV data and checks for issues such as negative revenue and expenses greater than revenue.

## Features

- Loads CSV financial data with pandas
- Detects negative revenue
- Detects rows where expenses exceed revenue
- Simple project structure for validation workflows

## Tech Used

- Python
- pandas
- CSV

## Project Structure

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