from copy import deepcopy

with open("input.txt") as f:
    lines = f.readlines()
    lines = [list(map(int, line.split())) for line in lines]

def parseLine(line):
    for num, ele in enumerate(line[:-1]):
        if num == 0:
            if ele - line[num+1] > 0:
                dir = -1
            elif ele - line[num+1] < 0:
                dir = 1
            else:
                return 0
        if ele - line[num+1] == 0 or abs(ele - line[num+1]) > 3:
            return 0
        elif ele - line[num+1] < 0 and dir == -1 or ele - line[num+1] > 0 and dir == 1:
            return 0
    return 1

count = 0
for line in lines:
    count += parseLine(line)
print("Part 1: ", count)

def parseLine2(line):

    for num, ele in enumerate(line[:-1]):

        previous_element = deepcopy(line) 
        first_element = deepcopy(line)
        second_element = deepcopy(line)
        del first_element[num]
        del second_element[num+1]

        if num == 0:
            if ele - line[num+1] > 0:
                dir = -1
            elif ele - line[num+1] < 0:
                dir = 1
            else:
                return parseLine(first_element) or parseLine(second_element)

        del previous_element[num-1]
        if (ele - line[num+1] == 0 or abs(ele - line[num+1]) > 3):
            return parseLine(previous_element) or parseLine(first_element) or parseLine(second_element)
        elif (ele - line[num+1] < 0 and dir == -1) or (ele - line[num+1] > 0 and dir == 1):
            return parseLine(previous_element) or parseLine(first_element) or parseLine(second_element)
    return 1

out = open("my_output.txt", "w")
count = 0
for line in lines:
    if parseLine2(line):
        out.write(str(line) + "\n")
        count += 1
print("Part 2: ", count)


