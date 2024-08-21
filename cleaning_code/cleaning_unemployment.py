import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv("UnemploymentRates_all.csv")

# Step 2: Drop unnecessary columns
columns_to_drop = ['Rural_Urban_Continuum_Code_2013', 'Urban_Influence_Code_2013', 'Metro_2013']
columns_to_drop.extend([col for col in df.columns if col.startswith('Civilian_labor_force')])
df.drop(columns=columns_to_drop, inplace=True)

# Step 3: Melt the DataFrame to have separate rows for each year
melted_df = pd.melt(df, id_vars=['FIPS_Code', 'State', 'Area_Name'], var_name='Variable', value_name='Value')

# Step 4: Extract year from the column names
melted_df['Year'] = melted_df['Variable'].str.extract(r'_(\d{4})')

# Step 5: Extract metric from the column names
melted_df['Metric'] = melted_df['Variable'].str.extract(r'([a-zA-Z]+)_\d{4}')

# Step 6: Filter the DataFrame to include only rows where the state is NY or MD
filtered_df = melted_df[melted_df['State'].isin(['NY', 'MD'])]

# Step 7: Pivot the filtered DataFrame to have separate columns for Employed, Unemployed, and Unemployment_rate
pivot_df = filtered_df.pivot_table(index=['FIPS_Code', 'State', 'Area_Name', 'Year'], columns='Metric', values='Value').reset_index()

# Step 8: Merge the pivoted DataFrame with the original DataFrame
merged_df = pd.merge(pivot_df, df, on=['FIPS_Code', 'State', 'Area_Name'])

# Step 9: Save the merged and generalized data into a new CSV file
merged_df.to_csv('pleasework.csv', index=False)

df2 = pd.read_csv('pleasework.csv')

# Define columns for employed, unemployed, and unemployment rate for each year
employed_cols = [f'Employed_{year}' for year in range(2000, 2023)]
unemployed_cols = [f'Unemployed_{year}' for year in range(2000, 2023)]
unemployment_rate_cols = [f'Unemployment_rate_{year}' for year in range(2000, 2023)]

# Initialize a list to store the transformed data
transformed_data = []

# Iterate over rows of original DataFrame and populate the transformed data list
for index, row in df2.iterrows():
    fips_code = row['FIPS_Code']
    state = row['State']
    area_name = row['Area_Name']
    
    # Remove commas, state identifiers (NY or MD), and quotation marks
    area_name = area_name.replace(',', '').replace('NY', '').replace('MD', '').replace('"', '').replace(' County', '').strip()
    
    # Skip rows with Area_Name "Maryland"
    if area_name.lower() == 'maryland':
        continue
    
    # Skip rows with Area_Name "New York" and employed count greater than a million
    if area_name.lower() == 'new york' and any(int(row[f'Employed_{year}'].replace(',', '')) > 1000000 for year in range(2000, 2023)):
        continue
    
    # Iterate over years
    for year in range(2000, 2023):
        employed = row[f'Employed_{year}']
        unemployed = row[f'Unemployed_{year}']
        unemployment_rate = row[f'Unemployment_rate_{year}']
        
        # Append data for the current year
        transformed_data.append({
            'FIPS_Code': fips_code,
            'State': state,
            'County/Region': area_name,
            'Year': year,
            'Employed': employed,
            'Unemployed': unemployed,
            'Unemployment_rate': unemployment_rate
        })

# Create a DataFrame from the transformed data
transformed_df = pd.DataFrame(transformed_data)

# Remove duplicate rows
transformed_df.drop_duplicates(inplace=True)

meh = pd.read_csv('final_csv.csv')

transformed_df.to_csv('testtest.csv')

transformed_df['County/Region'] = transformed_df['County/Region'].str.replace("'", '')
transformed_df['County/Region'] = transformed_df['County/Region'].str.replace("St. ", 'Saint ')
transformed_df['County/Region'] = transformed_df['County/Region'].str.replace("city", 'City')




last_df = pd.merge(meh, transformed_df, on=['County/Region', 'Year', 'State'], how='inner')

last_df = last_df.drop_duplicates()

last_df.to_csv("final_final_csv.csv", index=False)

# Write the transformed data to a new CSV file
# transformed_df.to_csv('transformed_data.csv', index=False)