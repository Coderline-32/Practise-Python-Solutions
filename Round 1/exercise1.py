user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
current_year = 2025

def show_age():
    years_to_100 = 100 - user_age
    year_100 = current_year + years_to_100
    print(f"You will be truning 100 years old on {year_100}")

show_age()



