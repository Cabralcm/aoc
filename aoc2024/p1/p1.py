# Part 1

with open("input.txt", "r") as f:
    data = f.readlines()

col_1 = []
col_2 = []

for line in data:
    col_1.append(line.split()[0])
    col_2.append(line.split()[1])

col_1.sort()
col_2.sort()

diff_sum = 0
for i,ele in enumerate(col_1):
    diff_sum += abs(int(ele) - int(col_2[i]))

print("Part 1")
print(diff_sum)

# Part 2
dict_2 = {}

for ele in col_2:
    ele = int(ele)
    if ele in dict_2:
        dict_2[ele] += 1
    else:
        dict_2[ele] = 1

sim_score = 0
for ele in col_1:
    ele = int(ele)
    if ele in dict_2:
        sim_score += ele * dict_2[ele]
print("Part 2")
print(sim_score)