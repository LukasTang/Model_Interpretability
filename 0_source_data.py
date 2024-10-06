# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None

# -

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from plotnine import ggplot, aes, geom_bar, theme_minimal, labs, theme, element_text

# file path to data
filename = "/Users/lukastang/Documents/GitHub/Model_Interpretability/data/Obesity_Dataset.xlsx"

# Read the Excel file
# Define the relative path to the folder and the Excel file
obesity_dataset = pd.read_excel(filename , sheet_name="obesity_dataset")
obesity_dataset_mappings = pd.read_excel(filename, sheet_name="mappings")

# Print the head of the dataset
print(obesity_dataset.head())

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

# Some Visualizations

# Plot distribution of the mapped 'Class' variable
plt.figure(figsize=(10, 6))
sns.countplot(data=obesity_dataset, x='Class_mapped')
plt.title('Distribution of Obesity Classes')
plt.xlabel('Obesity Class')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Plot distribution of the mapped 'Class' variable using plotnine
plot = (
    ggplot(obesity_dataset, aes(x='Class_mapped')) +
    geom_bar() +
    theme_minimal() +
    labs(title='Distribution of Obesity Classes', x='Obesity Class', y='Count') +
    theme(axis_text_x=element_text(rotation=45, hjust=1))
)

print(plot)

# Save the DataFrame to a CSV file
obesity_dataset.to_csv("output/0_source_data/obesity_dataset.csv", index=False)

print("Obesity data generated and saved to 'obesity_dataset.csv'")
