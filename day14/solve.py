# with hash instead of array

def get_data():
    data = {}

    data_file = open("data.txt")

    for idx, val in enumerate(data_file):
        value = ''
        if (val[:7] == 'mask = '):
            v = val.strip()[7:]
            value = (int(v.replace('0', 'X').replace('X', '0'), 2),
                     int(v.replace('1', 'X').replace('X', '1'), 2),
                     v)
        else:
            v = val.strip().split(' = ')
            value = (v[0][4:-1], v[1])
        data[idx] = value

    data_file.close()

    print(f"read {len(data)-1} commands\n")

    return data


def check_data(data):
    memory = {}
    mask_ones = 0
    mask_zeros = 0
    for k, d in data.items():
        if len(d) == 3:
            mask_ones = d[0]
            mask_zeros = d[1]
            mask = d[2]
            print(f"\nNew Mask: {bin(mask_zeros)}\n")
        else:
            v = int(d[1])
            result = (v | mask_ones) & mask_zeros
            print(k, d[0])
            print(f" value: {v:36b}\t(decimal {v})")
            print(f"  mask: {mask}")
            print(f"result: {result:36b}\t(decimal {result})")
            memory[d[0]] = result
    print("\rresult", sum(memory.values()))
    return None


def main():
    data = get_data()
    check_data(data)


main()
