import re, string, sys

def normalize(iterator):
    total = sum(iterator())

    result = []
    for value in iterator():
        percent = 100*value/total
        result.append(percent)

    return result


def get_iterator(numbers):
    for num in numbers:
        yield num

if __name__ == '__main__':
    listNumbers = [15, 35, 80]

    result = normalize(lambda: get_iterator(listNumbers))
    print(result)
