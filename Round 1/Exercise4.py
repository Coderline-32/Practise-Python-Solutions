

try:
    number = int(input("Enter a number: "))
    for item in range(1, number):
         if number % item == 0:
            print(item)
except ValueError:
    print("Enter a valid number!")

