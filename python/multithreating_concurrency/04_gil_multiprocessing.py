from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")

if __name__ == "__main__":
# When Python runs a file directly (python script.py),
# it sets a special variable __name__ to the string "__main__" for that file.
# If the same file gets imported elsewhere instead (import script), __name__
# is set to the module's name ("script") instead.
# So this guard just means:
# "only run this block when the file is executed directly,
# not when it's imported."
#
# Rule of thumb: any code in a multiprocessing script that
# creates or starts processes must live inside if __name__ == "__main__":.
# Function/class definitions above it are fine to leave unguarded —
# those need to be importable by the child anyway.
#
# On Windows (and macOS by default), multiprocessing uses the spawn method to create new processes:
# instead of duplicating the current process's memory like Linux's fork() does, it starts a completely fresh
#  Python interpreter and re-imports your script file from scratch just to access the target function (e.g. crunch_number).
#  Re-importing means Python re-executes every top-level line in the file — so if process-creation code (Process(...), .start()) isn't
# guarded by if __name__ == "__main__":, each new
#  child process would re-run that code on import and spawn another process, which imports the file again and spawns
# another, recursing endlessly; Python detects this on spawn platforms and raises a RuntimeError rather than letting
# it run away. Guarding with if __name__ == "__main__": prevents this because __name__ equals "__main__" only when the file is run directly,
# not when it's imported — so the child process's import skips that block and just picks up the function definitions it needs.

    start = time.time()

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p1.close()
    p2.close()

    end = time.time()

    print(f"Total time with multi-processing is {end - start:.2f} seconds")
