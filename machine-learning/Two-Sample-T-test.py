import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Generate Synthetic Data
np.random.seed(42)
# Group A: Younger (Average ~48)
group_A = stats.poisson.rvs(loc=18, mu=30, size=100)
# Group B: Older (Average ~53)
group_B = stats.poisson.rvs(loc=18, mu=35, size=100)

# 2. Perform the Independent T-Test (Welch's)
t_stat, p_val = stats.ttest_ind(group_A, group_B, equal_var=False)

# 3. Visualization for Comparison
plt.figure(figsize=(10, 5))
sns.kdeplot(group_A, fill=True, label=f'Group A (Mean: {group_A.mean():.2f})', color='royalblue')
sns.kdeplot(group_B, fill=True, label=f'Group B (Mean: {group_B.mean():.2f})', color='tomato')

plt.axvline(group_A.mean(), color='blue', linestyle='--')
plt.axvline(group_B.mean(), color='red', linestyle='--')

plt.title("Two-Sample T-Test: Comparing Group A vs. Group B")
plt.xlabel("Value (Age)")
plt.ylabel("Density")
plt.legend()
plt.show()

# 4. Output Results
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value:     {p_val:.10f}")

alpha = 0.05
if p_val < alpha:
    print("Conclusion: Reject H0. There is a significant difference between the groups.")
else:
    print("Conclusion: Fail to Reject H0. No significant difference detected.")