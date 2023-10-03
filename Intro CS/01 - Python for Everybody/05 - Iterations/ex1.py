total = 0
count = 0
avg = 0

while True:
    snum = input("Enter a number: ")
    try:
        if snum == "done":
            break
        else:
            num = float(snum)
            total = total + num
            count = count + 1
    except:
        print("Please enter just numbers")

print(total, count, total / count)