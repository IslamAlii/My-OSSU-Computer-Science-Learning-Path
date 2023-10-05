fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Error in openning fiel", fname)
    quit()

count = dict()
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1




bigword = None
bigcount = None

for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    
print("Most frequntly word is '"+ bigword + "' with", bigcount, "times")



