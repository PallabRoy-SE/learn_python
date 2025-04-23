import threading
import time


def worker(identifier):
    print(f"Starting {identifier}...")
    time.sleep(2)
    print(f"Stopping {identifier}...")


threads = []

for i in range(1, 4):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All thread completed.")
