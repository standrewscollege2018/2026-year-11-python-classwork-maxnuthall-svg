'''raffle'''
print ("welcome to the raffle")

prize = str(input("what is the prize being raffeled?"))
print(f"the prize is {prize}")
value = int(input(f"enter the value of the object"))
print ("type end when you want to stop")
entrants = []
get_word = True
while get_word == True:
try:
    get_names = True
    while get_names == True:
        name = input("give me a name")
        if name == "end":
            get_names = False
        else:
         entrants.append(name)
print(f"the names of the contestants are {entrants}"

except ValueError:
        print("that is not a word")
