
def get_data():
    data = []

    data_file = open("data.txt")
    # data_file = open("test.txt")

    for val in data_file:
        data.append(val.strip())
    data_file.close()

    cubes = {}
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '#':
                cubes[f'{row}|{col}|0|0'] = 1

    print(f"read {len(data)} lines\n")

    return cubes


def print_state(cube_active_neighbor_counts, active_cubes):
    for z in range(-7, 8):
        print(f'z:{z}')
        for x in range(-7, 8):
            count_line = ''
            active_line = ''
            for y in range(-7, 8):
                cube_location = f'{x}|{y}|{z}'
                spacer = ' '
                if cube_location == '0|0|0':
                    spacer = '<'
                if cube_location in cube_active_neighbor_counts:
                    count_line += str(
                        cube_active_neighbor_counts[cube_location]) + spacer
                else:
                    count_line += '  '

                active = '#'
                inactive = '.'
                if cube_location == '0|0|0':
                    active = '*'
                    inactive = '+'

                if cube_location in active_cubes:
                    active_line += active
                else:
                    active_line += inactive
            print(active_line, ' ', count_line)


def check_data(active_cubes):

    for cycle in range(6):

        print(f'\nCycle: {cycle + 1}')

        cube_active_neighbor_counts = {}
        for cube in active_cubes:

            cx, cy, cz, cw = [int(c) for c in cube.split('|')]

            # set neighbor counts
            # print(cube)
            for x in range(cx-1, cx+2):
                for y in range(cy-1, cy+2):
                    for z in range(cz-1, cz+2):
                        for w in range(cw-1, cw+2):
                            cube_location = f'{x}|{y}|{z}|{w}'
                            if not (cube_location == cube):
                                if cube_location in cube_active_neighbor_counts:
                                    cube_active_neighbor_counts[cube_location] += 1
                                else:
                                    cube_active_neighbor_counts[cube_location] = 1
                            else:
                                if cube_location not in cube_active_neighbor_counts:
                                    cube_active_neighbor_counts[cube_location] = 0
                            # print(cube_location,
                            #       cube_active_neighbor_counts[cube_location])

        # now make new cubes
        new_cubes = {}
        for cube_location in cube_active_neighbor_counts:
            is_active = False
            if cube_location in active_cubes:
                is_active = active_cubes[cube_location]

            if is_active and (cube_active_neighbor_counts[cube_location] == 2 or
                              cube_active_neighbor_counts[cube_location] == 3):
                new_cubes[cube_location] = 1
            if not (is_active) and cube_active_neighbor_counts[cube_location] == 3:
                new_cubes[cube_location] = 1

        active_cubes = new_cubes
        print(f'Active Cube Count: {len(active_cubes)}')

        # print_state(cube_active_neighbor_counts, active_cubes)

    print(len(active_cubes))


def main():
    data = get_data()
    check_data(data)


main()

# track only live cubes
# track them as x-y-z strings in a hash
# so '1-2-1' in the hash means that cube is live.
