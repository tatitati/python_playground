import threading
import time

def do_something(seconds):
    print(f"thread sleeping {seconds} second...")
    time.sleep(seconds)
    print("thread DONE")

start = time.perf_counter()

threads = []
for _ in range(5):
    t=threading.Thread(target=do_something, args=[3])
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()

finish = time.perf_counter()
print("Main completed. total time: " + str(finish - start))


# > python 1-Threading/Threading_listthreads.py
#
# OUTPUT:
# ======
# thread sleeping 3 second...
# thread sleeping 3 second...
# thread sleeping 3 second...
# thread sleeping 3 second...
# thread sleeping 3 second...
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# Main completed. total time: 3.001568395



