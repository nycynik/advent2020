
def get_data():
    data = []

    data_file = open("test.txt")

    for val in data_file:
        data = list(map(int, list(val.strip())))
    data_file.close()

    print(f"read {len(data)} lines\n")

    return data


def print_cups(cups, current_cup_idx):

    output = "cups: "
    for c in range(len(cups)):
        if c == current_cup_idx:
            output += f'({cups[c]}) '
        else:
            output += f'{cups[c]} '

    print(output)


def check_data(cups):

    min_cup = min(cups)
    max_cup = max(cups)
    length = len(cups)
    pickup_cups = []

    round_number = 1
    current_cup_idx = 0
    while round_number < 10:
        print(f"-- move {round_number} --")
        current_cup = cups[current_cup_idx]

        print_cups(cups, current_cup_idx)

        # TODO: fix this logic
        pickup_idx = current_cup_idx + 1
        for x in range(3):
            if pickup_idx >= len(cups):
                pickup_idx = length - 1
            pickup_cups.append(cups.pop(pickup_idx))
        print(f"pick up: {pickup_cups}")

        destination_cup = current_cup - 1
        while destination_cup in pickup_cups:
            destination_cup -= 1
            if destination_cup < min_cup:
                destination_cup = max_cup
        print(f'destination: {destination_cup}\n')

        # replace pickups
        destination_cup_idx = cups.index(destination_cup)
        for cup in pickup_cups:
            destination_cup_idx += 1
            if destination_cup_idx > length:
                destination_cup_idx = 0
            cups.insert(destination_cup_idx, cup)
        pickup_cups = []

        # set current
        current_cup_idx += 1
        if current_cup_idx > len(cups):
            current_cup_idx = 0

        round_number += 1

    return None


def main():
    data = get_data()
    check_data(data)


main()
