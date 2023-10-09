import re

fname = input('Enter file name: ')
fhand = open(fname)
total_sum = 0

for line in fhand:
    numbers = re.findall(r'[0-9]+', line)
    for num_str in numbers:
        num = int(num_str)
        total_sum = total_sum + num



print( total_sum)

