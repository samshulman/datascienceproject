import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("/Users/caspar/Desktop/Folders/CompSci/DataScience/Data-Science-Final-Project/cleanedGDP.csv")

# Convert the string numbers to integers
for col in df.columns[1:]:
    df[col] = df[col].str.replace(",", "").astype(int)

# Melt the dataframe to convert it to long format
df_long = pd.melt(df, id_vars=['county_name'], var_name='year', value_name='gdpo')

# Sort the dataframe by county and year
df_long = df_long.sort_values(by=['county_name', 'year']).reset_index(drop=True)

# Write the modified dataframe to a new CSV file
df_long.to_csv("modified_data_long.csv", index=False)
