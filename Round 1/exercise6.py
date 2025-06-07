value= input("Enter a valuue to check whether it is a palindrome: ")

def check_palindrome():

    global value
    value = value.lower()
    if value == value[::-1]:
        print(f"{value} is palindrome!")
    else:
        print("value is not palindrome")

check_palindrome()
