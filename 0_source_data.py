# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None

# -

import numpy as np
import pandas as pd

# Read the Excel file
obesity_dataset = pd.read_excel("data/Obesity_Dataset.xlsx", sheet_name="Obesity_Dataset")
obesity_dataset_mappings = pd.read_excel("data/Obesity_Dataset.xlsx", sheet_name="Obesity_Dataset")

# Print the head of the dataset
print(dobesity_dataset.head())

def map_variable(df, mappings, variable):
    mapping_dict = mappings[mappings['Variable'] == variable].set_index('Value')['Mapping'].to_dict()
    df[variable + '_mapped'] = df[variable].map(mapping_dict)

variables_to_map = [
    'Sex', 'Overweight_Obese_Family', 'Consumption_of_Fast_Food', 
    'Frequency_of_Consuming_Vegetables', 'Number_of_Main_Meals_Daily', 
    'Food_Intake_Between_Meals', 'Smoking', 'Liquid_Intake_Daily', 
    'Calculation_of_Calorie_Intake', 'Physical_Excercise', 
    'Schedule_Dedicated_to_Technology', 'Type_of_Transportation_Used', 'Class'
]

for variable in variables_to_map:
    map_variable(obesity_dataset, obesity_dataset_mappings, variable)

# Print the head of the dataset with mapped variables
print(obesity_dataset.head())

# Add some mappings 

# Save the DataFrame to a CSV file
obesity_dataset.to_csv('obesity_dataset.csv', index=False)

print("Obesity data generated and saved to 'obesity_dataset.csv'")
