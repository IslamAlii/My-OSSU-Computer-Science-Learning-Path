fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Error in openning file", fname)

count = dict()
person = None
max_messages = 0

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        count[words[1]] = count.get(words[1], 0) + 1



    

print(count)