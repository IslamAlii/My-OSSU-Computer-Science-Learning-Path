sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40 :
    reg = fh * fr
    otp = (fh - 40) * 1.5 * fr
    pay = reg + otp
else :
    pay = fh * fr

print("Pay:", pay)

