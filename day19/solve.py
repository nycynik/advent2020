
def get_data():
    data = []

    data_file = open("test.txt")

    rules = {}
    messages = []

    type = 0
    for val in data_file:
        if (val.strip() == ''):
            type = 1
            continue

        if type == 0:
            # process rules
            rule_data = val.strip().split(': ')
            rules[rule_data[0]] = rule_data[1]
        else:
            messages.append(val.strip())

    data_file.close()

    print(f"read {len(rules)} rules\n")

    return (rules, messages)


def validate_message_against_sub_rule(m, sub_rule, rules):

    rule_numbers = sub_rule.split(' ')
    message = m
    for rule in rule_numbers:
        #process rule
        print(rules[rule], message)
        valid, char_count = check_message_for_rule(m, rule, rules)
        if not valid:
            return False
        else:
            message = message[char_count:]

    return True


def print_message(m, offset):
    return m[:offset-1] + '>' + m[offset] + '<' + m[offset+1:]


def check_message_for_rule(m, moffset, rule_id, rules):

    is_valid = False
    rule = rules[rule_id]
    print(
        f'Offset: {moffset}, Rule: {rule_id} message: {print_message(m, moffset)}')

    if (rule[0] == '"'):
        # simple rule.
        if m[moffset] == rule[1]:
            is_valid = True
            moffset += 1

    else:
        # numeric rule
        sub_rules = rule.split(' | ')

        for s in sub_rules:
            for next_rule_id in s.split(" "):
                outcome, moffset = check_message_for_rule(
                    m, moffset, next_rule_id, rules)
            #
            # if validate_message_against_sub_rule(m, s, rules) == True:
            #     return True

    return is_valid, moffset


def check_message(m, rules):

    # alwasy check vs rule 0
    return check_message_for_rule(m, 0, '0', rules)


def check_data(data):
    rules, messages = data

    print(rules)
    print("")
    valid_count = 0
    for m in messages:
        print("message", m)
        if (check_message(m, rules) == True):
            valid_count += 1

    return valid_count


def main():
    data = get_data()
    print(check_data(data))


main()
