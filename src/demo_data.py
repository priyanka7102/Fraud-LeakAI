import pandas as pd

def get_demo_transactions():
    data = [
        {"date": "2025-11-01", "vendor": "ABC Ltd", "amount": 50000, "description": "Office Supplies"},
        {"date": "2025-11-02", "vendor": "XYZ Pvt Ltd", "amount": 75000, "description": "Consulting Fee"},
        {"date": "2025-11-02", "vendor": "ABC Ltd", "amount": 50000, "description": "Office Supplies"},  # duplicate
        {"date": "2025-11-03", "vendor": "Ghost Vendor", "amount": 100000, "description": "Suspicious Payment"},
        {"date": "2025-11-04", "vendor": "LMN Corp", "amount": 100000, "description": "Round Figure Payment"},
    ]
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = get_demo_transactions()
    print(df)
