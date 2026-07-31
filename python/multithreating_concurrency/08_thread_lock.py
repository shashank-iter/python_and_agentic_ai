import threading

counter = 0
lock = threading.Lock()
# lock the memory space in case on same memory being used

def increament():
    global counter
    for _ in range(100000):
        with lock: # locks the particular mem location
            counter += 1

threads = [threading.Thread(target=increament) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")