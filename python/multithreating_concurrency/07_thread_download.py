import threading
import time

import requests


def download(url):
    print(f"Starting Download {url}")
    response = requests.get(url)
    print(f"Finished download from {url}, size: {len(response.content)} bytes")


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()

threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
print(f"All Downloads done")
time_taken = end - start
print(f"Time taken: {time_taken:.2f} seconds")

# why thread shines here, all three images are getting
# downloaded from a different source, write into different memory spaces
# thus one thread can work while other waits.
