import pandas as pd

# Read JSON file
df = pd.read_json("scraped_restaurants_from_501_to_501_20260603_012624.json")

# Save as Excel
df.to_excel("Varanasi6.xlsx", index=False)

print("Conversion complete!")