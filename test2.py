import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# URL of the CSV file
url = "https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(url)
base_array = np.arange(len(df['MolLogP']))
print(base_array)
# Display the first few rows of the DataFrame
print(df.head())

x_values = df['logS']
y_values = df['MolLogP']
sorted_series = x_values.sort_values()
num_groups = 3
split_lists = np.array_split(sorted_series, num_groups)

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Subtracting the maximum value for numerical stability
    return exp_x / exp_x.sum()

# Compute softmax for the column values
softmax_values = softmax(x_values)

plt.plot(x_values, softmax_values, 'o', markersize=3)
plt.xlabel('Original Values')
plt.ylabel('Softmax Values')
plt.title('Softmax Transformation')
plt.grid(True)
plt.show()