
def get_data():
    data = []

    # data_file = open("data.txt")
    data_file = open("test.txt")

    nearby_tickets = []
    your_ticket = ""
    lables = {}

    modes = ['values', 'you', 'nearby']
    mode = 0
    for val in data_file:
        if val.strip() == '':
            continue

        if (mode == 0):
            if val.strip() == 'your ticket:':
                mode += 1
            else:
                # print(val, val == 'your ticket:')
                data_lable, ranges = val.split(':')
                lables[data_lable] = ranges.strip().split(' or ')

        elif mode == 1:
            if val.strip() == 'nearby tickets:':
                mode += 1
                continue
            else:
                your_ticket = val

        elif mode == 2:
            nearby_tickets.append(val)

        data.append(val.strip())
    data_file.close()

    data = (lables, your_ticket, nearby_tickets)
    return data


def check_data(data):

    (lables, your_ticket, nearby_tickets) = data

    ranges = []
    label_ranges = {}

    for l in lables:
        for val in lables[l]:
            print(f'val: {val}')
            val_min, val_max = (int(v) for v in val.split('-'))
            extended = False
            for r_idx in range(len(ranges)):
                r_min, r_max = ranges[r_idx]
                # test if it's in the range already
                # if r_min >= val_min and r_max <= val_max:
                #     # completly contained in an existing range, move along.
                #     pass
                # elif r_max < val_min or r_min > val_max:
                #     pass  # outside of range entirely.
                # else:

                if (r_min <= val_min <= r_max) and val_max > r_max:
                    ranges[r_idx] = (r_min, val_max)
                    extended = True
                elif r_min <= val_max <= r_max and val_min < r_min:
                    ranges[r_idx] = (val_min, r_max)
                    extended = True

            if not extended:
                ranges.append((int(val_min), int(val_max)))
            print(ranges)

    # now find the problems
    error_count = 0
    valid_tickets = []
    for scan_values in nearby_tickets:
        is_ticket_valid = True
        for scan_value in (int(sval) for sval in scan_values.split(',')):
            is_valid = False
            for r_idx in range(len(ranges)):
                r_min, r_max = ranges[r_idx]
                if r_min <= scan_value <= r_max:
                    is_valid = True
                    break
            if not is_valid:
                error_count += scan_value
                is_ticket_valid = False
        if is_ticket_valid:
            valid_tickets.append(scan_values.strip())

    # work it out
    potentials = []
    for x in range(len(your_ticket.strip().split(','))):
        potentials.append([])
    for valid_ticket in valid_tickets:
        valid_ticket_values = valid_ticket.strip().split(',')
        for valid_data_idx in range(len(valid_ticket_values)):
            potentials[valid_data_idx].append(
                int(valid_ticket_values[valid_data_idx]))
    print(potentials)

    # now that we have all the potential valid values, go over each lable, and see if it works for these values.
    for p in range(len(potentials)):
        # for this grouping, see wich labels are valid for it.
        for l in lables:
            for val in lables[l]:
                print(f'val: {val}')
                val_min, val_max = (int(v) for v in val.split('-'))

    print(error_count)
    print(valid_tickets)


def main():
    data = get_data()
    check_data(data)


main()
