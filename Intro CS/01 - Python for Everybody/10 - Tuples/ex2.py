fname = input("Enter file name: ")
fhand = open(fname)

d = dict()
l = list()


for line in fhand:
    if line.startswith("From "):
        time= line.split()[5].split(':')[0]
        d[time] = d.get(time, 0) + 1

for k, v in d.items():
    l.append((k,v))

l.sort()
for i in l:
    print(i[0], i[1])

