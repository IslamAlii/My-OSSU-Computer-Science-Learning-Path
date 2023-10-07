fname = input("Enter file name: ")
fhand = open(fname)

d = dict()
l = list()
mails = list()

for line in fhand:
    if line.startswith("From "):
        mails.append(line.split()[1])
        
for mail in mails:
    d[mail] = d.get(mail, 0) + 1

for k,v in d.items():
    l.append((v,k))

l.sort(reverse = True)
print(l[0])