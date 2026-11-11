import time

start = time.time()
while True:
    seconds = int(time.time() - start)
    print(f"\rПрошло: {seconds} сек", end="")
    time.sleep(1)