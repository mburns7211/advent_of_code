path = "inputs/day1_input.txt"
f = open(path, "r")

input_lst = f.read().split("\n")


curr_sum = 0
sum_lst = []

for i in input_lst:
    if i == "":
        sum_lst.append(curr_sum)
        curr_sum = 0
    else:
        curr_sum += int(i)

sum_lst.sort()
top_three = sum_lst[-1] + sum_lst[-2] + sum_lst[-3]
print(f"max sum: {sum_lst[-1]}")
print(f"top 3 sum: {top_three}")
