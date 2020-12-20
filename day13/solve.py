
def get_data():
    data = []

    data_file = open("data.txt")

    for val in data_file:
        data.append(val.strip())
    data_file.close()

    print(f"read {len(data)} lines\n")

    return data


def check_data(data):
    departure_target_time = int(data[0])
    busIDs = data[1].strip().split(',')

    delays = []
    for bus in busIDs:
        if bus != 'x':
            b = int(bus)
            delays.append((b, (b - (departure_target_time % b))))
            print(f"{b}\t{delays[-1][1]}")
        else:
            delays.append((b, 939))

    best = min(delays, key=lambda t: t[1])
    print(f"shortest wait is {best[1]} minutes on bus {best[0]}")
    print(f"answer: {best[0] * best[1]}")


def checkConsecutive(l):
    """https://www.geeksforgeeks.org/python-check-if-list-contains-consecutive-numbers/"""
    return sorted(l) == list(range(min(l), max(l) + 1))


def check_data2(data):
    departure_target_time = int(data[0])
    busIDs = data[1].strip().split(',')

    departure_target_time = 0
    while True:
        departure_target_time += 1
        delays = []
        fake = int(busIDs[0])
        for bus in busIDs:
            if bus != 'x':
                b = int(bus)
                delays.append(b - (departure_target_time % b))
            else:
                delays.append(fake)
            fake += 1
        if checkConsecutive(delays):
            print(departure_target_time, delays)
    best = min(delays, key=lambda t: t[1])
    print(f"shortest wait is {best[1]} minutes on bus {best[0]}")
    print(f"answer: {best[0] * best[1]}")


def main():
    data = get_data()
    check_data(data)
    check_data2(data)


main()
