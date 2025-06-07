from random import Random

rand_gen =Random()
def guess_number():
    while True:
        guessed_number = int(input("Enter a number btn 1 and 10: "))
        random_interger = rand_gen.randint(1,10)
        if guessed_number == random_interger:
            print("You guessed the right number")
        else:
            print("You gueesed the wrong one.")
        again = input("Do you want to play the game again? (yes/no) ").strip() .lower()
        if again != "yes":
            print("Thankyou for playing the game.")
            break
       
           

guess_number()
        





