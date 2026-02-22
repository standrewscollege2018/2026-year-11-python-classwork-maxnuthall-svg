'''demonstrating how lists work'''
#list are used to store multiple peices of informtion
#We use square brackets to show its a list
names = ["Ace", "chopper", "luffy", "nami", "sanji", "ussop", "zoro"]

#print the entire list
#ths is useful for debugging
print(names)
#each item has an index, its location in the list
#the first item has a index of zero
#we can print individual items from a list by using there index
print (names[6])
#using a negative index counts backwards from the end of the list
# -1 prints the last item, -2 prints the second to last item, ect
print (names[-1])

#we can use len() to get the number of items in a list
length = len(names)
#this prints out the length of a particular item: print (len(names[5])), this will print the length of the name "ussop" which is 6 characters long
print (len(names[5]))

#to change an items name, just overwrite it by setting a new value for that position in the list
names[4] = "whitebeard"
print (names)

#you can inster items into a particular position in a list using the insert() method
names.insert(1, "maTHEW")
print (names)

#the most common method of adding items is to add them at the end using the append() method
names.append("robin")
print (names)
#when displaying all items from a list it is best to use a loop rather than printing a whole list with brackets and commas
#method 1: displaying each item
for name in names:
    print (name)
#method 2: dysplaying items in a numbered list
for i in range(len(names)):
    print (f"{i+1}. {names[i]}")
