import numpy as np


def get_data():
    data = []

    data_file = open("data.txt")

    for val in data_file:
        data.append(np.array(list(val.strip())))
    data_file.close()

    print(f"read {len(data)} lines\n")

    return np.array(data)


def check_adjacent_part1(data, row, col):
    rows, cols = data.shape[:2]
    count_adj = 0

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if(r >= 0 and c >= 0 and r < rows and c < cols):
                if data[r, c] == '#':
                    count_adj += 1

    if data[row][col] == '#':
        count_adj -= 1

    return count_adj


def check_adjacent(data, row, col):
    rows, cols = data.shape[:2]
    count_adj = 0

    directions = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),           (0, 1),
                   (1, -1),  (1, 0),  (1, 1)]


    for d in directions:
        offset_r = 1
        offset_c = 1

        searching = True
        while (searching):
            r = row + (d[0] * offset_r)
            c = col + (d[1] * offset_c)

            if (r >= 0 and c >= 0 and r < rows and c < cols):

                if data[r, c] != '.':

                    if data[r, c] == 'L':
                        searching = False

                    if data[r, c] == '#':
                        count_adj += 1
                        searching = False

            else:
                # we reached bounds and found nothing.
                searching = False

            offset_r += 1
            offset_c += 1

    return count_adj


def check_data(data):
    width = len(data[0])
    height = len(data)

    # print(data, data.shape)
    new_chairs = np.empty_like(data)
    counts = np.zeros_like(data, dtype=int)

    seats_unstable = True
    round_num = 0
    while seats_unstable:

        seats_unstable = False
        for row in range(height):
            for col in range(width):
                space = data[row, col]
                new_chairs[row][col] = space
                if space == '.':
                    continue

                counts[row][col] = check_adjacent(data, row, col)
                if space == 'L' and counts[row][col] == 0:
                    new_chairs[row][col] = '#'
                    seats_unstable = True
                if space == '#' and counts[row][col] >= 5:
                    new_chairs[row][col] = 'L'
                    seats_unstable = True

        # print('\n')
        # for r in range(new_chairs.shape[1]):
        #     print(str(data[r]).replace("'", ''), counts[r],
        #           str(new_chairs[r]).replace("'", ''))

        data = np.copy(new_chairs)
        round_num += 1
        print(round_num)

    print("seats: ", np.count_nonzero(data == '#'))


def main():
    data = get_data()
    check_data(data)


main()
