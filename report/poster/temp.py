import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use("TkAgg")

# Load the data
df = pd.read_csv("ASLFingerspelling.csv")

# Group by a field (e.g., 'ItemType')
library_data = df["Library Catalog"].value_counts()

type_data = df["Item Type"].value_counts()


# Create a function to calculate the absolute value
def absolute_value(val):
    a = np.round(val / 100.0 * library_data.sum(), 0)
    return int(a)

def absolute_value_type(val):
    a = np.round(val / 100.0 * type_data.sum(), 0)
    return int(a)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))  # Change to 1 row, 2 columns

# Create a larger pie chart in the first subplot
ax[0].pie(library_data, labels=library_data.index, autopct=absolute_value)
ax[0].set_title("Distribution of Library Catalog in Zotero Library")

# Create a smaller pie chart in the second subplot
# Use only a subset of the data for the smaller pie chart
ax[1].pie(type_data, labels=type_data.index, autopct=absolute_value_type)
ax[1].set_title(".. and their Item Types")

plt.show()

# Convert 'year' column to numeric
df['Year'] = pd.to_numeric(df['Publication Year'], errors='coerce')

# Count the occurrences of each year
year_counts = df['Publication Year'].value_counts().sort_index()

# Create a bar chart for the years
plt.figure(figsize=(10, 6))
plt.bar(year_counts.index, year_counts, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Distribution of Publication Years in ASL Fingerspelling Recognition Research')
plt.xticks(rotation=45)
plt.show()