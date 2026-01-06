import pandas as pd

# Load the CSV file
data = pd.read_csv("countries_full_dataset.csv")

# Convert country names to lowercase for easy searching
data["country"] = data["country"].str.lower()

while True:
    country_name = input("\nEnter country name (or type 'exit' to quit): ").lower()

    if country_name == "exit":
        print("Goodbye 👋")
        break

    # Search for the country
    result = data[data["country"] == country_name]

    if result.empty:
        print("❌ Country not found. Please try again.")
    else:
        row = result.iloc[0]

        print("\n🌍 Country Details")
        print("---------------------")
        print(f"Country     : {row['country'].title()}")
        print(f"Continent   : {row['continent']}")
        print(f"Currency    : {row['currency']}")
        print(f"Population  : {row['population']}")
        print(f"Nationality : {row['nationality']}")
        print(f"Religions   : {row['religions']}")
        print(f"Universities: {row['universities']}")
