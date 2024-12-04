import re
data = open("input.txt", "r").read().splitlines()
limits = {'red': 12, "green": 13, "blue": 14}
game_sum = 0
for line in data:
    game_array = line.split(":")
    game_num = game_array[0].split(" ")[1]
    green_games = [int(val) for val in re.findall(r'\d*\s(?=green)', game_array[1])]
    red_games = [int(val) for val in re.findall(r'\d*\s(?=red)', game_array[1])]
    blue_games = [int(val) for val in re.findall(r'\d*\s(?=blue)', game_array[1])]
    if limits['red'] >= int(max(red_games)) and limits['green'] >= int(max(green_games)) and limits['blue'] >= int(max(blue_games)):
        game_sum += int(game_num)
print(game_sum) 

total_power = 0
for line in data:
    game_array = line.split(":")
    game_num = game_array[0].split(" ")[1]
    green_games = max([int(val) for val in re.findall(r'\d*\s(?=green)', game_array[1])])
    red_games = max([int(val) for val in re.findall(r'\d*\s(?=red)', game_array[1])])
    blue_games = max([int(val) for val in re.findall(r'\d*\s(?=blue)', game_array[1])])
    total_power += red_games * green_games * blue_games
print(total_power)