from multiprocessing import Process, Queue

def worker(q, n):
    result = n * n
    q.put(result)   # send result back to main process

if __name__ == "__main__":
    q = Queue()
    processes = [Process(target=worker, args=(q, i)) for i in range(5)]
    # results are getting calculated in separate processes but they can be
    # pushed into the q and can be accessed from queue.
    for p in processes: p.start()
    for p in processes: p.join()

    results = [q.get() for _ in range(5)]
    print(results)
