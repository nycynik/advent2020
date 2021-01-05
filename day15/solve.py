
def get_data():
    data = []

    data_file = open("data.txt")

    for val in data_file:
        data = val.strip().split(',')
    data_file.close()

    print(f"read {len(data)} items\n")

    return data


def check_data(data):
    spoken_numbers = {}
    turn = 1
    starting_number_count = len(data)
    last_spoken_number = None
    next_spoken_number = int(data[0])

    while turn <= 30000000:  # 2021:
        # speak the number
        last_spoken_number = next_spoken_number
        if turn > 29990000:
            print(f'Turn {turn:3d}: spoke {last_spoken_number}.')

        # define next spoken number
        if turn < starting_number_count:
            next_spoken_number = int(data[turn])
        else:
            # rule based setting for last_spoken number
            if last_spoken_number not in spoken_numbers:
                next_spoken_number = 0
            else:
                # was in there, do math
                next_spoken_number = turn - spoken_numbers[last_spoken_number]

        # ready for next
        spoken_numbers[last_spoken_number] = turn
        turn += 1

    return None


def main():
    data = get_data()
    check_data(data)


main()
