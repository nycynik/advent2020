
def get_data():
    data = []

    data_file = open("data.txt")

    for val in data_file:
        data.append(int(val.strip()))
    data_file.close()

    print(f"read {len(data)} lines\n")

    return data


def transform(key, loop_size):
    encryption_key = 1
    for factor in range(1, loop_size + 1):
        encryption_key = (encryption_key * key) % 20201227

    return encryption_key


def check_data(data):

    # calc loop size
    found_key = False
    found_door = False
    factor = 1
    door_loop_size = 0
    key_loop_size = 0

    # we really only need one, but it's fast.
    for loop_size in range(1, 1500000000000000):
        factor = (factor * 7) % 20201227

        if not found_door and factor == data[0]:
            print(factor, data[0], 0, loop_size)
            door_loop_size = loop_size
            found_door = True

        if not found_key and factor == data[1]:
            print(factor, data[1], 1, loop_size)
            key_loop_size = loop_size
            found_key = True

        if factor == 5764801:
            print(5764801, loop_size)

        if factor == 17807724:
            print(17807724, loop_size)

        if found_key and found_door:
            break

    # now we have both loop_factors
    door_encryption_key = transform(data[0], key_loop_size)

    key_encryption_key = transform(data[1], door_loop_size)

    print(transform(17807724, 8))
    print(transform(5764801, 11))

    print(door_encryption_key, key_encryption_key)
    return None


def main():
    data = get_data()
    check_data(data)


main()
