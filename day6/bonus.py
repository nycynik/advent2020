
def get_data():
    data_file = open("data.txt")

    tree_count = 1

    groups = []
    group = ""
    g_size = 0
    for val in data_file:
        if len(val.strip()) == 0:
            # end of section, pack it up
            groups.append((g_size, group.strip(' \t\n\r')))
            group = ""
            g_size = 0
        else:
            group += val.strip(' \t\n\r')
            g_size += 1
    data_file.close()

    if group != "":
        groups.append((g_size, group.strip(' \t\n\r')))

    return (groups)


def check_data(groups):
    total = 0
    for c, g in groups:
        all_in_group = set(list(g))
        count = 0
        for val in all_in_group:
            if g.count(val) == c:
                count += 1
        total += count
    print(total)


def main():
    data = get_data()
    check_data(data)


main()
