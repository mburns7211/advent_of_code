path = "inputs/day1_input.txt"
f = open(path, "r")

input_lst = f.read().split("\n")

max_sum = 0
curr_sum = 0

for i in input_lst:
    if i == "":
        if curr_sum > max_sum:
            max_sum = curr_sum
        curr_sum = 0
    else:
        curr_sum += int(i)

print(f"max sum: {max_sum}")
