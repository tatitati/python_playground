import threading
import time

def do_something():
    print("thread sleeping 2 second...")
    time.sleep(2)
    print("thread DONE")


class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset

def worker(how_many, counter):
    for _ in range(how_many):
        counter.increment(1)


def run_threads(func, how_many, counter):
    threads = []
    for _ in range(5):
        args = (how_many, counter)
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


how_many = 100000
counter = Counter()
run_threads(worker, how_many, counter)
print(f'Counter is: {counter.count}')

start = time.perf_counter()


finish = time.perf_counter()
print("Main completed. total time: " + str(finish - start))



# OUTPUT 1:
# ======
# Counter is: 401371
# Main completed. total time: 5.22000000002798e-07

# OUTPUT 2:
# ======
# Counter is: 424795
# Main completed. total time: 1.8823000000001144e-05


# OUTPUT 3:
# ======
# Counter is: 315559
# Main completed. total time: 1.8993999999994404e-05


