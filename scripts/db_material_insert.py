import pandas as pd
import json
import requests


def excel_to_json(file_path, json_path):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Create a list to store the JSON records
    json_records = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Get the material description and price values from each row
        desc = row['Material Description']
        price = row['Price']

        # Create a dictionary for each record
        record = {
            'desc': desc,
            'price': price
        }

        # Add the record to the list
        json_records.append(record)

        url = "http://localhost:8000/materials/"
        requests.post(url, json=record)

    # Write the JSON records to a file
    with open(json_path, 'w') as json_file:
        json.dump(json_records, json_file)

    print("Conversion complete. JSON file created successfully.")


# Provide the path to your Excel file
file_path = 'material.xlsx'

# Provide the path where you want to save the JSON file
json_path = 'material.json'

# Call the function to convert the Excel file to JSON
excel_to_json(file_path, json_path)
