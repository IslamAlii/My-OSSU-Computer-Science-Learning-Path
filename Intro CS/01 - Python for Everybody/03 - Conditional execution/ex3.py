enteredScore = input("Enter your score: ")

try:
    score = float(enteredScore)
except:
   print("Error, please enter numeric input")
   quit()

if score >= 0.9 and score <= 1 :
    print("A")
elif score >= 0.8 and score < .9  :
    print("B")
elif score >= .7 and score < .8:
    print("C")
elif score >= .6 and score < .7:
    print("D")
elif score < .6 and score >= 0:
    print ("F") 
else:
    print("Error you are out of range")


