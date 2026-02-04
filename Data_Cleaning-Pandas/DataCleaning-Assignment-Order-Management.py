import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("Order_Management_Sheet.csv")

print("---------------------------RAW DATA-----------------------------")
print(df.info())

# 1. Drop completely empty columns and rows without an Order ID
df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col])
df = df.dropna(subset=['Order ID'])

# 2. Convert date columns to datetime objects
# dayfirst=True is often needed if your CSV uses DD-MM-YY format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
df['Appoint. Date'] = pd.to_datetime(df['Appoint. Date'], dayfirst=True, errors='coerce')

# 3. Robust Numeric Cleaning Function
def clean_numeric(value):
    if pd.isna(value):
        return 0.0
    if isinstance(value, str):
        # Remove currency symbols, commas, and percentage signs
        clean_val = value.replace('%', '').replace(',', '').replace('₹', '').strip()
        try:
            return float(clean_val)
        except ValueError:
            return 0.0
    return float(value)

# Apply to numeric columns
numeric_cols = ['Unit Price', 'Treat Disc', 'Retail Disc', 'Base Price', 'GST', 'Final Price', 'Qty']
for col in numeric_cols:
    df[col] = df[col].apply(clean_numeric)

# 4. Standardize Percentages (Converting 36.0 to 0.36)
df['Treat Disc'] = df['Treat Disc'] / 100
df['Retail Disc'] = df['Retail Disc'] / 100

# 5. Clean Text Fields
text_cols = ['Account', 'Aminu SKU', 'Category']
for col in text_cols:
    df[col] = df[col].fillna('Unknown').astype(str).str.strip()

# 6. Operational Logic Enhancements
# Convert Order ID to Int
df['Order ID'] = df['Order ID'].astype(int)

# Fill boolean check - assuming False if missing
df['Check (R/T)'] = df['Check (R/T)'].fillna(False)


print("-------------------------------DATA AFTER CLEANING---------------------------------")
print(df.head())
