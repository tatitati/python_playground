from queue import Queue
import threading
from time import sleep

queue = Queue()

def readFile():
    with open('2-Threading_with_Lock/text.txt') as f:
        for line in f:
            yield line

def stage1(func, toQueue):
    print("Stage1: waiting")
    result = queue.get()
    print("Stage1: done")
    func(result)

def stage2(func, fromQueue, toQueue):
    print("Stage2: waiting")
    result = queue.get()
    print("Stage2: done")
    func(result)

def stage3(func, fromQueue):
    print("Stage3: waiting")
    result = queue.get()
    print("Stage3: done")
    func(result)

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


