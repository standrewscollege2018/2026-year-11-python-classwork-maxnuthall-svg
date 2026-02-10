'''Demonstrateing how a conditinal statement (if/else) works 
It asks the user for a password and them checks if it is correct'''

#ask for password and store in a varialbe
password = input("Please enter the password: ")

#check if it is correct
if password == "chocolate":
    print("welcome user you have level 1 access")
elif password == "V@nilla":
    print("welcome user you have level 2 access")
elif password == "overwatcher":
    print("welcome user you have level 3 access")
elif password == "blackc!@#)*#^@rrentriv23red":
    print("welcome user you have admin panel access")
elif password == "blu88Yp!e":
    print("welcome user you have level 4 access")
elif password == "Str@berry!CEcrEam":
    print("welcome user you have level 5 access")
elif password == "p@ssw0rd":
    print(" HI HACKER U GOT IT WRONG HAHAHAHAAHHAHA")
else:    print("Incorrect password, DONT try again dummass")