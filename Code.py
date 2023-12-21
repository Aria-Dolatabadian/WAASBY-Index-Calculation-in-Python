import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Read data from CSV
df = pd.read_csv('genotype_data.csv')

# Calculate WAASBY index
def calculate_waasby(row):
    return row['WAASB'] / row['GY']

df['WAASBY'] = df.apply(calculate_waasby, axis=1)

# Set 'Genotype' column as the index
df.set_index('Genotype', inplace=True)

# Display the DataFrame with WAASBY index
print(df)

# Visualize the results using a cluster map
sns.clustermap(df[['WAASBY']], cmap='viridis', method='single', col_cluster=False)

plt.title('Cluster Map of WAASBY Index')
plt.show()

