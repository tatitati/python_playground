from queue import Queue
import threading
from time import sleep
import re

queue1 = Queue()
queue2 = Queue()


def readLineFile(filepath):
    with open(filepath) as f:
        for line in f:
            yield line


def findLinks(text):
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)


def stage1(filepath):
    for line in readLineFile(filepath):
        print(f"Stage1: putting")
        queue1.put(line)
    # send sentinel to allow the rest that there won't be more data coming and they can close
    queue1.put(None)
    queue1.task_done()
    print("stage 1: closing")
    print("Stage1: done")


def stage2():
    while True:
        textline = queue1.get()
        if textline is None:
            queue2.put(None)
            print("stage 2: closing")
            queue2.task_done()
            return

        urls = findLinks(textline)
        for url in urls:
            print(f"\t\t\t\tstage2: forwarding url -> {url}")
            queue2.put(url)
            queue2.task_done()


def stage3():
    while True:
        url = queue2.get()
        if url is None:
            print("stage 3: closing")
            return

        print(f"\t\t\t\t\t\t\t\tstage3: Received -> {url}")
        queue2.task_done()


def run_threads():
    t1 = threading.Thread(target=stage1, args=['2-Threading_with_Lock/text.txt'])
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

run_threads()
# q = Queue(2) # max amount of items that we can put in the queue. If we put more, then the .put() block until more space is released
# q.put("asdfasdf")
# print("-")
# q.put("11111")
# print("-")
# q.put("33434")  # this line becomes block, waitingo for the consumer to do space in the queue (by consuming). Otherwise this producer cannot put any other msg
# print("------")
# print(q.get())
# print(q.get())
# print(q.get())

