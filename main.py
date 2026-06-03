import os
import json
import pandas as pd
from glob import glob

json_folder = "json_folder"  # Folder containing all JSON files

all_restaurants = []

for file in glob(os.path.join(json_folder, "*.json")):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

        for restaurant in data:
            row = {
                "id": restaurant.get("id"),
                "name": restaurant.get("name"),
                "address": restaurant.get("address"),
                "phone": restaurant.get("phone"),
                "timing": restaurant.get("timing"),
                "cost_for_two": restaurant.get("cost_for_two"),

                # Ratings
                "dining_score": restaurant.get("ratings", {}).get("dining", {}).get("score"),
                "dining_count": restaurant.get("ratings", {}).get("dining", {}).get("count"),
                "delivery_score": restaurant.get("ratings", {}).get("delivery", {}).get("score"),
                "delivery_count": restaurant.get("ratings", {}).get("delivery", {}).get("count"),

                # Convert list to text
                "cuisines": ", ".join(restaurant.get("cuisines", []))
            }

            all_restaurants.append(row)

# Create DataFrame
df = pd.DataFrame(all_restaurants)

# Save to Excel
output_file = input("Enter file name: ")+".xlsx"
df.to_excel(output_file, index=False)

print(f"Saved {len(df)} restaurants to {output_file}")