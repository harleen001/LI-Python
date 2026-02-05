import pandas as pd
#Sample DataFrame with missing values
df = pd.DataFrame({
    'Name': ['David', 'Annabel', 'Charlie', None],
    'Age': [25, 30, None, 22],
    'Salary': [50000, None, 70000, 60000]
})

print("-----------------------1. Fill missing values with a constant---------------------------")
df_filled = df.fillna(value={'Name': 'Unknown', 'Age': 0, 'Salary': 0})
print(df_filled)

print("-----------------------2. Drop Duplicates-------------------------------------")
clean_df = df.drop_duplicates()
print(clean_df)


print("----------------3. Detects duplicate values----------------------------")
duplicates = df.duplicated()
print(duplicates)


#outliers are data points that differ significantly from the rest of the dataset. 
# Think of them as the "black sheep" of your data—values that are unusually high 
# or unusually low compared to the average.

print("--------------------------- 4.Handling outliers-----------------------------")
mean_age = df['Age'].mean()
std_age = df['Age'].std()
df['Z_Score'] = (df['Age'] - mean_age) / std_age

# Remove rows where Z-score is above 2 or below -2 (outliers)
df_no_outliers = df[df['Z_Score'].abs() <= 2]
df_no_outliers = df_no_outliers.drop(columns='Z_Score')   # Drop the Z_Score column
print(df_no_outliers)  # Output the result


print("---------------------------- 5. MIN MAX FOR NORMALIZING------------------------------")
df_normalized = (df - df.min()) / (df.max() - df.min())
print(df_normalized)


print("--------------------------------6. BINING VALUES USING PD CUT-------------------------")
bins = [0, 25, 35, 100]
labels = ['Young', 'Middle-aged', 'Old']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
print(df)

