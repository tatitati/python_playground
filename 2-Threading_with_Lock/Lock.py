import threading
import time

class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        with threading.Lock():
            self.count += offset # this was the line producing a data race in the data race example

def updateCountObj(counterObj):
    for _ in range(100000):
        counterObj.increment(1)

def run_threads(counterObj):
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=updateCountObj, args=[counterObj])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

counter = Counter() # all the thread will update the counter of this object
run_threads(counter)
print(f'Counter is: {counter.count}') # expected is 500000 (each thread increase count 100.000 and we have 5 threads)

start = time.perf_counter()

finish = time.perf_counter()
print("Main completed. total time: " + str(finish - start))



# OUTPUT 1:
# ======
# Counter is: 500000
# Main completed. total time: 5.22000000002798e-07

# OUTPUT 2:
# ======
# Counter is: 500000
# Main completed. total time: 1.8823000000001144e-05


# OUTPUT 3:
# ======
# Counter is: 500000
# Main completed. total time: 1.8993999999994404e-05


