import threading
import time

def do_something():
    print("thread sleeping 2 second...")
    time.sleep(2)
    print("thread DONE")



start = time.perf_counter()

threads = []

for _ in range(10):
    t=threading.Thread(target=do_something)
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
#
# thread sleeping 2 second...
# thread sleeping 2 second...
# thread sleeping 2 second...
# thread sleeping 2 second...
# thread sleeping 2 second...
# thread sleeping 2 second...
# thread sleeping 2 second...
# thread sleeping 2 second...
# thread sleeping 2 second...
# thread sleeping 2 second...
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# thread DONE
# Main completed. total time: 2.0073876370000003


