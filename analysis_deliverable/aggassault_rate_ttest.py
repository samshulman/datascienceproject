import pandas as pd
from scipy import stats
from scipy.stats import ttest_rel


## Null Hypothesis: There is no significant difference in the average agg assault rates between New York and Maryland.
## Conclusion: P-value is 1.3305636493005464e-50 so we reject the H0. Therefore, there is a significant difference in the mean murder rates between the two states


data = pd.read_csv('../final_final_csv.csv')

state_column = 'State'
agg_rate_column = 'Agg Assault Rate'

state1 = 'NY'
state2 = 'MD'

agg_rate_column1 = data[data[state_column] == state1][agg_rate_column]
agg_rate_column2 = data[data[state_column] == state2][agg_rate_column]

t_statistic, p_value = stats.ttest_ind(agg_rate_column1, agg_rate_column2, equal_var=False)

print(f'Two-sample t-test results for agg assult rates between {state1} and {state2}:')
print(f'T-statistic: {t_statistic}')
print(f'P-value: {p_value}')