import time

start = time.time()
while True:
    result = int(time.time() - start)
    mins = int(result // 60)
    secs = int(result % 60)
    if mins > 0:
        time_str = f"{mins} мин {secs} сек"
    else:
        time_str = f"{secs} сек"
    print(f"\rПрошло: {time_str}", end="")
    time.sleep(1)