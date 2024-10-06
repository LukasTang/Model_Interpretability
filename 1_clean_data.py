# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputsupstream = ['0_source_data']
upstream = ['0_source_data']
# -

import pandas as pd
from obesity_utils import set_categorical_order as ut

obesity_dataset = pd.read_csv(upstream['0_source_data']['obesity_data'])
obesity_dataset_mappings = pd.read_csv(upstream['0_source_data']['obesity_mappings'])
# some data cleaning code...

# Set the categorical order for the specified variables
ut.set_categorical_order(obesity_dataset, obesity_dataset_mappings)

print("Cleaned data generated and saved to 'artificial_data.csv'")

