import csv

def reformat_csv(input_file, output_file):
    data = {}
    
    # Read the CSV file and store data in a dictionary
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            county_name = row['RegionName'].replace(' County', '').strip()
            state = row['State']  # Extract state information
            for column, value in row.items():
                if column.startswith('1/31/') or column.startswith('2/29/') or column.startswith('3/31/') or column.startswith('4/30/') or column.startswith('5/31/') or column.startswith('6/30/') or column.startswith('7/31/') or column.startswith('8/31/') or column.startswith('9/30/') or column.startswith('10/31/') or column.startswith('11/30/') or column.startswith('12/31/'):
                    year = "20" + column.split('/')[2]
                    if year not in data:
                        data[year] = {}
                    if county_name not in data[year]:
                        data[year][county_name] = {'State': state, 'Values': []}
                    # Check if value is not empty before converting to float
                    if value.strip():  # Check if value is not empty after stripping whitespace
                        data[year][county_name]['Values'].append(float(value))
                    else:
                        data[year][county_name]['Values'].append(0)  # Assume 0 if value is empty
    
    # Write reformatted data to the output file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['County/Region', 'State', 'Year', 'Average Value'])
        for year, counties in data.items():
            for county, info in counties.items():
                state = info['State']
                values = info['Values']
                if values:  # Check if there are values for the county in the year
                    avg_value = sum(values) / len(values)
                else:
                    avg_value = 0  # Assume 0 if no values exist
                writer.writerow([county, state, year, avg_value])

input_file = "ny_mdforreal.csv"
output_file = "ny_md_parsed_data.csv"
reformat_csv(input_file, output_file)
