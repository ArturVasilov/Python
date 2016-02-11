# task 1
# sum of first n cubes


def sum_cubes(number):
    result = 0
    for value in range(1, number + 1):
        result += pow(value, 3)
    return result


# task 2
# middle value and median of numbers list


def task2(numbers):
    count = len(numbers)
    if count <= 0:
        raise Exception("Can't handle empty list")

    middle = 0.0
    for value in numbers:
        middle += value

    middle /= count

    sorted_numbers = numbers[:]
    sorted_numbers.sort()

    if count % 2 == 1:
        median = sorted_numbers[count / 2]
    else:
        median = (sorted_numbers[count / 2 - 1] + sorted_numbers[count / 2]) / 2.0

    return middle, median
