import threading
import time

def take_orders(n):
    for i in range(1, n):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

# create threads
#order_thread = threading.Thread(target=take_orders)
order_thread = threading.Thread(target=take_orders, args=(5,))

brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# wait for both to finish
# calling thread is main thread
# thread whose join method is caled is order and brew
order_thread.join() # blocks the main thread untile order_thread has terminated
brew_thread.join() # blocks the main thread untile brew_thread has terminated

print("All orders taken and chai brewed")
