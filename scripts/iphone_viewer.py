import csv

CSV_FILE = "iphone_data.csv"

def load_data():
    data = []
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def show_iphone_list(data):
    print("\n📱 Available iPhones:\n")
    for i, phone in enumerate(data, start=1):
        print(f"{i}. {phone['series']} {phone['variant']}")

def show_details(phone):
    print("\n" + "="*45)
    print(f"📱 {phone['series']} - {phone['variant']}")
    print("="*45)

    print(f"📅 Year        : {phone['model_year']}")
    print(f"🖥 Display     : {phone['display']}")
    print(f"📷 Camera      : {phone['camera']}")
    print(f"🔋 Battery     : {phone['battery']}")
    print(f"⚙ Chip        : {phone['chip']}")

    print("\n💾 Storage Options:")
    for s in phone['storage'].split("|"):
        print(" -", s)

    print("\n🎨 Colors:")
    for c in phone['colors'].split("|"):
        print(" -", c)

    print(f"\n💰 Price (USD) : ${phone['price_usd']}")
    print("="*45)

def main():
    data = load_data()

    while True:
        show_iphone_list(data)
        choice = input("\nSelect iPhone number (0 to exit): ")

        if choice == "0":
            print("Goodbye 👋")
            break

        if not choice.isdigit():
            print("❌ Enter a number only")
            continue

        choice = int(choice)
        if 1 <= choice <= len(data):
            show_details(data[choice - 1])
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
