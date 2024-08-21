import pandas as pd

crime_df = pd.read_csv('/Users/caspar/Desktop/Folders/CompSci/DataScience/Data-Science-Final-Project/Combined_Maryland_New_York.csv')

econ_df = pd.read_csv('ny_md_parsed_data.csv')


crime_df['County/Region'] = crime_df['County/Region'].str.replace('St Lawrence', 'Saint Lawrence')
crime_df['County/Region'] = crime_df['County/Region'].str.replace(' County', '')
crime_df['County/Region'] = crime_df['County/Region'].str.replace("'", '')
crime_df['County/Region'] = crime_df['County/Region'].str.replace("St. Marys", 'Saint Marys')


# maryland_counties = {
#     'Allegany', 'Anne Arundel', 'Baltimore', 'Calvert', 'Caroline', 'Carroll', 'Cecil',
#     'Charles', 'Dorchester', 'Frederick', 'Garrett', 'Harford', 'Howard', 'Kent',
#     'Montgomery', 'Prince George\'s', 'Queen Anne\'s', 'Somerset', 'St. Mary\'s',
#     'Talbot', 'Washington', 'Wicomico', 'Worcester'
# }

# new_york_counties = {
#     'Albany', 'Allegany', 'Bronx', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua',
#     'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware', 'Dutchess',
#     'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene', 'Hamilton', 'Herkimer',
#     'Jefferson', 'Kings', 'Lewis', 'Livingston', 'Madison', 'Monroe', 'Montgomery',
#     'Nassau', 'New York', 'Niagara', 'Oneida', 'Onondaga', 'Ontario', 'Orange', 'Orleans',
#     'Oswego', 'Otsego', 'Putnam', 'Queens', 'Rensselaer', 'Richmond', 'Rockland',
#     'Saint Lawrence', 'Saratoga', 'Schenectady', 'Schoharie', 'Schuyler', 'Seneca',
#     'Steuben', 'Suffolk', 'Sullivan', 'Tioga', 'Tompkins', 'Ulster', 'Warren',
#     'Washington', 'Wayne', 'Westchester', 'Wyoming', 'Yates'
# }

# # Function to determine the state identifier based on county name
# def get_state_identifier(county_name):
#     if county_name in maryland_counties and county_name not in new_york_counties:
#         return 'MD'
#     elif county_name in new_york_counties and county_name not in maryland_counties:
#         return 'NY'
#     else:
#         return ''

# Add a new column with state identifiers
# crime_df['State'] = crime_df['County/Region'].apply(lambda x: get_state_identifier(x.split()[0]))
# econ_df['State Identifier'] = econ_df['County/Region'].apply(lambda x: get_state_identifier(x.split()[0]))



merged_df = pd.merge(crime_df, econ_df, on=['County/Region', 'Year', 'State'], how='outer')




merged_df.to_csv("final_csv.csv", index=False)


