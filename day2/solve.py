# just going to brute force this. Need to find two numbers that sum to 2020
import sys


def is_valid(data):
    # 3-4 t: dttt
    # I'm 17 days behind, so just going to force it a bit.

    data_spaced = data.replace('-', ' ', 1)
    data_spaced = data_spaced.replace(':', ' ', 1)
    data_split = data_spaced.split()

    min = int(data_split[0])
    max = int(data_split[1])
    c = data_split[2]
    password = data_split[3]

    found_count = password.count(c)
    vald_count = 0
    if min <= found_count <= max:
        return True

    return False


data_file = open("data.txt")

valid_count = 0
total_count = 0

for val in data_file:
    total_count += 1
    if is_valid(val):
        valid_count += 1

data_file.close()

print(f"found {valid_count} out of {total_count} passowrds.")
