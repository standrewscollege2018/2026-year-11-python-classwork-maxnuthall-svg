"""paracitomol doasage per age"""
#get age and weight from user
weight = int(input("Enter your weight "))
age = int(input("Enter your age: "))
if age >= 0 and weight >= 0:
    if age <= 2:
        print(" you should take 2 500mg tables")
    else:
        dosage = weight * 10
        print ("you should take " (dosage) + "mg")
else:   
    print ("this isnt a valid input")