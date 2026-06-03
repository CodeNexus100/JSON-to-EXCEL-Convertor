import pandas as pd

# Read JSON file
df = pd.read_json("scraped_restaurants_from_201_to_300_20260603_171514.json")

# Save as Excel
df.to_excel("NCR3.xlsx", index=False)

print("Conversion complete!")