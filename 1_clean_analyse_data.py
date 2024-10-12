# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputsupstream = ['0_source_data']
upstream = ['0_source_data']
# -
import pandas as pd
from helpers.mymodule import greeting
greeting("Me")
from helpers.variable_ordering import  set_categorical_order 
from helpers.feature_charts import FeaturePlot
#from helpers.feature_charts import ordered_class_plot
#from helpers.feature_charts import numerical_feature_plot

obesity_dataset = pd.read_csv(upstream['0_source_data']['obesity_data'])
obesity_dataset_mappings = pd.read_csv(upstream['0_source_data']['obesity_mappings'])
# some data cleaning code...

# Set the categorical order for the specified variables
obesity_dataset = set_categorical_order(obesity_dataset, obesity_dataset_mappings)
# Filter cases where Sex_mapped is 'Male'
male_obesity_dataset = obesity_dataset[obesity_dataset['Sex_mapped'] == 'Male']
# Filter cases where Sex_mapped is 'Female'
female_obesity_dataset = obesity_dataset[obesity_dataset['Sex_mapped'] == 'Female']

# Print a summary of the dataset
print(obesity_dataset.describe(include='all'))
print(obesity_dataset.info())

# Various visualizations of the features
FeaturePlot_all = FeaturePlot(obesity_dataset)
FeaturePlot_male = FeaturePlot(male_obesity_dataset)
FeaturePlot_female = FeaturePlot(female_obesity_dataset)

# 

# Class distribution by Sex
FeaturePlot_all.create_plot(x='Class_mapped', fill='Sex_mapped', title='Class Distribution by Sex')
# Class distribution by Age
FeaturePlot_all.create_plot(x='Age', fill='Class_mapped', title='Class Distribution by Age',plot_type='histogram')
# Class distribution by Age (Male)
FeaturePlot_male.create_plot(x='Age', fill='Class_mapped', title='Class Distribution by Age (Male)',plot_type='histogram')
# Class distribution by Age (Female)
FeaturePlot_female.create_plot(x='Age', fill='Class_mapped', title='Class Distribution by Age (Female)',plot_type='histogram')

FeaturePlot_all.create_plot(x='Height', fill='Class_mapped', title='Class Distribution by Height',plot_type='histogram')

FeaturePlot_male.create_plot(x='Height', fill='Class_mapped', title='Class Distribution by Height (Male)',plot_type='histogram')

FeaturePlot_female.create_plot(x='Height', fill='Class_mapped', title='Class Distribution by Height (Female)',plot_type='histogram')


# Save the cleaned dataset to a CSV file
obesity_dataset.to_csv('output/1_clean_analyse_data/clean_analyse_data.csv', index=False)

print("Cleaned data generated and saved to 'artificial_data.csv'")

