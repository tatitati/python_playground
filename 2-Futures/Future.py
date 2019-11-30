import concurrent.futures
import time

def do_something(seconds):
    print(f"thread sleeping {seconds} second...")
    time.sleep(seconds)
    return "thread DONE"

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    future1 = executor.submit(do_something, 3)
    future2 = executor.submit(do_something, 6)

    print(future1.result())
    print(future2.result())

finish = time.perf_counter()
print("Main completed. total time: " + str(finish - start))


# > python python 2-Futures/Future.py 
#
# OUTPUT:
# ======
# thread sleeping 3 second...
# thread sleeping 6 second...
# thread DONE
# thread DONE
# Main completed. total time: 6.007382809



