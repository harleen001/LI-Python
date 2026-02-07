import pandas as pd
import numpy as np

#Dummy DataFrame
data = {
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "pandas", "Oracle", "Java"],
    'Fee': [20000, 25000, 26000, 22000, 24000, 21000, 22000],
    'Duration': [30, 40, 35, 40, 60, 50, 55]  # Changed to integers for math
}
df = pd.DataFrame(data)

# Example 1: Function on entire DataFrame (only works on numeric columns)
def add_3(x):
    return x + 3 if isinstance(x, (int, float)) else x
df_plus_3 = df.apply(add_3)

# Example 2: Apply to a single column
df["Fee"] = df["Fee"].apply(lambda x: x + 400)

# Example 3: Apply to multiple columns
df[['Fee', 'Duration']] = df[['Fee', 'Duration']].apply(lambda x: x + 10)

# Example 4: Using numpy functions
# We use np.square on Fee to show the math working
df['Fee_Squared'] = df['Fee'].apply(np.square)

# Example 5: Map for element-wise transformation
# Great for formatting strings
df['Courses'] = df['Courses'].map(lambda name: name.upper())

# Example 6: Assign for chaining
df = df.assign(Discounted_Fee = lambda x: x.Fee * 0.9)

print("Final Processed DataFrame:")
print(df)