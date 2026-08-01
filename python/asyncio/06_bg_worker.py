import asyncio
import threading
import time


def bg_worker():
    while True:
        time.sleep(1)
        print("Print logging system health")


async def fetch_order():
    await asyncio.sleep(3)
    print("Order fetched")


t1 = threading.Thread(target=bg_worker, daemon=True)
t1.start()
asyncio.run(fetch_order())
