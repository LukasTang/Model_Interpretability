# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None

# -

import numpy as np
import pandas as pd

# Set the random seed for reproducibility
np.random.seed(42)

# Generate 100 random x values
x = np.random.rand(100)

# Generate y values with some noise
y = 2 * x + 1 + np.random.normal(0, 0.1, 100)

# Create a DataFrame
data = pd.DataFrame({'x': x, 'y': y})

data.plot(title="DataFrame Plot")

# Save the DataFrame to a CSV file
data.to_csv('artificial_data.csv', index=False)

print("Artificial data generated and saved to 'artificial_data.csv'")
