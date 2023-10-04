nums = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        print("minimum:", min(nums))
        print("maximum:", max(nums))
        quit()

    try:
        fnum = float(num)
        nums.append(fnum)
    except:
        print("Error please enter a number or done to quit")



  