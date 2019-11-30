from queue import Queue
import threading
from time import sleep

queue = Queue()

def readFile():
    with open('2-Threading_with_Lock/text.txt') as f:
        for line in f:
            yield line

def consumer(callback):
    print("Consumer: waiting")
    result = queue.get()
    print("Consumer: done")
    callback(result)

def producer(data):
    print("Producer: putting")
    queue.put(data)
    print("Producer: done")

def run_threads(functionTarget):
    threads = []
    t = threading.Thread(target=functionTarget)
    t.start()



iterator = readFile()
line1 = iterator.__next__()
line2 = iterator.__next__()
line3 = iterator.__next__()

print(line1)
print(line2)
print(line3)


