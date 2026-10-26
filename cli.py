import agent

session = agent.new_session()
shown = 0
print("Підтримка Opti. Порожній рядок або Ctrl+C для виходу.")
try:
    while text := input("\nВи: ").strip():
        try:
            reply = agent.handle(session, text)
        except RuntimeError as e:  # наприклад, немає ключа
            raise SystemExit(f"Помилка: {e}")
        print(f"\nАгент: {reply}")
        for t in session["tickets"][shown:]:
            print(f"  [звернення {t['id']} · {t['kind']}] {t['summary']}")
        shown = len(session["tickets"])
except (KeyboardInterrupt, EOFError):
    print()
