# https://dev.to/rpalo/advent-of-code-2020-solution-megathread-day-9-encoding-error-594o
from collections import deque


def get_data():
    data = []

    data_file = open("test.txt")

    for val in data_file:
        data.append(int(val))
    data_file.close()

    return data


def pair_is_summable_to(n, iterable):
    seen = set()
    for x in iterable:
        target = n - x
        if target in seen:
            return True
        seen.add(x)
    return False


def check_data(data, preamble=25):
    queue = deque(data[:preamble], preamble)

    for i, n in enumerate(data[preamble:]):
        if pair_is_summable_to(n, queue):
            queue.append(n)
        else:
            print(f"found the problem!\nvalue: {n} at index {i}")
            return n, i


def break_it(data, weakness):
    for test_len in range(2, len(data)):
        queue = deque(data[:test_len], test_len)
        for pos in range(test_len, len(data)):
            if sum(queue) == weakness:
                w_0 = min(queue)
                w_1 = max(queue)
                print(
                    f"found the encryption weakness!\nvalue: {w_0+w_1} at index {pos}")
                return w_0+w_1, test_len, pos
            else:
                queue.append(data[pos])


def main():
    data = get_data()
    n, _ = check_data(data)
    break_it(data, n)


main()
