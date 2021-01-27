import numpy as np
import re

# with hash instead of array


def get_data():
    data = {}

    data_file = open("test.txt")

    state = 0
    piece = {'grid': np.empty((10, 10)), 'sides': [], 'matches': []}

    piece_row = 0
    for idx, val in enumerate(data_file):

        row_data = val.strip()
        if state == 0:  # looking for a name
            if row_data[0] == 'T':
                piece_id = int(row_data.split(' ')[1][:-1])
                piece = {'grid': np.full((10, 10), '!'),
                         'sides': [],
                         'matches': []}
                piece_row = 0
                state = 1
        elif state == 1:
            if row_data == '':
                state = 0  # we are on next one.
                data[piece_id] = piece
            else:
                # still fetching piece
                piece['grid'][piece_row] = np.array(list(row_data))
                piece_row += 1
            data[piece_id] = piece

    data_file.close()

    for p in data.keys():
        data[p]['sides'].append(''.join(data[p]['grid'][0]))
        data[p]['sides'].append(''.join(data[p]['grid'][-1]))
        data[p]['sides'].append(''.join(data[p]['grid'][:, -1]))
        data[p]['sides'].append(''.join(data[p]['grid'][:, 0]))

    for p in data.keys():
        print(p, len(data[p]['sides']))

    print(f"read {len(data)} lines\n")

    return data


def find_top_matches(this_key, data, side):

    matches = []
    for key in data.keys():
        if key != this_key:
            piece = data[key]
            for s_idx in range(len(piece['sides'])):
                this_side = piece['sides'][s_idx]
                if this_side == side:
                    matches.append((key, s_idx))
                if "".join(reversed(this_side)) == side:
                    matches.append((key, -s_idx))

    return matches


def trim_piece(piece):
    np_piece = piece['grid'][1:-1, 1:-1]
    pattern = "[\' \]\[]"

    block = []
    for row in np_piece:
        this_row = re.sub(pattern, "", str(row))
        block.append(this_row)

    return block


def print_puzzle(puzzle):
    for p in puzzle:
        print(p)


def add_piece_to_puzzle(current_piece, direction, puzzle_picture):

    piece_picture = trim_piece(current_piece)
    flip = False
    if direction < 0:
        flip = True

    for idx, p in enumerate(piece_picture):
        if flip:
            puzzle_picture[idx] += "".join(reversed(p))
        else:
            puzzle_picture[idx] += p

    return puzzle_picture


def build_puzzle(data, start_piece_id):

    current_piece = data[start_piece_id]
    puzzle_picture = trim_piece(current_piece)

    puzzle = [[start_piece_id]]

    # go left!
    has_left_piece = True
    row = 0
    while (has_left_piece):
        has_left_piece = False
        for m in current_piece['matches']:
            if m[1] == 3 or m[1] == -3:
                # we have a match left, so lets use it.
                current_piece_id = m[0]
                current_piece = data[current_piece_id]
                puzzle[row].append(current_piece_id)
                puzzle_picture = add_piece_to_puzzle(
                    current_piece, m[1], puzzle_picture)
                has_left_piece = True

    print_puzzle(puzzle_picture)
    print(puzzle)




def check_data(data):

    # find all matching sides
    for k, d in data.items():
        for s in d['sides']:
            matches = find_top_matches(k, data, s)
            if len(matches) > 0:
                d['matches'] += matches

    # build the puzzle.
    # this seems to have just 1 solution, but a more general solver would be interesting
    # to write. It would need to account for multiple solutions for any piece, until the
    # whole puzzle was put together. But this simple version seems ot have 1 solution,
    # so it's easy to implement.

    quot = 1
    corner_count = 0
    side_count = 0
    inner_count = 0
    start_piece_id = None
    for k, d in data.items():
        print(k, d['matches'])
        link_count = len(d['matches'])
        # corners have only 2 matches.
        if link_count == 2:
            corner_count += 1
            quot *= int(k)
            start_piece_id = k

        if link_count == 3:
            side_count += 1

        if link_count == 4:
            inner_count += 1

    print(f'Corners: {corner_count} sides: {side_count} inside: {inner_count}')
    print(quot)

    print(f'Building...')
    build_puzzle(data, 1951)

    return None


def main():
    data = get_data()
    check_data(data)


main()
