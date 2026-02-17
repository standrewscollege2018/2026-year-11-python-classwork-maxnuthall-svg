'''get numbers between 50-100 and print when over 200'''
total = 0
while total < 200:
    num = int(input("Enter a number between 50 and 100:"))
    if 50 <= num <= 100:
        total += num
    else:
        print("Number must be between 50 and 100.")
print(f"Total is {total}")