# some interesting stuff!
# https://en.wikipedia.org/wiki/Binary_space_partitioning


def get_seat_id(seat):

    row = (0, 127)
    col = (0, 7)
    seat_id = 0
    for i in range(len(seat)):
        c = seat[i]
        if i == 6:
            if c == 'F':
                row = row[0]
            else:
                row = row[1]
        elif i < 6:
            mid_row = row[0] + ((row[1] - row[0]) // 2)
            if c == 'F':
                row = (row[0], mid_row)
            elif c == 'B':
                row = (mid_row + 1, row[1])

        if i == 9:
            if c == 'L':
                col = col[0]
            else:
                col = col[1]
        elif 7 <= i <= 8:
            mid_col = col[0] + ((col[1] - col[0]) // 2)
            if c == 'L':
                col = (col[0], mid_col)
            elif c == 'R':
                col = (mid_col + 1, col[1])

        # print(c, row, col)
    seat_id = (row * 8) + col
    return seat_id


def get_data():
    data_file = open("data.txt")

    max_seat_id = 0
    min_seat_id = 100000000000
    seat_id_list = []
    for val in data_file:
        seat_id = get_seat_id(val)
        max_seat_id = max(max_seat_id, seat_id)
        min_seat_id = min(min_seat_id, seat_id)
        seat_id_list.append(int(seat_id))
    data_file.close()

    print(f"seat range is from {min_seat_id} to {max_seat_id}")
    sum_of_range = sum(list(range(min_seat_id, max_seat_id)))
    sum_of_ids = sum(seat_id_list)
    print(sum_of_range, sum_of_ids, sum_of_ids - sum_of_range)

    seat_id_list.sort()
    print(seat_id_list)
    return (max_seat_id)


def check_data(data):
    pass


def main():
    data = get_data()
    check_data(data)


main()
