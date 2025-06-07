
def check_number():
    while True:
        
        try:
            number = int(input("Enter a number: "))

            if number % 2 == 0:
                print(f"{number} is even")
            else:
                print(f"{number} is odd")
        except ValueError:
            print("Enter a valid number!")
            break
    
check_number()
    