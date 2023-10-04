fname = input("Enter file: ")

try:
    fhand = open(fname)
except:
    print("Error in opening file", fname)

count = 0
for line in fhand:
    if line.startswith('From')  and  not line.startswith("From:"):
        count = count + 1
        words = line.split()
        print(words[1])
    continue


print("There were", count  ,"lines in the file with From as the first word")