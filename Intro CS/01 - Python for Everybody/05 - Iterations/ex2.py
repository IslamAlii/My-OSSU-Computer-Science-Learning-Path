min = None
max = None
total = 0
count = 0

while True:
    snum = input("Enter a number: ")

    try:
        if snum == "done":
            break

        num = float(snum)
        total = total + num
        count = count + 1

        if min is None and max is None:
            min = num
            max = num
        elif min < num:
            min = num
        elif max > num:
            max = num
    except: 
        print("Please enter just numbers")

print(min, max, total / count)