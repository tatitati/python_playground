from queue import Queue
import threading
from time import sleep
import re

queue1 = Queue()
queue2 = Queue()

def readLineFile():
    with open('2-Threading_with_Lock/text.txt') as f:
        for line in f:
            yield line

def findLinks(text):
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)

def stage1():
    for line in readLineFile():
        sleep(1)
        print("Stage1: putting")
        queue1.put(line)
    print("Stage1: done")

def stage2():
    while True:
        textline = queue1.get()
        sleep(1)
        urls = findLinks(textline)
        for url in urls:
            print(f"\t\t\t\tstage2: Received -> {url}")
            queue2.put(url)
        print("\t\t\t\tStage2: done")


def stage3():
    while True:
        url = queue2.get()
        sleep(1)
        print(f"\t\t\t\t\t\t\t\tstage3: Received -> {url}")
        print("\t\t\t\t\t\t\t\tStage3: done")

def run_threads():
    t1 = threading.Thread(target=stage1)
    t2 = threading.Thread(target=stage2)
    t3 = threading.Thread(target=stage3)

    t1.start()
    t2.start()
    t3.start()

    threads = []
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)

    for thread in threads:
        thread.join()

# iterator = readLineFile()
# line1 = iterator.__next__()
# line2 = iterator.__next__()
# line3 = iterator.__next__()
#
# print(line1)
# print(line2)
# print(line3)

run_threads()

