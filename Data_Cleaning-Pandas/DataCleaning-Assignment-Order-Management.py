import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("Order_Management_Sheet.csv")

print("---------------------------RAW DATA-----------------------------")
print(df.info())
print(df.head())


print("------------------------------------------TASK 1----------------------------------------------------")
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

print(df.head())

print("--------------------------------------------TASK 2-----------------------------------------")
df['Product Type'] = df['Aminu SKU'].apply(lambda x: 'Retail' if str(x).startswith('FG') else 'Professional') #PRODUCT TYPE

acct_mix = df.groupby('Account')['Product Type'].unique()   #ACCOUNT TYPE
df['Account Type'] = df['Account'].map(acct_mix.apply(lambda x: 'Hybrid' if len(x)>1 else x[0]))

df['Date'] = pd.to_datetime(df['Date']) #DISPATCH DATE
df['Expected Dispatch Date'] = df['Date'] + pd.offsets.BusinessDay(2)

df['Priority'] = np.where(df['Qty'] >= 10, 'High', 'Standard') #PRIORITY FLAG
df['Order Status'] = 'Pending'
df['Internal Notes'] = np.where(df['Priority'] == 'High', 'Bulk Order - Prioritize', 'Routine Order')  #INTERNAL NOTES


print(df.head())


print("------------------------------------------TASK 3------------------------------------------------------")
# 1. Create the base summary
order_summary = df.groupby('Order ID').agg(
    Order_Date=('Date', 'first'),
    Account=('Account', 'first'),
    Total_Value=('Final Price', 'sum'),
    Total_Qty=('Qty', 'sum'),
    SKU_Count=('Aminu SKU', 'nunique'),
    Order_Status=('Order Status', 'first')
).reset_index()

# 2. Calculate product mix (Keep Order ID as a column to merge on)
mix = df.groupby(['Order ID', 'Product Type']).size().unstack(fill_value=0).reset_index()

# 3. Merge them together
order_summary = pd.merge(order_summary, mix, on='Order ID')

# 4. Now create the string summary safely using the columns
order_summary['Mix_Summary'] = order_summary.apply(
    lambda x: f"Retail: {x['Retail']} | Pro: {x['Professional']}", axis=1
)
print(order_summary)




print("--------------------------TASK 4--------------------------------------------------------------------")
account_summary = df.groupby('Account').agg(
    Total_Orders=('Order ID', 'nunique'),
    Total_Revenue=('Final Price', 'sum')
).sort_values(by='Total_Revenue', ascending=False)

# --- 2. Account Segmentation (Retail vs Professional) ---
# Check what types of products each account has purchased
account_mix = df.groupby('Account')['Product Type'].unique()

retail_only = account_mix[account_mix.apply(lambda x: len(x) == 1 and x[0] == 'Retail')].index.tolist()
pro_only = account_mix[account_mix.apply(lambda x: len(x) == 1 and x[0] == 'Professional')].index.tolist()
hybrid = account_mix[account_mix.apply(lambda x: len(x) > 1)].index.tolist()

# --- 3. Pattern Analysis: Revenue by Category ---
category_performance = df.groupby('Category')['Final Price'].sum().sort_values(ascending=False)

# --- 4. Risk Analysis: Status & Concentration ---
status_risk = df['Order Status'].value_counts()
largest_order_val = df.groupby('Order ID')['Final Price'].sum().max()
total_revenue = df['Final Price'].sum()
concentration_risk = (largest_order_val / total_revenue) * 100

# --- OUTPUTS ---
print("TOP 5 ACCOUNTS BY REVENUE:")
print(account_summary.head(5))

print(f"\nACCOUNT SEGMENTATION:")
print(f"- Retail-only Accounts: {len(retail_only)}")
print(f"- Professional-only Accounts: {len(pro_only)}")
print(f"- Hybrid Accounts (Both): {len(hybrid)}")

print("\nREVENUE BY PRODUCT CATEGORY:")
print(category_performance.head(5))

print("\nOPERATIONAL RISKS:")
print(f"- Status Distribution:\n{status_risk}")
print(f"- Single Order Concentration: {concentration_risk:.2f}% of total revenue comes from one order.")
