import re
data = open("input.txt", 'r').read().splitlines()
lookup = {'one': "1",'two': '2','three': '3','four': '4','five' : '5','six' : '6','seven' : '7','eight' : '8','nine' : '9', "1": '1', "2": '2', "3": '3', "4": '4', "5": '5', "6": '6', "7": '7',"8": '8', "9": '9'}

# P1
numbers = [''.join(re.findall(r'\d*', line)) for line in data]
total = sum([int(number)* 10 + int(number) if len(number) < 2 else (int(number[0]) * 10 + int(number[-1])) for number in numbers])
# P2

with open("out.txt", "w") as f:
    total = 0
    for num,line in enumerate(data):
        first = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line)
        last = re.match(r'.+(one|two|three|four|five|six|seven|eight|nine|\d)', line)
        first_value = lookup.get(first[0], None)
        last_value = first_value if last == None else lookup.get(last.group(1), None)
        value = int(first_value + last_value)
        total += value
        f.write(str(line) + "\n")
        f.write(str(num) + " " + str(first_value) + " " + str(last_value) + " " + str(value) + '\n')
        # f.write(str(total) + '\n')
    print(total)

with open("out_yifan.txt", "w") as f:
    total = 0
    for num,line in enumerate(data):
        first = re.match(r".*?(one|two|three|four|five|six|seven|eight|nine|\d)", line)
        last = re.match(r".*(one|two|three|four|five|six|seven|eight|nine|\d)", line)

        first_value = lookup.get(first.group(1), first.group(1))
        last_value = lookup.get(last.group(1), last.group(1))
        value = int(first_value + last_value)
        
        total += value
        f.write(str(line) + "\n")
        f.write(str(num) + " " + str(first_value) + " " + str(last_value) + " " + str(value) + '\n')
        # f.write(str(total) + '\n')
    print(total)