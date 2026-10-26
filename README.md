**agent.py** - промпт, інструменти, пошук по базі знань, цикл агента
**knowledge.md** - база знань: правила компанії. Агент бере з неї лише потрібні розділи
**server.py** - HTTP API (POST /chat)
**cli.py** - чат у терміналі
**.env** - OPENROUTER_API_KEY і MODEL

## Запуск
(я робив через venv - ви вже як бажаєте)
1) Впишіть ключ OpenRouter у .env
2) python3 -m venv .venv
3) .venv/bin/pip install -r requirements.txt
5) .venv/bin/python cli.py або .venv/bin/uvicorn server:app (http://127.0.0.1:8000)


## Обмеження
Сесії зберігаються в пам'яті процесу. Правила в **knowledge.md** тестові. Авторизації та ліміту запитів немає.
