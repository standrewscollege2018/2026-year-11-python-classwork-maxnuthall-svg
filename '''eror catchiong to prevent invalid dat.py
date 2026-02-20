'''eror catchiong to prevent invalid data types'''

get_number = True
while get_number == True:
    try:
        number = int(input("Enter a number: "))
        get_number = False
    except ValueError:
        print("that is not a number")

print (f"you entered {number}")