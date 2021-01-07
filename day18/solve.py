import re


def get_data():
    data = []

    data_file = open("test.txt")

    for val in data_file:
        data.append(val.strip())
    data_file.close()

    print(f"read {len(data)} lines\n")

    return data


def paren_matcher(n):
    # poor man's matched paren scanning, gives up
    # after n+1 levels.  Matches any string with balanced
    # parens inside; add the outer parens yourself if needed.
    # Nongreedy.
    return r"[^()]*?(?:\("*n+r"[^()]*?"+r"\)[^()]*?)*?"*n


def pop_expression(exp):
    """ returns the first thing to compute in a crazy expression """

    exp = exp.strip()
    was_paren = False
    pm = re.compile(paren_matcher(25))

    if exp[0] == '(':
        first_part = pm.findall(exp)[1]
        was_paren = True
    else:
        parts = exp.split(' ')
        # print(parts)
        if parts[0] not in ['+', '*']:
            first_part = parts[0]
        else:
            operation = parts[0]
            if (parts[1][0] != '('):
                first_part = operation + ' ' + parts[1]
            else:
                # deal with parens
                first_part = operation + ' ' + pm.findall(exp[2:])[1]

    return first_part, was_paren, exp[(len(first_part)):]


def calc_combine(a, expression):

    if expression[0] != '(':
        data = expression.split(' ')
        operation = data[0]
        operand = None
        if len(data) > 1:
            operand = data[1]
            if (operand[0] == '('):
                # 2 is to skip operation and space
                remaining_exp = expression[2:]
                m = re.findall(paren_matcher(25), remaining_exp)
                operand = do_calc(m[1][1:-1])

        if operation == '+':
            return a + int(operand)
        elif operation == '*':
            return a * int(operand)
        else:
            # special case, its the first thing
            return int(data[0])
    else:  # parens
        m = re.findall(paren_matcher(25), expression)
        return do_calc(m[1][1:-1])


def do_calc(exp):

    accumulator = 0
    starting = True

    while (len(exp) > 0):
        first, was_paren, remaining_exp = pop_expression(exp)

        accumulator = calc_combine(accumulator, first)

        # print('first:', first, was_paren, remaining_exp, accumulator)

        exp = remaining_exp.strip()

        starting = False

    return accumulator


def check_data(data):

    sum_total_pt1 = 0
    sum_total_pt2 = 0

    for calc in data:

        # part 1
        this_value = do_calc(calc)
        sum_total_pt1 += this_value
        print(f'pt1: {calc} = {this_value}')

        # part 2
        exp = calc.split(' * ')
        new_calc = exp[0]
        print(exp)
        for part in range(1, len(exp)):
            new_calc += ' * (' + exp[part] + ')'

        this_value = do_calc(new_calc)
        sum_total_pt2 += this_value
        print(f'pt2: {new_calc} = {this_value}\n')

    print(f'Sum pt1: {sum_total_pt1}')
    print(f'Sum pt2: {sum_total_pt2}')


def main():
    data = get_data()
    check_data(data)


main()
