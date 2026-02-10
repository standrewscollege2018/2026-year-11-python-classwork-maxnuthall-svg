"""paracitomol doasage per age"""
#get age and weight from user
weight = int(input("Enter your weight "))
age = int(input("Enter your age: "))

if age < 9 and weight <= 40:
    print(" you should take 400g of paracitomal")