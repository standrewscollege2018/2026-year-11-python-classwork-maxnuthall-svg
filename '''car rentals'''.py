'''car rentals'''
cars = ["Suzuki van", "Toyora corrola", "Honda CVR", "suzuki swift", "Mitsubishi Airteck", "Nissan DC Ute", "Toyota Previa", "Toyota high ace", "toyota high ace"]
status = ["2seat", "4seat", "4seat", "4seat", "4seat", "4seat", "7seat", "12seat", "12seat"]
avalibility = ["avalible", "avalible", "avalible", "avalible", "avalible", "avalible", "avalible", "avalible", "avalible"]

get_name = True
while get_name == True:
    name = input("enter your name")
    if name == "":
        print("enter a valid name")
    else:  
        get_name = False

print ("rental car status")
for i in range (len(cars)):
    print(f"{i+1} {cars[i]:20} {status[i]:10} {avalibility[i]}")