
def get_data():
    program = {}

    data_file = open("data.txt")

    for idx, val in enumerate(data_file):
        d = val.split()
        program[idx] = [d[0], int(d[1])]
    data_file.close()

    return program


def check_data(data, debug=False):

    program_counter = 0
    accumulator = 0

    line_visited = set()
    idx = 0

    while program_counter < len(data):
        idx += 1
        if program_counter in line_visited:
            break
        else:
            line_visited.add(program_counter)
            # run the line
            instruction, value = data[program_counter]
            if debug:
                print(f'{instruction} {value:3d} | {idx}')
            if instruction == 'nop':
                program_counter += 1  # we do nothing
            elif instruction == 'acc':
                accumulator += value
                program_counter += 1
            elif instruction == 'jmp':
                program_counter += value

    print(f"Accumulator value: {accumulator}")

    return program_counter


def check_data2(data):

    # total brute force not even trying to backtrack.
    for idx in range(len(data)):

        instruction, value = data[idx]
        if instruction == 'nop' or instruction == 'jmp':
            # hack it!
            hacked_program = data.copy()
            if instruction == 'nop':
                hacked_program[idx] = ['jmp', data[idx][1]]
            else:
                hacked_program[idx] = ['nop', data[idx][1]]

            # just try it.
            print('hacked line ', idx, 'of', len(data))
            pc = check_data(hacked_program)

            if pc == len(hacked_program):
                print("it worked!")
                break
            else:
                print("infinite loop detected.")
            print(f"terminated with pc: {pc} / {len(hacked_program)}\n")


def main():
    data = get_data()
    check_data(data)
    check_data2(data)


main()
