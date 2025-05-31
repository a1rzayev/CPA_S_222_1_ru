import re

def scan_text(text):
    findings = {}

    patterns = {
        "Emails": r'\b[\w.-]+@[\w.-]+\.\w+\b',
        "Phone Numbers": r'\+?\d{1,3}[-\s]?\(?\d{2,3}\)?[-\s]?\d{3}[-\s]?\d{4}',
        "Credit Cards": r'\b(?:\d[ -]*?){13,16}\b',
        "Passwords": r'\b(?:[A-Za-z0-9@#$%^&+=]{8,})\b',
        "URLs": r'https?://[^\s]+',
        "Sensitive Words": r'\b(?:пароль|взлом|admin|root|token|secret)\b',
    }

    for name, pattern in patterns.items():
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if matches:
            findings[name] = matches

    return findings


def main():
    print("Добро пожаловать в Киберзащитник!")
    print("Введите текст для анализа (или оставьте пустым для выхода):")

    while True:
        user_input = input("\nВведите текст:\n> ")
        if not user_input.strip():
            print("Завершение работы")
            break

        results = scan_text(user_input)
        if results:
            print("\n⚠ Найдено подозрительное:")
            for category, items in results.items():
                print(f"\n {category}:")
                for item in items:
                    print(f"   - {item}")
        else:
            print("✅ Всё чисто. Нарушений не найдено.")


if __name__ == "__main__":
    main()
