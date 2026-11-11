⏱️ #Таймер на Python
```
Простой консольный таймер, показывающий сколько секунд прошло с запуска.
```

💻 #Код

```
import time

start = time.time()
while True:
    seconds = int(time.time() - start)
    print(f"\rПрошло: {seconds} сек", end="")
    time.sleep(1)
```

🚀 #Запуск

```
python timer.py
```

Остановка — Ctrl + C.

