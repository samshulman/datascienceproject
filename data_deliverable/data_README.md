# Data Deliverable

## A complete data spec

The dataset we use for this project has 29 columns and 1932 rows. Many of the crime columns have similar data purpose, so below I will explain the following headers: county/region, year, population, index total count, index total rate, violent total count, violet total rate, average home value, FIPS_Code, Employed, Unemployed, Unemployment_rate:

### County/region:

Type of data that will be used for the representation - Strings

Default value - No default value because there will only ever be a record where we have a location.

Range of value - 96 unique values from two states: Maryland and New York

Simplified analysis of the distribution of values - There are approximately 23 rows of each unique county present in the dataset, corresponding to the data for each year from 2000-2022 for each county

Are these values unique? - Same answer as above

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? - No, because each county/year pair exists once in the dataset 

Is this a required value? - Yes

Do you plan to use this attribute/feature in the analysis? If so, how? - Yes, we want to compare each county’s historical crime and economic data over the years so we will stratify by county to look for patterns
Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? - No

### Year: 

Type of data that will be used for the representation - Integers

Default value - No default value because there will only ever be a record where we have a year to look at.

Range of value - 2000 to 2024

Simplified analysis of the distribution of values - The values 2000 to 2020 each have 99 instances. The values 2021 and 2022 each have 95 instances. The values 2023 and 2024 each have 83 instances. 

Are these values unique? - No because we need repeated years to compare counties in the same year

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? - No, because each county/year pair exists once in the dataset 

Is this a required value? - Yes

Do you plan to use this attribute/feature in the analysis? If so, how? - Yes, we want to compare each county’s historical crime and economic data over the years so we will see how this data changes/correlates over time

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? - No

### Population: The population of the County/Region in the specified year. Values are integers.
Type of data that will be used for the representation - Floats

Default value - No default value because we have population data for all counties

Range of values - 4342 to 19845038

Simplified analysis of the distribution of values -

Maximum: 19845038.0

Minimum: 4342.0

Median: 110203.5

Mean: 779703.838168631

Standard Deviation: 2416637.512391104

Are these values unique? - No, coincidentally there are 10 counties with the same population, and these repeated values are [47336. 75671. 31909. 87228. 30734. 37221. 51170. 47382. 51082. 24704.]

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? - No

Is this a required value? - Yes

Do you plan to use this attribute/feature in the analysis? If so, how? - Potentially used, it’s not the main part of the analysis but would be cool to see how crime and economic data differ between larger and smaller populations

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? - No

### Index Total Count: The total count of index (violent and theft) crimes reported.
Type of data that will be used for the representation - Floats

Default value - No default value because we have this data for all counties

Range of values - 28 to 585173

Simplified analysis of the distribution of values -

Maximum: 585173.0

Minimum: 28.0

Median: 2602.0

Mean: 18252.516319129645

Standard Deviation: 55676.02352920783

Are these values unique? - No, there are 496 repeated values in this column

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? - No

Is this a required value? - Yes

Do you plan to use this attribute/feature in the analysis? If so, how? - Yes, we want to compare each county’s historical crime data over time, and this is one type of crime we will take into account

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? - No because it is just a count of crimes, no personal details about trials

### Index Total Rate: The rate of index crimes per 100,000 population

Type of data that will be used for the representation - Floats

Default value - No default value because we have this data for all counties

Range of values - 276 to 10257

Simplified analysis of the distribution of values -

Maximum: 10257.3

Minimum: 276.5

Median: 2076.1499999999996

Mean: 2245.113372620127

Standard Deviation: 1032.0038229629808

Are these values unique? - No, there are 126 repeated values in this column

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? - No

Is this a required value? - Yes

Do you plan to use this attribute/feature in the analysis? If so, how? - Yes, we want to compare each county’s historical crime data over time, and this is one type of crime we will take into account

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? - No because it is just a rate of crimes, no personal details about trials

### Violent Total Count: The total count of violent crimes reported.

Type of data that will be used for the representation - Floats

Default value - No default value because we have this data for all counties

Range of values - 1 to 104487

Simplified analysis of the distribution of values -

Maximum: 104487.0

Minimum: 1.0

Median: 263.5

Mean: 3101.0630099728014

Standard Deviation: 10375.470977135858

Are these values unique? - No, there are 1347 repeated values in this column

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? - No

Is this a required value? - Yes

Do you plan to use this attribute/feature in the analysis? If so, how? - Yes, we want to compare each county’s historical crime data over time, and this is one type of crime we will take into account

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? - No because it is just a count of crimes, no personal details about trials

### Violent Total Rate: The rate of violent crimes per 100,000 population. Values are floats.

Type of data that will be used for the representation - Floats

Default value - No default value because we have this data for all counties

Range of values - 20.6 to 2462.6

Simplified analysis of the distribution of values -

Maximum: 2462.6

Minimum: 20.6

Median: 226.35000000000002

Mean: 287.0771985494107

Standard Deviation: 230.9565390132192

Are these values unique? - No, there are 792 repeated values in this column

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? - No

Is this a required value? - Yes

Do you plan to use this attribute/feature in the analysis? If so, how? - Yes, we want to compare each county’s historical crime data over time, and this is one type of crime we will take into account

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? - No because it is just a rate of crimes, no personal details about trials

### Murder Count: The count of reported murders. Values are integers.
### Murder Rate: The rate of murders per 100,000 population. Values are floats.
### Rape Count: The count of reported rapes. Values are integers.
### Rape Rate: The rate of rapes per 100,000 population. Values are floats.
### Robbery Count: The count of reported robberies. Values are integers.
### Robbery Rate: The rate of robberies per 100,000 population. Values are floats.
### Agg Assault Count: The count of reported aggravated assaults. Values are integers.
### Agg Assault Rate: The rate of aggravated assaults per 100,000 population. Values are floats.
### Property Total Count: The total count of property crimes reported. Values are integers.
### Property Total Rate: The rate of property crimes per 100,000 population. Values are floats.
### Burglary Count: The count of reported burglaries. Values are integers.
#### Burglary Rate: The rate of burglaries per 100,000 population. Values are floats.
### Larceny Count: The count of reported larcenies. Values are integers.
### Larceny Rate: The rate of larcenies per 100,000 population. Values are floats.
### MV Theft Count: The count of reported motor vehicle thefts. Values are integers.
### MV Theft Rate: The rate of motor vehicle thefts per 100,000 population. Values are floats.
### Employed
### Unemployed
### Employment rate
### Average Value: Zillow Home Value Index (ZHVI) averaged over a yearly period. ZHVI is a measure of the typical home value (35th to 65th percentile range) in a given county. 

Type of data that will be used for the representation - Float

Default value - No default value because we have average house values for all counties and years.

Range of value - 47288 to 1375318

Simplified analysis of the distribution of values - 

Maximum: 1375318.6415454545

Minimum: 47288.427065

Median: 148845.64120833334

Mean: 201956.5367243325

Are these values unique? - No, there are 126 repeated values in thai column

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? - No

Is this a required value? - Yes

Do you plan to use this attribute/feature in the analysis? If so, how? - Yes, we want to use this value as an economic statistic to gain insight into a county’s financial status and compare the historical financial status to historical crime data

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? - No because specific addresses with corresponding prices are not included

### FIPS_Code: The state (either MD or NY) where the data is from. Values are integers.
### Employed: The number of employed people. Values are integers.
### Unemployed: The number of unemployed people. Values are integers.
### Unemployment_rate: The unemployment rate. Values are floats.


## A link to your full data in downloadable form
https://github.com/cschlie/Data-Science-Final-Project - final_final_csv.csv file
A sample of your data (e.g. 100 rows) that we can easily open and view on our computers.
Go to the sample.csv file

## A concise tech report in README format
We have roughly 60,000 records (2000 rows * 30 columns), from the states of New York and Maryland. We definitely think this is enough data to perform our analysis on. 
Below are the links to the various sources from which we extracted our data. We intentionally chose sources that are representative and reliable. For example, for crime statistics we chose to go for census and government data. We stayed away from using privately obtained data, or data from news publications, in this context as we knew that crime statistics are a highly politically-charged metric that can be exploited by publications. By using only official census and government data we tried to avoid this issue as best we could. The housing data was slightly harder to collect as many publications had missing data, or data that did not span over our desired time period. However, we overcome these obstacles by leveraging Zillow's extensive database of housing information. Zillow provided us with invaluable access to a wide range of house prices, allowing us to conduct our analysis with confidence. However, it's important to note that the Zillow Home Value Index (ZHVI), which we relied on as a proxy for house price changes, is a metric formulated by Zillow and may carry a degree of subjectivity. While Zillow's vast dataset offers valuable insights into housing trends, including fluctuations in home values, it's essential to acknowledge that the ZHVI represents Zillow's own assessment of market conditions. Hence, we thought it was necessary to really dig deeper into how this metric is formulated at this link. We also decided to cross-reference Zillow's findings with other housing sources to make sure that the general trends present in the data were robust.  

Income data sources:
https://www.census.gov/library/visualizations/time-series/demo/census-poverty-tool.html
https://www.bea.gov/data/gdp/gdp-county-metro-and-other-areas

Crime data:
https://www.nyc.gov/site/nypd/stats/crime-statistics/historical.page

Education data:
https://data.ers.usda.gov/reports.aspx?ID=17829#Pf7081e5b1f514b5fb1a0027a9fe44848_5_47iT1

Unemployment data:
https://data.ers.usda.gov/reports.aspx?ID=17828
https://www.ers.usda.gov/data-products/county-level-data-sets/county-level-data-sets-download-data/

Housing data:
https://www.zillow.com/research/data/

We were checking for cleanliness mainly though checking our datasets by hand, as we were using pre established datasets I was able to look back and forth to make sure I was getting the right data transmitted while joining and cleaning. We mainly used pandas and csv tools to clean due to their ease of use and speed for cleaning, seeing as we were handling thousands of entries at a time. During the process of cleaning and combing datasets there were inevitably duplicates that came up in the process which was first removing pandas drop duplicates functions but later rectified once I understood the root cause of the issue. Thankfully very little numerical adjustment/scale adjustment was needed as we found data with similar scales which was helpful meaning that the data, once put into visual representation will stay within each other's scale. In terms of cleaning we performed basic column drops of useless information as well as string clean ups, such as turning strings to ints, removing apostrophes, or rectifying strange spelling decisions for counties, by using pandas in built functions. Obviously in the process of cleaning, data had to be discarded but this was overall for the benefit of the questions we are trying to answer and was information not pertinent to our project. One particular annoyance was the different spellings of counties in different data sets which made merging particularly annoying meaning we had to go through our data by hand, find the differences between the spellings and write a string replace function. 
		
The persistent challenge of missing or omitted data required careful handling throughout our data parsing process. By addressing these edge cases, we think we have successfully ensured the completeness and reliability of our dataset. Another significant, and unexpected, challenge we faced at this stage in the project was addressing the fact that some counties in different states have the same name. For example, there is a Washington County in both New York and Maryland.
Our next steps will be to conduct diligent analysis on the trends present in our data. We will formulate at least three hypotheses and rigorously test their validity. One of these hypotheses, we expect, will be that crime rates have a strong negative correlation on prices in different counties. Additionally, we aim to explore correlations between various indicators such as GDP per capita and education levels, and their impact on house prices within different areas. We will also conduct a supervised machine learning analysis on our data set, and confirm these results using k-fold validation. Overall, our work on the project so far has elucidated the importance of meticulous data preprocessing and fine tuning, as well as influenced the type of analysis we intend to conduct. 







