from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value('i', 0)
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    # counter variable is a shared variable between the 4 processes being created above
    # the lock prevents another process to edit the variable when one process is using it.
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value: ",counter.value )