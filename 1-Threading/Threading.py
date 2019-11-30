import threading
import time

def do_something():
    print("thread sleeping 2 second...")
    time.sleep(2)
    print("thread DONE")



start = time.perf_counter()

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

finish = time.perf_counter()
print("Main completed. total time: " + str(finish - start))


# > python 1-Threading/1-Threading.py                                                                                                                                                           master * ] 3:13 PM
#
# OUTPUT:
# ======
# thread sleeping 2 second...
# thread sleeping 2 second...
# Main completed. total time: 0.00037168500000000007
# thread DONE
# thread DONE

