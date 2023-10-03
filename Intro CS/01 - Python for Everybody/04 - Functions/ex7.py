def computeGrade(score):
    if score >= 0.9 and score <= 1 :
        return "A"
    elif score >= 0.8 and score < .9  :
        return "B"
    elif score >= .7 and score < .8:
        return "C"
    elif score >= .6 and score < .7:
        return "D"
    elif score < .6 and score >= 0:
        return  "F" 
    else:
        return "Error you are out of range"

score = input("Enter score: ")
print(computeGrade(float(score)))