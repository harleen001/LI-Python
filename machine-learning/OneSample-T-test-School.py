import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import ttest_1samp

# 1. Setup Data
# Population: The whole school (Average age ~53: 18 + 35)
np.random.seed(42)
school_ages = stats.poisson.rvs(loc=18, mu=35, size=1500)

# Sample: Class A (Average age ~48: 18 + 30)
# Note: We expect this to be significantly different from the school average
classA_ages = stats.poisson.rvs(loc=18, mu=30, size=60)

# 2. Define the Decision Function
def test_results(p, alpha=0.05):
    print(f"P-Value: {p:.10f}") # Using 10 decimal places as it will be very small
    if p <= alpha:
        print("Result: REJECT the Null Hypothesis (H0).")
        print("Conclusion: Class A's age is significantly different from the school average.")
    else:
        print("Result: FAIL TO REJECT the Null Hypothesis (H0).")
        print("Conclusion: No significant difference found.")

# 3. Perform One-Sample T-Test
# We test if the mean of Class A is equal to the known mean of the school
pop_mean = school_ages.mean()
ttest, p_val = ttest_1samp(classA_ages, pop_mean)

# 4. Visualization
plt.figure(figsize=(10, 6))
sns.histplot(school_ages, kde=True, color="skyblue", label="School (Population)", stat="density")
sns.histplot(classA_ages, kde=True, color="orange", label="Class A (Sample)", stat="density")

# Add lines for the means
plt.axvline(pop_mean, color='blue', linestyle='--', label=f'School Mean: {pop_mean:.2f}')
plt.axvline(classA_ages.mean(), color='red', linestyle='--', label=f'Class A Mean: {classA_ages.mean():.2f}')

plt.title("Age Distribution: Class A vs. Entire School")
plt.xlabel("Age")
plt.legend()
plt.show()

# 5. Output Results
test_results(p_val)