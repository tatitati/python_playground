import re, string, sys



def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)

    return result


def read_visits(numbers):
    for num in numbers:
        yield num

if __name__ == '__main__':
    listNumbers = [15, 35, 80]
    print(normalize(listNumbers)) # [11.538461538461538, 26.923076923076923, 61.53846153846154]


    iterator = read_visits(listNumbers)
    result = normalize(iterator)
    print(result) # []
