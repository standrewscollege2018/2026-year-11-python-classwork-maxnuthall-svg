'''student drivers status'''
names  = ['Alice', 'Charlie', 'David', 'Eve']
licensestatus = ['full', 'learners', 'restricted', 'no license' ]
changing = "yes"

print ("student drivers status")
print ("=======================")
get_number = True
while name == True:
    try:
        name = int(input("Enter a name: "))
        name = False
for i in range(len(names)):
    print (f"{i+1} {names[i]:>10} {licensestatus[i]:>15}")
while changing != "n":
    changing = input("do you want to change a license status? (y/n)")
    if changing == "y":
        name = input("enter the name of the student:")
        if name in names:
            newstatus = input("enter the new license status:")
            index = names.index(name)
            licensestatus[index] = newstatus
        else:
            print("name not found")
    except ValueError:
        print("invalid input")