import pandas as pd
from scipy import stats


# Null hypothesis: there is no difference in the means of the average housing prices between MD and NY 
# Conclusion: p-value = 0.00126390 which is less than 0.05. So we reject the null hypothesis and conclude 
# that there is a significant difference in the average unemployment rates between the two states.

data = pd.read_csv('../final_final_csv.csv')

state1 = 'MD'  
state2 = 'NY'  

price_state1 = data[data['State'] == state1]['Average Value']
price_state2 = data[data['State'] == state2]['Average Value']

t_statistic, p_value = stats.ttest_ind(price_state1, price_state2, nan_policy='omit')

print(f'Two-sample T-test results:')
print(f'T-statistic: {t_statistic}')
print(f'P-value: {p_value}')