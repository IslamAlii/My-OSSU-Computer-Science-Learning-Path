import re

fname = input("Enter file name: ")
fhand = open(fname)
text = fhand.read()
pattern = r'New Revision: (\d+)'

numbers  = re.findall(pattern, text)
        

if numbers:
    numbers = [int(num) for num in numbers]  
    average = sum(numbers) // len(numbers)  

    print(average)
else:
    print("No matching lines found")