import re, string, sys


def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index+1


if __name__ == '__main__':
    words = 'Four score and seven years ago'

    result1 = index_words(words)  # result: <generator object index_words at 0x106724c00>
    print(list(result1))  # [0, 5, 11, 15, 21, 27]

    result2 = index_words(words) # result: <generator object index_words at 0x106724c00>
    print(result2.__next__()) # 0
    print(result2.__next__()) # 5
    print(result2.__next__()) # 11
    print(result2.__next__()) # 15
    print(result2.__next__()) # 21
    print(result2.__next__()) # 27
    print(result2.__next__()) # StopIteration



