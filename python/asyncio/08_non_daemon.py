import threading
import time

# Daemon threads are those threads which automatically shutdown when main thread is gone


def monitor():
    while True:
        print("Monitoring")
        time.sleep(2)


t = threading.Thread(target=monitor, daemon=False)
t.start()
print("Main Program Done")
