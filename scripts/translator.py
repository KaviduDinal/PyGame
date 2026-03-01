from deep_translator import GoogleTranslator

def translate_text():
    print("🌍 Language Translator")
    print("-----------------------")

    text = input("Enter text to translate: ")
    source = input("Source language (auto or en, si, ta, fr): ")
    target = input("Target language (en, si, ta, fr): ")

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        print("\n✅ Translated Text:")
        print(translated)

    except Exception as e:
        print("\n❌ Error:", e)

if __name__ == "__main__":
    translate_text()
