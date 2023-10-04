fname = input("Enter file name: ")
total = 0
count = 0



try:
    fhand = open(fname)
except: 
    print("there is no file with name:", fname)
    exit()

for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    
    pos = line.find(":") + 1
    total = total + float(line[pos: ])
    count = count + 1

print("Average spam confidence:", total / count)