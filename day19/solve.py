import re

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
            rules[int(rule_data[0])] = rule_data[1]
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


def make_rule(rules):
    rle = '^'

    # first find our a's and b's
    a_rule = None
    b_rule = None
    for k in rules.keys():
        if (rules[k][1] == 'a'):
            a_rule = k
        if (rules[k][1] == 'b'):
            b_rule = k
    del rules[a_rule]
    del rules[b_rule]
    print(f"found a at {a_rule} and b at {b_rule}")
    
    # replace the as and b's
    for r in rules.keys():
        print(rules[r])
        rules[r] = rules[r].replace(str(a_rule), "a").replace(str(b_rule), "b")

    print (rules)
    # for r in rules[0]:
    #     if r != ' ':
    #         rule = rules[int(r)]
    #         if (rule[0] == '"'):
    #             # simple rule.
    #             rle.append(rule[1])
    #         else:
    #             done = False
    #             rle.append(rules[int(r)])

    done = False

    checker = re.compile('[ab |]+')
    while not done:
         done = True

         # for each rule, check if it contains only letters and |. If not, 
         # try to replace it, but only if the rule it links is already converted to
         # only letters.
         for r in rules.keys():
            
            c = checker.match(rules[r])
            if c is None:
                # done = False
                print('found', rules[r])
                for item in rules[r].split(' '):
                    if item != 'a' and item != 'b':
                        lookup = rules[int(item)]
                        if checker.match(lookup) != None:
                            print(lookup)


    print(rle)
    return rle

def check_message(m, rules):

    # alwasy check vs rule 0

    # checker = re.compile('^a[[aa|bb]?[ab|ba]?|[ab|ba]?[aa|bb]?]b')
    checker = re.compile('^a((aaab|aaba|bbab|bbba)|(abaa|abbb|baaa|babb))b')
    print(m, checker.match(m))

    # return check_message_for_rule(m, 0, '0', rules)


def check_data(data):
    rules, messages = data

    print(rules)
    regex_string = make_rule(rules)
    print("matcher", regex_string)
    
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
