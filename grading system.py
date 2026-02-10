"""get a numbe from 1-100 to get  a grade from a b c d or f"""

#get the grade from 1-100
grade = int(input("Enter your score from 1-100: "))
if grade > 100:
    print("Invalid score, please enter a number from 1-100")
elif grade == 100:
    print("You got the highest score A+!")
elif grade >= 90:
    print("You got an A")
elif grade >= 70:
    print("You got a B")
elif grade >= 60:
    print("You got a C")   
elif grade >= 50:
    print("You got a D")
elif grade < 0: 
    print("Invalid score, please enter a number from 1-100")
else: 
    print("You failed")