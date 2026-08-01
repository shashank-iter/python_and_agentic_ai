import asyncio
import time


async def brew(name):
    print(f"Brewing {name}")
    await asyncio.sleep(2)
    print(f"{name} is ready")


async def main():
    start = time.time()
    await asyncio.gather(brew("Masala Chai"), brew("Cardomom Chai"), brew("Green Tea"))
    # await means you will wait but in a non blocking fashion
    end = time.time()
    print(f"time consumed {end - start}")


asyncio.run(main())
