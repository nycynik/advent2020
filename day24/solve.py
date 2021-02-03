import copy


def get_data():
    data = []

    data_file = open("data.txt")

    for val in data_file:
        line = val.strip()
        cur_word = ''
        cur_line = []
        for idx in range(len(line)):
            c = line[idx]
            if cur_word == '' and (c == 'e' or c == 'w'):
                cur_line.append(c)
            else:
                if cur_word == '':
                    cur_word = c
                else:
                    cur_word += c
                    cur_line.append(cur_word)
                    cur_word = ''
        data.append(cur_line)
    data_file.close()

    print(f"read {len(data)} lines\n")

    return data


def count_black_neighbors(key, tiles):
    directions = {
        'e':  (-1,  0),
        'ne': (0, -1),
        'nw': (+1, -1),
        'w':  (+1,  0),
        'sw': (0,  +1),
        'se': (-1, +1)
    }

    count = 0
    for d in directions.values():
        loc = (key[0] + d[0], key[1] + d[1])
        if loc in tiles and tiles[loc] == 0:
            count += 1

    return count


def check_data(data):

    directions = {
        'e':  (-1,  0),
        'ne': (0, -1),
        'nw': (+1, -1),
        'w':  (+1,  0),
        'sw': (0,  +1),
        'se': (-1, +1)
    }

    locations = {}

    for tile_instruction in data:
        location = (0, 0)
        for direction in tile_instruction:
            location = (location[0] + directions[direction]
                        [0], location[1] + directions[direction][1])

        if location in locations:
            if locations[location] == 0:  # black
                locations[location] = 1
            else:
                locations[location] = 0
        else:
            locations[location] = 0

    print("part 1", len(locations) - sum(locations.values()), '\n')

    for day_num in range(1, 101):
        next_locations = copy.deepcopy(locations)

        for tile_key in locations:
            count = count_black_neighbors(tile_key, locations)
            next_locations[tile_key] = locations[tile_key]
            if locations[tile_key] == 0 and (count == 0 or count > 2):
                next_locations[tile_key] = 1
            if locations[tile_key] == 1 and count == 2:
                next_locations[tile_key] = 0

        locations = next_locations

        count = len(locations) - sum(locations.values())

        print(f'Day {day_num}: {count}')


def main():
    data = get_data()
    check_data(data)


main()
