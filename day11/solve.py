
def get_data():
    data = []

    data_file = open("data.txt")

    for val in data_file:
        data.append(val)
    data_file.close()

    print(f"read {len(data)} lines\n")

    return data


def check_data(data):
    return None


def main():
    data = get_data()
    check_data(data)


main()


# with hash instead of array

def get_data():
    data = {}

    data_file = open("data.txt")

    for idx, val in enumerate(data_file):
        data[idx] = val.split()
    data_file.close()

    print(f"read {len(data)} lines\n")

    return data


def check_data(data):
    for k, d in data.items():
        print(k, d)
    return None


def main():
    data = get_data()
    check_data(data)


main()
