"""ask for a grater number than the number set """
#get base number
bn= int(input("what is the base number?"))

getnum = True
while getnum == True:
    gn = int(input("enter a number greater than the first number"))
    if gn > bn:
        getnum = False
    else:
        print("try again")
print ("you got it right!")