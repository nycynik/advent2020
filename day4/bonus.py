import re


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
                break

        if is_valid:
            identity_data = {}
            data = i.split(' ')
            for d in data:
                k, v = d.split(':')
                identity_data[k] = v

            # silly buy here we go!
            if 1920 <= int(identity_data['byr']) <= 2002:
                if 2010 <= int(identity_data['iyr']) <= 2020:
                    if 2020 <= int(identity_data['eyr']) <= 2030:
                        if (identity_data['hgt'].endswith('cm') and (150 <= int(identity_data['hgt'][:-2]) <= 193)) or \
                                (identity_data['hgt'].endswith('in') and (59 <= int(identity_data['hgt'][:-2]) <= 76)):
                            if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', identity_data['hcl']):
                                if identity_data['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                    if identity_data['pid'].isdigit() and len(identity_data['pid']) == 9:
                                        valid_count += 1

    print(f"Found {valid_count} valid identities.")


def main():
    data = get_data()
    check_data(data)


main()
