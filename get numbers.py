"""ask for 2 numbers, print the 2 numbers, tell which num is greater than and add the tgther"""
#get numbers
get_number = True
while get_number == True:
    try:
        number_1 = int(input("what is number 1?"))
        get_number = False
    except ValueError:
        print("that is not a number")
get_number = True
while get_number == True:
    try:
        number_2 = int(input("what is number 2?"))
        get_number = False
    except ValueError:
        print("that is not a number")
print (f"this is number 1 = {number_1} and this is number 2 = {number_2}")
# add them tgther then print
print(f"this is them added together {number_1+number_2}")
#which is greater/equal
if number_1 > number_2:
    print("number 1 is greater")
elif number_1 == number_2:
    print ("they are equal")
else:
    print ("number 2 is greater")