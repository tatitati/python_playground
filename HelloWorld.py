import re, string, sys


def index_words(text):
    print("START")
    if text:
        print("called--")
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            print("called")
            yield index+1


if __name__ == '__main__':
    words = 'Four score and seven years ago'

    iterator1 = index_words(words)  # result: <generator object index_words at 0x106724c00>
    print(list(iterator1))
    # START
    # called--
    # called
    # called
    # called
    # called
    # [0, 5, 11, 15, 21, 27]

    print(list(iterator1))
    # []

    iterator2 = index_words(words) # result: <generator object index_words at 0x106724c00>
    print(iterator2.__next__())
    # START
    # called--
    # 0
    print(iterator2.__next__())
    # called
    # 5
    print(iterator2.__next__())
    # called
    # 11
    print(iterator2.__next__())
    # called
    # 15
    print(iterator2.__next__())
    # called
    # 21
    print(iterator2.__next__())
    # called
    # 27






