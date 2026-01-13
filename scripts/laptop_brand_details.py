# ============================================
# Laptop Brand Information System
# Single File Python Program
# ============================================

# Dataset stored as a list of dictionaries
laptops = [
    {"Brand":"Apple","Model":"MacBook Air M1","Color":"Silver","RAM":"8GB","Storage":"256GB SSD","Processor":"Apple M1","GPU":"Integrated","ScreenSize":13.3,"OS":"macOS","PriceUSD":999,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Air M1","Color":"Gold","RAM":"16GB","Storage":"512GB SSD","Processor":"Apple M1","GPU":"Integrated","ScreenSize":13.3,"OS":"macOS","PriceUSD":1249,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Air M2","Color":"Midnight","RAM":"8GB","Storage":"256GB SSD","Processor":"Apple M2","GPU":"Integrated","ScreenSize":13.6,"OS":"macOS","PriceUSD":1199,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Air M2","Color":"Starlight","RAM":"16GB","Storage":"512GB SSD","Processor":"Apple M2","GPU":"Integrated","ScreenSize":13.6,"OS":"macOS","PriceUSD":1399,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Air M3","Color":"Silver","RAM":"16GB","Storage":"512GB SSD","Processor":"Apple M3","GPU":"Integrated","ScreenSize":13.6,"OS":"macOS","PriceUSD":1499,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Pro M1","Color":"Space Gray","RAM":"16GB","Storage":"512GB SSD","Processor":"Apple M1 Pro","GPU":"Integrated","ScreenSize":14.0,"OS":"macOS","PriceUSD":1999,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Pro M2","Color":"Silver","RAM":"16GB","Storage":"1TB SSD","Processor":"Apple M2 Pro","GPU":"Integrated","ScreenSize":14.0,"OS":"macOS","PriceUSD":2299,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Pro M3","Color":"Black","RAM":"18GB","Storage":"1TB SSD","Processor":"Apple M3 Max","GPU":"Integrated","ScreenSize":16.0,"OS":"macOS","PriceUSD":3199,"MarketRank":1,"MadeCountry":"China"},

    {"Brand":"Dell","Model":"XPS 13 9310","Color":"Silver","RAM":"16GB","Storage":"512GB SSD","Processor":"Intel i7 11th Gen","GPU":"Intel Iris Xe","ScreenSize":13.4,"OS":"Windows 11","PriceUSD":1399,"MarketRank":2,"MadeCountry":"USA"},
    {"Brand":"Dell","Model":"XPS 13 Plus","Color":"Graphite","RAM":"32GB","Storage":"1TB SSD","Processor":"Intel i7 13th Gen","GPU":"Intel Iris Xe","ScreenSize":13.4,"OS":"Windows 11","PriceUSD":1999,"MarketRank":2,"MadeCountry":"USA"},
    {"Brand":"Dell","Model":"XPS 15","Color":"Platinum","RAM":"32GB","Storage":"1TB SSD","Processor":"Intel i9","GPU":"NVIDIA RTX 4070","ScreenSize":15.6,"OS":"Windows 11","PriceUSD":2899,"MarketRank":2,"MadeCountry":"USA"},
    {"Brand":"Dell","Model":"Inspiron 14","Color":"Black","RAM":"8GB","Storage":"512GB SSD","Processor":"Intel i5","GPU":"Intel UHD","ScreenSize":14.0,"OS":"Windows 11","PriceUSD":699,"MarketRank":5,"MadeCountry":"China"},
    {"Brand":"Dell","Model":"Inspiron 15","Color":"Silver","RAM":"16GB","Storage":"1TB HDD","Processor":"Intel i7","GPU":"Intel UHD","ScreenSize":15.6,"OS":"Windows 11","PriceUSD":849,"MarketRank":5,"MadeCountry":"China"},
    {"Brand":"Dell","Model":"Latitude 5420","Color":"Gray","RAM":"16GB","Storage":"512GB SSD","Processor":"Intel i7","GPU":"Intel Iris Xe","ScreenSize":14.0,"OS":"Windows 11","PriceUSD":1299,"MarketRank":4,"MadeCountry":"Malaysia"},
    {"Brand":"Dell","Model":"Alienware m15","Color":"White","RAM":"32GB","Storage":"1TB SSD","Processor":"Intel i9","GPU":"NVIDIA RTX 4080","ScreenSize":15.6,"OS":"Windows 11","PriceUSD":2999,"MarketRank":2,"MadeCountry":"USA"}
]

# ============================================
# Function to display laptops by brand
# ============================================

def show_brand_details(brand_name):
    found = False
    print("\n" + "="*60)
    print(f" LAPTOP DETAILS FOR BRAND: {brand_name.upper()}")
    print("="*60)

    for laptop in laptops:
        if laptop["Brand"].lower() == brand_name.lower():
            found = True
            print("\n----------------------------------------")
            print(f"Model        : {laptop['Model']}")
            print(f"Color        : {laptop['Color']}")
            print(f"RAM          : {laptop['RAM']}")
            print(f"Storage      : {laptop['Storage']}")
            print(f"Processor    : {laptop['Processor']}")
            print(f"GPU          : {laptop['GPU']}")
            print(f"Screen Size  : {laptop['ScreenSize']} inches")
            print(f"Operating OS : {laptop['OS']}")
            print(f"Price (USD)  : ${laptop['PriceUSD']}")
            print(f"Market Rank  : {laptop['MarketRank']}")
            print(f"Made In      : {laptop['MadeCountry']}")
            print("----------------------------------------")

    if not found:
        print("\n❌ Brand not found!")
        print("Available Brands: Apple, Dell, HP, Lenovo, Asus")

# ============================================
# Main Program
# ============================================

def main():
    print("\n========================================")
    print("     LAPTOP BRAND INFORMATION SYSTEM")
    print("========================================")

    while True:
        brand = input("\nEnter Laptop Brand (or 'exit' to quit): ")

        if brand.lower() == "exit":
            print("\nThank you for using the system 👍")
            break

        show_brand_details(brand)

# Run program
main()
