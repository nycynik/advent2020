
def get_data():
    data_file = open("data.txt")

    tree_count = 1

    identities = []
    identity = ""
    for val in data_file:
        if len(val.strip()) == 0:
            # end of identity, pack it up
            identities.append(identity.strip(' \t\n\r'))
            identity = ""
        else:
            identity += val.strip(' \t\n\r') + " "
    data_file.close()

    if identity != "":
        identities.append(identity.strip(' \t\n\r'))

    return(identities)


def check_data(identities):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid_count = 0
    for i in identities:
        is_valid = True
        for rf in required_fields:
            if i.count(rf + ":") == 0:
                is_valid = False
                print(f"invalid={i}\n")
                break

        if is_valid:
            valid_count += 1

    print(f"Found {valid_count} valid identities.")


def main():
    data = get_data()
    check_data(data)


main()
