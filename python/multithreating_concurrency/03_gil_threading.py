# Global Interpreter Lock GIL in Threading
# CPython (Classic Python): Multithreading in classic python is not
# memory safe, in the case of race conditions, two threads can try to modify the
# same memory space, thus the GIL provides a mutex lock. In this example, make it clear
# that lock is not on the variable count as two threads would have different copy of functions and
# internal variables to run, but GIL here takes care of internal memory management of python and acquires
# lock there.
# The GIL protects the interpreter's own bookkeeping (refcounts, internal data structures) — and it does this
# by brute force, locking out all other threads from running any Python code whatsoever, regardless of what data
# they're touching.

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

thread1 =threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken: {end - start:.2f} seconds")
# more amount of time to be taken as both threads trying to manipulate same variable
#
