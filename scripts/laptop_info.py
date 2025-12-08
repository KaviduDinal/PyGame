# ============================================
# Laptop Brand Information System
# Single File Python Program (WORKING VERSION)
# ============================================

laptops = [
    {"Brand":"Apple","Model":"MacBook Air M1","Color":"Silver","RAM":"8GB","Storage":"256GB SSD","Processor":"Apple M1","GPU":"Integrated","ScreenSize":13.3,"OS":"macOS","PriceUSD":999,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Air M1","Color":"Gold","RAM":"16GB","Storage":"512GB SSD","Processor":"Apple M1","GPU":"Integrated","ScreenSize":13.3,"OS":"macOS","PriceUSD":1249,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Air M2","Color":"Midnight","RAM":"8GB","Storage":"256GB SSD","Processor":"Apple M2","GPU":"Integrated","ScreenSize":13.6,"OS":"macOS","PriceUSD":1199,"MarketRank":1,"MadeCountry":"China"},
    {"Brand":"Apple","Model":"MacBook Air M3","Color":"Silver","RAM":"16GB","Storage":"512GB SSD","Processor":"Apple M3","GPU":"Integrated","ScreenSize":13.6,"OS":"macOS","PriceUSD":1499,"MarketRank":1,"MadeCountry":"China"},

    {"Brand":"Dell","Model":"XPS 13","Color":"Silver","RAM":"16GB","Storage":"512GB SSD","Processor":"Intel i7","GPU":"Intel Iris Xe","ScreenSize":13.4,"OS":"Windows 11","PriceUSD":1399,"MarketRank":2,"MadeCountry":"USA"},
    {"Brand":"Dell","Model":"Alienware m15","Color":"White","RAM":"32GB","Storage":"1TB SSD","Processor":"Intel i9","GPU":"RTX 4080","ScreenSize":15.6,"OS":"Windows 11","PriceUSD":2999,"MarketRank":2,"MadeCountry":"USA"}
]

# ============================================
# Display laptops by brand
# ============================================

def show_brand_details(brand_name):
    found = False

    print("\n" + "="*55)
    print(f" LAPTOP DETAILS FOR: {brand_name.upper()}")
    print("="*55)

    for laptop in laptops:
        if laptop["Brand"].lower() == brand_name.lower():
            found = True
            print(f"""
Model       : {laptop['Model']}
Color       : {laptop['Color']}
RAM         : {laptop['RAM']}
Storage     : {laptop['Storage']}
Processor   : {laptop['Processor']}
GPU         : {laptop['GPU']}
Screen Size : {laptop['ScreenSize']} inches
OS          : {laptop['OS']}
Price       : ${laptop['PriceUSD']}
Market Rank : {laptop['MarketRank']}
Made In     : {laptop['MadeCountry']}
-----------------------------------------
""")

    if not found:
        print("❌ Brand not found!")
        print("Available brands: Apple, Dell")

# ============================================
# Main Program
# ============================================

def main():
    print("="*55)
    print("     LAPTOP BRAND INFORMATION SYSTEM")
    print("="*55)

    while True:
        brand = input("\nEnter Laptop Brand (or 'exit'): ").strip()

        if brand.lower() == "exit":
            print("\nThank you for using the system 😊")
            break

        if brand == "":
            print("⚠️ Please enter a brand name!")
            continue

        show_brand_details(brand)

# Run program
if __name__ == "__main__":
    main()
