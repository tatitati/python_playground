import re, string, sys


class Readvisits(object):
    def __init__(self, listNumbers):
        self.listNumbers = listNumbers

    def __iter__(self):
        for number in self.listNumbers:
            yield number

def normalize(iterator):
    total = sum(iterator)

    result = []
    for value in iterator:
        percent = 100*value/total
        result.append(percent)

    return result

if __name__ == '__main__':
    listNumbers = [15, 35, 80]
    visits = Readvisits(listNumbers)

    result = normalize(visits)
    print(result) # [11.538461538461538, 26.923076923076923, 61.53846153846154]


