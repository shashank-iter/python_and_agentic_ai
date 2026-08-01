import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# thread pool executer is smiliar to asyncio.gather but for threads


def check_stock(item):
    print(f"Checking stock for {item}")
    time.sleep(3)  # blocking operation
    return f"{item} stock: 42"


async def main():
    loop = asyncio.get_running_loop()
    # gets a handle to currently running event loop, which drives all our async/await scheduling.
    with ThreadPoolExecutor() as pool:
        # creates a pool of worker threads (default: a handful, based on CPU count) sitting ready to
        # run regular, blocking, synchronous functions.
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        # run_in_executor: Hey thread pool (pool), please run check_stock("Masala Chai") on one of your worker threads." This call doesn't wait for the result —
        # it fires off the request and immediately hands back a placeholder object (a Future) that represents "the result that will eventually show up here.
        # the await on future means pause the main() right here, and don't resume until the future actually has a result in it.
        # pausing main() does not freeze the event loop, it just tells the event loop that main() has nothing to do right now, go find other work if there's
        # any and come back to main() once the thread pool finishes.
        # meanwhile a completely saperate thread runs the check_stock function doing its blocking ops, but not impacting event loop.
        print(result)


asyncio.run(main())
