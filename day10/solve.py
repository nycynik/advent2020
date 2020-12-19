
def get_data():
    data = []

    data_file = open("data.txt")

    for val in data_file:
        data.append(int(val))
    data_file.close()
    print(f"read {len(data)} lines\n")
    return data


def check_data(data):
    adapters = data
    adapters.sort()
    chain_val = adapters[0]
    volts = [0, 0, 0, 0]
    volts[chain_val] += 1
    print(f"{adapters[0]:4d} | {chain_val}")
    for idx in range(1, len(adapters)):
        diff = adapters[idx] - adapters[idx - 1]
        print(f"{adapters[idx]:4d} | {diff}")
        chain_val += diff
        volts[diff] += 1

    print(f" lap | 3")
    chain_val += 3
    volts[3] += 1

    print(f"chain value: {chain_val}")
    print(f"Volts: {volts[1]} * {volts[3]} = {volts[1] * volts[3]}")


def main():
    data = get_data()
    check_data(data)


main()


# # with hash instead of array

# def get_data():
#     data = {}

#     data_file = open("data.txt")

#     for idx, val in enumerate(data_file):
#         data[idx] = val.split()
#     data_file.close()

#     return data


# def check_data(data):
#     for k, d in data.items():
#         print(k, d)
#     return None


# def main():
#     data = get_data()
#     check_data(data)


# main()
