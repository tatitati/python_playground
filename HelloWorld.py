import re, string, sys


def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index+1


if __name__ == '__main__':
    words = 'Four score and seven years ago'

    iterator1 = index_words(words)  # result: <generator object index_words at 0x106724c00>
    print(list(iterator1))  # [0, 5, 11, 15, 21, 27]

    iterator2 = index_words(words) # result: <generator object index_words at 0x106724c00>
    print(iterator2.__next__()) # 0
    print(iterator2.__next__()) # 5
    print(iterator2.__next__()) # 11
    print(iterator2.__next__()) # 15
    print(iterator2.__next__()) # 21
    print(iterator2.__next__()) # 27
    print(iterator2.__next__()) # StopIteration



