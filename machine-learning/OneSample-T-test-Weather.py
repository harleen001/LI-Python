import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 1. Setup: Define the Population
# We'll use a seed so our "random" sample is the same every time we run it
np.random.seed(42) 

ages = [10,20,30,10,20,22,32,42,33,44,12,34,56,70,26,10,
        50,18,26,24,21,15,67,34,25,24,36,34,25,32,33,26]

pop_mean = np.mean(ages)

# 2. Sampling
sample_size = 10
age_sample = np.random.choice(ages, size=sample_size)
sample_mean = np.mean(age_sample)

# 3. Execution: One-Sample T-Test
# H0: Sample Mean = Population Mean
# H1: Sample Mean != Population Mean
t_stat, p_value = stats.ttest_1samp(age_sample, pop_mean)

# 4. Reporting Function
def report_test_results(p, alpha=0.05):
    print(f"--- Statistical Report ---")
    print(f"Population Mean: {pop_mean:.2f}")
    print(f"Sample Mean:     {sample_mean:.2f}")
    print(f"P-Value:         {p:.4f}")
    
    if p <= alpha:
        return "REJECT H0: There is a significant difference."
    else:
        return "FAIL TO REJECT H0: No significant difference found."

print(report_test_results(p_value))

# 5. Optional: Visualizing the Difference
plt.figure(figsize=(8, 5))
plt.hist(ages, alpha=0.3, label='Population Distribution', color='gray')
plt.axvline(pop_mean, color='red', linestyle='dashed', label='Pop Mean')
plt.axvline(sample_mean, color='blue', label='Sample Mean')
plt.title("Population vs. Sample Mean Comparison")
plt.legend()
plt.show()