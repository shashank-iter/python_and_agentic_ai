# Parallelism and Concurrency
- Concurrency: Switching and doing multiple work.
- Parallelism: Running multiple task on same time, using multiple cores for multiple tasks

- Any CPU intesive task being done with threads won't give you the benefit of speed. The reason being mutex and GIL.
- Where threads shine is actually is I/O bound tasks, Disk read and writes, web requests. 
- Queue, Value in Multiprocessing: both are used for inter-process communication. Value is basically a shared variable between different processes. Queue is used for passing messages and results between processes. Data put into a Queue is pickled (serialized) by the sending process and unpickled by the receiving process — because, again, they don't share memory, so the actual bytes have to be copied across the process boundary.
Unlike Value, Queue can hold arbitrary, complex Python objects (lists, dicts, strings, whole data structures) — not just a single fixed-type number.
