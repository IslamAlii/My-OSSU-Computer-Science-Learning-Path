def computePay(hours, rate):
    if hours > 40 :
        reg = hours * rate
        otp = (hours - 40) * 1.5 * rate
        return reg + otp
    else :
        return hours * rate
    
stringHours = input("Enter hours: ")
stringRate = input("Enter rate: ")
print("pay",computePay(float(stringHours), float(stringRate)))