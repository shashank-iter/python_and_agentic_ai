def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1


# jitna chahiye utna generate karke dega
# depends on comsuming function what it want to generate

refill = infinite_chai()
refill2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(refill2))
