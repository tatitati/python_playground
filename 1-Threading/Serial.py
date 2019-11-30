import threading
import time

def do_something():
    print("sleeping 2 second...")
    time.sleep(2)
    print("DONE...")



start = time.perf_counter()

do_something()
do_something()

finish = time.perf_counter()
print("total time: " + str(finish - start))
