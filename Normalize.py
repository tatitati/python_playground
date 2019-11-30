import re, string, sys

def normalize(lamba_iterator):
    total = sum(lamba_iterator())

    result = []
    for value in lamba_iterator():
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
