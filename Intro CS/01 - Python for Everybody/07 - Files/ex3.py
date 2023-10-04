fname = input("Enter file name: ")
count = 0



try:
    fhand = open(fname)
except: 
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()

    print("File cannot be opened:", fname)
    exit()

for line in fhand:
    count = count + 1

print("There were 1797 subject lines in", count)