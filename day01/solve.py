# just going to brute force this. Need to find two numbers that sum to 2020
import sys

data_file = open("data.txt")

all_values = []
for val in data_file:
    all_values.append(int(val))

total_values = len(all_values)

if total_values > 0:

    for ii in range(0, total_values):
        for ix in range(1, total_values):
            if ii % 100 == 0:
                sys.stdout.write(".") 
            if all_values[ii] + all_values[ix] == 2020:
                print(f"\nfound that {all_values[ii]} + {all_values[ix]} = 2020\nTheir product is {all_values[ii] * all_values[ix]}")

else:
    print("\ncould not read values")

data_file.close()
