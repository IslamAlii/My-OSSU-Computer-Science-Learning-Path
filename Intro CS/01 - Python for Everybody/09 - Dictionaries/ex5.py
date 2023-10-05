fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Error in openning file", fname)

count = dict()
domains = dict()


for line in fhand:
    if line.startswith("From "):
        words = line.split()
        count[words[1]] = count.get(words[1], 0) + 1

for domain in count:
    d = domain[domain.find("@")+1: ]
    domains[d] = domains.get(d, 0) +1




    

print(domains)