# Analysis Deliverable

### Hypothesis testing component: the group must formulate a minimum of three distinct research hypotheses and test them using a statistical testing method.

- 1) The unemployment rate and the average housing price of a given county are independent of each other.

- 2) The observed difference in aggressive assault rates between New York and Maryland is statistically significant – tested using a two-sample t-test

- 3) The observed difference in average home values between New York and Maryland is statistically significant - tested using a two-sample t-test


### Machine learning component: you should use at least two of the Machine Learning techniques shown in class. You can use either a supervised or unsupervised learning method. 
	
- 1) We classified a county's unemployment rate as either low, medium, high, or very high based on the nine crime rate statistics using a SVC classifer.

- 2) We performed a linear regression between two columns of data, Average Home Value and Violent Crime Rate


### For both components, provide a description of the result and adequate complementary information describing and motivating your process:

Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?


- 1) We used a chi square test for independence to check for independence between the average housing price and unemployment rate because the chi square test checks for correlation between two variables. We considered other tests, but this one made the most sense when trying to analyze a potential correlation between the desired variables. We had to restructure the data into quartiles to successfully complete this test.

- 2) We used a two-sample t-test to analyze the observed difference in aggressive assault rates as this is an appropriate choice for comparing means between two groups. The primary metric for evaluation is the p-value (shown in next question), which indicates the strength of evidence against the null hypothesis. Since there were no missing values or outliers, and our data met the assumptions of the t-test, it was not necessary to restructure or clean the data. It was enough to just filter the data file for our relevant information.

- 3) Again, We used a two-sample t-test to analyze the observed difference in home prices between states as this is an appropriate choice for comparing means between two groups. The primary metric for evaluation is again the p-value (shown in next question), which indicates the strength of evidence against the null hypothesis. Since there were also no missing values or outliers, and our data met the assumptions of the t-test, it was not necessary to restructure or clean the data. It was enough to just filter the data file for our relevant information.

- 4) We used an SVM classifier (SVC) to predict whether a county’s unemployment rate is high, or very high based on the nine crime rate statistics. We used this type of classifier because it is good for analyzing complex relationships and patterns between features and classes. SVM is good for high dimensional features, and this classification task includes nine predictive crime statistics.

- 5) We used linear regression because I wanted to find if there was any correlation between average home values in a county and different crime rates, I tested multiple different continuous variables against average home value but ended up choosing violent crime rate. Linear regression provides a straightforward way to examine whether there's any linear association between the variables. Allowing me to see if any one variable has a significant impact on another one. 



What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

- 1) Test 1 results: We reject the first null hypothesis since the p-value is 4.376e-42, which is less than 0.05. This means we cannot conclude that average housing price and unemployment rate are independent. This result makes sense because it is logical for these two variables to have some correlation in any given county.

- 2) Test 2 results: The P-value is 1.3305636493005464e-50, giving us very strong evidence to reject the H0. Therefore, there is a significant difference in the mean aggressive assault rates between the two states. Again, this intuitively makes sense as NY contains the city of New York which contributes significantly to its higher crime rates. 

- 3) Test 3 results: the p-value is 0.00126390 which is less than 0.05. So we reject the null hypothesis and conclude that there is a significant difference in the average unemployment rates between the two states. This makes sense intuitively as NY is generally considered a more prosperous and economically active state than MD.

- 4) For the SVM classifier, we have an overall accuracy of 48%, which is higher than chance (25%) when predicting one of four classes. The model is better at recall for ‘very high’ and ‘low’ unemployment rates, with recall rates of 66% and 64% respectively. This accuracy discrepancy may be due to unequally distributed data between the four classes or potentially crime rate statistics are just more predictive of extreme values (very high and low) rather than mild values (medium and high).

- 5) The linear regression analysis between average home value and violent crime rate yielded a coefficient of 0.0002617, indicating a positive but small relationship—suggesting that as average home value increases, so does the violent crime rate, though minimally. The low R-squared value of 0.027 suggests the model explains only 2.72% of the variation in violent crime rates, indicating limitations in its predictive power. Ultimately linear regression failed to find much meaningful correlation between average home value and violent crime rates which looks to disprove our question about whether the two are related in any way. 
