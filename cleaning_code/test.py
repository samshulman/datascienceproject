import pandas as pd

# Load Maryland.csv
maryland_df = pd.read_csv("/Users/caspar/Desktop/Folders/CompSci/DataScience/Data-Science-Final-Project/code/MARYLAND-Violent_Crime___Property_Crime_by_County__1975_to_Present_20240320.csv")



# Rename columns to match the structure of New York.csv
maryland_df = maryland_df.rename(columns={
    'JURISDICTION': 'County/Region',
    'YEAR': 'Year',
    'POPULATION': 'Population',
    'GRAND TOTAL': 'Index Total Count',
    'OVERALL CRIME RATE PER 100,000 PEOPLE': 'Index Total Rate',
    'VIOLENT CRIME TOTAL': 'Violent Total Count',
    'VIOLENT CRIME RATE PER 100,000 PEOPLE': 'Violent Total Rate',
    'MURDER': 'Murder Count',
    'MURDER PER 100,000 PEOPLE': 'Murder Rate',
    'RAPE': 'Rape Count',
    'RAPE PER 100,000 PEOPLE': 'Rape Rate',
    'ROBBERY': 'Robbery Count',
    'ROBBERY PER 100,000 PEOPLE': 'Robbery Rate',
    'AGG. ASSAULT': 'Agg Assault Count',
    'AGG. ASSAULT PER 100,000 PEOPLE': 'Agg Assault Rate',
    'PROPERTY CRIME TOTALS': 'Property Total Count',
    'PROPERTY CRIME RATE PER 100,000 PEOPLE': 'Property Total Rate',
    'B & E': 'Burglary Count',
    'B & E PER 100,000 PEOPLE': 'Burglary Rate',
    'LARCENY THEFT': 'Larceny Count',
    'LARCENY THEFT PER 100,000 PEOPLE': 'Larceny Rate',
    'M/V THEFT': 'MV Theft Count',
    'M/V THEFT PER 100,000 PEOPLE': 'MV Theft Rate'
})

# Drop any unnecessary columns from Maryland DataFrame
maryland_df = maryland_df[['County/Region', 'Year', 'Population', 'Index Total Count', 'Index Total Rate',
                           'Violent Total Count', 'Violent Total Rate', 'Murder Count', 'Murder Rate',
                           'Rape Count', 'Rape Rate', 'Robbery Count', 'Robbery Rate', 'Agg Assault Count',
                           'Agg Assault Rate', 'Property Total Count', 'Property Total Rate', 'Burglary Count',
                           'Burglary Rate', 'Larceny Count', 'Larceny Rate', 'MV Theft Count', 'MV Theft Rate']]

# Load New York.csv
new_york_df = pd.read_csv("/Users/caspar/Desktop/Folders/CompSci/DataScience/Data-Science-Final-Project/code/NEW_YORK_CRIME.csv")

# Concatenate both DataFrames
combined_df = pd.concat([maryland_df, new_york_df], ignore_index=True)

# Save the concatenated DataFrame to a new CSV file
combined_df.to_csv("Combined_Maryland_New_York.csv", index=False)
