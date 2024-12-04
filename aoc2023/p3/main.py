import re
data = open("input.txt", "r").read().split('\n')
#data = open("input_sample.txt", "r").read().split('\n')
pattern_int = re.compile(r'(\d+)')
valid_symbols  = ['\*', '@', '#', '-', '=', '/', '\+', '%', '$', '&']
valid_symbol_reg = "|".join(valid_symbols)
#print(valid_symbol_reg)
pattern_symbol = re.compile(fr'({valid_symbol_reg})')
#pattern_symbol = re.compile(r'(\*|@|#|-|=|/|\+|%|$|&)')
# value_lookup = []

for num,line in enumerate(data):
    for match in pattern_symbol.finditer(line):
         
        if len(match.group()) == 0:
            continue
        print(match.group())
        
    # for match in pattern.finditer(line):
    #     value_lookup.append((num, match.group(1), match.span))
    





def get_sym(data):
    valid_symbols = []
    for num,line in enumerate(data):
        result = re.findall(r'[^\d|^\.]', line)
        for symbol in result:
            if not symbol in valid_symbols:
                valid_symbols[symbol] = True
    return valid_symbols