import datatable as dt
from datatable import f, by, sort # type: ignore

# 1. Create a Frame (The 'datatable' version of a DataFrame)
data = {
    "ID": range(5),
    "City": ["London", "New York", "London", "Paris", "New York"],
    "Sales": [100, 250, 150, 300, 200]
}
df = dt.Frame(data)

print("--- Original Frame ---")
print(df)

# 2. Filter and Select (Using the 'f' expression)
# Selecting rows where City is London and only the ID and Sales columns
london_sales = df[f.City == "London", ["ID", "Sales"]]

print("\n--- Filtered: London Sales ---")
print(london_sales)

# 3. GroupBy and Aggregate
# Calculate total sales by City
analysis = df[:, dt.sum(f.Sales), by("City")]

print("\n--- Aggregated: Sales by City ---")
print(analysis)

# 4. Fast conversion to Pandas (if needed)
pandas_df = df.to_pandas()