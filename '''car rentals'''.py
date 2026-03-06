'''car rentals'''

#set lists
cars = ["Suzuki van", "Toyora corrola", "Honda CVR", "suzuki swift", "Mitsubishi Airteck", "Nissan DC Ute", "Toyota Previa", "Toyota high ace", "toyota high ace"]
status = ["2seat", "4seat", "4seat", "4seat", "4seat", "4seat", "7seat", "12seat", "12seat"]
avalibility = ["avalible", "avalible", "avalible", "avalible", "avalible", "avalible", "avalible", "avalible", "avalible"]

run_program = True
while run_program == True:
    #get the name of user
    get_name = True
    while get_name == True:
        name = input("enter your name")
        if name == "":
            print("enter a valid name")
        else:  
            get_name = False
    #print the avalible cars
    print ("rental car status")
    for i in range (len(cars)):
        print(f"{i+1} {cars[i]:20} {status[i]:10} {avalibility[i]}")

    #get the car they want to book
    get_num = True
    while get_num == True:
        try:
            selection = int(input("what number is the car"))
            if selection >= 0 and selection <= len(cars):
                get_num = False
            else:
                print("Error")
            if selection == 0:
                run_program = False
            else:
            #Make the booking
                avalibility[selection-1] = "unavalible"
        except  ValueError:
            print("this is not a number, type a number of the 9 cars, if it says unavalible it doesnt work")