import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets

# 1. Load Data
iris = datasets.load_iris()
sep_length = iris.data[:, 0]

# 2. Create Samples (Unequal sizes to test flexibility)
# Random state ensures reproducibility
a_1, _ = train_test_split(sep_length, test_size=0.4, random_state=0)
b_1, _ = train_test_split(sep_length, test_size=0.5, random_state=1)

# 3. Descriptive Statistics
stats_data = {
    "Sample A": {"mean": np.mean(a_1), "std": np.std(a_1, ddof=1), "n": len(a_1)},
    "Sample B": {"mean": np.mean(b_1), "std": np.std(b_1, ddof=1), "n": len(b_1)}
}

print("--- Descriptive Statistics ---")
for name, s in stats_data.items():
    print(f"{name}: Mean={s['mean']:.3f}, StdDev={s['std']:.3f}, N={s['n']}")

# 4. Inferential Statistics (T-Tests)
# Welch's T-Test (equal_var=False) is generally safer in the real world
t_stat, p_val = stats.ttest_ind(a_1, b_1, equal_var=False)

print("\n--- Independent T-Test Results (Welch's) ---")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value:     {p_val:.4f}")

# 5. Visualization
plt.figure(figsize=(10, 6))
plt.hist(a_1, alpha=0.5, label=f'Sample A (n={len(a_1)})', color='skyblue', edgecolor='black')
plt.hist(b_1, alpha=0.5, label=f'Sample B (n={len(b_1)})', color='orange', edgecolor='black')
plt.axvline(np.mean(a_1), color='blue', linestyle='dashed', linewidth=2, label='Mean A')
plt.axvline(np.mean(b_1), color='darkorange', linestyle='dashed', linewidth=2, label='Mean B')

plt.title('Distribution of Sepal Lengths: Sample A vs Sample B')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()