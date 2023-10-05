fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Error in openning file", fname)

count = dict()

for line in fhand:
    if line.startswith('From') and not line.startswith("From:"):
        words = line.split()
        count[words[2]] = count.get(words[2], 0) + 1
    

print(count)