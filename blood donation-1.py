"""blood donor"""
WEIGHT = int(input("Enter your weight in kg: "))
AGE = int(input("Enter your age: "))
if AGE >= 16 and WEIGHT >= 50:
    print("You are eligible to donate blood.")
else :
    print("You are not eligible to donate blood.")