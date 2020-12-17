
def get_data():
    data_file = open("data.txt")

    tree_count = 1

    groups = []
    group = ""
    for val in data_file:
        if len(val.strip()) == 0:
            # end of section, pack it up
            groups.append(group.strip(' \t\n\r'))
            group = ""
        else:
            group += val.strip(' \t\n\r')
    data_file.close()

    if group != "":
        groups.append(group.strip(' \t\n\r'))

    return (groups)


def check_data(groups):
    total = 0
    for g in groups:
        count = len(set(list(g)))
        total += count
    print(total)


def main():
    data = get_data()
    check_data(data)


main()
