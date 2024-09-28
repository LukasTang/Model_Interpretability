# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputsupstream = ['0_source_data']
upstream = ['0_source_data']
# -

import pandas as pd

df = pd.read_csv(upstream['0_source_data']['data'])
# some data cleaning code...

df.to_csv('output/1_clean_data/clean_data.csv', index=False)

print("Cleaned data generated and saved to 'artificial_data.csv'")

