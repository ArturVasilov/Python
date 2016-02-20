def zero_crossing_counts_list(numbers, overlay, step):
    if len(numbers) == 0:
        return []

    step_with_overlay = int(step * (1 - overlay))

    if step_with_overlay == 0:
        raise Exception("we can't iterate list with such overlay")

    size = len(numbers) / step_with_overlay
    results = []

    left = 0 if (len(numbers) % step_with_overlay == 0) else 1
    for index in xrange(0, size + left):
        start = index * step_with_overlay
        end = start + step
        results.append(zero_crossing_count(numbers[start:end]))

    return results


def zero_crossing_count(numbers):
    result = 0
    count = len(numbers)
    index = 0
    while index < count - 1:
        if is_different_sign(numbers[index], numbers[index + 1]):
            result += 1
        else:
            if numbers[index] == 0:
                result += 1
        index += 1
    return result


def is_different_sign(first, second):
    return (first < 0 < second) or (first > 0 > second)
