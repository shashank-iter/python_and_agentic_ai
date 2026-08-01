import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    with lock_a:
        print("Lock A acquired by T1")
        with lock_b:
            print("Lock B acquired by T1")


def task2():
    with lock_b:
        print("Lock A acquired by T1")
        with lock_a:
            print("Lock B acquired by T1")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task1)

t1.start()
t2.start()
