import pandas as pd
import scipy.stats
from scipy.stats import chi2_contingency


# NULL HYPOTHESIS: The unemployment rate and the average housing price of a given county are independent of each other.
# CONCLUSION: Since the p-value is 4.376423651864803e-42, which is less than 0.05, we reject the null hypothesis.


data = pd.read_csv('../final_final_csv.csv')

# raw data cross table
cross_table = pd.crosstab(data['Unemployment_rate'], data['Violent Total Rate'])

tstats, pvalue, dof, expected = chi2_contingency(cross_table)



data['Unemployment_q'] = pd.qcut(data['Unemployment_rate'], q=4, labels=['low', 'medium', 'high', 'very high'])
data['Average Value_q'] = pd.qcut(data['Average Value'], q=4, labels=['low', 'medium', 'high', 'very high'])

# quartile cross table
quartile_cross_table = pd.crosstab(data['Unemployment_q'], data['Average Value_q'])

tstats_q, pvalue_q, dof_q, expected_q = chi2_contingency(quartile_cross_table)
    

print(data['Unemployment_rate'].describe())
print(data['Average Value'].describe())
print(data['Unemployment_q'].describe())
print(data['Average Value_q'].describe())



# quartile test stats
print(tstats_q)
# = 218.47644309714647

print(pvalue_q)
# = 4.376423651864803e-42

# raw value test stats
# print(tstats)
# print(pvalue)

