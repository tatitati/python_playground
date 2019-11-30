import concurrent.futures
import time

def do_something(seconds):
    print(f"thread sleeping {seconds} second...")
    time.sleep(seconds)
    return "thread DONE"

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(4)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print("Main completed. total time: " + str(finish - start))


# > python python 2-Futures/Future.py
#
# OUTPUT:
# ======
# thread sleeping 1 second...
# thread sleeping 1 second...
# thread sleeping 1 second...
# thread sleeping 1 second...
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# Main completed. total time: 1.006365931




