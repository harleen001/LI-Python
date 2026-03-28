#two sample T test
from scipy.stats import ttest_ind

# Sample data: Blood pressure reduction
group1 = [8, 9, 7, 10, 6]  # New drug
group2 = [5, 6, 5, 7, 4]   # Existing drug

# Perform a two-sample t-test
stat, p_value = ttest_ind(group1, group2)

# Results
print(f"T-Statistic: {stat}")
print(f"P-Value: {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: The new drug is more effective.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")