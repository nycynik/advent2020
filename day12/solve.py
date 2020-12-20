from math import cos, sin, pi, radians, degrees


def get_data():
    data = []

    data_file = open("data.txt")

    for val in data_file:
        data.append(val.strip())
    data_file.close()

    print(f"read {len(data)} lines\n")

    return data


def check_data(data):

    # n=0/360, w=270, e=90, s=180
    # arbitrarily decide to start at 0,0 in a quadrant, so north is -, west is -, s&e +

    ship_heading = 0  # east
    pos = (0, 0)

    for move in data:
        action = move[0]
        distance_angel = int(move[1:])
        if action in ['N', 'S', 'W', 'E']:
            # we move the ship
            if action == 'N':
                pos = (pos[0], pos[1] + distance_angel)
            elif action == 'S':
                pos = (pos[0], pos[1] - distance_angel)
            elif action == 'W':
                pos = (pos[0] - distance_angel, pos[1])
            elif action == 'E':
                pos = (pos[0] + distance_angel, pos[1])

        elif action in ['L', 'R']:
            # we position the heading
            if action == 'L':
                ship_heading += distance_angel
            else:  # right
                ship_heading -= distance_angel
            # no reason to keep over rotations
            ship_heading = ship_heading % 360

        elif action == 'F':
            # we go forward
            delta = (round(cos(radians(ship_heading))) * distance_angel,
                     round(sin(radians(ship_heading))) * distance_angel)
            pos = (int(pos[0] + delta[0]), int(pos[1] + delta[1]))

        print(
            f"Command: {move}\tPos: ({pos[0]:5d}, {pos[1]:5d})\t Heading: {ship_heading}")

    # calk manhattan dist
    # super simple, since I started at 0,0
    print(f"Distance from starting point: {abs(0 - pos[0]) + abs(0-pos[1])}\n")
    return None


def check_data2(data):

    # new iterpretation of the data

    # n=0/360, w=270, e=90, s=180
    # arbitrarily decide to start at 0,0 in a quadrant, so north is -, west is -, s&e +

    waypoint_heading = 0  # east
    ship_pos = (0, 0)
    waypoint_pos = (10, 1)  # relative to ship

    for move in data:
        action = move[0]
        distance_angel = int(move[1:])
        if action in ['N', 'S', 'W', 'E']:
            # we move the ship
            if action == 'N':
                waypoint_pos = (waypoint_pos[0],
                                waypoint_pos[1] + distance_angel)
            elif action == 'S':
                waypoint_pos = (waypoint_pos[0],
                                waypoint_pos[1] - distance_angel)
            elif action == 'W':
                waypoint_pos = (
                    waypoint_pos[0] - distance_angel, waypoint_pos[1])
            elif action == 'E':
                waypoint_pos = (
                    waypoint_pos[0] + distance_angel, waypoint_pos[1])

        elif action in ['L', 'R']:
            # we position the heading
            if action == 'L':
                waypoint_heading += distance_angel
            else:  # right
                waypoint_heading -= distance_angel
            # no reason to keep over rotations
            waypoint_heading = waypoint_heading % 360

            # silly, but I didn't want to type more
            if distance_angel > 180:
                distance_angel = distance_angel - 180
                if action == 'L':
                    action = 'R'
                else:
                    action = 'L'

            # now move the waypoint
            if distance_angel == 180:
                waypoint_pos = (-waypoint_pos[0], -waypoint_pos[1])
            elif distance_angel == 90 and action == 'R':
                waypoint_pos = (waypoint_pos[1], -waypoint_pos[0])
            elif distance_angel == 90 and action == 'L':
                waypoint_pos = (-waypoint_pos[1], waypoint_pos[0])
            else:
                print(f"\n\nOH NO - {distance_angel}\n\n")

            delta = (round(cos(radians(waypoint_heading))),
                     round(sin(radians(waypoint_heading))))
            # move waypoint to origin, rotate it, and move back
            # (-(y - b_ + a, (x - a) + b))
            #waypoint_pos = (
            #    int(waypoint_pos[0] + delta[0]), int(waypoint_pos[1] + delta[1]))

        elif action == 'F':
            # we go forward x times
            delta = (waypoint_pos[0] * distance_angel,
                     waypoint_pos[1] * distance_angel)
            ship_pos = (int(ship_pos[0] + delta[0]),
                        int(ship_pos[1] + delta[1]))

        print(f"Command: {move}\tPos: ({ship_pos[0]:5d}, {ship_pos[1]:5d})\t"
              f"Waypoint: ({waypoint_pos[0]:5d}, {waypoint_pos[1]:5d})\t Heading: {waypoint_heading}")

    # calk manhattan dist
    # super simple, since I started at 0,0
    print(
        f"Distance from starting point: {abs(0 - ship_pos[0]) + abs(0-ship_pos[1])}")
    return None


def main():
    data = get_data()
    check_data(data)
    check_data2(data)


main()
